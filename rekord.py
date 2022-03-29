import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *

class Ui_Rekordleirasok(QtWidgets.QMainWindow):
    def setupUi(x,  Ui_Rekordleirasok):
         Ui_Rekordleirasok.setObjectName("Ui_Rekordleirasok")
         Ui_Rekordleirasok.resize(1175, 500)
         
         Ui_Rekordleirasok.setWindowTitle("Rekordleírások kezelése")        
         
         x.tableWidget = QtWidgets.QTableWidget(Ui_Rekordleirasok)        
         x.tableWidget.setGeometry(QtCore.QRect(60, 75, 650, 370))
         x.tableWidget.setObjectName("tableWidget")
         x.tableWidget.horizontalHeader().setStretchLastSection(True)
         x.db=DbConnectRekord()
         x.tableWidgetSetUp(x.tableWidget)

         # x.tableWidget.setColumnCount(6)
         # x.tableWidget.setRowCount(3)
         #
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setVerticalHeaderItem(0, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setVerticalHeaderItem(1, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setVerticalHeaderItem(2, item)
         #
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setHorizontalHeaderItem(0, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setHorizontalHeaderItem(1, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setHorizontalHeaderItem(2, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setHorizontalHeaderItem(3, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setHorizontalHeaderItem(4, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setHorizontalHeaderItem(5, item)
         
         
         
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(0, 0, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(0, 1, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(0, 2, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(0, 4, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(0, 5, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(1, 0, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(1, 1, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(1, 2, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(1, 4, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(1, 5, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(2, 0, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(2, 1, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(2, 2, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(2, 4, item)
         # item = QtWidgets.QTableWidgetItem()
         # x.tableWidget.setItem(2, 5, item)
              
         #x.pushButton_modosit = QtWidgets.QPushButton(Ui_Rekordleirasok)
       #  x.pushButton_modosit.setGeometry(QtCore.QRect(60, 26, 91, 23))
        # x.pushButton_modosit.setObjectName("pushButton_modosit")          
         x.pushButton_ujrekord = QtWidgets.QPushButton(Ui_Rekordleirasok)
         x.pushButton_ujrekord.setGeometry(QtCore.QRect(60, 26, 140, 23))
         x.pushButton_ujrekord.setObjectName("pushButton_ujrekord")    
         x.pushButton_mezok = QtWidgets.QPushButton(Ui_Rekordleirasok)
         x.pushButton_mezok.setGeometry(QtCore.QRect(240, 26, 91, 23))
         x.pushButton_mezok.setObjectName("pushButton_mezok")
         x.pushButton_torol = QtWidgets.QPushButton(Ui_Rekordleirasok)
         x.pushButton_torol.setGeometry(QtCore.QRect(371, 26, 91, 23))
         x.pushButton_torol.setObjectName("pushButton_torol") 


         x.valtoztatUi(Ui_Rekordleirasok)
         QtCore.QMetaObject.connectSlotsByName(Ui_Rekordleirasok)
         
          
         x.pushButton_mezok.clicked.connect(x.rekord_mezok_window)
         
         x.pushButton_ujrekord.clicked.connect(x.rekord_uj_Window)
         
         #ez fogja törölni a kiválasztott sort 
         x.pushButton_torol.clicked.connect(x.deleteCurrentRow)
          #modosit torol gomb allapot valtozasahoz 
         x.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
         x.tableWidget.selectionModel().selectionChanged.connect(
             x.on_selection_changed
         )
 
         x.on_selection_changed()

    def tableWidgetSetUp(self, tableWidget, nomen=False):
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
        result = QtWidgets.QMessageBox.question(self,
                      "Törlés megerősítése...",
                      "Biztos ki akarod törölni a kiválaszott sorokat?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        

        if result == QtWidgets.QMessageBox.Yes:
            indexes = self.tableWidget.selectionModel().selectedRows() 
            for index in sorted(indexes):
                self.tableWidget.removeRow(index.row())                
        
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
         x.window = QtWidgets.QMainWindow()
         x.ui = Ui_Mezok()
         x.ui.setupUi(x.window)
         x.window.show()     
            
    def rekord_uj_Window(x):
        x.window = QtWidgets.QMainWindow()
        x.ui = Ui_Rekord_Uj()
        x.ui.setupUi(x.window)            
        x.window.show()     
      
      
class Ui_Rekord_Uj(object):
    def setupUi(x, Ui_Rekord_Uj):
        x.ablak=Ui_Rekord_Uj
        x.ablak.setObjectName("Ui_Rekord_Uj")
        x.ablak.resize(429, 392)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.tabWidget = QtWidgets.QTabWidget(x.centralwidget)
        x.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 281))
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
        

    def retranslateUi(x, Ui_Rekord_Uj):
        _translate = QtCore.QCoreApplication.translate
        Ui_Rekord_Uj.setWindowTitle(_translate("Ui_Rekord_Uj", "Új rekord létrehozása"))
        x.comboBox_tipus.setItemText(0, _translate("Ui_Rekord_Uj", "SAS"))
        x.comboBox_tipus.setItemText(1, _translate("Ui_Rekord_Uj", "SQL"))
        x.label.setText(_translate("Ui_Rekord_Uj", "Rekord neve:"))
        x.label_2.setText(_translate("Ui_Rekord_Uj", "Típus:"))
        x.label_3.setText(_translate("Ui_Rekord_Uj", "Nyomtatási címke:"))
        x.label_4.setText(_translate("Ui_Rekord_Uj", "Leírás:"))
        x.tabWidget.setTabText(x.tabWidget.indexOf(x.tab_attributum), _translate("Ui_Rekord_Uj", "Attribútumok"))
        x.pushButton_Megse.setText(_translate("Ui_Rekord_Uj", "Mégse"))
        x.pushButton_Mentes.setText(_translate("Ui_Rekord_Uj", "Mentés"))
        x.pushButton_Kezeles.setText(_translate("Ui_Rekord_Uj", "Mezők kezelése"))
        
    def open_Ui_Mezok_Szerk(x):
        x.window = QtWidgets.QMainWindow()
        x.ui_mezok = Ui_Mezok_Szerk()
        x.ui_mezok.setupUi(x.window)
        x.window.setWindowTitle("Új rekord mezőinek a kiválaszása")
        x.window.show()    

    def save_record(self):
        mezok=self.get_mezok(self.ui_mezok.mezok)

    def get_mezok(self, ablak):
        pass


class Ui_Mezok(object):
    def setupUi(x, Ui_Mezok):
        Ui_Mezok.setObjectName("Ui_Mezok")
        Ui_Mezok.resize(687, 515)
        x.centralwidget = QtWidgets.QWidget(Ui_Mezok)
        x.centralwidget.setObjectName("centralwidget")
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 0, 671, 471))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.pushButton_szerk = QtWidgets.QPushButton(x.frame)
        x.pushButton_szerk.setGeometry(QtCore.QRect(30, 20, 260, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        x.pushButton_szerk.setIcon(icon)
        x.pushButton_szerk.setIconSize(QtCore.QSize(20, 20))
        x.pushButton_szerk.setDefault(True)
        x.pushButton_szerk.setObjectName("pushButton_szerk")
      #  x.pushButton_modosit = QtWidgets.QPushButton(x.frame)
      #  x.pushButton_modosit.setGeometry(QtCore.QRect(170, 20, 111, 31))
      #  icon1 = QtGui.QIcon()
      #  icon1.addPixmap(QtGui.QPixmap("edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #x.pushButton_modosit.setIcon(icon1)
        #x.pushButton_modosit.setIconSize(QtCore.QSize(20, 20))
        #x.pushButton_modosit.setObjectName("pushButton_modosit")
        #x.pushButton_metatrendel = QtWidgets.QPushButton(x.frame)
        #x.pushButton_metatrendel.setGeometry(QtCore.QRect(300, 20, 151, 31))
        #x.pushButton_metatrendel.setObjectName("pushButton_metatrendel")
        x.pushButton_torol = QtWidgets.QPushButton(x.frame)
        x.pushButton_torol.setGeometry(QtCore.QRect(320, 20, 131, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        x.pushButton_torol.setIcon(icon2)
        x.pushButton_torol.setIconSize(QtCore.QSize(20, 20))
        x.pushButton_torol.setObjectName("pushButton_torol")
        x.pushButton_frissit = QtWidgets.QPushButton(x.frame)
        x.pushButton_frissit.setGeometry(QtCore.QRect(620, 20, 41, 31))
        x.pushButton_frissit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        x.pushButton_frissit.setIcon(icon3)
        x.pushButton_frissit.setIconSize(QtCore.QSize(30, 30))
        x.pushButton_frissit.setFlat(True)
        x.pushButton_frissit.setObjectName("pushButton_frissit")
        x.tableWidget = QtWidgets.QTableWidget(x.frame)
        x.tableWidget.setGeometry(QtCore.QRect(30, 100, 601, 341))
        x.tableWidget.setShowGrid(True)
        x.tableWidget.setRowCount(10)
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
        Ui_Mezok.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Mezok)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        x.menubar.setObjectName("menubar")
        Ui_Mezok.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Mezok)
        x.statusbar.setObjectName("statusbar")
        Ui_Mezok.setStatusBar(x.statusbar)
        
        x.pushButton_szerk.clicked.connect(x.open_Ui_Mezok_Szerk)
        #x.pushButton_modosit.clicked.connect(x.open_Ui_Mezok_Modosit)
        
        x.retranslateUi(Ui_Mezok)
        QtCore.QMetaObject.connectSlotsByName(Ui_Mezok)

    def retranslateUi(x, Ui_Mezok):
        _translate = QtCore.QCoreApplication.translate
        Ui_Mezok.setWindowTitle(_translate("Ui_Mezok", "Mezők"))
        x.pushButton_szerk.setText(_translate("Ui_Mezok", "Rekordhoz tartozó mezők kezelése"))
      #  x.pushButton_modosit.setText(_translate("Ui_Mezok", "Módosít"))
      #  x.pushButton_metatrendel.setText(_translate("Ui_Mezok", "Meta hozzárendelés"))
     #   x.pushButton_torol.setText(_translate("Ui_Mezok", "Törlés"))
        x.tableWidget.setSortingEnabled(True)
        item = x.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Mezok", "Mező neve"))
        item = x.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Mezok", "Típus"))
        item = x.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Ui_Mezok", "Hossz"))
        
    
    
    
    def open_Ui_Mezok_Szerk(x):
        x.window = QtWidgets.QMainWindow()
        x.ui_mezok_szerkeztese = Ui_Mezok_Szerk()
        x.ui_mezok_szerkeztese.setupUi(x.window)
        x.window.show()    
        

class Ui_Mezok_Szerk(object):
    def setupUi(x, Ui_Mezok_Szerk):
        x.ablak=Ui_Mezok_Szerk
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
        # x.tableWidget_mutato.setColumnCount(5)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(0, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(1, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(1, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(2, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(2, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(3, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(3, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_mutato.setItem(3, 2, item)
        x.tableWidget_mutato.horizontalHeader().setSortIndicatorShown(False)
        x.tableWidget_mutato.horizontalHeader().setStretchLastSection(True)
        x.tableWidget_mutato.verticalHeader().setStretchLastSection(False)
        x.tableWidget_nomen = QtWidgets.QTableWidget(x.frame)
        x.tableWidget_nomen.setGeometry(QtCore.QRect(30, 600, 461, 221))
        x.tableWidgetSetUp(x.tableWidget_nomen,[60,370,700,300], nomen=True)
        # x.tableWidget_nomen.setRowCount(4)
        x.tableWidget_nomen.setObjectName("tableWidget_nomen")
        # x.tableWidget_nomen.setColumnCount(4)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(0, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(1, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(1, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(2, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(2, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(3, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(3, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # x.tableWidget_nomen.setItem(3, 2, item)
        x.tableWidget_nomen.horizontalHeader().setSortIndicatorShown(False)
        x.tableWidget_nomen.horizontalHeader().setStretchLastSection(True)
        x.tableWidget_nomen.verticalHeader().setStretchLastSection(False)
        # x.checkBox = QtWidgets.QCheckBox(x.tableWidget_mutato)
        # x.checkBox.setGeometry(QtCore.QRect(520, 80, 21, 21))
        # x.checkBox.setText("")
        # x.checkBox.setObjectName("checkBox")
        # x.checkBox_2 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_2.setGeometry(QtCore.QRect(520, 110, 21, 21))
        # x.checkBox_2.setText("")
        # x.checkBox_2.setObjectName("checkBox_2")
        # x.checkBox_3 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_3.setGeometry(QtCore.QRect(520, 140, 21, 21))
        # x.checkBox_3.setText("")
        # x.checkBox_3.setObjectName("checkBox_3")
        # x.checkBox_4 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_4.setGeometry(QtCore.QRect(520, 170, 21, 21))
        # x.checkBox_4.setText("")
        # x.checkBox_4.setObjectName("checkBox_4")
        # x.checkBox_5 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_5.setGeometry(QtCore.QRect(410, 340, 21, 21))
        # x.checkBox_5.setText("")
        # x.checkBox_5.setObjectName("checkBox_5")
        # x.checkBox_6 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_6.setGeometry(QtCore.QRect(410, 370, 21, 21))
        # x.checkBox_6.setText("")
        # x.checkBox_6.setObjectName("checkBox_6")
        # x.checkBox_7 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_7.setGeometry(QtCore.QRect(410, 400, 21, 21))
        # x.checkBox_7.setText("")
        # x.checkBox_7.setObjectName("checkBox_7")
        # x.checkBox_8 = QtWidgets.QCheckBox(x.frame)
        # x.checkBox_8.setGeometry(QtCore.QRect(410, 430, 21, 21))
        # x.checkBox_8.setText("")
        # x.checkBox_8.setObjectName("checkBox_8")
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def retranslateUi(x):
        _translate = QtCore.QCoreApplication.translate
        x.ablak.setWindowTitle(_translate("Ui_Mezok_Szerk", "Kiválasztott rekord mezőinek a kezelése"))
        x.pushButton_mentes.setText(_translate("Ui_Mezok_Szerk", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Mezok_Szerk", "Mégse"))
        x.label.setText(_translate("Ui_Mezok_Szerk", "Mutatók kiválasztása:"))
        x.label_2.setText(_translate("Ui_Mezok_Szerk", "Nómenklatúrák kiválasztása:"))
        # item = x.tableWidget_mutato.horizontalHeaderItem(0)
        # item.setText(_translate("Ui_Mezok_Szerk", "Változó neve"))
        # item = x.tableWidget_mutato.horizontalHeaderItem(1)
        # item.setText(_translate("Ui_Mezok_Szerk", "Hossz"))
        # item = x.tableWidget_mutato.horizontalHeaderItem(2)
        # item.setText(_translate("Ui_Mezok_Szerk", "Típus"))
        # item = x.tableWidget_mutato.horizontalHeaderItem(3)
        # item.setText(_translate("Ui_Mezok_Szerk", "Mutató csoport"))
        # item = x.tableWidget_mutato.horizontalHeaderItem(4)
        # item.setText(_translate("Ui_Mezok_Szerk", "Rekordhoz ad"))
        # __sortingEnabled = x.tableWidget_mutato.isSortingEnabled()
        # x.tableWidget_mutato.setSortingEnabled(False)
        # # item = x.tableWidget_mutato.item(0, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Testsuly"))
        # # item = x.tableWidget_mutato.item(0, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "3"))
        # # item = x.tableWidget_mutato.item(0, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Egész szám"))
        # # item = x.tableWidget_mutato.item(1, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Datum"))
        # # item = x.tableWidget_mutato.item(1, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "8"))
        # # item = x.tableWidget_mutato.item(1, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Dátum"))
        # # item = x.tableWidget_mutato.item(2, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "sum_bevetel"))
        # # item = x.tableWidget_mutato.item(2, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "15"))
        # # item = x.tableWidget_mutato.item(2, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Egész szám"))
        # # item = x.tableWidget_mutato.item(3, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Adokedvezmeny"))
        # # item = x.tableWidget_mutato.item(3, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "8"))
        # # item = x.tableWidget_mutato.item(3, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Lebegőpontos szám"))
        # # x.tableWidget_mutato.setSortingEnabled(__sortingEnabled)
        # item = x.tableWidget_nomen.horizontalHeaderItem(0)
        # item.setText(_translate("Ui_Mezok_Szerk", "Változó neve"))
        # item = x.tableWidget_nomen.horizontalHeaderItem(1)
        # item.setText(_translate("Ui_Mezok_Szerk", "Hossz"))
        # item = x.tableWidget_nomen.horizontalHeaderItem(2)
        # item.setText(_translate("Ui_Mezok_Szerk", "Típus"))
        # item = x.tableWidget_nomen.horizontalHeaderItem(3)
        # item.setText(_translate("Ui_Mezok_Szerk", "Rekordhoz ad"))
        # __sortingEnabled = x.tableWidget_nomen.isSortingEnabled()
        # x.tableWidget_nomen.setSortingEnabled(False)
        # # item = x.tableWidget_nomen.item(0, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "phone"))
        # # item = x.tableWidget_nomen.item(0, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "1"))
        # # item = x.tableWidget_nomen.item(0, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Karakteres"))
        # # item = x.tableWidget_nomen.item(1, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "address"))
        # # item = x.tableWidget_nomen.item(1, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "18"))
        # # item = x.tableWidget_nomen.item(1, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Karakteres"))
        # # item = x.tableWidget_nomen.item(2, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "telepules_id"))
        # # item = x.tableWidget_nomen.item(2, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "9"))
        # # item = x.tableWidget_nomen.item(2, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Egész szám"))
        # # item = x.tableWidget_nomen.item(3, 0)
        # # item.setText(_translate("Ui_Mezok_Szerk", "postcode"))
        # # item = x.tableWidget_nomen.item(3, 1)
        # # item.setText(_translate("Ui_Mezok_Szerk", "8"))
        # # item = x.tableWidget_nomen.item(3, 2)
        # # item.setText(_translate("Ui_Mezok_Szerk", "Egész szám"))
        # x.tableWidget_nomen.setSortingEnabled(__sortingEnabled)
        #
        # _translate = QtCore.QCoreApplication.translate

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


