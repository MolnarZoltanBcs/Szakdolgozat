import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *
import sqlite3


class Ui_Adatallomanyok(QtWidgets.QMainWindow):
    def setupUi(x, Ui_Adatallomanyok):
        x.ablak=Ui_Adatallomanyok
        x.ablak.setObjectName("Ui_Adatallomanyok")
        x.ablak.resize(1150, 586)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.db=DbConnectAdatAll()
       
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 10, 1090, 521))
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
        x.pushButton_elonezet = QtWidgets.QPushButton(x.frame)
        x.pushButton_elonezet.setGeometry(QtCore.QRect(60, 40, 101, 25))
        x.pushButton_elonezet.setObjectName("pushButton_elonezet")
        x.pushButton__kodfuttatas = QtWidgets.QPushButton(x.frame)
        x.pushButton__kodfuttatas.setGeometry(QtCore.QRect(200, 40, 111, 25))
        x.pushButton__kodfuttatas.setObjectName("pushButton__kodfuttatas")
        # x.pushButton_torles = QtWidgets.QPushButton(x.frame)
        # x.pushButton_torles.setGeometry(QtCore.QRect(350, 40, 101, 25))
        # x.pushButton_torles.setObjectName("pushButton_torles")
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 937, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)


        x.tableWidgetSetUp(x.tableWidget)
        
        
        x.pushButton_elonezet.clicked.connect(x.open_tabla)
        x.pushButton__kodfuttatas.clicked.connect(x.open_kod)
                 #ez fogja törölni a kiválasztott sort 
        # x.pushButton_torles.clicked.connect(x.deleteCurrentRow)
        

        x.retranslateUi(x.ablak)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

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

    def retranslateUi(x, Ui_Adatallomanyok):
        _translate = QtCore.QCoreApplication.translate
        Ui_Adatallomanyok.setWindowTitle(_translate("Ui_Adatallomanyok", "Adatállományok"))

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
        

        x.pushButton_elonezet.setText(_translate("Ui_Adatallomanyok", "Előnézet"))
        x.pushButton__kodfuttatas.setText(_translate("Ui_Adatallomanyok", "Kód végrehajtása"))
        # x.pushButton_torles.setText(_translate("Ui_Adatallomanyok", "Törlés"))
    
    def open_tabla(x):#TODO: check if this len() check is enough
        if len(x.tableWidget.selectionModel().selectedRows()) !=1:
            QtWidgets.QMessageBox.question(x,
                                                "Helytelen sorkiválasztás",
                                                "Kérlek pontosan egy sort jelölj ki!",
                                                QtWidgets.QMessageBox.Ok)
            return
        x.window = QtWidgets.QMainWindow()
        x.ui = Ui_Tablatartalom()
        sorok=x.tableWidget.selectionModel().selectedRows()
        rekordleiras_nev=""
        adatallomany_nev=""
        for sor in sorok:
            rekordleiras_nev=str(x.tableWidget.item(sor.row(),2).text())
            adatallomany_nev=str(x.tableWidget.item(sor.row(),0).text())
        x.ui.setupUi(x.window,adatallomany_nev, rekordleiras_nev)
        x.window.show()
        
    def open_kod(x):
        if len(x.tableWidget.selectionModel().selectedRows()) !=1:
            QtWidgets.QMessageBox.question(x,
                                                "Helytelen sorkiválasztás",
                                                "Kérlek pontosan egy sort jelölj ki!",
                                                QtWidgets.QMessageBox.Ok)
            return
        x.window = QtWidgets.QMainWindow()
        x.ui = Ui_Kod()
        x.ui.setupUi(x.window, x.tableWidget, parent=x)
        x.window.show()


class Ui_Tablatartalom(object):
    def setupUi(x, Ui_Tablatartalom,adatallomany_nev, rekordleiras_nev):
        x.ablak=Ui_Tablatartalom
        x.ablak.setObjectName("Ui_Tablatartalom")
        x.ablak.resize(622, 449)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.db=DbConnectAdatAll()
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
        x.tableWidget.horizontalHeader().setStretchLastSection(True)
        # x.pushButton_modosit = QtWidgets.QPushButton(x.frame)
        # x.pushButton_modosit.setGeometry(QtCore.QRect(10, 10, 101, 31))
        # x.pushButton_modosit.setObjectName("pushButton_modosit")
        # x.pushButton_aktualizal = QtWidgets.QPushButton(x.frame)
        # x.pushButton_aktualizal.setGeometry(QtCore.QRect(130, 10, 101, 31))
        # x.pushButton_aktualizal.setObjectName("pushButton_aktualizal")
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(adatallomany_nev,rekordleiras_nev)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def retranslateUi(x,adatallomany_nev, rekordleiras_nev):
        _translate = QtCore.QCoreApplication.translate
        x.ablak.setWindowTitle(_translate("Ui_Tablatartalom", "Tábla tartalma"))
        # x.pushButton_modosit.setText(_translate("Ui_Tablatartalom", "Módosít"))
        # x.pushButton_aktualizal.setText(_translate("Ui_Tablatartalom", "Aktualizál"))

        szamlalo=0
        mezoLista=[]
        query=x.db.listMezokForRekordleiras(rekordleiras_nev)
        for sor in query:
            mezoLista.append(str(sor[1])+f" ({x.intToMezo(int(sor[2]))})")
            szamlalo+=1
        x.tableWidget.setColumnCount(szamlalo)
        for i in range(szamlalo):
            item = QtWidgets.QTableWidgetItem()
            x.tableWidget.setHorizontalHeaderItem(i, item)
            x.tableWidget.horizontalHeaderItem(i).setText(mezoLista[i])
        sorok=x.db.listSpecififcTable(adatallomany_nev)
        k=0
        for sor in sorok:
            x.tableWidget.setRowCount(k+1)
            for i in range(szamlalo):
                x.tableWidget.setItem(k,i,QTableWidgetItem(str(sor[i])))
            k+=1

    def intToMezo(self, szam):
        if szam == 0:
            return "Mutató"
        return "Nómenklatúra"

class Ui_Kod(object):
    def setupUi(x, Ui_Kod, tableWidget, parent=None):
        x.ablak=Ui_Kod
        x.ablak.setObjectName("Ui_Kod")
        x.ablak.resize(443, 396)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.db=DbConnectAdatAll()
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
        x.pushButton_megse.clicked.connect(lambda: x.ablak.close())
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
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)
        x.pushButton_futtat.clicked.connect(lambda: x.runQuery(tableWidget, parent))
        x.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

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


    def retranslateUi(x):
        _translate = QtCore.QCoreApplication.translate
        x.ablak.setWindowTitle(_translate("Ui_Kod", "Kód végrehajtása"))
        x.pushButton_futtat.setText(_translate("Ui_Kod", "Futtatás"))
        x.pushButton_megse.setText(_translate("Ui_Kod", "Mégse"))
        x.groupBox.setTitle(_translate("Ui_Kod", "Futtatandó utasítás"))


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
