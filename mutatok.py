import sys
import traceback

import sip
sip.setapi('QString', 2)
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow, QLineEdit
from PyQt5.QtCore import pyqtSlot
from app_modules import *
import sqlite3

import datetime
from datetime import date
import pandas as pd
import numpy as np

valtnev = ""
cimke = ""
leiras = ""
hossz = 8
tipus = ""
csoport = ""
kepzett_e="Nem"
kezdoidopont = QtCore.QDate
vegidopont = QtCore.QDate
query = ()
class Ui_Mutatok(QtWidgets.QMainWindow):

    def setupUi(self,  Ui_Mutatok, nomen=False):
         self.ablak=Ui_Mutatok
         self.ablak.setObjectName("Mutatok_Ablak")
         self.ablak.resize(1175, 500)
         self.newMutatDB = DbConnectMutato()

         if not nomen:
            self.ablak.setWindowTitle("Mutatók kezelése")
         else:
             self.ablak.setWindowTitle("Nómenklatúrák kezelése")
         self.newmutatdb = DbConnectMutato()
         DbConnectMutato.listMutat(self.newmutatdb, nomen=nomen)
         
         self.tableWidget = QtWidgets.QTableWidget(self.ablak)
         self.tableWidgetSetUp(self.tableWidget, nomen=nomen)

         QtCore.QMetaObject.connectSlotsByName(self.ablak)

         self.pushButton_uj = QtWidgets.QPushButton(self.ablak)
         self.pushButton_modosit = QtWidgets.QPushButton(self.ablak)
         self.pushButton_torol = QtWidgets.QPushButton(self.ablak)
         self.pushButton_export = QtWidgets.QPushButton(self.ablak)
         self.pushButtonSetUp(self.pushButton_uj,self.pushButton_modosit,self.pushButton_torol,self.pushButton_export)

         self.valtoztatUi(self.ablak, nomen=nomen)

         self.pushButton_uj.clicked.connect(lambda: self.openUjMutato(nomen=nomen)) #ez fogja megnyitni azt az ablakot amelyikkel uj sort vehetunk fel

         self.pushButton_modosit.clicked.connect(lambda: self.openModositMutato(nomen=nomen))#ez fogja megnyitni azt az ablakot amelyikkel modosithatunk a felvett adatokon

         self.pushButton_torol.clicked.connect(lambda: self.deleteCurrentRow(nomen=nomen))#ez fogja törölni a kiválasztott sort

         self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)#modosit torol gomb allapot valtozasahoz

         self.tableWidget.selectionModel().selectionChanged.connect(lambda: self.on_selection_changed())

         self.radioButton_export_csv = QtWidgets.QRadioButton(self.ablak)
         self.radioButton_export_csv.setGeometry(QtCore.QRect(550, 26, 110, 23))
         self.radioButtonSetUp(self.radioButton_export_csv, "RadioButtonCsv", "Csv", checked=True)

         self.radioButton_export_excel = QtWidgets.QRadioButton(self.ablak)
         self.radioButtonSetUp(self.radioButton_export_excel, "RadioButtonExcel", "Excel")
         self.radioButton_export_excel.setGeometry(QtCore.QRect(600, 26, 110, 23))

         self.pushButton_export.clicked.connect(lambda: self.radio_button_checked(nomen=nomen))

         self.on_selection_changed()

    def tableWidgetSetUp(self, tableWidget, oszlopszam=9, nomen=False):
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.setGeometry(QtCore.QRect(60, 75, 1025, 370))
        tableWidget.setAlternatingRowColors(True)
        tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tableWidget.setObjectName("tableWidget")

        tableWidget.setColumnCount(oszlopszam)
        tableWidget.setRowCount(0)
        for i in range(oszlopszam):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setHorizontalHeaderItem(i, item)


    def pushButtonSetUp(self, pushButton_uj, pushButton_modosit, pushButton_torol, pushButton_export):
        pushButton_uj.setGeometry(QtCore.QRect(60, 26, 91, 23))
        pushButton_uj.setObjectName("pushButton_uj")  # uj
        pushButton_uj.setDefault(True)  # ez lesz az alapertelmezett gomb
        pushButton_modosit.setGeometry(QtCore.QRect(181, 26, 91, 23))
        pushButton_modosit.setObjectName("pushButton_modosit")  # modosit
        pushButton_torol.setGeometry(QtCore.QRect(302, 26, 91, 23))
        pushButton_torol.setObjectName("pushButton_torol")  # torol
        pushButton_export.setGeometry(QtCore.QRect(423, 26, 110, 23))
        pushButton_export.setObjectName("pushButton_export")  # exportal

    def radioButtonSetUp(self, button, nev, text, checked=False):
        button.setObjectName(nev)
        button.setText(text)
        button.setChecked(checked)

    def radio_button_checked(self, nomen=None):
        if self.radioButton_export_csv.isChecked():
            kiterjesztes = "CSV fájl (*.csv)"
        else:
            kiterjesztes="Excel fájl (*.xlsx)"
        self.newmutatdb.exportMutat(self, kiterjesztes=kiterjesztes, nomen=nomen)
                  
        
    def on_selection_changed(self):
        self.pushButton_modosit.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_torol.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )

    def valtoztatUi(self, Ui_Mutatok, nomen=False):
         global query
         _translate = QtCore.QCoreApplication.translate
         if not nomen:
            Ui_Mutatok.setWindowTitle(_translate("Ui_Mutatok", "Mutatók"))
         else:
             Ui_Mutatok.setWindowTitle(_translate("Ui_Mutatok", "Nómenklatúrák"))

         oszlopnevek=["Változó neve","Nyomtatási cimke","Leírás","Hossz","Típus","Mutató csoport","Utolsó módosítás","Érvényesség kezdete","Érvényesség vége"]
         if nomen:
             oszlopnevek = ["Változó neve", "Nyomtatási cimke", "Leírás", "Hossz", "Típus", "Képzett",
                            "Utolsó módosítás", "Érvényesség kezdete", "Érvényesség vége"]

         for row in query:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            for oszlop in range(len(oszlopnevek)):
                self.tableWidget.setItem(rows, oszlop, QTableWidgetItem(str(row[oszlop])))
                if row[oszlop] == 0:
                    self.tableWidget.setItem(rows, oszlop, QTableWidgetItem("Nem"))
                if row[oszlop] == 1:
                    self.tableWidget.setItem(rows, oszlop, QTableWidgetItem("Igen"))

         self.oszlopNevBeallitas(oszlopnevek)
         self.tableWidget.resizeColumnsToContents()

         # __sortingEnabled = self.tableWidget.isSortingEnabled()
         # self.tableWidget.setSortingEnabled(False)
         #
         # self.tableWidget.setSortingEnabled(__sortingEnabled)
         self.pushButton_uj.setText(_translate(self.pushButton_uj.objectName(), "Új létrehozása"))
         self.pushButton_modosit.setText(_translate(self.pushButton_modosit.objectName(), "Módosítás"))
         self.pushButton_torol.setText(_translate(self.pushButton_torol.objectName(), "Törlés"))
         self.pushButton_export.setText(_translate(self.pushButton_export.objectName(), "Kijelöltek exportja"))

    def oszlopNevBeallitas(self, oszlopnevek):
        oszlopszam = 0
        for oszlopnev in oszlopnevek:
            item = self.tableWidget.horizontalHeaderItem(oszlopszam)
            item.setText(oszlopnev)
            oszlopszam+=1

    def openUjMutato(self, nomen=False):#definialjuk az uj mutato letrehozasa ablakot #ez nyitja meg
         self.window = QtWidgets.QMainWindow()
         self.ui =  Ui_Mutatok_UJ()
         self.ui.setupUi(self, nomen=nomen)
         self.window.show()

    def openModositMutato(self, nomen=False):#es definialjuk a modosit mutato ablakot
         self.window = QtWidgets.QMainWindow()
         self.ui =  Ui_Mutatok_UJ()
         self.ui.setupModositUi(self.window, self, nomen=nomen)
    
    def deleteCurrentRow(self, nomen=False):
        result = QtWidgets.QMessageBox.question(self,
                      "Törlés megerősítése...",
                      "Biztos ki akarod törölni a kiválaszott sorokat?",
                      QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        

        if result == QtWidgets.QMessageBox.Yes:
            indexes = self.tableWidget.selectionModel().selectedRows()
            conn = sqlite3.connect('datagov.db')
            cursor=conn.cursor()
            lista=[]
            if nomen:
                for index in sorted(indexes):
                    cursor.execute("DELETE from nomenklaturak WHERE nev = '"+(self.tableWidget.item(index.row(),0).text())+"'")
                    lista.append(index.row())
            else:
                for index in sorted(indexes):
                    cursor.execute("DELETE from mutatok WHERE nev = '"+(self.tableWidget.item(index.row(),0).text())+"'")
                    lista.append(index.row())
            i=0
            for elem in lista:
                self.tableWidget.removeRow(elem-i)
                i+=1
            conn.commit()
            conn.close()

def addNewRow(ablak,lista):#tábla frissítése a beszúrás után
    pozicio=ablak.tableWidget.rowCount()
    i=0
    ablak.tableWidget.insertRow(pozicio)
    for elem in lista:
        ablak.tableWidget.setItem(pozicio,i, QTableWidgetItem(elem))
        i+=1
    ablak.tableWidget.setRowCount(pozicio+1)

#ez az uj mutato felvetel ablaka
class Ui_Mutatok_UJ(object):

    def setupModositUi(self, Ui_Mutatok_UJ, parentAblak, nomen=False):
        indexes = parentAblak.tableWidget.selectionModel().selectedRows()
        if (len(indexes) > 1):
            QtWidgets.QMessageBox.question(parentAblak,
                                                    "Kérlek csak egy sort jelölj ki!",
                                                    "Nem tudsz egyszerre több soron is változtatni!",
                                                    QtWidgets.QMessageBox.Ok)
        else:
            self.setupUi(parentAblak, modosit=True, nomen=nomen)

    def setupUi(self, parentAblak, modosit=False, nomen=False):

        self.parentAblak=parentAblak
        self.ablak=parentAblak.window
        if not nomen:
            self.ablak.setObjectName("Uj mutatok ablak")
        else:
            self.ablak.setObjectName("Uj nomenklatura letrehozasa")
        self.ablak.resize(484, 466)
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Mentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mentes.setGeometry(QtCore.QRect(270, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)

        #mentés logika
        self.newMutatDB = DbConnectMutato()
        self.pushButton_Mentes.clicked.connect(lambda: self.save_text(modosit=modosit))
        self.pushButton_Mentes.setFont(font)
        self.pushButton_Mentes.setObjectName("pushButton_Mentes")
        self.pushButton_Mentes.clicked.connect(lambda: self.newMutatDB.newMutat(parentAblak,modosit=modosit, nomen=nomen))

        self.pushButton_Megse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Megse.setGeometry(QtCore.QRect(370, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Megse.setFont(font)
        self.pushButton_Megse.setDefault(True)
        self.pushButton_Megse.setObjectName("pushButton_Megse")
        self.pushButton_Megse.clicked.connect(lambda: self.ablak.close())

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")


        self.valtozonevLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.valtozonevLabel, 40, 10, 161, 31, "valtozonevLabel")

        self.cimkeLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.cimkeLabel, 40, 50, 161, 31, "cimkeLabel")

        self.leirasLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.leirasLabel,40, 90, 161, 31, "leirasLabel")

        self.hosszLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.hosszLabel, 40, 130, 161, 31, "hosszLabel")

        self.tipusLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.tipusLabel, 40, 170, 161, 31, "tipusLabel")
        if not nomen:
            self.csoportLabel = QtWidgets.QLabel(self.tab)
            self.labelSetUp(self.csoportLabel, 40, 200, 161, 51, "csoportLabel")

        self.ervenyessegKezdetLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.ervenyessegKezdetLabel, 40, 250, 161, 31, "ervenyessegKezdetLabel")

        self.ervenyessegVegeLabel = QtWidgets.QLabel(self.tab)
        self.labelSetUp(self.ervenyessegVegeLabel, 40, 280, 161, 41, "ervenyessegVegeLabel")

        self.dateEdit_veg = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_veg.setGeometry(QtCore.QRect(220, 290, 151, 31))
        self.dateEdit_veg.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_veg.setCalendarPopup(True)
        self.dateEdit_veg.setObjectName("dateEdit_veg")
        if not nomen:
            self.lineEdit_csoport = QtWidgets.QLineEdit(self.tab)
            self.lineEdit_csoport.setGeometry(QtCore.QRect(220, 210, 201, 31))
            self.lineEdit_csoport.setObjectName("lineEdit_csoport")
        self.dateEdit_kezdet = QtWidgets.QDateEdit(self.tab)
        self.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 250, 151, 31))
        self.dateEdit_kezdet.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_kezdet.setCalendarPopup(True)
        self.dateEdit_kezdet.setObjectName("dateEdit_kezdet")
        self.lineEdit_leiras = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_leiras.setGeometry(QtCore.QRect(220, 90, 201, 31))
        self.lineEdit_leiras.setObjectName("lineEdit_leiras")
        self.lineEdit_valtozonev = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_valtozonev.setGeometry(QtCore.QRect(220, 10, 201, 31))
        self.lineEdit_valtozonev.setObjectName("lineEdit_valtozonev")

        if modosit:
            self.lineEdit_valtozonev.setReadOnly(True)
            self.lineEdit_valtozonev.setStyleSheet("QLineEdit"
                                    "{"
                                    "background : lightgray;"
                                    "}")
        self.lineEdit_cimke = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_cimke.setGeometry(QtCore.QRect(220, 50, 201, 31))
        self.lineEdit_cimke.setObjectName("lineEdit_cimke")
        self.lineEdit_hossz = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_hossz.setGeometry(QtCore.QRect(220, 130, 201, 31))
        self.lineEdit_hossz.setObjectName("lineEdit_hossz")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(220, 170, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tabWidget.addTab(self.tab, "")
        self.ablak.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(self.ablak, modosit, parentAblak=parentAblak, nomen=nomen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)
        # parentAblak.window.setWindowTitle("Kiválasztott mutató módosítása")
        parentAblak.window.show()

    def labelSetUp(self, label, kezdopont_x, kezdopont_y, hossz_x, hossz_y, nev):
        label.setGeometry(QtCore.QRect(kezdopont_x, kezdopont_y, hossz_x, hossz_y))
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        label.setObjectName(nev)

    def save_text(self, modosit=False):
        global valtnev, cimke, leiras, hossz, tipus, csoport, kepzett_e, kezdoidopont, vegidopont
        valtnev = self.lineEdit_valtozonev.text()
        cimke = self.lineEdit_cimke.text()
        leiras = self.lineEdit_leiras.text()
        hossz= self.lineEdit_hossz.text()
        tipus=self.comboBox.currentText()
        try:
            csoport = self.lineEdit_csoport.text()
        except Exception:
            pass # nomen
        kezdoidopont=self.dateEdit_kezdet.date().toPyDate()
        vegidopont=self.dateEdit_veg.date().toPyDate()
        if not modosit:
            kepzett_e="Nem"
        try:
            self.ablak.close()
        except Exception as e:
            print(e)

    def retranslateUi(self, Ui_Mutatok_UJ, modosit, parentAblak=None, nomen=False):
        # a translate-nek most még nem igazán van értelme, majd ha angolra vagy németre is akarnánk fordítani az oldalt akkor kellhet, most egyelőre így hagyom
        _translate = QtCore.QCoreApplication.translate
        if not modosit and not nomen:
            Ui_Mutatok_UJ.setWindowTitle(_translate(Ui_Mutatok_UJ.objectName(), "Mutató létrehozása"))
        if not modosit and nomen:
            Ui_Mutatok_UJ.setWindowTitle(_translate(Ui_Mutatok_UJ.objectName(),"Nómenklatúra létrehozása"))
        self.pushButton_Mentes.setText(_translate(self.pushButton_Mentes.objectName(), "Mentés"))
        self.pushButton_Megse.setText(_translate(self.pushButton_Megse.objectName(), "Mégse"))

        self.valtozonevLabel.setText(_translate(self.valtozonevLabel.objectName(), "Változó neve:"))
        self.cimkeLabel.setText(_translate(self.cimkeLabel.objectName(), "Nyomtatási címkéje:"))
        self.leirasLabel.setText(_translate(self.leirasLabel.objectName(), "Leírása:"))
        self.hosszLabel.setText(_translate(self.hosszLabel.objectName(), "Hossz:"))
        self.tipusLabel.setText(_translate(self.tipusLabel.objectName(), "Típus:"))
        if not nomen:
            self.csoportLabel.setText(_translate(self.csoportLabel.objectName(), "Mutató csoport:"))
        self.ervenyessegKezdetLabel.setText(_translate(self.ervenyessegKezdetLabel.objectName(), "Érvényesség kezdete:"))
        self.ervenyessegVegeLabel.setText(_translate(self.ervenyessegVegeLabel.objectName(), "Érvényesség vége:"))

        self.comboBox.setItemText(0, _translate(self.comboBox.itemText(0), "Egész szám"))
        self.comboBox.setItemText(1, _translate(self.comboBox.itemText(1), "Lebegőpontos szám"))
        self.comboBox.setItemText(2, _translate(self.comboBox.itemText(2), "Dátum"))
        self.comboBox.setItemText(3, _translate(self.comboBox.itemText(3), "Szöveg"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate(self.tabWidget.objectName(), "Attribútumok"))

        if modosit and parentAblak is not None:
            indexes = parentAblak.tableWidget.selectionModel().selectedRows()
            if not nomen:
                Ui_Mutatok_UJ.setWindowTitle(_translate(Ui_Mutatok_UJ.objectName(), "Kiválasztott mutató módosítása"))
            else:
                Ui_Mutatok_UJ.setWindowTitle(_translate(Ui_Mutatok_UJ.objectName(), "Kiválasztott nómenklatúra módosítása"))
            for index in sorted(indexes):
                valtnev=parentAblak.tableWidget.item(index.row(),0).text()
                cimke=parentAblak.tableWidget.item(index.row(),1).text()
                leiras=parentAblak.tableWidget.item(index.row(),2).text()
                hossz=parentAblak.tableWidget.item(index.row(),3).text()
                tipus=parentAblak.tableWidget.item(index.row(),4).text()
                if not nomen:
                    csoport=parentAblak.tableWidget.item(index.row(),5).text()
                    self.lineEdit_csoport.setText(csoport)
                kezdoidopont=parentAblak.tableWidget.item(index.row(),7).text()
                vegidopont=parentAblak.tableWidget.item(index.row(),8).text()
                self.lineEdit_valtozonev.setText(valtnev)
                self.lineEdit_cimke.setText(cimke)
                self.lineEdit_leiras.setText(leiras)
                self.lineEdit_hossz.setText(hossz)
                self.comboBox.setCurrentText(tipus)
                self.dateEdit_kezdet.setDate(datetime.datetime.strptime(kezdoidopont,'%Y-%m-%d'))
                self.dateEdit_veg.setDate(datetime.datetime.strptime(vegidopont,'%Y-%m-%d'))

class DbConnectMutato(object):

    def exportMutat(self, parentablak, kiterjesztes, nomen=False):
        self.parentAblak=parentablak
        if self.parentAblak.tableWidget.selectionModel().hasSelection():
            rows= self.parentAblak.tableWidget.selectionModel().selectedRows()
            exportalando_dataframe=pd.DataFrame({'nev':[],
                         'cimke':[],
                         'leiras':[],
                         'hossz':[],
                         'tipus':[],
                         'csoport':[],
                         'utolso_modositas':[],
                         'kezdoidopont':[],
                         'vegidopont':[]})
            if nomen:
                exportalando_dataframe = pd.DataFrame({'nev': [],'cimke': [],'leiras': [],'hossz': [],'tipus': [],
                                                       'kepzett_e':[],
                                                       'utolso_modositas': [],'kezdoidopont': [],'vegidopont': []})

            for elem in sorted(rows):
                if not nomen:
                    exportalando_dataframe=exportalando_dataframe.append({'nev':self.parentAblak.tableWidget.item(elem.row(),0).text(),
                                                                      'cimke':self.parentAblak.tableWidget.item(elem.row(),1).text(),
                                                                      'leiras':self.parentAblak.tableWidget.item(elem.row(),2).text(),
                                                                      'hossz':self.parentAblak.tableWidget.item(elem.row(),3).text(),
                                                                      'tipus':self.parentAblak.tableWidget.item(elem.row(),4).text(),
                                                                      'csoport':self.parentAblak.tableWidget.item(elem.row(),5).text(),
                                                                      'utolso_modositas':self.parentAblak.tableWidget.item(elem.row(),6).text(),
                                                                      'kezdoidopont':self.parentAblak.tableWidget.item(elem.row(),7).text(),
                                                                      'vegidopont':self.parentAblak.tableWidget.item(elem.row(),8).text()}, ignore_index=True)
                else:
                    exportalando_dataframe = exportalando_dataframe.append(
                        {'nev': self.parentAblak.tableWidget.item(elem.row(), 0).text(),
                         'cimke': self.parentAblak.tableWidget.item(elem.row(), 1).text(),
                         'leiras': self.parentAblak.tableWidget.item(elem.row(), 2).text(),
                         'hossz': self.parentAblak.tableWidget.item(elem.row(), 3).text(),
                         'tipus': self.parentAblak.tableWidget.item(elem.row(), 4).text(),
                         'kepzett_e': self.parentAblak.tableWidget.item(elem.row(), 5).text(),
                         'utolso_modositas': self.parentAblak.tableWidget.item(elem.row(), 6).text(),
                         'kezdoidopont': self.parentAblak.tableWidget.item(elem.row(), 7).text(),
                         'vegidopont': self.parentAblak.tableWidget.item(elem.row(), 8).text()}, ignore_index=True)

            exportalando_dataframe.index +=1
        else:
            conn = sqlite3.connect('datagov.db', isolation_level=None)
            if not nomen:
                exportalando_dataframe =pd.DataFrame(pd.read_sql_query("SELECT * FROM mutatok", conn))
            else:
                exportalando_dataframe =pd.DataFrame(pd.read_sql_query("SELECT nev, cimke, leiras, hossz, tipus, kepzett_e,utolso_modositas, kezdoidopont, vegidopont FROM nomenklaturak", conn))
            exportalando_dataframe.index += 1

        fajl_nev=QtWidgets.QFileDialog.getSaveFileUrl(caption="Fájl mentése "+kiterjesztes+"-ként", filter=kiterjesztes, initialFilter=kiterjesztes)
        try:
            if kiterjesztes=="CSV fájl (*.csv)":
                exportalando_dataframe.to_csv(QtCore.QUrl.toLocalFile(fajl_nev[0]))
            else:
                exportalando_dataframe.to_excel(QtCore.QUrl.toLocalFile(fajl_nev[0]))
        except Exception as e:
            print("Nem lett szabályosan megadva útvónal")


    def newMutat(self, parentAblak, modosit=False, nomen=False):
        self.parentAblak=parentAblak
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        try:
            if not nomen:
                sor=c.execute("SELECT * FROM mutatok WHERE nev='"+valtnev+"'")
            else:
                sor=c.execute("select * from nomenklaturak where nev='"+valtnev+"'")
            for elem in sor: # lényegében ezzek ellenőrzöm hogy van e már ilyen sor az adatbázisban
                 if not modosit:
                     raise Exception("Már van ilyen változónév")
                 else:
                     if not nomen:
                        c.execute("UPDATE mutatok SET cimke='"+cimke+"', leiras='"+leiras+"', hossz='"+hossz+"', tipus='"+tipus+"', csoport='"+csoport+"', utolso_modositas='"+str(date.today())+"', kezdoidopont='"+str(kezdoidopont)+"', vegidopont='"+str(vegidopont)+"' WHERE nev='"+valtnev+"';")
                     else:
                         c.execute(
                             "UPDATE nomenklaturak SET cimke='" + cimke + "', leiras='" + leiras + "', hossz='" + hossz + "', tipus='" + tipus + "', utolso_modositas='" + str(
                                 date.today()) + "', kezdoidopont='" + str(kezdoidopont) + "', vegidopont='" + str(
                                 vegidopont) + "' WHERE nev='" + valtnev + "';")

                     indexek=self.parentAblak.tableWidget.selectionModel().selectedRows()
                     for index in indexek:
                         self.parentAblak.tableWidget.setItem(index.row(), 1, QTableWidgetItem(cimke))
                         self.parentAblak.tableWidget.setItem(index.row(), 2, QTableWidgetItem(leiras))
                         self.parentAblak.tableWidget.setItem(index.row(), 3, QTableWidgetItem(hossz))
                         self.parentAblak.tableWidget.setItem(index.row(), 4, QTableWidgetItem(tipus))
                         if nomen:
                             str_kepzett_e = c.execute("select kepzett_e from nomenklaturak where nev='"+valtnev+"'")
                             global kepzett_e
                             for elem in str_kepzett_e:
                                 kepzett_e="Nem"
                                 if elem[0]==1:
                                     kepzett_e="Igen"
                             self.parentAblak.tableWidget.setItem(index.row(), 5, QTableWidgetItem(kepzett_e))
                         else:
                             self.parentAblak.tableWidget.setItem(index.row(), 5, QTableWidgetItem(csoport))
                         self.parentAblak.tableWidget.setItem(index.row(), 6, QTableWidgetItem(str(date.today())))
                         self.parentAblak.tableWidget.setItem(index.row(), 7, QTableWidgetItem(str(kezdoidopont)))
                         self.parentAblak.tableWidget.setItem(index.row(), 8, QTableWidgetItem(str(vegidopont)))

            if not modosit:
                if not nomen:
                    script = "INSERT INTO mutatok (nev, cimke, leiras, hossz, tipus, csoport, utolso_modositas, kezdoidopont, vegidopont) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
                    c.execute(script,
                              (valtnev, cimke, leiras, hossz, tipus, csoport, str(date.today()), kezdoidopont, vegidopont))
                else:
                    script = "INSERT INTO nomenklaturak (nev, cimke, leiras, hossz, tipus, kepzett_e, elsodleges_kepzett_nev, masodlagos_kepzett_nev, utolso_modositas, kezdoidopont, vegidopont) VALUES (?, ?, ?, ?, ?, 0, '', '', ?, ?, ?);"
                    c.execute(script,
                              (valtnev, cimke, leiras, hossz, tipus, str(date.today()), kezdoidopont, vegidopont))

                conn.commit()
                conn.close()

                # ez a frissítéshez van
                if nomen:
                    addNewRow(self.parentAblak, [valtnev, cimke, leiras, hossz, tipus, kepzett_e, str(date.today()), str(kezdoidopont),str(vegidopont)])
                else:
                    addNewRow(self.parentAblak, [valtnev, cimke, leiras, hossz, tipus, csoport, str(date.today()), str(kezdoidopont),str(vegidopont)])
        except Exception as e:
            print(traceback.format_exc())
            QtWidgets.QMessageBox.question(parentAblak,"Ez a változónév már létezik", "Kérlek próbálkozz egy másik változónévvel", QtWidgets.QMessageBox.Ok)


    def listMutat(self, nomen=False):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        cursor = conn.cursor()
        global query
        # c.execute('''CREATE TABLE nomenklaturak
        #                     (nev text, cimke text, leiras text, hossz integer , tipus text, csoport text,utolso_modositas date, kezdoidopont date, vegidopont date)''')

        if not nomen:
            query = cursor.execute('SELECT * FROM mutatok;')
        else:
            query = cursor.execute('select nev, cimke, leiras, hossz, tipus,kepzett_e,utolso_modositas, kezdoidopont, vegidopont  from nomenklaturak;')
        conn.commit()

        # conn.close() #Closing the database, valamiért ezzel kifagy az egész
