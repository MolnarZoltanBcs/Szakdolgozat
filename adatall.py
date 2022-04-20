import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *
import sqlite3


class Ui_Adatallomanyok(QtWidgets.QMainWindow):
    def setupUi(self, Ui_Adatallomanyok):
        self.ablak=Ui_Adatallomanyok
        self.ablak.setObjectName("Ui_Adatallomanyok")
        self.ablak.resize(1150, 586)
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.db=DbConnectAdatAll()
       
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1090, 521))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(15, 121, 881, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.pushButton_elonezet = QtWidgets.QPushButton(self.frame)
        self.pushButton_elonezet.setGeometry(QtCore.QRect(60, 40, 101, 25))
        self.pushButton_elonezet.setObjectName("pushButton_elonezet")
        self.pushButton__kodfuttatas = QtWidgets.QPushButton(self.frame)
        self.pushButton__kodfuttatas.setGeometry(QtCore.QRect(200, 40, 111, 25))
        self.pushButton__kodfuttatas.setObjectName("pushButton__kodfuttatas")
        # self.pushButton_torles = QtWidgets.QPushButton(self.frame)
        # self.pushButton_torles.setGeometry(QtCore.QRect(350, 40, 101, 25))
        # self.pushButton_torles.setObjectName("pushButton_torles")
        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)


        self.tableWidgetSetUp(self.tableWidget)
        
        
        self.pushButton_elonezet.clicked.connect(self.open_tabla)
        self.pushButton__kodfuttatas.clicked.connect(self.open_kod)
                 #ez fogja törölni a kiválasztott sort 
        # self.pushButton_torles.clicked.connect(self.deleteCurrentRow)
        

        self.retranslateUi(self.ablak)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

        #modosit torol gomb allapot valtozasahoz 
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.selectionModel().selectionChanged.connect(
            self.on_selection_changed
        )
 
        self.on_selection_changed()
                  
        
    def on_selection_changed(self):
        self.pushButton_elonezet.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
       #  self.pushButton_torles.setEnabled(
       #      bool(self.tableWidget.selectionModel().selectedRows())
       # )
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

    def tableWidgetSetUp(self, tableWidget):
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.setGeometry(QtCore.QRect(60, 75, 1025, 370))
        tableWidget.setAlternatingRowColors(True)
        tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tableWidget.setObjectName("tableWidget")

        k=8
        tableWidget.setColumnCount(k)
        tableWidget.setRowCount(0)
        for i in range(k):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setHorizontalHeaderItem(i, item)
        sorok=self.db.listAdatAll()
        i = 0
        for sor in sorok:
            self.tableWidget.setRowCount(i + 1)
            for j in range(8):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(sor[j])))
            i += 1

    def retranslateUi(self, Ui_Adatallomanyok):
        _translate = QtCore.QCoreApplication.translate
        Ui_Adatallomanyok.setWindowTitle(_translate("Ui_Adatallomanyok", "Adatállományok"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Nomenklatura", "Adatállomány neve"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Nomenklatura", "Állomány rekordszáma"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Ui_Nomenklatura", "Rekordleírása"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Ui_Nomenklatura", "Verziószáma"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Ui_Nomenklatura", "Projekt"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Ui_Nomenklatura", "Tulajdonos"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Ui_Nomenklatura", "Állomány titkosítási kódja"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Ui_Nomenklatura", "Létrehozva"))
        

        self.pushButton_elonezet.setText(_translate("Ui_Adatallomanyok", "Előnézet"))
        self.pushButton__kodfuttatas.setText(_translate("Ui_Adatallomanyok", "Kód végrehajtása"))
        # self.pushButton_torles.setText(_translate("Ui_Adatallomanyok", "Törlés"))
    
    def open_tabla(self):
        if len(self.tableWidget.selectionModel().selectedRows()) !=1:
            QtWidgets.QMessageBox.question(self,
                                                "Helytelen sorkiválasztás",
                                                "Kérlek pontosan egy sort jelölj ki!",
                                                QtWidgets.QMessageBox.Ok)
            return
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Tablatartalom()
        sorok=self.tableWidget.selectionModel().selectedRows()
        rekordleiras_nev=""
        adatallomany_nev=""
        for sor in sorok:
            rekordleiras_nev=str(self.tableWidget.item(sor.row(),2).text())
            adatallomany_nev=str(self.tableWidget.item(sor.row(),0).text())
        self.ui.setupUi(self.window,adatallomany_nev, rekordleiras_nev)
        self.window.show()
        
    def open_kod(self):
        if len(self.tableWidget.selectionModel().selectedRows()) !=1:
            QtWidgets.QMessageBox.question(self,
                                                "Helytelen sorkiválasztás",
                                                "Kérlek pontosan egy sort jelölj ki!",
                                                QtWidgets.QMessageBox.Ok)
            return
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kod()
        self.ui.setupUi(self.window, self.tableWidget, parent=self)
        self.window.show()


class Ui_Tablatartalom(object):
    def setupUi(self, Ui_Tablatartalom,adatallomany_nev, rekordleiras_nev):
        self.ablak=Ui_Tablatartalom
        self.ablak.setObjectName("Ui_Tablatartalom")
        self.ablak.resize(622, 449)
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.db=DbConnectAdatAll()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 601, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 581, 311))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.pushButton_modosit = QtWidgets.QPushButton(self.frame)
        # self.pushButton_modosit.setGeometry(QtCore.QRect(10, 10, 101, 31))
        # self.pushButton_modosit.setObjectName("pushButton_modosit")
        # self.pushButton_aktualizal = QtWidgets.QPushButton(self.frame)
        # self.pushButton_aktualizal.setGeometry(QtCore.QRect(130, 10, 101, 31))
        # self.pushButton_aktualizal.setObjectName("pushButton_aktualizal")
        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(adatallomany_nev,rekordleiras_nev)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def retranslateUi(self,adatallomany_nev, rekordleiras_nev):
        _translate = QtCore.QCoreApplication.translate
        self.ablak.setWindowTitle(_translate("Ui_Tablatartalom", "Tábla tartalma"))
        # self.pushButton_modosit.setText(_translate("Ui_Tablatartalom", "Módosít"))
        # self.pushButton_aktualizal.setText(_translate("Ui_Tablatartalom", "Aktualizál"))

        szamlalo=0
        mezoLista=[]
        query=self.db.listMezokForRekordleiras(rekordleiras_nev)
        for sor in query:
            mezoLista.append(str(sor[1])+f" ({self.intToMezo(int(sor[2]))})")
            szamlalo+=1
        self.tableWidget.setColumnCount(szamlalo)
        for i in range(szamlalo):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.horizontalHeaderItem(i).setText(mezoLista[i])
        sorok=self.db.listSpecififcTable(adatallomany_nev)
        k=0
        for sor in sorok:
            self.tableWidget.setRowCount(k+1)
            for i in range(szamlalo):
                self.tableWidget.setItem(k,i,QTableWidgetItem(str(sor[i])))
            k+=1

    def intToMezo(self, szam):
        if szam == 0:
            return "Mutató"
        return "Nómenklatúra"

class Ui_Kod(object):
    def setupUi(self, Ui_Kod, tableWidget, parent=None):
        self.ablak=Ui_Kod
        self.ablak.setObjectName("Ui_Kod")
        self.ablak.resize(443, 396)
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.db=DbConnectAdatAll()
        self.pushButton_futtat = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_futtat.setGeometry(QtCore.QRect(200, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_futtat.setFont(font)
        self.pushButton_futtat.setObjectName("pushButton_futtat")
        self.pushButton_megse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_megse.setGeometry(QtCore.QRect(310, 320, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_megse.setFont(font)
        self.pushButton_megse.setDefault(True)
        self.pushButton_megse.clicked.connect(lambda: self.ablak.close())
        self.pushButton_megse.setObjectName("pushButton_megse")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 401, 301))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 381, 271))
        self.textEdit.setObjectName("textEdit")
        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)
        self.pushButton_futtat.clicked.connect(lambda: self.runQuery(tableWidget, parent))
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def runQuery(self, tableWidget, parent):
        indexes=tableWidget.selectionModel().selectedRows()
        for index in indexes:
            table=tableWidget.item(index.row(),0).text()
        query=self.textEdit.toPlainText()
        response=self.db.runQueryOnTable(table, query)
        if response=="":
            QtWidgets.QMessageBox.question(parent,
                                           "Az sql szerver válasza:",
                                           "Sikeres végrehajtás!",
                                           QtWidgets.QMessageBox.Ok)
            return
        if response.__class__==str:
            QtWidgets.QMessageBox.question(parent,
                                           "Az sql szerver válasza:",
                                           response,
                                           QtWidgets.QMessageBox.Ok)
            return
        else:
            eredmeny=""
            for sor in response:
                eredmeny+=str(sor)+"\n"
            QtWidgets.QMessageBox.question(parent,
                                           "Az sql szerver válasza:",
                                           eredmeny,
                                           QtWidgets.QMessageBox.Ok)
            return


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ablak.setWindowTitle(_translate("Ui_Kod", "Kód végrehajtása"))
        self.pushButton_futtat.setText(_translate("Ui_Kod", "Futtatás"))
        self.pushButton_megse.setText(_translate("Ui_Kod", "Mégse"))
        self.groupBox.setTitle(_translate("Ui_Kod", "Futtatandó utasítás"))


class DbConnectAdatAll():
    def __init__(self):
        pass

    def listAdatAll(self):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        query=c.execute("SELECT * from adatallomanyok;")
        conn.commit()
        return query

    def listSpecififcTable(self, table):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        query = c.execute(f"SELECT * from __{table};")
        conn.commit()
        return query

    def listMezokForRekordleiras(self,rekordleiras_nev):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        query = c.execute("SELECT * from rekord_mutato_nomen_kapcsolo where record_nev=? order by sorrend;", tuple([rekordleiras_nev]))
        conn.commit()
        return query

    def runQueryOnTable(self, table, query):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        response="A tábla nevének szerepelnie kell a query-ben"
        if table in query:
            query=query.replace(table,"__"+table)
            try:
                response = c.execute(query)
            except sqlite3.Error as error:
                response=str(error).replace("__","")
        conn.commit()
        return response
