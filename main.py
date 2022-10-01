import sys
import webbrowser
from utils.worker import *
from ui.app import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt6.QtGui import QTextCursor, QPixmap, QIcon
from PyQt6.QtCore import QThread
from datetime import timedelta

# Tela feita usando Qt Designer e convertida para Python com a biblioteca PyQt6 (pyuic6)
# Armazenado em ui/app.py


# BUG NO SEM ARTISTAS

# Classe principal do aplicativo
# noinspection PyUnresolvedReferences
class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Cria objetos do aplicativo
        self.setupUi(self)

        # Instancia variáveis
        self.thread: QThread | None = None
        self.worker: Worker | None = None

        # Conecta eventos
        self.btDownload.clicked.connect(self.download)
        self.btImportTxt.clicked.connect(self.import_txt)

        # Importa ícones dinamicamente
        self.setWindowIcon(QIcon('./assets/icon.png'))
        self.lb_logo.setPixmap(QPixmap('./assets/youtube_logo.png'))

        # Coloca foco no txtSongs
        self.txtSongs.setFocus()

        # Abre o navegador ao clicar no botão de ajuda
        self.actionComo_Usar.triggered.connect(lambda: webbrowser.open('https://github.com/Paulo1402/YouTube'
                                                                       '-Downloader#ComoUsar'))

        # Define aliases para constantes
        self.yes = QMessageBox.StandardButton.Yes
        self.no = QMessageBox.StandardButton.No

        # Cria um template de uma messagebox para uso posterior
        self.popup = QMessageBox(self)
        self.popup.setStandardButtons(self.yes | self.no)
        self.popup.setDefaultButton(self.yes)

        # Altera o caption padrão
        self.popup.button(self.yes).setText('Sim')
        self.popup.button(self.no).setText('Não')

    # Evento disparado ao tentar fechar o aplicativo
    def closeEvent(self, event):
        # Se a thread estiver em execução
        if self.thread and self.thread.isRunning():
            # Executa um popup e aguarda resposta do usuário
            self.popup.setWindowTitle('ATENÇÃO')
            self.popup.setText('Processo em andamento!\nDeseja sair mesmo assim?')
            self.popup.setDefaultButton(self.no)
            self.popup.setIcon(QMessageBox.Icon.Warning)

            answer = self.popup.exec()

            if answer == self.no:
                event.ignore()
                return

        event.accept()

    # Importa um arquivo .txt para dentro do aplicativo
    def import_txt(self):
        path = QFileDialog.getOpenFileName(self.centralwidget, 'Importar .txt', '.', 'txt (*.txt)')[0]

        if path:
            encoding = get_encoding(path)

            with open(path, 'r', encoding=encoding) as txt:
                self.txtSongs.clear()
                self.txtSongs.setText(txt.read())

    # Baixa lista do YouTube
    def download(self):
        # Informa o usuário caso o processo já esteja em andamento
        if self.thread and self.thread.isRunning():
            QMessageBox.warning(self.centralwidget, 'ATENÇÃO', 'Já existe um processo em andamento, por favor aguarde.',
                                QMessageBox.StandardButton.Ok)
            return

        # Pega o texto armazenado no aplicativo
        song_list = self.txtSongs.toPlainText()

        # Retorna um dicionário com a lista de músicas e a quantidade total
        artists, count = get_songs(song_list)

        if not count:
            QMessageBox.critical(self, 'ATENÇÃO', 'Nenhuma música encontrada, verifique por favor. '
                                 'Na dúvida clique no botão ajuda.', QMessageBox.StandardButton.Ok)
            return

        # Estima o tempo da operação
        estimate = str(timedelta(seconds=count * 3))

        # Executa um popup e aguarda resposta do usuário
        self.popup.setWindowTitle('ATENÇÃO')
        self.popup.setText(f'Deseja fazer o download? \nTempo estimado: {estimate}')
        self.popup.setIcon(QMessageBox.Icon.Information)

        answer = self.popup.exec()

        if answer == self.no:
            return

        # Limpa o terminal
        self.txtTerminal.clear()

        # Prepara a thread que irá realizar os downloads
        self.thread = QThread()
        self.worker = Worker(artists, count)

        self.worker.moveToThread(self.thread)

        # Conecta eventos
        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.finished_thread)
        self.worker.progress.connect(lambda x: self.progressBar.setValue(x))
        self.worker.print_on_terminal.connect(lambda x: self.print_on_terminal(x))

        # Inicia os downloads
        self.thread.start()

    # Printa no terminal informações durante o baixar
    def print_on_terminal(self, text):
        self.txtTerminal.append(text)

        # Move cursor para o fim do texto
        cursor = self.txtTerminal.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)

        self.txtTerminal.setTextCursor(cursor)

    # Elimina variáveis da memória e prepara para comprimir download
    def finished_thread(self):
        # Elimina variáveis
        self.thread.quit()
        self.thread.deleteLater()
        self.worker.deleteLater()
        self.thread = None

        # Informa o usuário que o processo terminou
        QMessageBox.information(self, 'AVISO', 'Download Concluído.', QMessageBox.StandardButton.Ok)
        path = QFileDialog.getSaveFileName(self, 'Salvar em', 'Songs')[0]

        # Comprime download em um arquivo .zip
        if path:
            compact_to_zip(path)
            QMessageBox.information(self, 'AVISO', 'Músicas compactadas com sucesso.', QMessageBox.StandardButton.Ok)

        # Remove pasta temporária
        shutil.rmtree('./temp', ignore_errors=True)


# Usado para auxiliar na depuração
def exception_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)
    sys.exit(1)


# Inicia o aplicativo
if __name__ == "__main__":
    sys.excepthook = exception_hook
    qt = QApplication(sys.argv)
    app = App()
    app.show()

    sys.exit(qt.exec())
