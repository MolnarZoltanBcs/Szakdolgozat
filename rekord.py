import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *

mutatok={}
nomenklaturak={}

class Ui_Rekordleirasok(QtWidgets.QMainWindow):
    def setupUi(x,  Ui_Rekordleirasok):
         global mainTableWidget
         x.ablak=Ui_Rekordleirasok
         x.ablak.setObjectName("Ui_Rekordleirasok")
         x.ablak.resize(1175, 500)
         
         x.ablak.setWindowTitle("Rekordleírások kezelése")
         
         x.tableWidget = QtWidgets.QTableWidget(x.ablak)
         x.tableWidget.setGeometry(QtCore.QRect(60, 75, 650, 370))
         x.tableWidget.setObjectName("tableWidget")
         x.tableWidget.horizontalHeader().setStretchLastSection(True)
         x.db=DbConnectRekord()
         x.tableWidgetSetUp(x.tableWidget)
         mainTableWidget=x.tableWidget

         x.pushButton_ujrekord = QtWidgets.QPushButton(x.ablak)
         x.pushButton_ujrekord.setGeometry(QtCore.QRect(60, 26, 180, 30))
         x.pushButton_ujrekord.setObjectName("pushButton_ujrekord")    
         x.pushButton_mezok = QtWidgets.QPushButton(x.ablak)
         x.pushButton_mezok.setGeometry(QtCore.QRect(260, 26, 110, 30))
         x.pushButton_mezok.setObjectName("pushButton_mezok")
         x.pushButton_torol = QtWidgets.QPushButton(x.ablak)
         x.pushButton_torol.setGeometry(QtCore.QRect(390, 26, 110, 30))
         x.pushButton_torol.setObjectName("pushButton_torol") 


         x.valtoztatUi(x.ablak)
         QtCore.QMetaObject.connectSlotsByName(x.ablak)
         
          
         x.pushButton_mezok.clicked.connect(x.rekord_mezok_window)
         
         x.pushButton_ujrekord.clicked.connect(x.rekord_uj_Window)
         
         #ez fogja törölni a kiválasztott sort 
         # x.pushButton_torol.clicked.connect(x.deleteCurrentRow)
          #modosit torol gomb allapot valtozasahoz
         x.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
         x.tableWidget.selectionModel().selectionChanged.connect(
             x.on_selection_changed
         )
 
         x.on_selection_changed()

         x.pushButton_torol.clicked.connect(lambda: x.delete_rekord())

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

    def valtoztatUi(x, Ui_Rekordleirasok):
         _translate = QtCore.QCoreApplication.translate
         Ui_Rekordleirasok.setWindowTitle(_translate("Ui_Rekordleirasok", "Rekordleírások kezelése"))
         
         
         item = x.tableWidget.horizontalHeaderItem(0)
         item.setText(_translate("Ui_Rekordleirasok", "Rekord neve"))
         item = x.tableWidget.horizontalHeaderItem(1)
         item.setText(_translate("Ui_Rekordleirasok", "Címke"))
         item = x.tableWidget.horizontalHeaderItem(2)
         item.setText(_translate("Ui_Rekordleirasok", "Leírás"))
         item = x.tableWidget.horizontalHeaderItem(3)
         item.setText(_translate("Ui_Rekordleirasok", "Típus"))
         item = x.tableWidget.horizontalHeaderItem(4)
         item.setText(_translate("Ui_Rekordleirasok", "Utolsó módosítás"))
         item = x.tableWidget.horizontalHeaderItem(5)
         item.setText(_translate("Ui_Rekordleirasok", "Érvényesség kezdete"))
         item = x.tableWidget.horizontalHeaderItem(6)
         item.setText(_translate("Ui_Rekordleirasok", "Érvényesség vége"))
         
         
         __sortingEnabled = x.tableWidget.isSortingEnabled()
         x.tableWidget.setSortingEnabled(False)

 
         x.tableWidget.setSortingEnabled(__sortingEnabled)
      
         x.pushButton_torol.setText(_translate("Ui_Rekordleirasok", "Törlés"))
         x.pushButton_mezok.setText(_translate("Ui_Rekordleirasok", "Mezők kezelése"))
         x.pushButton_ujrekord.setText(_translate("Ui_Rekordleirasok", "Új rekordleírás létrehozása"))

   
    
    def rekord_mezok_window(x):
         indexes = x.tableWidget.selectionModel().selectedRows()
         if len(indexes) != 1:
             QtWidgets.QMessageBox.question(x,
                                             "Helytelen kiválasztás",
                                             "Kérlek pontosan egy sort jelölj ki!",
                                             QtWidgets.QMessageBox.Ok)
             return
         for index in indexes:
             rekord=x.tableWidget.item(index.row(),0).text()
         x.window = QtWidgets.QMainWindow()
         x.ui_mezok = Ui_Mezok()
         x.ui_mezok.setupUi(x.window, rekord=rekord)
         x.window.show()     
            
    def rekord_uj_Window(x):
        x.window = QtWidgets.QMainWindow()
        x.ui_rekord_uj = Ui_Rekord_Uj()
        x.ui_rekord_uj.setupUi(x.window, x)
        x.window.show()     
      
      
class Ui_Rekord_Uj(object):
    def setupUi(x, Ui_Rekord_Uj, parent):
        x.ablak=Ui_Rekord_Uj
        x.parent=parent
        x.db=DbConnectRekord()
        x.ablak.setObjectName("Ui_Rekord_Uj")
        x.ablak.resize(429, 392)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.tabWidget = QtWidgets.QTabWidget(x.centralwidget)
        x.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 290))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.tabWidget.setFont(font)
        x.tabWidget.setObjectName("tabWidget")
        x.tab_attributum = QtWidgets.QWidget()
        x.tab_attributum.setObjectName("tab_attributum")
        x.comboBox_tipus = QtWidgets.QComboBox(x.tab_attributum)
        x.comboBox_tipus.setGeometry(QtCore.QRect(150, 150, 111, 22))
        x.comboBox_tipus.setObjectName("comboBox_tipus")
        x.comboBox_tipus.addItem("")
        x.comboBox_tipus.addItem("")
        x.lineEdit_rekordnev = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_rekordnev.setGeometry(QtCore.QRect(150, 30, 171, 20))
        x.lineEdit_rekordnev.setObjectName("lineEdit_rekordnev")
        x.label = QtWidgets.QLabel(x.tab_attributum)
        x.label.setGeometry(QtCore.QRect(30, 30, 111, 21))
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setObjectName("label")
        x.label_2 = QtWidgets.QLabel(x.tab_attributum)
        x.label_2.setGeometry(QtCore.QRect(30, 150, 111, 21))
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setObjectName("label_2")
        x.lineEdit_cimke = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_cimke.setGeometry(QtCore.QRect(150, 70, 171, 20))
        x.lineEdit_cimke.setObjectName("lineEdit_cimke")
        x.label_3 = QtWidgets.QLabel(x.tab_attributum)
        x.label_3.setGeometry(QtCore.QRect(10, 70, 131, 21))
        x.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_3.setObjectName("label_3")
        x.lineEdit_leiras = QtWidgets.QLineEdit(x.tab_attributum)
        x.lineEdit_leiras.setGeometry(QtCore.QRect(150, 110, 171, 20))
        x.lineEdit_leiras.setObjectName("lineEdit_leiras")
        x.label_4 = QtWidgets.QLabel(x.tab_attributum)
        x.label_4.setGeometry(QtCore.QRect(10, 110, 131, 21))
        x.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_4.setObjectName("label_4")
        x.tabWidget.addTab(x.tab_attributum, "")

        x.label_kezdet = QtWidgets.QLabel(x.tab_attributum)
        x.label_kezdet.setGeometry(QtCore.QRect(30, 190, 111, 21))
        x.label_kezdet.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        x.label_kezdet.setObjectName("label")

        x.dateEdit_kezdet = QtWidgets.QDateEdit(x.tab_attributum)
        x.dateEdit_kezdet.setGeometry(QtCore.QRect(150, 190, 131, 20))
        x.dateEdit_kezdet.setDateTime(QtCore.QDateTime.currentDateTime())
        x.dateEdit_kezdet.setCalendarPopup(True)
        x.dateEdit_kezdet.setObjectName("dateEdit_kezdet")

        x.label_veg = QtWidgets.QLabel(x.tab_attributum)
        x.label_veg.setGeometry(QtCore.QRect(30, 230, 111, 21))
        x.label_veg.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        x.label_veg.setObjectName("label")

        x.dateEdit_veg = QtWidgets.QDateEdit(x.tab_attributum)
        x.dateEdit_veg.setGeometry(QtCore.QRect(150, 230, 131, 20))
        x.dateEdit_veg.setDateTime(QtCore.QDateTime.currentDateTime())
        x.dateEdit_veg.setCalendarPopup(True)
        x.dateEdit_veg.setObjectName("dateEdit_veg")

        x.pushButton_Megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Megse.setGeometry(QtCore.QRect(310, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Megse.setFont(font)
        x.pushButton_Megse.clicked.connect(lambda: x.ablak.close())
        x.pushButton_Megse.setDefault(True)
        x.pushButton_Megse.setObjectName("pushButton_Megse")
        x.pushButton_Mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Mentes.setGeometry(QtCore.QRect(210, 310, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Mentes.setFont(font)
        x.pushButton_Mentes.setObjectName("pushButton_Mentes")
        x.pushButton_Kezeles = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_Kezeles.setGeometry(QtCore.QRect(70, 310, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.pushButton_Kezeles.setFont(font)
        x.pushButton_Kezeles.setObjectName("pushButton_Kezeles")
        x.ablak.setCentralWidget(x.centralwidget)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(x.ablak)
        x.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

        x.pushButton_Kezeles.clicked.connect(x.open_Ui_Mezok_Szerk)

        x.pushButton_Mentes.clicked.connect(lambda: x.save_record())
        x.pushButton_Mentes.clicked.connect(lambda: x.ablak.close())
        x.pushButton_Mentes.clicked.connect(lambda: x.parent.tableWidgetSetUp(x.parent.tableWidget))
        x.pushButton_Mentes.clicked.connect(lambda: x.parent.valtoztatUi(x.parent.ablak))


    def retranslateUi(x, Ui_Rekord_Uj):
        _translate = QtCore.QCoreApplication.translate
        Ui_Rekord_Uj.setWindowTitle(_translate("Ui_Rekord_Uj", "Új rekord létrehozása"))
        x.comboBox_tipus.setItemText(0, _translate("Ui_Rekord_Uj", "SAS"))
        x.comboBox_tipus.setItemText(1, _translate("Ui_Rekord_Uj", "SQL"))
        x.label.setText(_translate("Ui_Rekord_Uj", "Rekord neve:"))
        x.label_2.setText(_translate("Ui_Rekord_Uj", "Típus:"))
        x.label_3.setText(_translate("Ui_Rekord_Uj", "Nyomtatási címke:"))
        x.label_4.setText(_translate("Ui_Rekord_Uj", "Leírás:"))
        x.label_kezdet.setText(_translate("Ui_Rekord_Uj", "Kezdőidőpint:"))
        x.label_veg.setText(_translate("Ui_Rekord_Uj", "Végidőpont:"))
        x.tabWidget.setTabText(x.tabWidget.indexOf(x.tab_attributum), _translate("Ui_Rekord_Uj", "Attribútumok"))
        x.pushButton_Megse.setText(_translate("Ui_Rekord_Uj", "Mégse"))
        x.pushButton_Mentes.setText(_translate("Ui_Rekord_Uj", "Mentés"))
        x.pushButton_Kezeles.setText(_translate("Ui_Rekord_Uj", "Mezők kezelése"))
        
    def open_Ui_Mezok_Szerk(x):
        x.window = QtWidgets.QMainWindow()
        x.ui_mezok = Ui_Mezok_Szerk()
        x.ui_mezok.setupUi(x.window,x)
        x.window.setWindowTitle("Új rekord mezőinek a kiválaszása")
        x.window.show()    

    def save_record(x):
        global mutatok, nomenklaturak
        x.db.newRekord(x.lineEdit_rekordnev.text(), x.lineEdit_cimke.text(), x.lineEdit_leiras.text(),x.comboBox_tipus.currentText(),
                       x.dateEdit_kezdet.date().toPyDate(), x.dateEdit_veg.date().toPyDate())
        x.db.newRekordMezok(x.lineEdit_rekordnev.text())

    def get_mezok(self, ablak):
        pass


class Ui_Mezok(object):
    def setupUi(x, Ui_Mezok, rekord=None):
        x.ablak=Ui_Mezok
        x.ablak.setObjectName("Ui_Mezok")
        x.ablak.resize(687, 515)
        x.db=DbConnectRekord()
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 0, 671, 500))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.pushButton_szerk = QtWidgets.QPushButton(x.frame)
        x.pushButton_szerk.setGeometry(QtCore.QRect(30, 20, 300, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        x.pushButton_szerk.setIcon(icon)
        x.pushButton_szerk.setIconSize(QtCore.QSize(20, 20))
        x.pushButton_szerk.setDefault(True)
        x.pushButton_szerk.setObjectName("pushButton_szerk")

        x.tableWidget = QtWidgets.QTableWidget(x.frame)
        x.tableWidget.setShowGrid(True)
        x.tableWidgetSetUp(x.tableWidget,[30, 100, 601, 341], rekord=rekord)
        x.tableWidget.setColumnCount(3)
        x.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        x.tableWidget.setHorizontalHeaderItem(3, item)
        x.tableWidget.horizontalHeader().setStretchLastSection(True)
        x.tableWidget.verticalHeader().setVisible(True)
        x.tableWidget.verticalHeader().setSortIndicatorShown(False)
        x.tableWidget.verticalHeader().setStretchLastSection(False)
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)
        
        x.pushButton_szerk.clicked.connect(lambda: x.open_Ui_Mezok_Szerk(modosit=True, rekord=rekord))
        #x.pushButton_modosit.clicked.connect(x.open_Ui_Mezok_Modosit)
        
        x.retranslateUi(x.ablak)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def tableWidgetSetUp(x, tableWidget, lista : list, rekord=None):
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
        sorok=x.db.listMezok_all(rekord)
        sorok.sort(key=lambda y: y[2])
        sorszamlalo=0
        for sor in sorok:
            tableWidget.setRowCount(tableWidget.rowCount()+1)
            for i in range(3):
                if i==1:
                    item = QtWidgets.QTableWidgetItem(x.intToMezo(sor[1]))
                else:
                    item = QtWidgets.QTableWidgetItem(str(sor[i])) # kell még hogy ha elmentem a változásokat akkor bezáródjon mindkét ablak és úgy mentődjön el
                tableWidget.setItem(sorszamlalo,i,item)
            sorszamlalo+=1

    def retranslateUi(x, Ui_Mezok):
        _translate = QtCore.QCoreApplication.translate
        Ui_Mezok.setWindowTitle(_translate("Ui_Mezok", "Mezők"))
        x.pushButton_szerk.setText(_translate("Ui_Mezok", "Rekordhoz tartozó mezők kezelése"))
        x.tableWidget.setSortingEnabled(True)
        item = x.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Mezok", "Mező neve"))
        item = x.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Mezok", "Típus"))
        item = x.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Ui_Mezok", "Sorrend"))
        
    
    def intToMezo(self, szam):
        if szam == 0:
            return "Mutató"
        return "Nómenklatúra"
    
    def open_Ui_Mezok_Szerk(x, modosit=False, rekord=None):
        x.window = QtWidgets.QMainWindow()
        x.ui_mezok_szerkeztese = Ui_Mezok_Szerk()
        x.ui_mezok_szerkeztese.setupUi(x.window,x, modosit=modosit, rekord=rekord)
        x.window.show()    
        

class Ui_Mezok_Szerk(object):
    def setupUi(x, Ui_Mezok_Szerk,parent, modosit=False, rekord=None):
        x.ablak=Ui_Mezok_Szerk
        x.parent=parent
        x.ablak.setObjectName("Ui_Mezok_Szerk")
        x.ablak.resize(800, 815)
        x.mezok=None
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 10, 790, 805))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.pushButton_mentes = QtWidgets.QPushButton(x.frame)
        x.pushButton_mentes.setGeometry(QtCore.QRect(580, 700, 91, 41))
        x.pushButton_mentes.setObjectName("pushButton_mentes")
        x.pushButton_mentes.clicked.connect(lambda : x.save_mezok_es_sorrend(modosit=modosit, rekord=rekord))
        x.pushButton_mentes.clicked.connect(lambda : x.ablak.close())
        if modosit:
            x.pushButton_mentes.clicked.connect(lambda : x.parent.ablak.close())
        x.pushButton_megse = QtWidgets.QPushButton(x.frame)
        x.pushButton_megse.setGeometry(QtCore.QRect(690, 700, 91, 41))
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: x.ablak.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        x.label = QtWidgets.QLabel(x.frame)
        x.label.setGeometry(QtCore.QRect(30, 10, 300, 21))
        x.label.setObjectName("label")
        x.label_2 = QtWidgets.QLabel(x.frame)
        x.label_2.setGeometry(QtCore.QRect(20, 330, 300, 21))
        x.label_2.setObjectName("label_2")
        x.tableWidget_mutato = QtWidgets.QTableWidget(x.frame)
        x.tableWidget_mutato.setGeometry(QtCore.QRect(30, 40, 400, 211))
        x.tableWidgetSetUp(x.tableWidget_mutato,[60, 30, 700, 300])
        # x.tableWidget_mutato.setRowCount(4)
        x.tableWidget_mutato.setObjectName("tableWidget_mutato")

        x.tableWidget_mutato.horizontalHeader().setSortIndicatorShown(False)
        x.tableWidget_mutato.horizontalHeader().setStretchLastSection(True)
        x.tableWidget_mutato.verticalHeader().setStretchLastSection(False)
        x.tableWidget_nomen = QtWidgets.QTableWidget(x.frame)
        x.tableWidget_nomen.setGeometry(QtCore.QRect(30, 600, 461, 221))
        x.tableWidgetSetUp(x.tableWidget_nomen,[60,370,700,300], nomen=True)
        # x.tableWidget_nomen.setRowCount(4)
        x.tableWidget_nomen.setObjectName("tableWidget_nomen")

        x.tableWidget_nomen.horizontalHeader().setSortIndicatorShown(False)
        x.tableWidget_nomen.horizontalHeader().setStretchLastSection(True)
        x.tableWidget_nomen.verticalHeader().setStretchLastSection(False)

        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(modosit=modosit, rekord=rekord)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def save_mezok_es_sorrend(x, modosit=False, rekord=None):
        global mutatok
        global nomenklaturak
        k=x.tableWidget_mutato.rowCount()
        for sor in range(k):
            if x.tableWidget_mutato.cellWidget(sor,4).currentText() is not '' and int(x.tableWidget_mutato.cellWidget(sor,4).currentText())>0:
                mutatok[x.tableWidget_mutato.item(sor,0).text()]=int(x.tableWidget_mutato.cellWidget(sor,4).currentText())
        k = x.tableWidget_nomen.rowCount()
        for sor in range(k):
            if x.tableWidget_nomen.cellWidget(sor, 3).currentText() is not '' and int(x.tableWidget_nomen.cellWidget(sor, 3).currentText()) > 0:
                nomenklaturak[x.tableWidget_nomen.item(sor, 0).text()] = int(x.tableWidget_nomen.cellWidget(sor, 3).currentText())
        if modosit:
            x.db.refreshDb(rekord,mutatok,nomenklaturak)


    def retranslateUi(x, modosit=False, rekord=None):
        _translate = QtCore.QCoreApplication.translate
        x.ablak.setWindowTitle(_translate("Ui_Mezok_Szerk", "Kiválasztott rekord mezőinek a kezelése"))
        x.pushButton_mentes.setText(_translate("Ui_Mezok_Szerk", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Mezok_Szerk", "Mégse"))
        x.label.setText(_translate("Ui_Mezok_Szerk", "Mutatók kiválasztása:"))
        x.label_2.setText(_translate("Ui_Mezok_Szerk", "Nómenklatúrák kiválasztása:"))


        x.db=DbConnectRekord()
        oszlopnevek=["Változó neve","Hossz","Típus","Mutató csoport", "Rekordhoz ad"]
        k=4
        query=x.db.listMutat()
        for row in query:
            rows = x.tableWidget_mutato.rowCount()
            x.tableWidget_mutato.setRowCount(rows + 1)
            for oszlop in range(k):
                x.tableWidget_mutato.setItem(rows, oszlop, QTableWidgetItem(str(row[oszlop])))
            comboBox = QtWidgets.QComboBox()
            x.tableWidget_mutato.setCellWidget(rows, k, comboBox)
            comboBox.addItem("")
            for i in range(1,21):
                comboBox.addItem(str(i))
        if modosit and rekord:
            mutatok=x.db.listMezok_mutatok(rekord)
            i=0
            query = x.db.listMutat()
            for sor in query:
                for my_tuple in mutatok:
                    if sor[0] == my_tuple[0]:
                        x.tableWidget_mutato.cellWidget(i,4).setCurrentIndex(my_tuple[1])
                i+=1

        x.oszlopNevBeallitas(oszlopnevek)

        oszlopnevek = ["Változó neve", "Hossz", "Típus", "Rekordhoz ad"]
        k = 3
        query = x.db.listMutat(nomen=True)
        for row in query:
            rows = x.tableWidget_nomen.rowCount()
            x.tableWidget_nomen.setRowCount(rows + 1)
            for oszlop in range(k):
                x.tableWidget_nomen.setItem(rows, oszlop, QTableWidgetItem(str(row[oszlop])))
            comboBox = QtWidgets.QComboBox()
            x.tableWidget_mutato.setCellWidget(rows, k, comboBox)
            comboBox.addItem("")
            for i in range(1, 21):
                comboBox.addItem(str(i))
            x.tableWidget_nomen.setCellWidget(rows, k, comboBox)
        if modosit and rekord:
            nomenklaturak=x.db.listMezok_nomenklaturak(rekord)
            i=0
            query = x.db.listMutat(nomen=True)
            for sor in query:
                for my_tuple in nomenklaturak:
                    if sor[0] == my_tuple[0]:
                        x.tableWidget_nomen.cellWidget(i,3).setCurrentIndex(my_tuple[1])
                i+=1
        x.oszlopNevBeallitas(oszlopnevek, nomen=True)

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



