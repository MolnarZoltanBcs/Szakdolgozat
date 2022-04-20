import os
import sys
from datetime import date
import pandas
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *
from mutatok import Ui_Mutatok_UJ, Ui_Mutatok


class Ui_Nomenklatura(QtWidgets.QMainWindow):
    def setupUi(self,  Ui_Nomenklatura):
         self.ablak=Ui_Nomenklatura
         self.ui=Ui_Mutatok()
         self.db=DbConnect()
         self.ui.setupUi(self.ablak, nomen=True)
         self.ui.ablak.setWindowTitle("Nomenklaturák kezelése")
         self.ui.pushButton_elemek = QtWidgets.QPushButton(self.ui.ablak)
         self.ui.pushButton_elemek.setGeometry(QtCore.QRect(302, 26, 130, 23))
         self.ui.pushButton_elemek.setObjectName("pushButton_elemek") #nomeklatura elemek
         self.ui.pushButton_elemek.setText("Nomenklatúra Elemek") #nomeklatura elemek
         self.ui.pushButton_kepzes = QtWidgets.QPushButton(self.ui.ablak)
         self.ui.pushButton_kepzes.setGeometry(QtCore.QRect(462, 26, 91, 23))
         self.ui.pushButton_kepzes.setObjectName("pushButton_kepzes")  # kepzes
         self.ui.pushButton_kepzes.setText("Képzés")  # kepzes
         self.ui.pushButton_torol.setGeometry(QtCore.QRect(583, 26, 91, 23))
         self.ui.pushButton_export.setGeometry(QtCore.QRect(704, 26, 110, 23))
         self.ui.radioButton_export_csv.setGeometry(QtCore.QRect(845, 26, 110, 23))
         self.ui.radioButton_export_excel.setGeometry(QtCore.QRect(895, 26, 110, 23))



         #
         # self.valtoztatUi(self.ui.ablak)
         # QtCore.QMetaObject.connectSlotsByName(self.ui.ablak)

         #ez fogja megnyitni az nomenklatura elemek ablakot ablakot
         self.ui.pushButton_elemek.clicked.connect(self.open_Nomen_Elemek)
         #
         #     #ez nyitja meg a kepzest
         self.ui.pushButton_kepzes.clicked.connect(lambda: self.open_Nomen_Elemek_Kepzes(self.ui))
         #
         # self.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
         # self.ui.tableWidget.selectionModel().selectionChanged.connect(lambda: self.on_selection_changed())
         # self.on_selection_changed()
                  
        
    def on_selection_changed(self):
        self.pushButton_modosit.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_torol.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_elemek.setEnabled(
            bool(self.tableWidget.selectionModel().selectedRows())
       )
        self.pushButton_kepzes.setEnabled(
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

    def valtoztatUi(self, Ui_Nomenklatura):
         _translate = QtCore.QCoreApplication.translate
         Ui_Nomenklatura.setWindowTitle(_translate("Ui_Nomenklatura", "Nómenklatúrák kezelése"))
         
         cimkek = ["Változó neve", "Nyomtatási cimke", "Leírás", "Hossz", "Típus", "Utolsó módosítás", "Érvényesség kezdete", "Érvényesség vége"]
         i=0
         for elem in cimkek:
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Ui_Nomenklatura", elem))
            i+=1
         
         
         __sortingEnabled = self.tableWidget.isSortingEnabled()
         self.tableWidget.setSortingEnabled(False)
 
         self.tableWidget.setSortingEnabled(__sortingEnabled)
         self.pushButton_uj.setText(_translate("Ui_Nomenklatura", "Új létrehozása"))
         self.pushButton_modosit.setText(_translate("Ui_Nomenklatura", "Módosítás"))
         self.pushButton_torol.setText(_translate("Ui_Nomenklatura", "Törlés"))
         self.pushButton_export.setText(_translate("Ui_Nomenklatura", "Kijelöltek exportja"))
         self.pushButton_elemek.setText(_translate("Ui_Nomenklatura", "Nómenklatúra Elemek"))
         self.pushButton_kepzes.setText(_translate("Ui_Nomenklatura", "Képzés"))

    #definialjuk az uj mutato letrehozasa ablakot
    #ez nyitja meg
    def openUjNomeklatura(self):
         self.window = QtWidgets.QMainWindow()
         self.ui2 =  Ui_Mutatok_UJ()
         self.ui2.setupUi(self.window, self.ablak, nomen=True) #az ablak a parentje az új windownak
         self.ui2.comboBox.addItem("Karakteres")
         self.ui2.csoportLabel.deleteLater()
         self.ui2.lineEdit_csoport.deleteLater()
         self.ui2.ervenyessegVegeLabel.setGeometry(QtCore.QRect(40, 200, 161, 51))
         self.ui2.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 210, 201, 31))
         self.ui2.ervenyessegVegeLabel.setGeometry(QtCore.QRect(40, 250, 161, 31))
         self.ui2.dateEdit_veg.setGeometry(QtCore.QRect(220, 250, 151, 31))
         self.window.show()
    #es definialjuk a modosit mutato ablakot
    def openModositNomenklatura(self):
         self.window = QtWidgets.QMainWindow()
         self.ui_uj_nomen =  Ui_Mutatok_UJ()
         self.ui_uj_nomen.setupModositUi(self.window, self.ablak)
         self.window.setWindowTitle("Kiválasztott nómenklatúra módosítása")
         self.ui_uj_nomen.comboBox.addItem("Karakteres")
         # self.ui.label_6.deleteLater()
         self.ui_uj_nomen.lineEdit_csoport.deleteLater()
         # self.ui.label_7.setGeometry(QtCore.QRect(40, 200, 161, 51))
         self.ui_uj_nomen.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 210, 201, 31))
         # self.ui.label_8.setGeometry(QtCore.QRect(40, 250, 161, 31))
         self.ui_uj_nomen.dateEdit_veg.setGeometry(QtCore.QRect(220, 250, 151, 31))
         
         self.window.show()
         
    # itt definialjuk a nomen_elemek megnyitasa ablakot     
    def open_Nomen_Elemek(self):

         indexes = self.ui.tableWidget.selectionModel().selectedRows()
         self.ui.tableWidget.clearSelection()
         # self.ui.tableWidget.selectionModel()
         if len(indexes) != 1:
             result = QtWidgets.QMessageBox.question(self,
                                                     "Hibás kijelölés",
                                                     "Egyszerre csak egy sor elemeit tekintheted meg, kérlek pontosan egy sort jelölj ki!",
                                                     QtWidgets.QMessageBox.Ok)
             return
         for elem in sorted(indexes):
             kepzett = self.db.getKepzettE(self.ui.tableWidget.item(elem.row(),0).text())
             if kepzett:
                 result = QtWidgets.QMessageBox.question(self,
                                                         "Hibás kijelölés",
                                                         "A kijelölt elem egy képzett nomenklatúra, tehát nincsenek elemei. Kérlek válassz újra!",
                                                         QtWidgets.QMessageBox.Ok)
                 return
         for elem in sorted(indexes):
             nev=self.ui.tableWidget.item(elem.row(),0).text()
         self.window = QtWidgets.QMainWindow()
         self.ui_uj =  Ui_Nomen_Elemek()
         self.ui_uj.setupUi(self.window, nev)
         self.window.show()
    
    def open_Nomen_Elemek_Kepzes(self, ablak):
        indexes = ablak.tableWidget.selectionModel().selectedRows()
        ablak.tableWidget.selectionModel().clearSelection()
        lista = []
        for index in indexes:
            lista.append(ablak.tableWidget.item(index.row(), 0).text())
        if len(lista)<2:
            result = QtWidgets.QMessageBox.question(self,
                                                    "Hibás kijelölés",
                                                    "Kérlek kettő nomenklatúrát jelölj ki a képzéshez!",
                                                    QtWidgets.QMessageBox.Ok)
            return
        self.window = QtWidgets.QMainWindow()
        self.ui_uj_kepzes =  Ui_Nomen_Elemek_Kepzes()
        self.ui_uj_kepzes.setupUi(self.window,self.ui, lista[0], lista[1])
        self.window.show()
    




class Ui_Nomen_Elemek(object):
    def setupUi(self, Ui_Nomen_Elemek, nev):
        self.ablak=Ui_Nomen_Elemek
        self.nev=nev
        self.db=DbConnect()
        self.ablak.setObjectName("Ui_Nomen_Elemek")
        self.ablak.resize(786, 516)
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 771, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_uj = QtWidgets.QPushButton(self.frame)
        self.pushButton_uj.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.pushButton_uj.setAutoFillBackground(False)
        self.pushButton_uj.setObjectName("pushButton_uj")
        self.pushButton_modosit = QtWidgets.QPushButton(self.frame)
        self.pushButton_modosit.setGeometry(QtCore.QRect(160, 20, 121, 41))
        self.pushButton_modosit.setObjectName("pushButton_modosit")
        self.pushButton_aktualizal = QtWidgets.QPushButton(self.frame)
        self.pushButton_aktualizal.setGeometry(QtCore.QRect(310, 20, 171, 41))
        self.pushButton_aktualizal.setObjectName("pushButton_aktualizal")
        self.pushButton_torol = QtWidgets.QPushButton(self.frame)
        self.pushButton_torol.setGeometry(QtCore.QRect(510, 20, 121, 41))
        self.pushButton_torol.setObjectName("pushButton_torol")
        # self.pushButton_frissit = QtWidgets.QPushButton(self.frame)
        # self.pushButton_frissit.setGeometry(QtCore.QRect(640, 20, 121, 41))
        # self.pushButton_frissit.setObjectName("pushButton_frissit")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 650, 311))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        sorok=self.db.list_nomen_elemek(nev)
        i=0
        for sor in sorok:
            self.tableWidget.setRowCount(i+1)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(sor[1]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(sor[2]))
            i+=1

        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.nevButton = QLabel(self.frame)
        self.nevButton.setGeometry(QtCore.QRect(20, 450, 121, 41))
        self.nevButton.setAutoFillBackground(False)
        self.nevButton.setObjectName("pushButton_uj")

        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(self.nev)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)
        
        #ez nyitja meg az uj elemek ablakot
        self.pushButton_uj.clicked.connect(lambda: self.open_Nomen_Elemek_Uj(nev))
         
        #ez nyitja meg a modosit elemek ablakot
        self.pushButton_modosit.clicked.connect(lambda: self.open_Nomen_Elemek_Modosit(nev))
        
        #ez nyitja meg az aktualizal ablakot
        self.pushButton_aktualizal.clicked.connect(self.open_Nomen_Elemek_Akt)

        self.pushButton_torol.clicked.connect(lambda: self.db.delete_nomen_elem(self))
        
    def labelSetUp(self, label, kezdopont_x, kezdopont_y, hossz_x, hossz_y, nev):
        label.setGeometry(QtCore.QRect(kezdopont_x, kezdopont_y, hossz_x, hossz_y))
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        label.setObjectName(nev)

    def retranslateUi(self, nev):
        _translate = QtCore.QCoreApplication.translate
        self.ablak.setWindowTitle(_translate("Ui_Nomen_Elemek", "Nómenklatúra elemek - "+nev))
        self.pushButton_uj.setText(_translate("Ui_Nomen_Elemek", "Új létrehozása"))
        self.pushButton_modosit.setText(_translate("Ui_Nomen_Elemek", "Módosítás"))
        self.pushButton_aktualizal.setText(_translate("Ui_Nomen_Elemek", "Értékek aktualizálása"))
        self.pushButton_torol.setText(_translate("Ui_Nomen_Elemek", "Törlés"))
        # self.pushButton_frissit.setText(_translate("Ui_Nomen_Elemek", "Frissítés"))
        self.nevButton.setText(_translate(self.nevButton.objectName(), nev))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Nomen_Elemek", "Érték"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Nomen_Elemek", "Nyomtatási címke"))

    def open_Nomen_Elemek_Uj(self, nev):
         self.window = QtWidgets.QMainWindow()
         self.ui =  Ui_Nomen_Elemek_Ujfelvetel()
         self.window.setWindowTitle("Új nómenklatúra elem felvétele")
         self.ui.setupUi(self.window, nev, parentablak=self)
         self.window.show()
         
    def open_Nomen_Elemek_Modosit(self, nev):
         self.window = QtWidgets.QMainWindow()
         self.ui =  Ui_Nomen_Elemek_Ujfelvetel()
         self.window.setWindowTitle("Nómenklatúra elem módosítása")
         self.ui.setupUi(self.window, nev, parentablak=self, modosit=True)
         self.window.show()
    
    def open_Nomen_Elemek_Akt(self):
         self.window = QtWidgets.QMainWindow()
         self.ui =  Ui_Nomen_Elemek_Akt()
         self.ui.setupUi(self.window, self, self.db, self.nev)
         self.window.show()
         
   


class Ui_Nomen_Elemek_Ujfelvetel(object):
    def setupUi(self, Ui_Nomen_Elemek_Ujfelvetel, nev, parentablak=None, modosit=False):
        self.ablak =  Ui_Nomen_Elemek_Ujfelvetel
        self.ablak.setObjectName("Ui_Nomen_Elemek_Ujfelvetel")
        self.ablak.resize(459, 267)
        self.parentablak=parentablak
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 141, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 60, 191, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 191, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.db=DbConnect()
        self.pushButton_mentes = QtWidgets.QPushButton(self.frame)
        self.pushButton_mentes.setGeometry(QtCore.QRect(240, 170, 91, 41))
        self.pushButton_mentes.setObjectName("pushButton_mentes")
        if modosit:
            self.lineEdit.setReadOnly(True)
            indexes=self.parentablak.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                try:
                    self.lineEdit.setText(self.parentablak.tableWidget.item(index.row(), 0).text())
                    self.lineEdit_2.setText(self.parentablak.tableWidget.item(index.row(), 1).text())
                except Exception:
                    pass
            self.lineEdit.setStyleSheet("QLineEdit"
                                                "{"
                                                "background : lightgray;"
                                                "}")
            self.ablak.setWindowTitle("Kiválasztott érték módosítása")
            self.pushButton_mentes.clicked.connect(lambda: self.db.update_nomen_elem(nev, str(self.lineEdit.text()), str(self.lineEdit_2.text()), self))
        else:
            self.pushButton_mentes.clicked.connect(lambda: self.db.insert_nomen_elem(nev, str(self.lineEdit.text()), str(self.lineEdit_2.text()), self))
        self.pushButton_mentes.clicked.connect(lambda: self.ablak.close())
        self.pushButton_megse = QtWidgets.QPushButton(self.frame)
        self.pushButton_megse.setGeometry(QtCore.QRect(350, 170, 91, 41))
        self.pushButton_megse.setDefault(True)
        self.pushButton_megse.clicked.connect(lambda: self.ablak.close())
        self.pushButton_megse.setObjectName("pushButton_megse")
        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(self.ablak)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def retranslateUi(self, Ui_Nomen_Elemek_Ujfelvetel):
        _translate = QtCore.QCoreApplication.translate
        #Ui_Nomen_Elemek_Ujfelvetel.setWindowTitle(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Új felvétele"))
        self.label.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Érték:"))
        self.label_2.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Nyomtatási címke:"))
        self.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Mentés"))
        self.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Mégse"))

class Ui_Nomen_Elemek_Akt(object):
    def setupUi(self, Ui_Nomen_Elemek_Akt, parentAblak, parentDB, valtnev):
        self.ablak=Ui_Nomen_Elemek_Akt
        self.ablak.setObjectName("Ui_Nomen_Elemek_Akt")
        self.ablak.resize(459, 267)
        self.db=parentDB
        self.parentablak=parentAblak
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 411, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 40, 121, 51))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(210, 60, 161, 21))
        self.comboBox.setObjectName("comboBox")
        self.importedFiles=self.listImported()
        for file in self.importedFiles:
            self.comboBox.addItem(file)

        self.pushButton_mentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mentes.setGeometry(QtCore.QRect(230, 170, 91, 41))
        self.pushButton_mentes.setObjectName("pushButton_mentes")
        self.pushButton_mentes.clicked.connect(lambda: self.aktualizal(valtnev))
        self.pushButton_megse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_megse.setGeometry(QtCore.QRect(340, 170, 91, 41))
        self.pushButton_megse.setDefault(True)
        self.pushButton_megse.clicked.connect(lambda: self.ablak.close())
        self.pushButton_megse.setObjectName("pushButton_megse")
        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(self.ablak)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def retranslateUi(self, Ui_Nomen_Elemek_Akt):
        _translate = QtCore.QCoreApplication.translate
        Ui_Nomen_Elemek_Akt.setWindowTitle(_translate("Ui_Nomen_Elemek_Akt", "Adatállomány kiválasztása"))
        self.groupBox.setTitle(_translate("Ui_Nomen_Elemek_Akt", "Input állomány"))
        self.label.setText(_translate("Ui_Nomen_Elemek_Akt", "Rendelkezésre álló adatok:"))
        self.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Akt", "Mentés"))
        self.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Akt", "Mégse"))

    def aktualizal(self, valtnev):
        item=self.comboBox.itemText(self.comboBox.currentIndex())
        previouswd=os.getcwd()
        os.chdir("imported")
        uj_adatbazis=pandas.read_csv(item)
        os.chdir(previouswd)

        self.db.deleteAll(valtnev, self.parentablak)
        sorok = uj_adatbazis.values
        for i in range(self.parentablak.tableWidget.rowCount()):
            self.parentablak.tableWidget.removeRow(0)
            self.parentablak.tableWidget.setRowCount(self.parentablak.tableWidget.rowCount() - 1)
        i = 0
        for sor in sorok:
            self.parentablak.tableWidget.setRowCount(i + 1)
            i += 1
            self.db.insert_nomen_elem(valtnev, sor[0], sor[1], self)
        self.ablak.close()
        return


    def listImported(self):
        previouswd = os.getcwd()
        os.chdir("imported")
        lista=os.listdir()
        os.chdir(previouswd)
        lista=[elem for elem in lista if elem.endswith('.csv')]
        return lista

class Ui_Nomen_Elemek_Kepzes(object):
    def setupUi(self, Ui_Nomen_Elemek_Kepzes,parentablak, bal, jobb):
        self.ablak=Ui_Nomen_Elemek_Kepzes
        self.ablak.setObjectName("Ui_Nomen_Elemek_Kepzes")
        self.ablak.resize(563, 379)
        self.parentablak=parentablak
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 531, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.db=DbConnect()
        self.bal=bal
        self.jobb=jobb

        self.pushButton_csere = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_csere.setGeometry(QtCore.QRect(27, 70, 71, 21))
        self.pushButton_csere.setObjectName("pushButton_csere")

        self.label_bal = QtWidgets.QLabel(self.groupBox)
        self.label_bal.setGeometry(QtCore.QRect(261, 40, 121, 31))
        self.label_bal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_bal.setWordWrap(False)
        self.label_bal.setObjectName("label")
        self.label_jobb = QtWidgets.QLabel(self.groupBox)
        self.label_jobb.setGeometry(QtCore.QRect(261, 80, 121, 31))
        self.label_jobb.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_jobb.setWordWrap(False)
        self.label_jobb.setObjectName("label")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        # self.comboBox = QtWidgets.QComboBox(self.groupBox)
        # self.comboBox.setGeometry(QtCore.QRect(150, 50, 161, 21))
        # self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 121, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 125, 121, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 141, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        # self.lineEdit_lekerdezes = QtWidgets.QLineEdit(self.groupBox)
        # self.lineEdit_lekerdezes.setGeometry(QtCore.QRect(150, 80, 361, 31))
        # self.lineEdit_lekerdezes.setText("")
        # self.lineEdit_lekerdezes.setObjectName("lineEdit_lekerdezes")
        self.lineEdit_nev = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_nev.setGeometry(QtCore.QRect(190, 130, 191, 21))
        self.lineEdit_nev.setText("")
        self.lineEdit_nev.setObjectName("lineEdit_nev")
        self.lineEdit_ertek = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ertek.setGeometry(QtCore.QRect(190, 160, 191, 21))
        self.lineEdit_ertek.setText("")
        self.lineEdit_ertek.setObjectName("lineEdit_ertek")
        self.pushButton_mentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mentes.setGeometry(QtCore.QRect(350, 290, 91, 41))
        self.pushButton_mentes.setObjectName("pushButton_mentes")
        self.pushButton_mentes.clicked.connect(lambda: self.db.nomen_kepzes(self.ablak,self.parentablak,self.lineEdit_nev.text(), self.lineEdit_ertek.text(),self.bal, self.jobb))
        self.pushButton_megse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_megse.setGeometry(QtCore.QRect(460, 290, 91, 41))
        self.pushButton_megse.setDefault(True)
        self.pushButton_megse.clicked.connect(lambda: self.ablak.close())
        # self.pushButton_mentes.clicked.connect(lambda: self.ablak.close())
        self.pushButton_megse.setObjectName("pushButton_megse")

        self.pushButton_csere.clicked.connect(lambda:self.csere())

        self.ablak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.ablak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        self.ablak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.ablak)
        self.statusbar.setObjectName("statusbar")
        self.ablak.setStatusBar(self.statusbar)

        self.retranslateUi(self.ablak)
        QtCore.QMetaObject.connectSlotsByName(self.ablak)

    def csere(self):
        self.jobb, self.bal = self.bal, self.jobb
        self.retranslateUi(self.ablak)

    def retranslateUi(self, Ui_Nomen_Elemek_Kepzes):
        _translate = QtCore.QCoreApplication.translate
        Ui_Nomen_Elemek_Kepzes.setWindowTitle(_translate("Ui_Nomen_Elemek_Kepzes", "Nómenklatúra képzési szabályok"))
        self.groupBox.setTitle(_translate("Ui_Nomen_Elemek_Kepzes", "Paraméterek"))
        self.label.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Elsődleges:"))
        self.label_2.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Másodlagos:"))
        self.label_3.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Változónév:"))
        self.label_4.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Nyomtatási címke:"))
        self.label_bal.setText(_translate("Ui_Nomen_Elemek_Kepzes", self.bal))
        self.label_jobb.setText(_translate("Ui_Nomen_Elemek_Kepzes", self.jobb))
        self.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Mentés"))
        self.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Mégse"))
        self.pushButton_csere.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Csere"))

def addNewRow(ablak,lista):#tábla frissítése a beszúrás után
    pozicio=ablak.tableWidget.rowCount()
    i=0
    ablak.tableWidget.insertRow(pozicio)
    for elem in lista:
        ablak.tableWidget.setItem(pozicio,i, QTableWidgetItem(elem))
        i+=1
    ablak.tableWidget.setRowCount(pozicio+1)

def deleteRows(ablak):
    indexes = ablak.tableWidget.selectionModel().selectedRows()
    i=0
    for index in sorted(indexes):
        ablak.tableWidget.removeRow(index.row() - i)
        i+=1

def updateRow(ablak, cimke):
    indexes = ablak.tableWidget.selectionModel().selectedRows()
    for index in indexes:
        ablak.tableWidget.setItem(index.row(),1,QTableWidgetItem(cimke))



class DbConnect(object):
    def __init__(self):
        pass

    def nomen_kepzes(self,ablak,parentablak,nev, cimke, bal, jobb):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        results = c.execute('select * from nomenklaturak where nev = "' + nev + '";')
        if any(results):
            result = QtWidgets.QMessageBox.question(ablak,
                                                    "Ez a nomenklatúra már létezik",
                                                    "Kérlek adj meg egy új értéket!",
                                                    QtWidgets.QMessageBox.Ok)
            return
        c.execute('insert into nomenklaturak (nev, cimke, leiras, hossz, tipus,  kepzett_e, elsodleges_kepzett_nev, masodlagos_kepzett_nev, utolso_modositas, kezdoidopont, vegidopont) '
                  'values(?,?,?,?,?,?,?,?,?,?,?);',(nev,cimke,"","","Szöveg",1,bal,jobb,str(date.today()),str(date.today()),str(date.today())))
        if parentablak is not None:
            addNewRow(parentablak, [nev, cimke,"","","Szöveg","Igen",str(date.today()),str(date.today()),str(date.today())])
        ablak.close()
        conn.commit()
        conn.close()

    def insert_nomen_elem(self, valtnev, ertek, cimke, ablak=None):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        results=c.execute('select * from nomenklatura_elemek where ertek = "'+ertek+'" and nev="'+valtnev+'";')
        if any(results):
            result = QtWidgets.QMessageBox.question(ablak.ablak,
                                                    "Ez az elem már létezik",
                                                    "Kérlek adj meg egy új értéket!",
                                                    QtWidgets.QMessageBox.Ok)
            return
        c.execute('insert into nomenklatura_elemek values("'+valtnev+'", "'+ertek+'", "'+cimke+'");')
        if ablak is not None:
            addNewRow(ablak.parentablak,[ertek, cimke])
        conn.commit()
        conn.close()

    def update_nomen_elem(self, valtnev, ertek, cimke, ablak=None):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        results = c.execute('select * from nomenklatura_elemek where ertek = "' + ertek + '";')
        if not any(results):
            result = QtWidgets.QMessageBox.question(ablak.ablak,
                                                    "Adatbázis hiba",
                                                    "Nem található a kért elem",
                                                    QtWidgets.QMessageBox.Ok)
            return
        c.execute('update nomenklatura_elemek set cimke="'+cimke+'" where (ertek="'+ertek+'" and nev="'+valtnev+'");')
        updateRow(ablak.parentablak, cimke)
        conn.commit()
        conn.close()

    def list_nomen_elemek(self,nev):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        sorok=c.execute('select * from nomenklatura_elemek where nev="'+nev+'";')
        lista=[]
        for sor in sorok:
            lista.append(sor)
        conn.commit()
        conn.close()
        return lista

    def delete_nomen_elem(self, ablak):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        indexes = ablak.tableWidget.selectionModel().selectedRows()
        for index in indexes:
            try:
                valtnev=ablak.tableWidget.item(index.row(),0).text()
                c.execute('delete from nomenklatura_elemek where ertek="'+valtnev+'";')
            except Exception:
                pass
        deleteRows(ablak)
        conn.commit()
        conn.close()

    def deleteAll(self, valtnev, ablak):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        c.execute('delete from nomenklatura_elemek where nev="'+valtnev+'";')
        conn.commit()
        conn.close()

    def getKepzettE(self, nev) -> bool:
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        sorok=c.execute('select kepzett_e from nomenklaturak where nev="' + nev + '";')
        for sor in sorok:
            a=bool(sor[0])
        conn.commit()
        conn.close()
        return a
