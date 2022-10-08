# Form implementation generated from reading ui file 'ui/app.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(660, 363)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar.sizePolicy().hasHeightForWidth())
        self.progress_bar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        self.progress_bar.setFont(font)
        self.progress_bar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.progress_bar.setMouseTracking(False)
        self.progress_bar.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.progress_bar.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.progress_bar.setAcceptDrops(False)
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setStyleSheet("")
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout.addWidget(self.progress_bar, 8, 1, 1, 5)
        self.lb_action = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_action.sizePolicy().hasHeightForWidth())
        self.lb_action.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.lb_action.setFont(font)
        self.lb_action.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_action.setObjectName("lb_action")
        self.gridLayout.addWidget(self.lb_action, 8, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 10, 5, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_import_txt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_import_txt.sizePolicy().hasHeightForWidth())
        self.bt_import_txt.setSizePolicy(sizePolicy)
        self.bt_import_txt.setMinimumSize(QtCore.QSize(0, 50))
        self.bt_import_txt.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.bt_import_txt.setFont(font)
        self.bt_import_txt.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_import_txt.setMouseTracking(True)
        self.bt_import_txt.setStyleSheet("")
        self.bt_import_txt.setObjectName("bt_import_txt")
        self.horizontalLayout.addWidget(self.bt_import_txt)
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_download.sizePolicy().hasHeightForWidth())
        self.bt_download.setSizePolicy(sizePolicy)
        self.bt_download.setMinimumSize(QtCore.QSize(0, 50))
        self.bt_download.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.bt_download.setFont(font)
        self.bt_download.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_download.setMouseTracking(True)
        self.bt_download.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bt_download.setAutoFillBackground(False)
        self.bt_download.setStyleSheet("")
        self.bt_download.setCheckable(False)
        self.bt_download.setChecked(False)
        self.bt_download.setAutoRepeat(False)
        self.bt_download.setAutoExclusive(False)
        self.bt_download.setAutoDefault(False)
        self.bt_download.setDefault(False)
        self.bt_download.setFlat(False)
        self.bt_download.setObjectName("bt_download")
        self.horizontalLayout.addWidget(self.bt_download)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 3, 1, 3)
        self.lb_logo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_logo.sizePolicy().hasHeightForWidth())
        self.lb_logo.setSizePolicy(sizePolicy)
        self.lb_logo.setMinimumSize(QtCore.QSize(150, 80))
        self.lb_logo.setMaximumSize(QtCore.QSize(150, 80))
        self.lb_logo.setBaseSize(QtCore.QSize(150, 100))
        self.lb_logo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lb_logo.setText("")
        self.lb_logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lb_logo.setObjectName("lb_logo")
        self.gridLayout.addWidget(self.lb_logo, 1, 0, 1, 1)
        self.txt_terminal = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_terminal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_terminal.sizePolicy().hasHeightForWidth())
        self.txt_terminal.setSizePolicy(sizePolicy)
        self.txt_terminal.setMinimumSize(QtCore.QSize(260, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.txt_terminal.setFont(font)
        self.txt_terminal.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.txt_terminal.setAutoFillBackground(False)
        self.txt_terminal.setStyleSheet("background-color: black; border: 1px solid black; color: white;")
        self.txt_terminal.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.txt_terminal.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.txt_terminal.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.txt_terminal.setLineWidth(2)
        self.txt_terminal.setMidLineWidth(2)
        self.txt_terminal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.txt_terminal.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.txt_terminal.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.WidgetWidth)
        self.txt_terminal.setReadOnly(True)
        self.txt_terminal.setMarkdown("")
        self.txt_terminal.setAcceptRichText(True)
        self.txt_terminal.setCursorWidth(1)
        self.txt_terminal.setPlaceholderText("")
        self.txt_terminal.setObjectName("txt_terminal")
        self.gridLayout.addWidget(self.txt_terminal, 3, 3, 2, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.txt_songs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_songs.setStyleSheet("border: 1px solid black; \n"
"font: 12pt \"Segoe UI\";")
        self.txt_songs.setObjectName("txt_songs")
        self.gridLayout.addWidget(self.txt_songs, 3, 0, 2, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuAjuda = QtWidgets.QMenu(self.menuBar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menuBar)
        self.actionComo_Usar = QtGui.QAction(MainWindow)
        self.actionComo_Usar.setObjectName("actionComo_Usar")
        self.menuAjuda.addAction(self.actionComo_Usar)
        self.menuBar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.lb_action.setText(_translate("MainWindow", "..."))
        self.bt_import_txt.setText(_translate("MainWindow", "IMPORTAR"))
        self.bt_download.setText(_translate("MainWindow", "BAIXAR"))
        self.txt_terminal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-style:italic;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "ESCREVA ABAIXO OU \n"
"IMPORTE UM ARQUIVO .TXT"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionComo_Usar.setText(_translate("MainWindow", "Como Usar"))
