import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *
import sqlite3

content = "abb"

class Ui_Szelekcio(object):
    def setupUi(x, Ui_Szelekcio):
        Ui_Szelekcio.setObjectName("Ui_Szelekcio")
        Ui_Szelekcio.resize(572, 632)
        x.centralwidget = QtWidgets.QWidget(Ui_Szelekcio)
        x.centralwidget.setObjectName("centralwidget")
        x.groupBox = QtWidgets.QGroupBox(x.centralwidget)
        x.groupBox.setGeometry(QtCore.QRect(20, 30, 531, 241))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.groupBox.setFont(font)
        x.groupBox.setObjectName("groupBox")
        x.label = QtWidgets.QLabel(x.groupBox)
        x.label.setGeometry(QtCore.QRect(40, 80, 151, 21))
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setWordWrap(True)
        x.label.setObjectName("label")
        x.label_2 = QtWidgets.QLabel(x.groupBox)
        x.label_2.setGeometry(QtCore.QRect(40, 40, 151, 21))
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setWordWrap(True)
        x.label_2.setObjectName("label_2")
        x.comboBox_forras = QtWidgets.QComboBox(x.groupBox)
        x.comboBox_forras.setGeometry(QtCore.QRect(210, 40, 151, 22))
        x.comboBox_forras.setObjectName("comboBox_forras")
        x.comboBox_forras.addItem("")
        x.comboBox_forras.addItem("")
        x.comboBox_forras.addItem("")
        x.lineEdit_ujAll = QtWidgets.QLineEdit(x.groupBox)
        x.lineEdit_ujAll.setGeometry(QtCore.QRect(210, 80, 151, 20))
        x.lineEdit_ujAll.setObjectName("lineEdit_ujAll")
        x.label_4 = QtWidgets.QLabel(x.groupBox)
        x.label_4.setGeometry(QtCore.QRect(40, 120, 151, 21))
        x.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_4.setWordWrap(True)
        x.label_4.setObjectName("label_4")
        #az sql szöveget beolvasó input doboz 
        x.textEdit_szelekcio = QtWidgets.QTextEdit(x.groupBox)
        x.textEdit_szelekcio.setGeometry(QtCore.QRect(210, 120, 291, 101))
        x.textEdit_szelekcio.setObjectName("textEdit_szelekcio")
        #a szöveget megjelenítő doboz
        x.listWidget = QtWidgets.QListWidget(x.centralwidget)
        x.listWidget.setGeometry(QtCore.QRect(120, 300, 331, 231))
        x.listWidget.setObjectName("listWidget")
        x.pushButton_futtat = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_futtat.setGeometry(QtCore.QRect(180, 560, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_futtat.setFont(font)
        x.selection = Selection()
        x.pushButton_futtat.clicked.connect(x.save_text)
        x.pushButton_futtat.clicked.connect(x.selection.newTable)
        x.pushButton_futtat.setObjectName("pushButton_futtat")
        x.pushButton_megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_megse.setGeometry(QtCore.QRect(300, 560, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_megse.setFont(font)
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: Ui_Szelekcio.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        Ui_Szelekcio.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Szelekcio)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
        x.menubar.setObjectName("menubar")
        Ui_Szelekcio.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Szelekcio)
        x.statusbar.setObjectName("statusbar")
        Ui_Szelekcio.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Szelekcio)
        QtCore.QMetaObject.connectSlotsByName(Ui_Szelekcio)

    def retranslateUi(x, Ui_Szelekcio):
        _translate = QtCore.QCoreApplication.translate
        Ui_Szelekcio.setWindowTitle(_translate("Ui_Szelekcio", "Szelekció"))
        x.groupBox.setTitle(_translate("Ui_Szelekcio", "Paraméterek"))
        x.label.setText(_translate("Ui_Szelekcio", "Új állomány neve:"))
        x.label_2.setText(_translate("Ui_Szelekcio", "Forrás állomány:"))
        x.comboBox_forras.setItemText(0, _translate("Ui_Szelekcio", "Személyek leltára"))
        x.comboBox_forras.setItemText(1, _translate("Ui_Szelekcio", "Települések"))
        x.comboBox_forras.setItemText(2, _translate("Ui_Szelekcio", "Bevételek"))
        x.label_4.setText(_translate("Ui_Szelekcio", "Szelekció szabálya:"))
        x.pushButton_futtat.setText(_translate("Ui_Szelekcio", "Futtatás"))
        x.pushButton_megse.setText(_translate("Ui_Szelekcio", "Mégse"))

    def save_text(x):
        global content
        content = x.textEdit_szelekcio.toPlainText()
        
class Selection(object):

    def newTable(x):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        #c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        #user_input = input("Expense Amount: ")
        #sql = "SELECT * FROM ?"
        #for row in c.execute(content):
        #    print(row)
        for row in c.execute(format(content.replace('"', '""'))):
            print(row)
        # Save (commit) the changes
        #print(content)
        conn.commit()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.


        #for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        #        print(row)

        conn.close()