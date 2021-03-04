import sys
import sip
sip.setapi('QString', 2)
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow, QLineEdit
from PyQt5.QtCore import pyqtSlot
from app_modules import *
import sqlite3

valtnev = ""
cimke = ""
leiras = ""
hossz = 0.0
csoport = ""
query = ()
class Ui_Mutatok(QtWidgets.QMainWindow):
    def setupUi(x,  Ui_Mutatok):
         Ui_Mutatok.setObjectName("Ui_Mutatok")
         Ui_Mutatok.resize(1175, 500)
         
         Ui_Mutatok.setWindowTitle("Mutatók kezelése")
         x.newmutatdb = newMutatDB()
         newMutatDB.listMutat()
         
         x.tableWidget = QtWidgets.QTableWidget(Ui_Mutatok)
         x.tableWidget.horizontalHeader().setStretchLastSection(True)
         x.tableWidget.setGeometry(QtCore.QRect(60, 75, 1025, 370))
         x.tableWidget.setAlternatingRowColors(True)
         x.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
         x.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
         x.tableWidget.setObjectName("tableWidget")
         
         x.tableWidget.setColumnCount(9)
         x.tableWidget.setRowCount(4)
         
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setVerticalHeaderItem(0, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setVerticalHeaderItem(1, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setVerticalHeaderItem(2, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setVerticalHeaderItem(3, item)
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
         x.tableWidget.setHorizontalHeaderItem(8, item)
         
         
         
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(0, 0, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(0, 3, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(0, 4, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(1, 0, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(1, 3, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(1, 4, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(2, 0, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(2, 3, item)        
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(2, 4, item)         
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(3, 0, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(3, 3, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(3, 4, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(3, 6, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(3, 7, item)
         item = QtWidgets.QTableWidgetItem()
         x.tableWidget.setItem(3, 8, item)
        
        
         x.pushButton_uj = QtWidgets.QPushButton(Ui_Mutatok)
         x.pushButton_uj.setGeometry(QtCore.QRect(60, 26, 91, 23))
         x.pushButton_uj.setObjectName("pushButton_uj") #uj
         x.pushButton_uj.setDefault(True) #ez lesz az alapertelmezett gomb
         x.pushButton_modosit = QtWidgets.QPushButton(Ui_Mutatok)
         x.pushButton_modosit.setGeometry(QtCore.QRect(181, 26, 91, 23))
         x.pushButton_modosit.setObjectName("pushButton_modosit") #modosit
         x.pushButton_torol = QtWidgets.QPushButton(Ui_Mutatok)
         x.pushButton_torol.setGeometry(QtCore.QRect(302, 26, 91, 23))
         x.pushButton_torol.setObjectName("pushButton_torol") #torol
         x.pushButton_export = QtWidgets.QPushButton(Ui_Mutatok)
         x.pushButton_export.setGeometry(QtCore.QRect(423, 26, 110, 23))
         x.pushButton_export.setObjectName("pushButton_export") #exportal


         x.valtoztatUi(Ui_Mutatok)
         QtCore.QMetaObject.connectSlotsByName(Ui_Mutatok)
         
         #ez fogja megnyitni azt az ablakot amelyikkel uj sort vehetunk fel     
         x.pushButton_uj.clicked.connect(x.openUjMutato)
         
         #ez fogja megnyitni azt az ablakot amelyikkel modosithatunk a felvett adatokon     
         x.pushButton_modosit.clicked.connect(x.openModositMutato)

         #ez fogja törölni a kiválasztott sort 
         x.pushButton_torol.clicked.connect(x.deleteCurrentRow)
         
         #modosit torol gomb allapot valtozasahoz 
         x.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
         x.tableWidget.selectionModel().selectionChanged.connect(
             x.on_selection_changed
         )
 
         x.on_selection_changed()
                  
        
    def on_selection_changed(self):
        self.pushButton_modosit.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_torol.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )




    def valtoztatUi(x, Ui_Mutatok):
         _translate = QtCore.QCoreApplication.translate
         Ui_Mutatok.setWindowTitle(_translate("Ui_Mutatok", "Mutatók"))
         item = x.tableWidget.verticalHeaderItem(0)
         item.setText(_translate("Ui_Mutatok", "1"))
         item = x.tableWidget.verticalHeaderItem(1)
         item.setText(_translate("Ui_Mutatok", "2"))
         item = x.tableWidget.verticalHeaderItem(2)
         item.setText(_translate("Ui_Mutatok", "3"))
         item = x.tableWidget.verticalHeaderItem(3)
         item.setText(_translate("Ui_Mutatok", "4"))
         x.newMutatDB = newMutatDB()
         #query = x.newMutatDB.listMutat()
         
         #while query.next():
         for row in query:
            rows = x.tableWidget.rowCount()
            x.tableWidget.setRowCount(rows + 1)
            x.tableWidget.setItem(rows, 0, QTableWidgetItem(str(row[0])))
            x.tableWidget.setItem(rows, 1, QTableWidgetItem(str(row[1])))
            x.tableWidget.setItem(rows, 2, QTableWidgetItem(str(row[2])))
            #x.tableWidget.setItem(rows, 3, QTableWidgetItem(query.value(3)))

         x.tableWidget.resizeColumnsToContents()
         item = x.tableWidget.horizontalHeaderItem(0)
         item.setText(_translate("Ui_Mutatok", "Változó neve"))
         item = x.tableWidget.horizontalHeaderItem(1)
         item.setText(_translate("Ui_Mutatok", "Nyomtatási cimke"))
         item = x.tableWidget.horizontalHeaderItem(2)
         item.setText(_translate("Ui_Mutatok", "Leírás"))
         item = x.tableWidget.horizontalHeaderItem(3)
         item.setText(_translate("Ui_Mutatok", "Hossz"))
         item = x.tableWidget.horizontalHeaderItem(4)
         item.setText(_translate("Ui_Mutatok", "Típus"))
         item = x.tableWidget.horizontalHeaderItem(5)
         item.setText(_translate("Ui_Mutatok", "Mutató csoport"))
         item = x.tableWidget.horizontalHeaderItem(6)
         item.setText(_translate("Ui_Mutatok", "Utolsó módosítás"))
         item = x.tableWidget.horizontalHeaderItem(7)
         item.setText(_translate("Ui_Mutatok", "Érvényesség kezdete"))
         item = x.tableWidget.horizontalHeaderItem(8)
         item.setText(_translate("Ui_Mutatok", "Érvényesség vége"))
         
         
         __sortingEnabled = x.tableWidget.isSortingEnabled()
         x.tableWidget.setSortingEnabled(False)
         
         """item = x.tableWidget.item(0, 0)
         item.setText(_translate("Ui_Mutatok", "Testsuly"))
         item = x.tableWidget.item(0, 3)
         item.setText(_translate("Ui_Mutatok", "3"))
         item = x.tableWidget.item(1, 0)
         item.setText(_translate("Ui_Mutatok", "Datum"))
         item = x.tableWidget.item(1, 3)
         item.setText(_translate("Ui_Mutatok", "8"))
         item = x.tableWidget.item(2, 0)
         item.setText(_translate("Ui_Mutatok", "sum_bevetel"))
         item = x.tableWidget.item(2, 3)
         item.setText(_translate("Ui_Mutatok", "15"))
         item = x.tableWidget.item(0, 4)
         item.setText(_translate("Ui_Mutatok", "Egész szám"))
         item = x.tableWidget.item(1, 4)
         item.setText(_translate("Ui_Mutatok", "Dátum"))
         item = x.tableWidget.item(2, 4)
         item.setText(_translate("Ui_Mutatok", "Egész szám"))
         item = x.tableWidget.item(3, 0)
         item.setText(_translate("Ui_Mutatok", "Adokedvezmeny"))
         item = x.tableWidget.item(3, 3)
         item.setText(_translate("Ui_Mutatok", "8"))
         item = x.tableWidget.item(3, 4)
         item.setText(_translate("Ui_Mutatok", "Lebegőpontos szám"))
         item = x.tableWidget.item(3, 6)
         item.setText(_translate("Ui_Mutatok", "2008.10.25."))
         item = x.tableWidget.item(3, 7)
         item.setText(_translate("Ui_Mutatok", "2005.01.01."))
         item = x.tableWidget.item(3, 8)
         item.setText(_translate("Ui_Mutatok", "2010.12.31."))"""
        
         
         
         x.tableWidget.setSortingEnabled(__sortingEnabled)
         x.pushButton_uj.setText(_translate("Ui_Mutatok", "Új létrehozása"))
         x.pushButton_modosit.setText(_translate("Ui_Mutatok", "Módosítás"))
         x.pushButton_torol.setText(_translate("Ui_Mutatok", "Törlés"))
         x.pushButton_export.setText(_translate("Ui_Mutatok", "Kijelöltek exportja"))
        
    #definialjuk az uj mutato letrehozasa ablakot
    #ez nyitja meg
    def openUjMutato(x):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Mutatok_UJ()
         x.ui.setupUi(x.window)
         #x.window.setWindowTitle("Új mutató létrehozása")
         x.window.show()
    #es definialjuk a modosit mutato ablakot
    def openModositMutato(x):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Mutatok_UJ()
         x.ui.setupUi(x.window)
         x.window.setWindowTitle("Kiválasztott mutató módosítása")
         x.window.show()
        
    
    def deleteCurrentRow(self):
        result = QtWidgets.QMessageBox.question(self,
                      "Törlés megerősítése...",
                      "Biztos ki akarod törölni a kiválaszott sorokat?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        

        if result == QtWidgets.QMessageBox.Yes:
            indexes = self.tableWidget.selectionModel().selectedRows() 
            for index in sorted(indexes):
                self.tableWidget.removeRow(index.row())
            
    def newRow(self):
        self.text_from_window2 = QLineEdit()
        self.text_from_window2.setStyleSheet("color: red;")
        self.text_from_window2.setDisabled(True)

    @pyqtSlot(str)
    def update_label(self, txt):
        self.text_from_window2.setText(txt)
        
#ez az uj mutato felvetel ablaka
class Ui_Mutatok_UJ(object):
    def setupUi(x, Ui_Mutatok_UJ):
        Ui_Mutatok_UJ.setObjectName("Ui_Mutatok_UJ")
        Ui_Mutatok_UJ.resize(484, 466)
        x.centralwidget = QtWidgets.QWidget(Ui_Mutatok_UJ)
        x.centralwidget.setObjectName("centralwidget")
        x.pushButton_Mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Mentes.setGeometry(QtCore.QRect(270, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        #mentés logika
        x.newMutatDB = newMutatDB()
        x.pushButton_Mentes.clicked.connect(x.save_text)
        x.pushButton_Mentes.setFont(font)
        x.pushButton_Mentes.setObjectName("pushButton_Mentes")
        x.pushButton_Mentes.clicked.connect(x.newMutatDB.newMutat)
        #x.pushButton_Mentes.clicked.connect(Ui_Mutatok.setupUi())
        x.pushButton_Megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Megse.setGeometry(QtCore.QRect(370, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Megse.setFont(font)
        x.pushButton_Megse.setDefault(True)
        x.pushButton_Megse.setObjectName("pushButton_Megse")
        x.pushButton_Megse.clicked.connect(lambda: Ui_Mutatok_UJ.close())
        x.tabWidget = QtWidgets.QTabWidget(x.centralwidget)
        x.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.tabWidget.setFont(font)
        x.tabWidget.setObjectName("tabWidget")
        x.tab = QtWidgets.QWidget()
        x.tab.setObjectName("tab")
        x.label_8 = QtWidgets.QLabel(x.tab)
        x.label_8.setGeometry(QtCore.QRect(40, 280, 161, 41))
        x.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_8.setObjectName("label_8")
        x.label_5 = QtWidgets.QLabel(x.tab)
        x.label_5.setGeometry(QtCore.QRect(40, 170, 161, 31))
        x.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_5.setObjectName("label_5")
        x.label_2 = QtWidgets.QLabel(x.tab)
        x.label_2.setGeometry(QtCore.QRect(40, 50, 161, 31))
        x.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setObjectName("label_2")
        x.label_3 = QtWidgets.QLabel(x.tab)
        x.label_3.setGeometry(QtCore.QRect(40, 90, 161, 31))
        x.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_3.setObjectName("label_3")
        x.label_4 = QtWidgets.QLabel(x.tab)
        x.label_4.setGeometry(QtCore.QRect(40, 130, 161, 31))
        x.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_4.setObjectName("label_4")
        x.label = QtWidgets.QLabel(x.tab)
        x.label.setGeometry(QtCore.QRect(40, 10, 161, 31))
        x.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setObjectName("label")
        x.label_6 = QtWidgets.QLabel(x.tab)
        x.label_6.setGeometry(QtCore.QRect(40, 200, 161, 51))
        x.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_6.setObjectName("label_6")
        x.label_7 = QtWidgets.QLabel(x.tab)
        x.label_7.setGeometry(QtCore.QRect(40, 250, 161, 31))
        x.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_7.setObjectName("label_7")
        x.dateEdit_veg = QtWidgets.QDateEdit(x.tab)
        x.dateEdit_veg.setGeometry(QtCore.QRect(220, 290, 151, 31))
        x.dateEdit_veg.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        x.dateEdit_veg.setCalendarPopup(True)
        x.dateEdit_veg.setObjectName("dateEdit_veg")
        x.lineEdit_csoport = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_csoport.setGeometry(QtCore.QRect(220, 210, 201, 31))
        x.lineEdit_csoport.setObjectName("lineEdit_csoport")
        x.dateEdit_kezdet = QtWidgets.QDateEdit(x.tab)
        x.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 250, 151, 31))
        x.dateEdit_kezdet.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        x.dateEdit_kezdet.setCalendarPopup(True)
        x.dateEdit_kezdet.setObjectName("dateEdit_kezdet")
        x.lineEdit_leiras = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_leiras.setGeometry(QtCore.QRect(220, 90, 201, 31))
        x.lineEdit_leiras.setObjectName("lineEdit_leiras")
        x.lineEdit_valtozonev = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_valtozonev.setGeometry(QtCore.QRect(220, 10, 201, 31))
        x.lineEdit_valtozonev.setObjectName("lineEdit_valtozonev")
        x.lineEdit_cimke = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_cimke.setGeometry(QtCore.QRect(220, 50, 201, 31))
        x.lineEdit_cimke.setObjectName("lineEdit_cimke")
        x.lineEdit_hossz = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_hossz.setGeometry(QtCore.QRect(220, 130, 201, 31))
        x.lineEdit_hossz.setObjectName("lineEdit_hossz")
        x.comboBox = QtWidgets.QComboBox(x.tab)
        x.comboBox.setGeometry(QtCore.QRect(220, 170, 201, 31))
        x.comboBox.setObjectName("comboBox")
        x.comboBox.addItem("")
        x.comboBox.addItem("")
        x.comboBox.addItem("")
        x.tabWidget.addTab(x.tab, "")
        Ui_Mutatok_UJ.setCentralWidget(x.centralwidget)
        x.statusbar = QtWidgets.QStatusBar(Ui_Mutatok_UJ)
        x.statusbar.setObjectName("statusbar")
        Ui_Mutatok_UJ.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Mutatok_UJ)
        x.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_Mutatok_UJ)

    def save_text(x):
        global valtnev, cimke, leiras, hossz, csoport
        valtnev = x.lineEdit_valtozonev.text()
        cimke = x.lineEdit_cimke.text()
        leiras = x.lineEdit_leiras.text()
        hossz= x.lineEdit_hossz.text()
        csoport = x.lineEdit_csoport.text()

    def newRowUj(self):
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(parent.update_label)

    def retranslateUi(x, Ui_Mutatok_UJ):
        _translate = QtCore.QCoreApplication.translate
        Ui_Mutatok_UJ.setWindowTitle(_translate("Ui_Mutatok_UJ", "Mutato letrehozasa"))
        x.pushButton_Mentes.setText(_translate("Ui_Mutatok_UJ", "Mentés"))
        x.pushButton_Megse.setText(_translate("Ui_Mutatok_UJ", "Mégse"))
        x.label_8.setText(_translate("Ui_Mutatok_UJ", "Érvényesség vége:"))
        x.label_5.setText(_translate("Ui_Mutatok_UJ", "Típus:"))
        x.label_2.setText(_translate("Ui_Mutatok_UJ", "Nyomtatási címkéje:"))
        x.label_3.setText(_translate("Ui_Mutatok_UJ", "Leírása:"))
        x.label_4.setText(_translate("Ui_Mutatok_UJ", "Hossz:"))
        x.label.setText(_translate("Ui_Mutatok_UJ", "Változó neve:"))
        x.label_6.setText(_translate("Ui_Mutatok_UJ", "Mutató csoport:"))
        x.label_7.setText(_translate("Ui_Mutatok_UJ", "Érvényesség kezdete:"))
        x.comboBox.setItemText(0, _translate("Ui_Mutatok_UJ", "Egész szám"))
        x.comboBox.setItemText(1, _translate("Ui_Mutatok_UJ", "Lebegőpontos szám"))
        x.comboBox.setItemText(2, _translate("Ui_Mutatok_UJ", "Dátum"))
        x.tabWidget.setTabText(x.tabWidget.indexOf(x.tab), _translate("Ui_Mutatok_UJ", "Attribútumok"))


"""class Ui_Mutatok_Modosit(object):
    def setupUi(x, Ui_Mutatok_Modosit):
        Ui_Mutatok_Modosit.setObjectName("Ui_Mutatok_Modosit")
        Ui_Mutatok_Modosit.resize(484, 466)
        x.centralwidget = QtWidgets.QWidget(Ui_Mutatok_Modosit)
        x.centralwidget.setObjectName("centralwidget")
        x.pushButton_Mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Mentes.setGeometry(QtCore.QRect(270, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Mentes.setFont(font)
        x.pushButton_Mentes.setObjectName("pushButton_Mentes")
        x.pushButton_Megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Megse.setGeometry(QtCore.QRect(370, 400, 91, 41))
        x.pushButton_Megse.clicked.connect(lambda: Ui_Mutatok_Modosit.close())
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Megse.setFont(font)
        x.pushButton_Megse.setDefault(True)
        x.pushButton_Megse.setObjectName("pushButton_Megse")
        x.tabWidget = QtWidgets.QTabWidget(x.centralwidget)
        x.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.tabWidget.setFont(font)
        x.tabWidget.setObjectName("tabWidget")
        x.tab_attributum = QtWidgets.QWidget()
        x.tab_attributum.setObjectName("tab_attributum")
        x.label_8 = QtWidgets.QLabel(x.tab_attributum)
        x.label_8.setGeometry(QtCore.QRect(40, 280, 161, 41))
        x.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_8.setObjectName("label_8")
        x.label_5 = QtWidgets.QLabel(x.tab_attributum)
        x.label_5.setGeometry(QtCore.QRect(40, 170, 161, 31))
        x.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_5.setObjectName("label_5")
        x.label_2 = QtWidgets.QLabel(x.tab_attributum)
        x.label_2.setGeometry(QtCore.QRect(40, 50, 161, 31))
        x.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setObjectName("label_2")
        x.label_3 = QtWidgets.QLabel(x.tab_attributum)
        x.label_3.setGeometry(QtCore.QRect(40, 90, 161, 31))
        x.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_3.setObjectName("label_3")
        x.label_4 = QtWidgets.QLabel(x.tab_attributum)
        x.label_4.setGeometry(QtCore.QRect(40, 130, 161, 31))
        x.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_4.setObjectName("label_4")
        x.label = QtWidgets.QLabel(x.tab_attributum)
        x.label.setGeometry(QtCore.QRect(40, 10, 161, 31))
        x.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setObjectName("label")
        x.label_6 = QtWidgets.QLabel(x.tab_attributum)
        x.label_6.setGeometry(QtCore.QRect(40, 200, 161, 51))
        x.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_6.setObjectName("label_6")
        x.label_7 = QtWidgets.QLabel(x.tab_attributum)
        x.label_7.setGeometry(QtCore.QRect(40, 250, 161, 31))
        x.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_7.setObjectName("label_7")
        x.dateEdit_veg = QtWidgets.QDateEdit(x.tab_attributum)
        x.dateEdit_veg.setGeometry(QtCore.QRect(220, 290, 151, 31))
        x.dateEdit_veg.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        x.dateEdit_veg.setCalendarPopup(True)
        x.dateEdit_veg.setObjectName("dateEdit_veg")
        x.lineEdit_csoport = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_csoport.setGeometry(QtCore.QRect(220, 210, 201, 31))
        x.lineEdit_csoport.setObjectName("lineEdit_csoport")
        x.dateEdit_kezdet = QtWidgets.QDateEdit(x.tab_attributum)
        x.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 250, 151, 31))
        x.dateEdit_kezdet.setObjectName("dateEdit_kezdet")
        x.dateEdit_kezdet.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        x.dateEdit_kezdet.setCalendarPopup(True) 
        x.lineEdit_leiras = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_leiras.setGeometry(QtCore.QRect(220, 90, 201, 31))
        x.lineEdit_leiras.setObjectName("lineEdit_leiras")
        x.lineEdit_valtozonev = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_valtozonev.setGeometry(QtCore.QRect(220, 10, 201, 31))
        x.lineEdit_valtozonev.setObjectName("lineEdit_valtozonev")
        x.lineEdit_cimke = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_cimke.setGeometry(QtCore.QRect(220, 50, 201, 31))
        x.lineEdit_cimke.setObjectName("lineEdit_cimke")
        x.lineEdit_hossz = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_hossz.setGeometry(QtCore.QRect(220, 130, 201, 31))
        x.lineEdit_hossz.setObjectName("lineEdit_hossz")
        x.comboBox = QtWidgets.QComboBox(x.tab_attributum)
        x.comboBox.setGeometry(QtCore.QRect(220, 170, 201, 31))
        x.comboBox.setObjectName("comboBox")
        x.comboBox.addItem("")
        x.comboBox.addItem("")
        x.comboBox.addItem("")
        x.tabWidget.addTab(x.tab_attributum, "")
        x.tab_leiras = QtWidgets.QWidget()
        x.tab_leiras.setObjectName("tab_leiras")
        x.pushButton_uj = QtWidgets.QPushButton(x.tab_leiras)
        x.pushButton_uj.setGeometry(QtCore.QRect(50, 20, 101, 31))
        x.pushButton_uj.setObjectName("pushButton_uj")
        x.pushButton_modosit = QtWidgets.QPushButton(x.tab_leiras)
        x.pushButton_modosit.setGeometry(QtCore.QRect(170, 20, 101, 31))
        x.pushButton_modosit.setObjectName("pushButton_modosit")
        x.pushButton_torol = QtWidgets.QPushButton(x.tab_leiras)
        x.pushButton_torol.setGeometry(QtCore.QRect(290, 20, 101, 31))
        x.pushButton_torol.setObjectName("pushButton_torol")
        x.tableWidget = QtWidgets.QTableWidget(x.tab_leiras)
        x.tableWidget.setGeometry(QtCore.QRect(10, 70, 431, 261))
        x.tableWidget.setRowCount(5)
        x.tableWidget.setObjectName("tableWidget")
        x.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(3, item)
        x.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        x.tableWidget.horizontalHeader().setStretchLastSection(True)
        x.tabWidget.addTab(x.tab_leiras, "")
        Ui_Mutatok_Modosit.setCentralWidget(x.centralwidget)
        x.statusbar = QtWidgets.QStatusBar(Ui_Mutatok_Modosit)
        x.statusbar.setObjectName("statusbar")
        Ui_Mutatok_Modosit.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Mutatok_Modosit)
        x.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Ui_Mutatok_Modosit)

    def retranslateUi(x, Ui_Mutatok_Modosit):
        _translate = QtCore.QCoreApplication.translate
        Ui_Mutatok_Modosit.setWindowTitle(_translate("Ui_Mutatok_Modosit", "Mutató módosítása"))
        x.pushButton_Mentes.setText(_translate("Ui_Mutatok_Modosit", "Mentés"))
        x.pushButton_Megse.setText(_translate("Ui_Mutatok_Modosit", "Mégse"))
        x.label_8.setText(_translate("Ui_Mutatok_Modosit", "Érvényesség vége:"))
        x.label_5.setText(_translate("Ui_Mutatok_Modosit", "Típus:"))
        x.label_2.setText(_translate("Ui_Mutatok_Modosit", "Nyomtatási címkéje:"))
        x.label_3.setText(_translate("Ui_Mutatok_Modosit", "Leírása:"))
        x.label_4.setText(_translate("Ui_Mutatok_Modosit", "Hossz:"))
        x.label.setText(_translate("Ui_Mutatok_Modosit", "Változó neve:"))
        x.label_6.setText(_translate("Ui_Mutatok_Modosit", "Mutató csoport:"))
        x.label_7.setText(_translate("Ui_Mutatok_Modosit", "Érvényesség kezdete:"))
        x.comboBox.setItemText(0, _translate("Ui_Mutatok_Modosit", "Egész szám"))
        x.comboBox.setItemText(1, _translate("Ui_Mutatok_Modosit", "Lebegőpontos szám"))
        x.comboBox.setItemText(2, _translate("Ui_Mutatok_Modosit", "Dátum"))
        x.tabWidget.setTabText(x.tabWidget.indexOf(x.tab_attributum), _translate("Ui_Mutatok_Modosit", "Attribútumok"))
        x.pushButton_uj.setText(_translate("Ui_Mutatok_Modosit", "Új létrehozása"))
        x.pushButton_modosit.setText(_translate("Ui_Mutatok_Modosit", "Módosítás"))
        x.pushButton_torol.setText(_translate("Ui_Mutatok_Modosit", "Törlés"))
        item = x.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Mutatok_Modosit", "Nyelv"))
        item = x.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Mutatok_Modosit", "Címke"))
        item = x.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Ui_Mutatok_Modosit", "Leírás"))
        item = x.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Ui_Mutatok_Modosit", "Megjegyzés"))
        x.tabWidget.setTabText(x.tabWidget.indexOf(x.tab_leiras), _translate("Ui_Mutatok_Modosit", "Leírások"))"""
        

class newMutatDB(object):
    def newMutat(x):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        #c.execute('''DROP TABLE mutatok''')
        #c.execute('''CREATE TABLE mutatok
        #             (nev text, cimke text, leiras text, hossz real, csoport text)''')
        script = "INSERT INTO mutatok (nev, cimke, leiras, hossz, csoport) VALUES (?, ?, ?, ?, ?);"
        c.execute(script, (valtnev,cimke,leiras,hossz,csoport))
        #c.execute('''INSERT INTO mutatok VALUES
         #            (nev text, cimke text, leiras text, hossz real, tipus real)''')
                 # Save (commit) the changes
        conn.commit()
        #Closing the database
        conn.close()

    def listMutat():
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        #c.execute('''DROP TABLE mutatok''')
        #c.execute('''CREATE TABLE mutatok
        #             (nev text, cimke text, leiras text, hossz real, csoport text)''')
        global query
        query = c.execute('''SELECT * FROM mutatok''')
        #c.execute('''INSERT INTO mutatok VALUES
         #            (nev text, cimke text, leiras text, hossz real, tipus real)''')
                 # Save (commit) the changes
        conn.commit()
        #Closing the database
        #conn.close()