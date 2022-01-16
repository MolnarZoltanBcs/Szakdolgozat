import sys
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
hossz = 0.0
tipus = ""
csoport = ""
kezdoidopont = QtCore.QDate
vegidopont = QtCore.QDate
query = ()
class Ui_Mutatok(QtWidgets.QMainWindow):

    def setupUi(x,  Ui_Mutatok):
         x.ablak=Ui_Mutatok
         x.ablak.setObjectName("Ui_Mutatok")
         x.ablak.resize(1175, 500)
         
         x.ablak.setWindowTitle("Mutatók kezelése")
         x.newmutatdb = newMutatDB()
         newMutatDB.listMutat(x.newmutatdb)
         
         x.tableWidget = QtWidgets.QTableWidget(x.ablak)
         x.tableWidgetSetUp(x.tableWidget)

         QtCore.QMetaObject.connectSlotsByName(x.ablak)

         x.pushButton_uj = QtWidgets.QPushButton(x.ablak)
         x.pushButton_modosit = QtWidgets.QPushButton(x.ablak)
         x.pushButton_torol = QtWidgets.QPushButton(x.ablak)
         x.pushButton_export = QtWidgets.QPushButton(x.ablak)
         x.pushButtonSetUp(x.pushButton_uj,x.pushButton_modosit,x.pushButton_torol,x.pushButton_export)

         x.valtoztatUi(x.ablak)

         x.pushButton_uj.clicked.connect(x.openUjMutato) #ez fogja megnyitni azt az ablakot amelyikkel uj sort vehetunk fel

         x.pushButton_modosit.clicked.connect(x.openModositMutato)#ez fogja megnyitni azt az ablakot amelyikkel modosithatunk a felvett adatokon

         x.pushButton_torol.clicked.connect(x.deleteCurrentRow)#ez fogja törölni a kiválasztott sort

         x.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)#modosit torol gomb allapot valtozasahoz

         x.tableWidget.selectionModel().selectionChanged.connect(x.on_selection_changed)

         x.radioButton_export_csv = QtWidgets.QRadioButton(x.ablak)
         x.radioButton_export_csv.setGeometry(QtCore.QRect(550, 26, 110, 23))
         x.radioButtonSetUp(x.radioButton_export_csv, "RadioButtonCsv", "Csv", checked=True)

         x.radioButton_export_excel = QtWidgets.QRadioButton(x.ablak)
         x.radioButtonSetUp(x.radioButton_export_excel, "RadioButtonExcel", "Excel")
         x.radioButton_export_excel.setGeometry(QtCore.QRect(600, 26, 110, 23))

         x.pushButton_export.clicked.connect(lambda: x.radio_button_checked())
 
         x.on_selection_changed()

    def tableWidgetSetUp(self, tableWidget):
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.setGeometry(QtCore.QRect(60, 75, 1025, 370))
        tableWidget.setAlternatingRowColors(True)
        tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tableWidget.setObjectName("tableWidget")

        tableWidget.setColumnCount(9)
        tableWidget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(8, item)

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

    def radio_button_checked(self):
        if self.radioButton_export_csv.isChecked():
            kiterjesztes = "CSV fájl (*.csv)"
        else:
            kiterjesztes="Excel fájl (*.xlsx)"
        self.newmutatdb.exportMutat(self, kiterjesztes=kiterjesztes)
                  
        
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
         x.newMutatDB = newMutatDB()

         for row in query:
            rows = x.tableWidget.rowCount()
            x.tableWidget.setRowCount(rows + 1)
            for oszlop in range(9):
                x.tableWidget.setItem(rows, oszlop, QTableWidgetItem(str(row[oszlop])))

         oszlopnevek=["Változó neve","Nyomtatási cimke","Leírás","Hossz","Típus","Mutató csoport","Utolsó módosítás","Érvényesség kezdete","Érvényesség vége"]
         x.oszlopNevBeallitas(oszlopnevek)
         #x.tableWidget.resizeColumnsToContents()

         __sortingEnabled = x.tableWidget.isSortingEnabled()#ezt a két sort még nem értem miért kellett belerakni, nem én csináltam de nem tudom mi a változás szóval meghagyom
         x.tableWidget.setSortingEnabled(False)

         x.tableWidget.setSortingEnabled(__sortingEnabled)
         x.pushButton_uj.setText(_translate("Ui_Mutatok", "Új létrehozása"))
         x.pushButton_modosit.setText(_translate("Ui_Mutatok", "Módosítás"))
         x.pushButton_torol.setText(_translate("Ui_Mutatok", "Törlés"))
         x.pushButton_export.setText(_translate("Ui_Mutatok", "Kijelöltek exportja"))

    def oszlopNevBeallitas(self, oszlopnevek):
        oszlopszam = 0
        for oszlopnev in oszlopnevek:
            item = self.tableWidget.horizontalHeaderItem(oszlopszam)
            item.setText(oszlopnev)
            oszlopszam+=1

    def openUjMutato(x):#definialjuk az uj mutato letrehozasa ablakot #ez nyitja meg
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Mutatok_UJ()
         x.ui.setupUi(x.window, x)
         x.window.show()

    def openModositMutato(x):#es definialjuk a modosit mutato ablakot
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Mutatok_UJ()
         x.ui.setupModositUi(x.window, x)
    
    def deleteCurrentRow(self):
        result = QtWidgets.QMessageBox.question(self,
                      "Törlés megerősítése...",
                      "Biztos ki akarod törölni a kiválaszott sorokat?",
                      QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        

        if result == QtWidgets.QMessageBox.Yes:
            indexes = self.tableWidget.selectionModel().selectedRows()
            conn = sqlite3.connect('datagov.db')
            cursor=conn.cursor()
            lista=[]
            for index in sorted(indexes):
                cursor.execute("DELETE from mutatok WHERE nev = '"+(self.tableWidget.item(index.row(),0).text())+"'")
                lista.append(index.row())
            i=0
            for elem in lista:
                self.tableWidget.removeRow(elem-i)
                i+=1
            conn.commit()
            conn.close()

def addNewRow(ablak,valtnev,cimke,leiras,hossz, tipus, csoport, today, kezdoidopont, vegidopont):#tábla frissítése a beszúrás után
    item = QtWidgets.QTableWidgetItem()
    pozicio=ablak.tableWidget.rowCount()
    ablak.tableWidget.insertRow(pozicio)
    ablak.tableWidget.setItem(pozicio,0, QTableWidgetItem(valtnev))
    ablak.tableWidget.setItem(pozicio,1, QTableWidgetItem(cimke))
    ablak.tableWidget.setItem(pozicio,2, QTableWidgetItem(leiras))
    ablak.tableWidget.setItem(pozicio,3, QTableWidgetItem(hossz))
    ablak.tableWidget.setItem(pozicio,4, QTableWidgetItem(tipus))
    ablak.tableWidget.setItem(pozicio,5, QTableWidgetItem(csoport))
    ablak.tableWidget.setItem(pozicio,6, QTableWidgetItem(today))
    ablak.tableWidget.setItem(pozicio,7, QTableWidgetItem(kezdoidopont))
    ablak.tableWidget.setItem(pozicio,8, QTableWidgetItem(vegidopont))

    ablak.tableWidget.setRowCount(pozicio+1)

#ez az uj mutato felvetel ablaka
class Ui_Mutatok_UJ(object):

    def setupModositUi(self, Ui_Mutatok_UJ, parentAblak):
        indexes = parentAblak.tableWidget.selectionModel().selectedRows()
        if (len(indexes) > 1):
            result = QtWidgets.QMessageBox.question(parentAblak,
                                                    "Kérlek csak egy sort jelölj ki!",
                                                    "Nem tudsz egyszerre több soron is változtatni!",
                                                    QtWidgets.QMessageBox.Ok)
        else:
            self.setupUi(Ui_Mutatok_UJ,parentAblak, modosit=True)

    def setupUi(x, Ui_Mutatok_UJ, parentAblak, modosit=False):

        x.parentAblak=parentAblak
        x.ablak=Ui_Mutatok_UJ
        x.ablak.setObjectName("Uj mutatok ablak")
        x.ablak.resize(484, 466)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
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
        x.pushButton_Mentes.clicked.connect(lambda: x.newMutatDB.newMutat(x.parentAblak,modosit=modosit))

        x.pushButton_Megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Megse.setGeometry(QtCore.QRect(370, 400, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Megse.setFont(font)
        x.pushButton_Megse.setDefault(True)
        x.pushButton_Megse.setObjectName("pushButton_Megse")
        x.pushButton_Megse.clicked.connect(lambda: x.ablak.close())

        x.tabWidget = QtWidgets.QTabWidget(x.centralwidget)
        x.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 371))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.tabWidget.setFont(font)
        x.tabWidget.setObjectName("tabWidget")
        x.tab = QtWidgets.QWidget()
        x.tab.setObjectName("tab")


        x.valtozonevLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.valtozonevLabel, 40, 10, 161, 31, "valtozonevLabel")

        x.cimkeLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.cimkeLabel, 40, 50, 161, 31, "cimkeLabel")

        x.leirasLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.leirasLabel,40, 90, 161, 31, "leirasLabel")
        x.hosszLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.hosszLabel, 40, 130, 161, 31, "hosszLabel")

        x.tipusLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.tipusLabel, 40, 170, 161, 31, "tipusLabel")

        x.csoportLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.csoportLabel, 40, 200, 161, 51, "csoportLabel")

        x.ervenyessegKezdetLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.ervenyessegKezdetLabel, 40, 250, 161, 31, "ervenyessegKezdetLabel")

        x.ervenyessegVegeLabel = QtWidgets.QLabel(x.tab)
        x.labelSetUp(x.ervenyessegVegeLabel, 40, 280, 161, 41, "ervenyessegVegeLabel")

        x.dateEdit_veg = QtWidgets.QDateEdit(x.tab)
        x.dateEdit_veg.setGeometry(QtCore.QRect(220, 290, 151, 31))
        x.dateEdit_veg.setDateTime(QtCore.QDateTime.currentDateTime())
        x.dateEdit_veg.setCalendarPopup(True)
        x.dateEdit_veg.setObjectName("dateEdit_veg")
        x.lineEdit_csoport = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_csoport.setGeometry(QtCore.QRect(220, 210, 201, 31))
        x.lineEdit_csoport.setObjectName("lineEdit_csoport")
        x.dateEdit_kezdet = QtWidgets.QDateEdit(x.tab)
        x.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 250, 151, 31))
        x.dateEdit_kezdet.setDateTime(QtCore.QDateTime.currentDateTime())
        x.dateEdit_kezdet.setCalendarPopup(True)
        x.dateEdit_kezdet.setObjectName("dateEdit_kezdet")
        x.lineEdit_leiras = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_leiras.setGeometry(QtCore.QRect(220, 90, 201, 31))
        x.lineEdit_leiras.setObjectName("lineEdit_leiras")
        x.lineEdit_valtozonev = QtWidgets.QLineEdit(x.tab)
        x.lineEdit_valtozonev.setGeometry(QtCore.QRect(220, 10, 201, 31))
        x.lineEdit_valtozonev.setObjectName("lineEdit_valtozonev")

        if modosit:
            x.lineEdit_valtozonev.setReadOnly(True)
            x.lineEdit_valtozonev.setStyleSheet("QLineEdit"
                                    "{"
                                    "background : lightgray;"
                                    "}")
            x.ablak.setWindowTitle("Kiválasztott mutató módosítása")
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
        x.ablak.setCentralWidget(x.centralwidget)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(x.ablak,  x.parentAblak)
        x.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)
        x.parentAblak.window.show()

    def labelSetUp(x, label, kezdopont_x, kezdopont_y, hossz_x, hossz_y, nev):
        label.setGeometry(QtCore.QRect(kezdopont_x, kezdopont_y, hossz_x, hossz_y))
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        label.setObjectName(nev)

    def save_text(x):
        global valtnev, cimke, leiras, hossz, tipus, csoport, kezdoidopont, vegidopont
        valtnev = x.lineEdit_valtozonev.text()
        cimke = x.lineEdit_cimke.text()
        leiras = x.lineEdit_leiras.text()
        hossz= x.lineEdit_hossz.text()
        tipus=x.comboBox.currentText()
        csoport = x.lineEdit_csoport.text()
        kezdoidopont=x.dateEdit_kezdet.date().toPyDate()
        vegidopont=x.dateEdit_veg.date().toPyDate()
        print(valtnev, cimke, leiras, hossz, tipus, csoport, str(kezdoidopont), str(vegidopont))
        try:
            x.ablak.close()
        except Exception as e:
            print(e)
            print("save_text hiba")

    def retranslateUi(x, Ui_Mutatok_UJ, modosit):
        # a translate-nek most még nem igazán van értelme, majd ha angolra vagy németre is akarnánk fordítani az oldalt akkor kellhet, most egyelőre így hagyom
        _translate = QtCore.QCoreApplication.translate
        if not modosit:
            Ui_Mutatok_UJ.setWindowTitle(_translate(Ui_Mutatok_UJ.objectName(), "Mutato letrehozasa"))
        x.pushButton_Mentes.setText(_translate(x.pushButton_Mentes.objectName(), "Mentés"))
        x.pushButton_Megse.setText(_translate(x.pushButton_Megse.objectName(), "Mégse"))

        x.valtozonevLabel.setText(_translate(x.valtozonevLabel.objectName(), "Változó neve:"))
        x.cimkeLabel.setText(_translate(x.cimkeLabel.objectName(), "Nyomtatási címkéje:"))
        x.leirasLabel.setText(_translate(x.leirasLabel.objectName(), "Leírása:"))
        x.hosszLabel.setText(_translate(x.hosszLabel.objectName(), "Hossz:"))
        x.tipusLabel.setText(_translate(x.tipusLabel.objectName(), "Típus:"))
        x.csoportLabel.setText(_translate(x.csoportLabel.objectName(), "Mutató csoport:"))
        x.ervenyessegKezdetLabel.setText(_translate(x.ervenyessegKezdetLabel.objectName(), "Érvényesség kezdete:"))
        x.ervenyessegVegeLabel.setText(_translate(x.ervenyessegVegeLabel.objectName(), "Érvényesség vége:"))

        x.comboBox.setItemText(0, _translate(x.comboBox.itemText(0), "Egész szám"))
        x.comboBox.setItemText(1, _translate(x.comboBox.itemText(1), "Lebegőpontos szám"))
        x.comboBox.setItemText(2, _translate(x.comboBox.itemText(2), "Dátum"))
        x.tabWidget.setTabText(x.tabWidget.indexOf(x.tab), _translate(x.tabWidget.objectName(), "Attribútumok"))

        if modosit and x.parentAblak is not None:
            indexes = x.parentAblak.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                valtnev=x.parentAblak.tableWidget.item(index.row(),0).text()
                cimke=x.parentAblak.tableWidget.item(index.row(),1).text()
                leiras=x.parentAblak.tableWidget.item(index.row(),2).text()
                hossz=x.parentAblak.tableWidget.item(index.row(),3).text()
                tipus=x.parentAblak.tableWidget.item(index.row(),4).text()
                csoport=x.parentAblak.tableWidget.item(index.row(),5).text()
                kezdoidopont=x.parentAblak.tableWidget.item(index.row(),7).text()
                vegidopont=x.parentAblak.tableWidget.item(index.row(),8).text()
                x.lineEdit_valtozonev.setText(valtnev)
                x.lineEdit_cimke.setText(cimke)
                x.lineEdit_leiras.setText(leiras)
                x.lineEdit_hossz.setText(hossz)
                x.lineEdit_csoport.setText(csoport)
                x.comboBox.setCurrentText(tipus)
                x.dateEdit_kezdet.setDate(datetime.datetime.strptime(kezdoidopont,'%Y-%m-%d'))
                x.dateEdit_veg.setDate(datetime.datetime.strptime(vegidopont,'%Y-%m-%d'))

class newMutatDB(object):

    def exportMutat(self, parentablak, kiterjesztes):
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

            for elem in sorted(rows):
                exportalando_dataframe=exportalando_dataframe.append({'nev':self.parentAblak.tableWidget.item(elem.row(),0).text(),
                                                                      'cimke':self.parentAblak.tableWidget.item(elem.row(),1).text(),
                                                                      'leiras':self.parentAblak.tableWidget.item(elem.row(),2).text(),
                                                                      'hossz':self.parentAblak.tableWidget.item(elem.row(),3).text(),
                                                                      'tipus':self.parentAblak.tableWidget.item(elem.row(),4).text(),
                                                                      'csoport':self.parentAblak.tableWidget.item(elem.row(),5).text(),
                                                                      'utolso_modositas':self.parentAblak.tableWidget.item(elem.row(),6).text(),
                                                                      'kezdoidopont':self.parentAblak.tableWidget.item(elem.row(),7).text(),
                                                                      'vegidopont':self.parentAblak.tableWidget.item(elem.row(),8).text()}, ignore_index=True)

            exportalando_dataframe.index +=1
        else:
            conn = sqlite3.connect('datagov.db', isolation_level=None)
            exportalando_dataframe =pd.DataFrame(pd.read_sql_query("SELECT * FROM mutatok", conn))
            exportalando_dataframe.index += 1

        fajl_nev=QtWidgets.QFileDialog.getSaveFileUrl(caption="Fájl mentése "+kiterjesztes+"-ként", filter=kiterjesztes, initialFilter=kiterjesztes)
        try:
            if kiterjesztes=="CSV fájl (*.csv)":
                exportalando_dataframe.to_csv(QtCore.QUrl.toLocalFile(fajl_nev[0]))
            else:
                exportalando_dataframe.to_excel(QtCore.QUrl.toLocalFile(fajl_nev[0]))
        except Exception as e:
            print("Nem lett szabályosan megadva útvónal")


    def newMutat(self, parentAblak, modosit=False):
        self.parentAblak=parentAblak
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        # c.execute('''DROP TABLE mutatok''')
        # c.execute('''CREATE TABLE mutatok
        #             (nev text, cimke text, leiras text, hossz integer , tipus text, csoport text,utolso_modositas date, kezdoidopont date, vegidopont date)''')
        try:
            sor=c.execute("SELECT * FROM mutatok WHERE nev='"+valtnev+"'")
            for elem in sor: # lényegében ezzek csekkolom hogy van e már ilyen sor az adatbázisban
                 if not modosit:
                     raise Exception("Már van ilyen változónév")
                 else:
                     c.execute("UPDATE mutatok SET cimke='"+cimke+"', leiras='"+leiras+"', hossz='"+hossz+"', tipus='"+tipus+"', csoport='"+csoport+"', utolso_modositas='"+str(date.today())+"', kezdoidopont='"+str(kezdoidopont)+"', vegidopont='"+str(vegidopont)+"' WHERE nev='"+valtnev+"';")
                     indexek=self.parentAblak.tableWidget.selectionModel().selectedRows()
                     for index in indexek:
                         self.parentAblak.tableWidget.setItem(index.row(), 1, QTableWidgetItem(cimke))
                         self.parentAblak.tableWidget.setItem(index.row(), 2, QTableWidgetItem(leiras))
                         self.parentAblak.tableWidget.setItem(index.row(), 3, QTableWidgetItem(hossz))
                         self.parentAblak.tableWidget.setItem(index.row(), 4, QTableWidgetItem(tipus))
                         self.parentAblak.tableWidget.setItem(index.row(), 5, QTableWidgetItem(csoport))
                         self.parentAblak.tableWidget.setItem(index.row(), 6, QTableWidgetItem(str(date.today())))
                         self.parentAblak.tableWidget.setItem(index.row(), 7, QTableWidgetItem(str(kezdoidopont)))
                         self.parentAblak.tableWidget.setItem(index.row(), 8, QTableWidgetItem(str(vegidopont)))

            if not modosit:

                script = "INSERT INTO mutatok (nev, cimke, leiras, hossz, tipus, csoport, utolso_modositas, kezdoidopont, vegidopont) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
                c.execute(script, (valtnev, cimke, leiras, hossz, tipus, csoport, str(date.today()), kezdoidopont, vegidopont))
                conn.commit()
                conn.close()

                # ez a frissítéshez van
                addNewRow(self.parentAblak, valtnev, cimke, leiras, hossz, tipus, csoport, str(date.today()), str(kezdoidopont),str(vegidopont))
        except Exception as e:
            QtWidgets.QMessageBox.question(parentAblak,"Ez a változónév már létezik", "Kérlek próbálkozz egy másik változónévvel", QtWidgets.QMessageBox.Ok)


    def listMutat(self):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        global query
        query = c.execute('''SELECT * FROM mutatok''')
        conn.commit()

        # conn.close() #Closing the database, valamiért ezzel kifagy az egész
