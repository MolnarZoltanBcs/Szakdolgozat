import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *


class Ui_Adatallomanyok(QtWidgets.QMainWindow):
    def setupUi(x, Ui_Adatallomanyok):
        Ui_Adatallomanyok.setObjectName("Ui_Adatallomanyok")
        Ui_Adatallomanyok.resize(937, 586)
        x.centralwidget = QtWidgets.QWidget(Ui_Adatallomanyok)
        x.centralwidget.setObjectName("centralwidget")
       
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 10, 911, 521))
        font = QtGui.QFont()
        font.setPointSize(8)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.tableWidget = QtWidgets.QTableWidget(x.frame)
        x.tableWidget.setGeometry(QtCore.QRect(15, 121, 881, 381))
        x.tableWidget.setObjectName("tableWidget")
        x.tableWidget.horizontalHeader().setStretchLastSection(True)
        x.tableWidget.setColumnCount(8)
        x.tableWidget.setRowCount(3)
        x.pushButton_elonezet = QtWidgets.QPushButton(x.frame)
        x.pushButton_elonezet.setGeometry(QtCore.QRect(20, 40, 101, 25))
        x.pushButton_elonezet.setObjectName("pushButton_elonezet")
        x.pushButton__kodfuttatas = QtWidgets.QPushButton(x.frame)
        x.pushButton__kodfuttatas.setGeometry(QtCore.QRect(160, 40, 111, 25))
        x.pushButton__kodfuttatas.setObjectName("pushButton__kodfuttatas")
        x.pushButton_torles = QtWidgets.QPushButton(x.frame)
        x.pushButton_torles.setGeometry(QtCore.QRect(310, 40, 101, 25))
        x.pushButton_torles.setObjectName("pushButton_torles")
        Ui_Adatallomanyok.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Adatallomanyok)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 937, 21))
        x.menubar.setObjectName("menubar")
        Ui_Adatallomanyok.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Adatallomanyok)
        x.statusbar.setObjectName("statusbar")
        Ui_Adatallomanyok.setStatusBar(x.statusbar)

        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setVerticalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(7, item)
       
        
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(0, 7, item)
        
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(1, 7, item)
        
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setItem(2, 7, item)
        
        
        x.pushButton_elonezet.clicked.connect(x.open_tabla)
        x.pushButton__kodfuttatas.clicked.connect(x.open_kod)
                 #ez fogja törölni a kiválasztott sort 
        x.pushButton_torles.clicked.connect(x.deleteCurrentRow)
        

        x.retranslateUi(Ui_Adatallomanyok)
        QtCore.QMetaObject.connectSlotsByName(Ui_Adatallomanyok)

        #modosit torol gomb allapot valtozasahoz 
        x.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        x.tableWidget.selectionModel().selectionChanged.connect(
            x.on_selection_changed
        )
 
        x.on_selection_changed()
                  
        
    def on_selection_changed(self):
        self.pushButton_elonezet.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_torles.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton__kodfuttatas.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )

    def deleteCurrentRow(self):
        result = QtWidgets.QMessageBox.question(self,
                      "Törlés megerősítése...",
                      "Biztos ki akarod törölni a kiválaszott sorokat?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        

        if result == QtWidgets.QMessageBox.Yes:
            indexes = self.tableWidget.selectionModel().selectedRows() 
            for index in sorted(indexes):
                self.tableWidget.removeRow(index.row())

    def retranslateUi(x, Ui_Adatallomanyok):
        _translate = QtCore.QCoreApplication.translate
        Ui_Adatallomanyok.setWindowTitle(_translate("Ui_Adatallomanyok", "Adatállományok"))
        
        
        item = x.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Ui_Nomenklatura", "1"))
        item = x.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Ui_Nomenklatura", "2"))
        item = x.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Ui_Nomenklatura", "3"))

        item = x.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Nomenklatura", "Adatállomány neve"))
        item = x.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Nomenklatura", "Állomány rekordszáma"))
        item = x.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Ui_Nomenklatura", "Rekordleírása"))
        item = x.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Ui_Nomenklatura", "Verziószáma"))
        item = x.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Ui_Nomenklatura", "Projekt"))
        item = x.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Ui_Nomenklatura", "Tulajdonos"))
        item = x.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Ui_Nomenklatura", "Állomány titkosítási kódja"))
        item = x.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Ui_Nomenklatura", "Létrehozva"))
        


        __sortingEnabled = x.tableWidget.isSortingEnabled()
        x.tableWidget.setSortingEnabled(False)
        item = x.tableWidget.item(0, 0)
        item.setText(_translate("Ui_Adatallomanyok", "Személyek_leltára"))
        item = x.tableWidget.item(0, 1)
        item.setText(_translate("Ui_Adatallomanyok", "456"))
        item = x.tableWidget.item(0, 2)
        item.setText(_translate("Ui_Adatallomanyok", "szemelyek"))
        item = x.tableWidget.item(0, 3)
        item.setText(_translate("Ui_Adatallomanyok", "2"))
        item = x.tableWidget.item(0, 4)
        item.setText(_translate("Ui_Adatallomanyok", "UP/01"))
        item = x.tableWidget.item(0, 5)
        item.setText(_translate("Ui_Adatallomanyok", "Data Governance"))
        item = x.tableWidget.item(0, 6)
        item.setText(_translate("Ui_Adatallomanyok", "OLDXXXZB"))
        item = x.tableWidget.item(0, 7)
        item.setText(_translate("Ui_Adatallomanyok", "2020.10.10. 10:09"))
        
        item = x.tableWidget.item(1, 0)
        item.setText(_translate("Ui_Adatallomanyok", "Települések"))
        item = x.tableWidget.item(1, 1)
        item.setText(_translate("Ui_Adatallomanyok", "1500"))
        item = x.tableWidget.item(1, 2)
        item.setText(_translate("Ui_Adatallomanyok", "telepulesek"))
        item = x.tableWidget.item(1, 3)
        item.setText(_translate("Ui_Adatallomanyok", "1"))
        item = x.tableWidget.item(1, 4)
        item.setText(_translate("Ui_Adatallomanyok", "UP/02"))
        item = x.tableWidget.item(1, 5)
        item.setText(_translate("Ui_Adatallomanyok", "Data Governance"))
        item = x.tableWidget.item(1, 6)
        item.setText(_translate("Ui_Adatallomanyok", "XYWZXYZW"))
        item = x.tableWidget.item(1, 7)
        item.setText(_translate("Ui_Adatallomanyok", "2020.09.09. 13:54"))
       
        item = x.tableWidget.item(2, 0)
        item.setText(_translate("Ui_Adatallomanyok", "Bevételek"))
        item = x.tableWidget.item(2, 1)
        item.setText(_translate("Ui_Adatallomanyok", "100"))
        item = x.tableWidget.item(2, 2)
        item.setText(_translate("Ui_Adatallomanyok", "bevetelek"))
        item = x.tableWidget.item(2, 3)
        item.setText(_translate("Ui_Adatallomanyok", "3"))
        item = x.tableWidget.item(2, 4)
        item.setText(_translate("Ui_Adatallomanyok", "UP/05"))
        item = x.tableWidget.item(2, 5)
        item.setText(_translate("Ui_Adatallomanyok", "Data Governance"))
        item = x.tableWidget.item(2, 6)
        item.setText(_translate("Ui_Adatallomanyok", "QPQWLPQL"))
        item = x.tableWidget.item(2, 7)
        item.setText(_translate("Ui_Adatallomanyok", "2020.07.09. 09:08"))

        x.tableWidget.setSortingEnabled(__sortingEnabled)
        x.pushButton_elonezet.setText(_translate("Ui_Adatallomanyok", "Előnézet"))
        x.pushButton__kodfuttatas.setText(_translate("Ui_Adatallomanyok", "Kód végrehajtása"))
        x.pushButton_torles.setText(_translate("Ui_Adatallomanyok", "Törlés"))
    
    def open_tabla(x):
        x.window = QtWidgets.QMainWindow()
        x.ui = Ui_Tablatartalom()
        x.ui.setupUi(x.window)
        x.window.show()
        
    def open_kod(x):
        x.window = QtWidgets.QMainWindow()
        x.ui = Ui_Kod()
        x.ui.setupUi(x.window)
        x.window.show()


class Ui_Tablatartalom(object):
    def setupUi(x, Ui_Tablatartalom):
        Ui_Tablatartalom.setObjectName("Ui_Tablatartalom")
        Ui_Tablatartalom.resize(622, 449)
        x.centralwidget = QtWidgets.QWidget(Ui_Tablatartalom)
        x.centralwidget.setObjectName("centralwidget")
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 10, 601, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.tableWidget = QtWidgets.QTableWidget(x.frame)
        x.tableWidget.setGeometry(QtCore.QRect(10, 70, 581, 311))
        x.tableWidget.setColumnCount(5)
        x.tableWidget.setObjectName("tableWidget")
        x.tableWidget.setRowCount(0)
        x.pushButton_modosit = QtWidgets.QPushButton(x.frame)
        x.pushButton_modosit.setGeometry(QtCore.QRect(10, 10, 101, 31))
        x.pushButton_modosit.setObjectName("pushButton_modosit")
        x.pushButton_aktualizal = QtWidgets.QPushButton(x.frame)
        x.pushButton_aktualizal.setGeometry(QtCore.QRect(130, 10, 101, 31))
        x.pushButton_aktualizal.setObjectName("pushButton_aktualizal")
        Ui_Tablatartalom.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Tablatartalom)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        x.menubar.setObjectName("menubar")
        Ui_Tablatartalom.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Tablatartalom)
        x.statusbar.setObjectName("statusbar")
        Ui_Tablatartalom.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Tablatartalom)
        QtCore.QMetaObject.connectSlotsByName(Ui_Tablatartalom)

    def retranslateUi(x, Ui_Tablatartalom):
        _translate = QtCore.QCoreApplication.translate
        Ui_Tablatartalom.setWindowTitle(_translate("Ui_Tablatartalom", "Tábla tartalma"))
        x.pushButton_modosit.setText(_translate("Ui_Tablatartalom", "Módosít"))
        x.pushButton_aktualizal.setText(_translate("Ui_Tablatartalom", "Aktualizál"))

class Ui_Kod(object):
    def setupUi(x, Ui_Kod):
        Ui_Kod.setObjectName("Ui_Kod")
        Ui_Kod.resize(443, 396)
        x.centralwidget = QtWidgets.QWidget(Ui_Kod)
        x.centralwidget.setObjectName("centralwidget")
        x.pushButton_futtat = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_futtat.setGeometry(QtCore.QRect(200, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_futtat.setFont(font)
        x.pushButton_futtat.setObjectName("pushButton_futtat")
        x.pushButton_megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_megse.setGeometry(QtCore.QRect(310, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_megse.setFont(font)
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: Ui_Kod.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        x.groupBox = QtWidgets.QGroupBox(x.centralwidget)
        x.groupBox.setGeometry(QtCore.QRect(20, 10, 401, 301))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.groupBox.setFont(font)
        x.groupBox.setObjectName("groupBox")
        x.textEdit = QtWidgets.QTextEdit(x.groupBox)
        x.textEdit.setGeometry(QtCore.QRect(10, 20, 381, 271))
        x.textEdit.setObjectName("textEdit")
        Ui_Kod.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Kod)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        x.menubar.setObjectName("menubar")
        Ui_Kod.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Kod)
        x.statusbar.setObjectName("statusbar")
        Ui_Kod.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Kod)
        QtCore.QMetaObject.connectSlotsByName(Ui_Kod)

    def retranslateUi(x, Ui_Kod):
        _translate = QtCore.QCoreApplication.translate
        Ui_Kod.setWindowTitle(_translate("Ui_Kod", "Kód végrehajtása"))
        x.pushButton_futtat.setText(_translate("Ui_Kod", "Futtatás"))
        x.pushButton_megse.setText(_translate("Ui_Kod", "Mégse"))
        x.groupBox.setTitle(_translate("Ui_Kod", "Futtatandó utasítás"))
