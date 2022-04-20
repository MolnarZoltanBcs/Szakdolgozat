import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *

mutatok={}
nomenklaturak={}

class Ui_Rekordleirasok(QtWidgets.QMainWindow):
    def setupUi(self,  Ui_Rekordleirasok):
         global mainTableWidget
         self.ablak=Ui_Rekordleirasok
         self.ablak.setObjectName("Ui_Rekordleirasok")
         self.ablak.resize(1175, 500)
         
         self.ablak.setWindowTitle("Rekordleírások kezelése")
         
         self.tableWidget = QtWidgets.QTableWidget(self.ablak)
         self.tableWidget.setGeometry(QtCore.QRect(60, 75, 650, 370))
         self.tableWidget.setObjectName("tableWidget")
         self.tableWidget.horizontalHeader().setStretchLastSection(True)
         self.db=DbConnectRekord()
         self.tableWidgetSetUp(self.tableWidget)
         mainTableWidget=self.tableWidget

         self.pushButton_ujrekord = QtWidgets.QPushButton(self.ablak)
         self.pushButton_ujrekord.setGeometry(QtCore.QRect(60, 26, 180, 30))
         self.pushButton_ujrekord.setObjectName("pushButton_ujrekord")
         self.pushButton_mezok = QtWidgets.QPushButton(self.ablak)
         self.pushButton_mezok.setGeometry(QtCore.QRect(260, 26, 110, 30))
         self.pushButton_mezok.setObjectName("pushButton_mezok")
         self.pushButton_torol = QtWidgets.QPushButton(self.ablak)
         self.pushButton_torol.setGeometry(QtCore.QRect(390, 26, 110, 30))
         self.pushButton_torol.setObjectName("pushButton_torol")


         self.valtoztatUi(self.ablak)
         QtCore.QMetaObject.connectSlotsByName(self.ablak)
         
          
         self.pushButton_mezok.clicked.connect(self.rekord_mezok_window)
         
         self.pushButton_ujrekord.clicked.connect(self.rekord_uj_Window)
         
         #ez fogja törölni a kiválasztott sort 
         # self.pushButton_torol.clicked.connect(self.deleteCurrentRow)
          #modosit torol gomb allapot valtozasahoz
         self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
         self.tableWidget.selectionModel().selectionChanged.connect(
             self.on_selection_changed
         )
 
         self.on_selection_changed()

         self.pushButton_torol.clicked.connect(lambda: self.delete_rekord())

    def delete_rekord(self):
        result = QtWidgets.QMessageBox.question(self,
                                                "Törlés megerősítése...",
                                                "Biztos ki akarod törölni a kiválaszott sorokat?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.db.delete_rekord(self)

    def tableWidgetSetUp(self, tableWidget, nomen=False):
        tableWidget.reset()
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.setGeometry(QtCore.QRect(60, 75, 1025, 370))
        tableWidget.setAlternatingRowColors(True)
        tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tableWidget.setObjectName("tableWidget")

        k = 7
        tableWidget.setColumnCount(k)
        tableWidget.setRowCount(0)
        for i in range(k):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setHorizontalHeaderItem(i, item)
        sorok=self.db.listRekordok()
        i = 0
        for sor in sorok:
            self.tableWidget.setRowCount(i + 1)
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(sor[j]))
            i += 1

    def deleteCurrentRow(self):
        i=0
        indexes = self.tableWidget.selectionModel().selectedRows()
        for index in sorted(indexes):
            self.tableWidget.removeRow(index.row()-i)
            i+=1
        
    def on_selection_changed(self):
        #self.pushButton_modosit.setEnabled(
        #    bool(self.tableWidget.selectionModel().selectedRows())
       #)
        self.pushButton_torol.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_mezok.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
       #  self.pushButton_ujrekord.setEnabled(
       #      bool(self.tableWidget.selectionModel().selectedRows())
       # )

    def valtoztatUi(self, Ui_Rekordleirasok):
         _translate = QtCore.QCoreApplication.translate
         Ui_Rekordleirasok.setWindowTitle(_translate("Ui_Rekordleirasok", "Rekordleírások kezelése"))
         
         
         item = self.tableWidget.horizontalHeaderItem(0)
         item.setText(_translate("Ui_Rekordleirasok", "Rekord neve"))
         item = self.tableWidget.horizontalHeaderItem(1)
         item.setText(_translate("Ui_Rekordleirasok", "Címke"))
         item = self.tableWidget.horizontalHeaderItem(2)
         item.setText(_translate("Ui_Rekordleirasok", "Leírás"))
         item = self.tableWidget.horizontalHeaderItem(3)
         item.setText(_translate("Ui_Rekordleirasok", "Típus"))
         item = self.tableWidget.horizontalHeaderItem(4)
         item.setText(_translate("Ui_Rekordleirasok", "Utolsó módosítás"))
         item = self.tableWidget.horizontalHeaderItem(5)
         item.setText(_translate("Ui_Rekordleirasok", "Érvényesség kezdete"))
         item = self.tableWidget.horizontalHeaderItem(6)
         item.setText(_translate("Ui_Rekordleirasok", "Érvényesség vége"))
         
         
         __sortingEnabled = self.tableWidget.isSortingEnabled()
         self.tableWidget.setSortingEnabled(False)

 
         self.tableWidget.setSortingEnabled(__sortingEnabled)
      
         self.pushButton_torol.setText(_translate("Ui_Rekordleirasok", "Törlés"))
         self.pushButton_mezok.setText(_translate("Ui_Rekordleirasok", "Mezők kezelése"))
         self.pushButton_ujrekord.setText(_translate("Ui_Rekordleirasok", "Új rekordleírás létrehozása"))

   
    
    def rekord_mezok_window(self):
         indexes = self.tableWidget.selectionModel().selectedRows()
         if len(indexes) != 1:
             QtWidgets.QMessageBox.question(self,
                                             "Helytelen kiválasztás",
                                             "Kérlek pontosan egy sort jelölj ki!",
                                             QtWidgets.QMessageBox.Ok)
             return
         for index in indexes:
             rekord=self.tableWidget.item(index.row(),0).text()
         self.window = QtWidgets.QMainWindow()
         self.ui_mezok = Ui_Mezok()
         self.ui_mezok.setupUi(self.window, rekord=rekord)
         self.window.show()
            
    def rekord_uj_Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_rekord_uj = Ui_Rekord_Uj()
        self.ui_rekord_uj.setupUi(self.window, self)
        self.window.show()


class Ui_Mezok(object):
    def setupUi(self, Ui_Mezok, rekord=None):
        self.ablak=Ui_Mezok
        self.ablak.setObjectName("Ui_Mezok")
        self.ablak.resize(687, 515)
        self.db=DbConnectRekord()
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 671, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_szerk = QtWidgets.QPushButton(self.frame)
        self.pushButton_szerk.setGeometry(QtCore.QRect(30, 20, 300, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_szerk.setIcon(icon)
        self.pushButton_szerk.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_szerk.setDefault(True)
        self.pushButton_szerk.setObjectName("pushButton_szerk")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setShowGrid(True)
        self.tableWidgetSetUp(self.tableWidget,[30, 100, 601, 341], rekord=rekord)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.pushButton_szerk.clicked.connect(lambda: self.open_Ui_Mezok_Szerk(modosit=True, rekord=rekord))
        #self.pushButton_modosit.clicked.connect(self.open_Ui_Mezok_Modosit)

        self.retranslateUi(self.ablak)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def tableWidgetSetUp(self, tableWidget, lista : list, rekord=None):
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.setGeometry(QtCore.QRect(lista[0], lista[1], lista[2], lista[3]))
        tableWidget.setAlternatingRowColors(True)
        tableWidget.setObjectName("tableWidget")

        k=3
        tableWidget.setColumnCount(k)
        tableWidget.setRowCount(0)
        for i in range(k):
            item = QtWidgets.QTableWidgetItem()
            tableWidget.setHorizontalHeaderItem(i, item)
        sorok=self.db.listMezok_all(rekord)
        sorok.sort(key=lambda y: y[2])
        sorszamlalo=0
        for sor in sorok:
            tableWidget.setRowCount(tableWidget.rowCount()+1)
            for i in range(3):
                if i==1:
                    item = QtWidgets.QTableWidgetItem(self.intToMezo(sor[1]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(sor[i])) # kell még hogy ha elmentem a változásokat akkor bezáródjon mindkét ablak és úgy mentődjön el
                tableWidget.setItem(sorszamlalo,i,item)
            sorszamlalo+=1

    def retranslateUi(self, Ui_Mezok):
        _translate = QtCore.QCoreApplication.translate
        Ui_Mezok.setWindowTitle(_translate("Ui_Mezok", "Mezők"))
        self.pushButton_szerk.setText(_translate("Ui_Mezok", "Rekordhoz tartozó mezők kezelése"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Mezok", "Mező neve"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Mezok", "Típus"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Ui_Mezok", "Sorrend"))


    def intToMezo(self, szam):
        if szam == 0:
            return "Mutató"
        return "Nómenklatúra"

    def open_Ui_Mezok_Szerk(self, modosit=False, rekord=None):
        self.window = QtWidgets.QMainWindow()
        self.ui_mezok_szerkeztese = Ui_Mezok_Szerk()
        self.ui_mezok_szerkeztese.setupUi(self.window,self, modosit=modosit, rekord=rekord)
        self.window.show()


class Ui_Rekord_Uj(object):
    def setupUi(self, Ui_Rekord_Uj, parent):
        self.ablak=Ui_Rekord_Uj
        self.parent=parent
        self.db=DbConnectRekord()
        self.ablak.setObjectName("Ui_Rekord_Uj")
        self.ablak.resize(429, 392)
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 290))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_attributum = QtWidgets.QWidget()
        self.tab_attributum.setObjectName("tab_attributum")
        self.comboBox_tipus = QtWidgets.QComboBox(self.tab_attributum)
        self.comboBox_tipus.setGeometry(QtCore.QRect(150, 150, 111, 22))
        self.comboBox_tipus.setObjectName("comboBox_tipus")
        self.comboBox_tipus.addItem("")
        self.comboBox_tipus.addItem("")
        self.lineEdit_rekordnev = QtWidgets.QLineEdit(self.tab_attributum)
        self.lineEdit_rekordnev.setGeometry(QtCore.QRect(150, 30, 171, 20))
        self.lineEdit_rekordnev.setObjectName("lineEdit_rekordnev")
        self.label = QtWidgets.QLabel(self.tab_attributum)
        self.label.setGeometry(QtCore.QRect(30, 30, 111, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_attributum)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 111, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_cimke = QtWidgets.QLineEdit(self.tab_attributum)
        self.lineEdit_cimke.setGeometry(QtCore.QRect(150, 70, 171, 20))
        self.lineEdit_cimke.setObjectName("lineEdit_cimke")
        self.label_3 = QtWidgets.QLabel(self.tab_attributum)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_leiras = QtWidgets.QLineEdit(self.tab_attributum)
        self.lineEdit_leiras.setGeometry(QtCore.QRect(150, 110, 171, 20))
        self.lineEdit_leiras.setObjectName("lineEdit_leiras")
        self.label_4 = QtWidgets.QLabel(self.tab_attributum)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 131, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_attributum, "")

        self.label_kezdet = QtWidgets.QLabel(self.tab_attributum)
        self.label_kezdet.setGeometry(QtCore.QRect(30, 190, 111, 21))
        self.label_kezdet.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_kezdet.setObjectName("label")

        self.dateEdit_kezdet = QtWidgets.QDateEdit(self.tab_attributum)
        self.dateEdit_kezdet.setGeometry(QtCore.QRect(150, 190, 131, 20))
        self.dateEdit_kezdet.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_kezdet.setCalendarPopup(True)
        self.dateEdit_kezdet.setObjectName("dateEdit_kezdet")

        self.label_veg = QtWidgets.QLabel(self.tab_attributum)
        self.label_veg.setGeometry(QtCore.QRect(30, 230, 111, 21))
        self.label_veg.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_veg.setObjectName("label")

        self.dateEdit_veg = QtWidgets.QDateEdit(self.tab_attributum)
        self.dateEdit_veg.setGeometry(QtCore.QRect(150, 230, 131, 20))
        self.dateEdit_veg.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_veg.setCalendarPopup(True)
        self.dateEdit_veg.setObjectName("dateEdit_veg")

        self.pushButton_Megse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Megse.setGeometry(QtCore.QRect(310, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Megse.setFont(font)
        self.pushButton_Megse.clicked.connect(lambda: self.ablak.close())
        self.pushButton_Megse.setDefault(True)
        self.pushButton_Megse.setObjectName("pushButton_Megse")
        self.pushButton_Mentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mentes.setGeometry(QtCore.QRect(210, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Mentes.setFont(font)
        self.pushButton_Mentes.setObjectName("pushButton_Mentes")
        self.pushButton_Kezeles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Kezeles.setGeometry(QtCore.QRect(70, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_Kezeles.setFont(font)
        self.pushButton_Kezeles.setObjectName("pushButton_Kezeles")
        self.ablak.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(self.ablak)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

        self.pushButton_Kezeles.clicked.connect(self.open_Ui_Mezok_Szerk)

        self.pushButton_Mentes.clicked.connect(lambda: self.save_record())
        self.pushButton_Mentes.clicked.connect(lambda: self.ablak.close())
        self.pushButton_Mentes.clicked.connect(lambda: self.parent.tableWidgetSetUp(self.parent.tableWidget))
        self.pushButton_Mentes.clicked.connect(lambda: self.parent.valtoztatUi(self.parent.ablak))


    def retranslateUi(self, Ui_Rekord_Uj):
        _translate = QtCore.QCoreApplication.translate
        Ui_Rekord_Uj.setWindowTitle(_translate("Ui_Rekord_Uj", "Új rekord létrehozása"))
        self.comboBox_tipus.setItemText(0, _translate("Ui_Rekord_Uj", "SAS"))
        self.comboBox_tipus.setItemText(1, _translate("Ui_Rekord_Uj", "SQL"))
        self.label.setText(_translate("Ui_Rekord_Uj", "Rekord neve:"))
        self.label_2.setText(_translate("Ui_Rekord_Uj", "Típus:"))
        self.label_3.setText(_translate("Ui_Rekord_Uj", "Nyomtatási címke:"))
        self.label_4.setText(_translate("Ui_Rekord_Uj", "Leírás:"))
        self.label_kezdet.setText(_translate("Ui_Rekord_Uj", "Kezdőidőpint:"))
        self.label_veg.setText(_translate("Ui_Rekord_Uj", "Végidőpont:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_attributum), _translate("Ui_Rekord_Uj", "Attribútumok"))
        self.pushButton_Megse.setText(_translate("Ui_Rekord_Uj", "Mégse"))
        self.pushButton_Mentes.setText(_translate("Ui_Rekord_Uj", "Mentés"))
        self.pushButton_Kezeles.setText(_translate("Ui_Rekord_Uj", "Mezők kezelése"))

    def open_Ui_Mezok_Szerk(self):
        self.window = QtWidgets.QMainWindow()
        self.ui_mezok = Ui_Mezok_Szerk()
        self.ui_mezok.setupUi(self.window,self)
        self.window.setWindowTitle("Új rekord mezőinek a kiválaszása")
        self.window.show()

    def save_record(self):
        global mutatok, nomenklaturak
        self.db.newRekord(self.lineEdit_rekordnev.text(), self.lineEdit_cimke.text(), self.lineEdit_leiras.text(),self.comboBox_tipus.currentText(),
                       self.dateEdit_kezdet.date().toPyDate(), self.dateEdit_veg.date().toPyDate())
        self.db.newRekordMezok(self.lineEdit_rekordnev.text())

        

class Ui_Mezok_Szerk(object):
    def setupUi(self, Ui_Mezok_Szerk,parent, modosit=False, rekord=None):
        self.ablak=Ui_Mezok_Szerk
        self.parent=parent
        self.ablak.setObjectName("Ui_Mezok_Szerk")
        self.ablak.resize(800, 815)
        self.mezok=None
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 790, 805))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_mentes = QtWidgets.QPushButton(self.frame)
        self.pushButton_mentes.setGeometry(QtCore.QRect(580, 700, 91, 41))
        self.pushButton_mentes.setObjectName("pushButton_mentes")
        self.pushButton_mentes.clicked.connect(lambda : self.save_mezok_es_sorrend(modosit=modosit, rekord=rekord))
        self.pushButton_mentes.clicked.connect(lambda : self.ablak.close())
        if modosit:
            self.pushButton_mentes.clicked.connect(lambda : self.parent.ablak.close())
        self.pushButton_megse = QtWidgets.QPushButton(self.frame)
        self.pushButton_megse.setGeometry(QtCore.QRect(690, 700, 91, 41))
        self.pushButton_megse.setDefault(True)
        self.pushButton_megse.clicked.connect(lambda: self.ablak.close())
        self.pushButton_megse.setObjectName("pushButton_megse")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 300, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 300, 21))
        self.label_2.setObjectName("label_2")
        self.tableWidget_mutato = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_mutato.setGeometry(QtCore.QRect(30, 40, 400, 211))
        self.tableWidgetSetUp(self.tableWidget_mutato,[60, 30, 700, 300])
        # self.tableWidget_mutato.setRowCount(4)
        self.tableWidget_mutato.setObjectName("tableWidget_mutato")

        self.tableWidget_mutato.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_mutato.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_mutato.verticalHeader().setStretchLastSection(False)
        self.tableWidget_nomen = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_nomen.setGeometry(QtCore.QRect(30, 600, 461, 221))
        self.tableWidgetSetUp(self.tableWidget_nomen,[60,370,700,300], nomen=True)
        # self.tableWidget_nomen.setRowCount(4)
        self.tableWidget_nomen.setObjectName("tableWidget_nomen")

        self.tableWidget_nomen.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_nomen.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_nomen.verticalHeader().setStretchLastSection(False)

        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(modosit=modosit, rekord=rekord)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def save_mezok_es_sorrend(self, modosit=False, rekord=None):
        global mutatok
        global nomenklaturak
        k=self.tableWidget_mutato.rowCount()
        for sor in range(k):
            if self.tableWidget_mutato.cellWidget(sor,4).currentText() is not '' and int(self.tableWidget_mutato.cellWidget(sor,4).currentText())>0:
                mutatok[self.tableWidget_mutato.item(sor,0).text()]=int(self.tableWidget_mutato.cellWidget(sor,4).currentText())
        k = self.tableWidget_nomen.rowCount()
        for sor in range(k):
            if self.tableWidget_nomen.cellWidget(sor, 3).currentText() is not '' and int(self.tableWidget_nomen.cellWidget(sor, 3).currentText()) > 0:
                nomenklaturak[self.tableWidget_nomen.item(sor, 0).text()] = int(self.tableWidget_nomen.cellWidget(sor, 3).currentText())
        if modosit:
            self.db.refreshDb(rekord,mutatok,nomenklaturak)


    def retranslateUi(self, modosit=False, rekord=None):
        _translate = QtCore.QCoreApplication.translate
        self.ablak.setWindowTitle(_translate("Ui_Mezok_Szerk", "Kiválasztott rekord mezőinek a kezelése"))
        self.pushButton_mentes.setText(_translate("Ui_Mezok_Szerk", "Mentés"))
        self.pushButton_megse.setText(_translate("Ui_Mezok_Szerk", "Mégse"))
        self.label.setText(_translate("Ui_Mezok_Szerk", "Mutatók kiválasztása:"))
        self.label_2.setText(_translate("Ui_Mezok_Szerk", "Nómenklatúrák kiválasztása:"))


        self.db=DbConnectRekord()
        oszlopnevek=["Változó neve","Hossz","Típus","Mutató csoport", "Rekordhoz ad"]
        k=4
        query=self.db.listMutat()
        for row in query:
            rows = self.tableWidget_mutato.rowCount()
            self.tableWidget_mutato.setRowCount(rows + 1)
            for oszlop in range(k):
                self.tableWidget_mutato.setItem(rows, oszlop, QTableWidgetItem(str(row[oszlop])))
            comboBox = QtWidgets.QComboBox()
            self.tableWidget_mutato.setCellWidget(rows, k, comboBox)
            comboBox.addItem("")
            for i in range(1,21):
                comboBox.addItem(str(i))
        if modosit and rekord:
            mutatok=self.db.listMezok_mutatok(rekord)
            i=0
            query = self.db.listMutat()
            for sor in query:
                for my_tuple in mutatok:
                    if sor[0] == my_tuple[0]:
                        self.tableWidget_mutato.cellWidget(i,4).setCurrentIndex(my_tuple[1])
                i+=1

        self.oszlopNevBeallitas(oszlopnevek)

        oszlopnevek = ["Változó neve", "Hossz", "Típus", "Rekordhoz ad"]
        k = 3
        query = self.db.listMutat(nomen=True)
        for row in query:
            rows = self.tableWidget_nomen.rowCount()
            self.tableWidget_nomen.setRowCount(rows + 1)
            for oszlop in range(k):
                self.tableWidget_nomen.setItem(rows, oszlop, QTableWidgetItem(str(row[oszlop])))
            comboBox = QtWidgets.QComboBox()
            self.tableWidget_mutato.setCellWidget(rows, k, comboBox)
            comboBox.addItem("")
            for i in range(1, 21):
                comboBox.addItem(str(i))
            self.tableWidget_nomen.setCellWidget(rows, k, comboBox)
        if modosit and rekord:
            nomenklaturak=self.db.listMezok_nomenklaturak(rekord)
            i=0
            query = self.db.listMutat(nomen=True)
            for sor in query:
                for my_tuple in nomenklaturak:
                    if sor[0] == my_tuple[0]:
                        self.tableWidget_nomen.cellWidget(i,3).setCurrentIndex(my_tuple[1])
                i+=1
        self.oszlopNevBeallitas(oszlopnevek, nomen=True)

    def oszlopNevBeallitas(self, oszlopnevek, nomen=False):
        oszlopszam = 0
        for oszlopnev in oszlopnevek:
            if not nomen:
                item = self.tableWidget_mutato.horizontalHeaderItem(oszlopszam)
            else:
                item = self.tableWidget_nomen.horizontalHeaderItem(oszlopszam)
            item.setText(oszlopnev)
            oszlopszam+=1

    def tableWidgetSetUp(self, tableWidget, lista : list, nomen=False):
        tableWidget.horizontalHeader().setStretchLastSection(True)
        tableWidget.setGeometry(QtCore.QRect(lista[0], lista[1], lista[2], lista[3]))
        tableWidget.setAlternatingRowColors(True)
        # tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        tableWidget.setObjectName("tableWidget")

        k=5
        if nomen:
            k=4
        tableWidget.setColumnCount(k)
        tableWidget.setRowCount(0)
        for i in range(k):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(i))
            tableWidget.setHorizontalHeaderItem(i, item)

class DbConnectRekord():
    def __init__(self):
        pass

    def listRekordok(self):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        sorok = c.execute('select * from rekordleirasok;')
        lista = []
        for sor in sorok:
            lista.append(sor)
        conn.commit()
        conn.close()
        return lista

    def listMutat(self, nomen=False):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        global query
        # c.execute('''CREATE TABLE nomenklaturak
        #                     (nev text, cimke text, leiras text, hossz integer , tipus text, csoport text,utolso_modositas date, kezdoidopont date, vegidopont date)''')

        if not nomen:
            query = c.execute('''select nev, hossz, tipus, csoport from mutatok;''')
        else:
            query = c.execute('''select nev, hossz, tipus from nomenklaturak;''')
        conn.commit()
        return query

    def newRekordMezok(self, rekord):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        global mutatok, nomenklaturak
        for key, value in mutatok.items():
            c.execute('insert into rekord_mutato_nomen_kapcsolo (record_nev, nomen_vagy_mutato_nev, nomen_vagy_mutato, sorrend) values(?,?,0,?);',(rekord,key,int(value)))
        for key, value in nomenklaturak.items():
            c.execute('insert into rekord_mutato_nomen_kapcsolo (record_nev, nomen_vagy_mutato_nev, nomen_vagy_mutato, sorrend) values(?,?,1,?);',(rekord,key,int(value)))
        conn.commit()
        conn.close()

    def newRekord(self,nev,cimke,leiras,tipus,kezdoidopont,vegidopont):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        date1=date.today()
        c.execute("insert into rekordleirasok (nev, cimke, leiras, tipus, utolso_modositas, kezdoidopont, vegidopont) values (?,?,?,?,?,?,?);",(nev,cimke,leiras,tipus,date.today(),kezdoidopont,vegidopont))
        conn.commit()
        conn.close()

    def listMezok_mutatok(self,rekord):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        query=c.execute('select nomen_vagy_mutato_nev, sorrend from rekord_mutato_nomen_kapcsolo where record_nev=? and nomen_vagy_mutato=?;',(rekord,0))
        eredmeny=[]
        for sor in query:
            eredmeny.append(sor)
        conn.commit()
        conn.close()
        return eredmeny

    def listMezok_nomenklaturak(self, rekord):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        query = c.execute(
            'select nomen_vagy_mutato_nev, sorrend from rekord_mutato_nomen_kapcsolo where record_nev=? and nomen_vagy_mutato=?;',
            (rekord, 1))
        eredmeny = []
        for sor in query:
            eredmeny.append(sor)
        conn.commit()
        conn.close()
        return eredmeny

    def listMezok_all(self, rekord):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        my_tuple=tuple([rekord])
        query = c.execute(
            'select nomen_vagy_mutato_nev,nomen_vagy_mutato, sorrend from rekord_mutato_nomen_kapcsolo where record_nev=?;',my_tuple)
        eredmeny = []
        for sor in query:
            eredmeny.append(sor)
        conn.commit()
        conn.close()
        return eredmeny

    def refreshDb(self, rekord, mutatok, nomenklaturak):
        global mainTableWidget
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        my_tuple = tuple([rekord])
        c.execute(
            'delete from rekord_mutato_nomen_kapcsolo where record_nev=?;',my_tuple)
        for key, value in mutatok.items():
            c.execute('insert into rekord_mutato_nomen_kapcsolo values(?,?,?,?)',(rekord,key,0,value))
        for key, value in nomenklaturak.items():
            c.execute('insert into rekord_mutato_nomen_kapcsolo values(?,?,?,?)', (rekord, key, 1, value))
        c.execute(
            'update rekordleirasok set utolso_modositas=? where nev=?;', (date.today(), rekord))
        conn.commit()
        conn.close()

        for row in range(mainTableWidget.rowCount()):
            if mainTableWidget.item(row,0).text() == rekord:
                mainTableWidget.item(row,4).setText(str(date.today()))

    def delete_rekord(self,x):
            conn = sqlite3.connect('datagov.db')
            conn.isolation_level = None
            c = conn.cursor()
            sorok=x.tableWidget.selectionModel().selectedRows()
            rekordok = []
            for sor in sorok:
                rekordok.append(x.tableWidget.item(sor.row(), 0).text())
            for rekord in rekordok:
                c.execute(
                    'delete from rekordleirasok where nev=?;', tuple([rekord]))
            x.deleteCurrentRow()
            x.valtoztatUi(x.ablak)
            conn.commit()
            conn.close()



