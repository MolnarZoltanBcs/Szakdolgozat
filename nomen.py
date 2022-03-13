import os
import sys
from datetime import date
import pandas
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *
from mutatok import Ui_Mutatok_UJ, Ui_Mutatok


class Ui_Nomenklatura(QtWidgets.QMainWindow):
    def setupUi(x,  Ui_Nomenklatura):
         x.ablak=Ui_Nomenklatura
         x.ui=Ui_Mutatok()
         x.db=DbConnect()
         x.ui.setupUi(x.ablak, nomen=True)
         x.ui.ablak.setWindowTitle("Nomenklaturák kezelése")
         x.ui.pushButton_elemek = QtWidgets.QPushButton(x.ui.ablak)
         x.ui.pushButton_elemek.setGeometry(QtCore.QRect(302, 26, 130, 23))
         x.ui.pushButton_elemek.setObjectName("pushButton_elemek") #nomeklatura elemek
         x.ui.pushButton_elemek.setText("Nomenklatúra Elemek") #nomeklatura elemek
         x.ui.pushButton_kepzes = QtWidgets.QPushButton(x.ui.ablak)
         x.ui.pushButton_kepzes.setGeometry(QtCore.QRect(462, 26, 91, 23))
         x.ui.pushButton_kepzes.setObjectName("pushButton_kepzes")  # kepzes
         x.ui.pushButton_kepzes.setText("Képzés")  # kepzes
         x.ui.pushButton_torol.setGeometry(QtCore.QRect(583, 26, 91, 23))
         x.ui.pushButton_export.setGeometry(QtCore.QRect(704, 26, 110, 23))
         x.ui.radioButton_export_csv.setGeometry(QtCore.QRect(845, 26, 110, 23))
         x.ui.radioButton_export_excel.setGeometry(QtCore.QRect(895, 26, 110, 23))



         #
         # x.valtoztatUi(x.ui.ablak)
         # QtCore.QMetaObject.connectSlotsByName(x.ui.ablak)

         #ez fogja megnyitni az nomenklatura elemek ablakot ablakot
         x.ui.pushButton_elemek.clicked.connect(x.open_Nomen_Elemek)
         #
         #     #ez nyitja meg a kepzest
         x.ui.pushButton_kepzes.clicked.connect(lambda: x.open_Nomen_Elemek_Kepzes(x.ui))
         #
         # x.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
         # x.ui.tableWidget.selectionModel().selectionChanged.connect(lambda: x.on_selection_changed())
         # x.on_selection_changed()
                  
        
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

    def valtoztatUi(x, Ui_Nomenklatura):
         _translate = QtCore.QCoreApplication.translate
         Ui_Nomenklatura.setWindowTitle(_translate("Ui_Nomenklatura", "Nómenklatúrák kezelése"))
         
         cimkek = ["Változó neve", "Nyomtatási cimke", "Leírás", "Hossz", "Típus", "Utolsó módosítás", "Érvényesség kezdete", "Érvényesség vége"]
         i=0
         for elem in cimkek:
            item = x.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Ui_Nomenklatura", elem))
            i+=1
         
         
         __sortingEnabled = x.tableWidget.isSortingEnabled()
         x.tableWidget.setSortingEnabled(False)
 
         x.tableWidget.setSortingEnabled(__sortingEnabled)
         x.pushButton_uj.setText(_translate("Ui_Nomenklatura", "Új létrehozása"))
         x.pushButton_modosit.setText(_translate("Ui_Nomenklatura", "Módosítás"))
         x.pushButton_torol.setText(_translate("Ui_Nomenklatura", "Törlés"))
         x.pushButton_export.setText(_translate("Ui_Nomenklatura", "Kijelöltek exportja"))
         x.pushButton_elemek.setText(_translate("Ui_Nomenklatura", "Nómenklatúra Elemek"))
         x.pushButton_kepzes.setText(_translate("Ui_Nomenklatura", "Képzés"))

    #definialjuk az uj mutato letrehozasa ablakot
    #ez nyitja meg
    def openUjNomeklatura(x):
         x.window = QtWidgets.QMainWindow()
         x.ui2 =  Ui_Mutatok_UJ()
         x.ui2.setupUi(x.window, x.ablak, nomen=True) #az ablak a parentje az új windownak
         x.ui2.comboBox.addItem("Karakteres")
         x.ui2.csoportLabel.deleteLater()
         x.ui2.lineEdit_csoport.deleteLater()
         x.ui2.ervenyessegVegeLabel.setGeometry(QtCore.QRect(40, 200, 161, 51))
         x.ui2.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 210, 201, 31))
         x.ui2.ervenyessegVegeLabel.setGeometry(QtCore.QRect(40, 250, 161, 31))
         x.ui2.dateEdit_veg.setGeometry(QtCore.QRect(220, 250, 151, 31))
         x.window.show()
    #es definialjuk a modosit mutato ablakot
    def openModositNomenklatura(x):
         x.window = QtWidgets.QMainWindow()
         x.ui_uj_nomen =  Ui_Mutatok_UJ()
         x.ui_uj_nomen.setupModositUi(x.window, x.ablak)
         x.window.setWindowTitle("Kiválasztott nómenklatúra módosítása")
         x.ui_uj_nomen.comboBox.addItem("Karakteres")
         # x.ui.label_6.deleteLater()
         x.ui_uj_nomen.lineEdit_csoport.deleteLater()
         # x.ui.label_7.setGeometry(QtCore.QRect(40, 200, 161, 51))
         x.ui_uj_nomen.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 210, 201, 31))
         # x.ui.label_8.setGeometry(QtCore.QRect(40, 250, 161, 31))
         x.ui_uj_nomen.dateEdit_veg.setGeometry(QtCore.QRect(220, 250, 151, 31))
         
         x.window.show()
         
    # itt definialjuk a nomen_elemek megnyitasa ablakot     
    def open_Nomen_Elemek(x):

         indexes = x.ui.tableWidget.selectionModel().selectedRows()
         x.ui.tableWidget.clearSelection()
         # x.ui.tableWidget.selectionModel()
         if len(indexes) != 1:
             result = QtWidgets.QMessageBox.question(x,
                                                     "Hibás kijelölés",
                                                     "Egyszerre csak egy sor elemeit tekintheted meg, kérlek pontosan egy sort jelölj ki!",
                                                     QtWidgets.QMessageBox.Ok)
             return
         for elem in sorted(indexes):
             kepzett = x.db.getKepzettE(x.ui.tableWidget.item(elem.row(),0).text())
             if kepzett:
                 result = QtWidgets.QMessageBox.question(x,
                                                         "Hibás kijelölés",
                                                         "A kijelölt elem egy képzett nomenklatúra, tehát nincsenek elemei. Kérlek válassz újra!",
                                                         QtWidgets.QMessageBox.Ok)
                 return
         for elem in sorted(indexes):
             nev=x.ui.tableWidget.item(elem.row(),0).text()
         x.window = QtWidgets.QMainWindow()
         x.ui_uj =  Ui_Nomen_Elemek()
         x.ui_uj.setupUi(x.window, nev)
         x.window.show()
    
    def open_Nomen_Elemek_Kepzes(x, ablak):
        indexes = ablak.tableWidget.selectionModel().selectedRows()
        ablak.tableWidget.selectionModel().clearSelection()
        lista = []
        for index in indexes:
            lista.append(ablak.tableWidget.item(index.row(), 0).text())
        if len(lista)<2:
            result = QtWidgets.QMessageBox.question(x,
                                                    "Hibás kijelölés",
                                                    "Kérlek kettő nomenklatúrát jelölj ki a képzéshez!",
                                                    QtWidgets.QMessageBox.Ok)
            return
        x.window = QtWidgets.QMainWindow()
        x.ui_uj_kepzes =  Ui_Nomen_Elemek_Kepzes()
        x.ui_uj_kepzes.setupUi(x.window,x.ui, lista[0], lista[1])
        x.window.show()
    




class Ui_Nomen_Elemek(object):
    def setupUi(x, Ui_Nomen_Elemek, nev):
        x.ablak=Ui_Nomen_Elemek
        x.nev=nev
        x.db=DbConnect()
        x.ablak.setObjectName("Ui_Nomen_Elemek")
        x.ablak.resize(786, 516)
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(10, 0, 771, 491))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.pushButton_uj = QtWidgets.QPushButton(x.frame)
        x.pushButton_uj.setGeometry(QtCore.QRect(10, 20, 121, 41))
        x.pushButton_uj.setAutoFillBackground(False)
        x.pushButton_uj.setObjectName("pushButton_uj")
        x.pushButton_modosit = QtWidgets.QPushButton(x.frame)
        x.pushButton_modosit.setGeometry(QtCore.QRect(160, 20, 121, 41))
        x.pushButton_modosit.setObjectName("pushButton_modosit")
        x.pushButton_aktualizal = QtWidgets.QPushButton(x.frame)
        x.pushButton_aktualizal.setGeometry(QtCore.QRect(310, 20, 171, 41))
        x.pushButton_aktualizal.setObjectName("pushButton_aktualizal")
        x.pushButton_torol = QtWidgets.QPushButton(x.frame)
        x.pushButton_torol.setGeometry(QtCore.QRect(510, 20, 121, 41))
        x.pushButton_torol.setObjectName("pushButton_torol")
        # x.pushButton_frissit = QtWidgets.QPushButton(x.frame)
        # x.pushButton_frissit.setGeometry(QtCore.QRect(640, 20, 121, 41))
        # x.pushButton_frissit.setObjectName("pushButton_frissit")
        x.tableWidget = QtWidgets.QTableWidget(x.frame)
        x.tableWidget.setGeometry(QtCore.QRect(50, 100, 650, 311))
        x.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        x.tableWidget.setDragEnabled(False)
        x.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        x.tableWidget.setAlternatingRowColors(True)
        x.tableWidget.setRowCount(1)
        x.tableWidget.setColumnCount(2)
        sorok=x.db.list_nomen_elemek(nev)
        i=0
        for sor in sorok:
            x.tableWidget.setRowCount(i+1)
            x.tableWidget.setItem(i, 0, QTableWidgetItem(sor[1]))
            x.tableWidget.setItem(i, 1, QTableWidgetItem(sor[2]))
            i+=1

        x.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        x.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        x.tableWidget.setHorizontalHeaderItem(1, item)
        x.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        x.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        x.tableWidget.horizontalHeader().setHighlightSections(True)
        x.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        x.tableWidget.horizontalHeader().setStretchLastSection(True)
        x.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        x.tableWidget.verticalHeader().setSortIndicatorShown(False)
        x.tableWidget.verticalHeader().setStretchLastSection(False)

        x.nevButton = QLabel(x.frame)
        x.nevButton.setGeometry(QtCore.QRect(20, 450, 121, 41))
        x.nevButton.setAutoFillBackground(False)
        x.nevButton.setObjectName("pushButton_uj")

        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 786, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(x.nev)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)
        
        #ez nyitja meg az uj elemek ablakot
        x.pushButton_uj.clicked.connect(lambda: x.open_Nomen_Elemek_Uj(nev))
         
        #ez nyitja meg a modosit elemek ablakot
        x.pushButton_modosit.clicked.connect(lambda: x.open_Nomen_Elemek_Modosit(nev))
        
        #ez nyitja meg az aktualizal ablakot
        x.pushButton_aktualizal.clicked.connect(x.open_Nomen_Elemek_Akt)

        x.pushButton_torol.clicked.connect(lambda: x.db.delete_nomen_elem(x))
        
    def labelSetUp(x, label, kezdopont_x, kezdopont_y, hossz_x, hossz_y, nev):
        label.setGeometry(QtCore.QRect(kezdopont_x, kezdopont_y, hossz_x, hossz_y))
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        label.setObjectName(nev)

    def retranslateUi(x, nev):
        _translate = QtCore.QCoreApplication.translate
        x.ablak.setWindowTitle(_translate("Ui_Nomen_Elemek", "Nómenklatúra elemek - "+nev))
        x.pushButton_uj.setText(_translate("Ui_Nomen_Elemek", "Új létrehozása"))
        x.pushButton_modosit.setText(_translate("Ui_Nomen_Elemek", "Módosítás"))
        x.pushButton_aktualizal.setText(_translate("Ui_Nomen_Elemek", "Értékek aktualizálása"))
        x.pushButton_torol.setText(_translate("Ui_Nomen_Elemek", "Törlés"))
        # x.pushButton_frissit.setText(_translate("Ui_Nomen_Elemek", "Frissítés"))
        x.nevButton.setText(_translate(x.nevButton.objectName(), nev))
        item = x.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Nomen_Elemek", "Érték"))
        item = x.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Nomen_Elemek", "Nyomtatási címke"))

    def open_Nomen_Elemek_Uj(x, nev):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Ujfelvetel()
         x.window.setWindowTitle("Új nómenklatúra elem felvétele")
         x.ui.setupUi(x.window, nev, parentablak=x)
         x.window.show()
         
    def open_Nomen_Elemek_Modosit(x, nev):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Ujfelvetel()
         x.window.setWindowTitle("Nómenklatúra elem módosítása")
         x.ui.setupUi(x.window, nev, parentablak=x, modosit=True)
         x.window.show()
    
    def open_Nomen_Elemek_Akt(x):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Akt()
         x.ui.setupUi(x.window, x, x.db, x.nev)
         x.window.show()
         
   


class Ui_Nomen_Elemek_Ujfelvetel(object):
    def setupUi(x, Ui_Nomen_Elemek_Ujfelvetel, nev, parentablak=None, modosit=False):
        x.ablak =  Ui_Nomen_Elemek_Ujfelvetel
        x.ablak.setObjectName("Ui_Nomen_Elemek_Ujfelvetel")
        x.ablak.resize(459, 267)
        x.parentablak=parentablak
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.frame = QtWidgets.QFrame(x.centralwidget)
        x.frame.setGeometry(QtCore.QRect(0, 0, 451, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.frame.setFont(font)
        x.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        x.frame.setObjectName("frame")
        x.label = QtWidgets.QLabel(x.frame)
        x.label.setGeometry(QtCore.QRect(70, 60, 81, 21))
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setObjectName("label")
        x.label_2 = QtWidgets.QLabel(x.frame)
        x.label_2.setGeometry(QtCore.QRect(10, 100, 141, 21))
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setObjectName("label_2")
        x.lineEdit = QtWidgets.QLineEdit(x.frame)
        x.lineEdit.setGeometry(QtCore.QRect(160, 60, 191, 21))
        x.lineEdit.setText("")
        x.lineEdit.setObjectName("lineEdit")
        x.lineEdit_2 = QtWidgets.QLineEdit(x.frame)
        x.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 191, 21))
        x.lineEdit_2.setText("")
        x.lineEdit_2.setObjectName("lineEdit_2")
        x.db=DbConnect()
        x.pushButton_mentes = QtWidgets.QPushButton(x.frame)
        x.pushButton_mentes.setGeometry(QtCore.QRect(240, 170, 91, 41))
        x.pushButton_mentes.setObjectName("pushButton_mentes")
        if modosit:
            x.lineEdit.setReadOnly(True)
            indexes=x.parentablak.tableWidget.selectionModel().selectedRows()
            for index in sorted(indexes):
                x.lineEdit.setText(x.parentablak.tableWidget.item(index.row(), 0).text())
                x.lineEdit_2.setText(x.parentablak.tableWidget.item(index.row(), 1).text())
            x.lineEdit.setStyleSheet("QLineEdit"
                                                "{"
                                                "background : lightgray;"
                                                "}")
            x.ablak.setWindowTitle("Kiválasztott érték módosítása")
            x.pushButton_mentes.clicked.connect(lambda: x.db.update_nomen_elem(nev, str(x.lineEdit.text()), str(x.lineEdit_2.text()), x))
        else:
            x.pushButton_mentes.clicked.connect(lambda: x.db.insert_nomen_elem(nev, str(x.lineEdit.text()), str(x.lineEdit_2.text()), x))
        x.pushButton_mentes.clicked.connect(lambda: x.ablak.close())
        x.pushButton_megse = QtWidgets.QPushButton(x.frame)
        x.pushButton_megse.setGeometry(QtCore.QRect(350, 170, 91, 41))
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: x.ablak.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(x.ablak)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def retranslateUi(x, Ui_Nomen_Elemek_Ujfelvetel):
        _translate = QtCore.QCoreApplication.translate
        #Ui_Nomen_Elemek_Ujfelvetel.setWindowTitle(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Új felvétele"))
        x.label.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Érték:"))
        x.label_2.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Nyomtatási címke:"))
        x.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Ujfelvetel", "Mégse"))

class Ui_Nomen_Elemek_Akt(object):
    def setupUi(x, Ui_Nomen_Elemek_Akt, parentAblak, parentDB, valtnev):
        x.ablak=Ui_Nomen_Elemek_Akt
        x.ablak.setObjectName("Ui_Nomen_Elemek_Akt")
        x.ablak.resize(459, 267)
        x.db=parentDB
        x.parentablak=parentAblak
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.groupBox = QtWidgets.QGroupBox(x.centralwidget)
        x.groupBox.setGeometry(QtCore.QRect(20, 10, 411, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.groupBox.setFont(font)
        x.groupBox.setObjectName("groupBox")
        x.label = QtWidgets.QLabel(x.groupBox)
        x.label.setGeometry(QtCore.QRect(70, 40, 121, 51))
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setWordWrap(True)
        x.label.setObjectName("label")
        x.comboBox = QtWidgets.QComboBox(x.groupBox)
        x.comboBox.setGeometry(QtCore.QRect(210, 60, 161, 21))
        x.comboBox.setObjectName("comboBox")
        x.importedFiles=x.listImported()
        for file in x.importedFiles:
            x.comboBox.addItem(file)

        x.pushButton_mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_mentes.setGeometry(QtCore.QRect(230, 170, 91, 41))
        x.pushButton_mentes.setObjectName("pushButton_mentes")
        x.pushButton_mentes.clicked.connect(lambda: x.aktualizal(valtnev))
        x.pushButton_megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_megse.setGeometry(QtCore.QRect(340, 170, 91, 41))
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: x.ablak.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(x.ablak)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def retranslateUi(x, Ui_Nomen_Elemek_Akt):
        _translate = QtCore.QCoreApplication.translate
        Ui_Nomen_Elemek_Akt.setWindowTitle(_translate("Ui_Nomen_Elemek_Akt", "Adatállomány kiválasztása"))
        x.groupBox.setTitle(_translate("Ui_Nomen_Elemek_Akt", "Input állomány"))
        x.label.setText(_translate("Ui_Nomen_Elemek_Akt", "Rendelkezésre álló adatok:"))
        x.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Akt", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Akt", "Mégse"))

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
    def setupUi(x, Ui_Nomen_Elemek_Kepzes,parentablak, bal, jobb):
        x.ablak=Ui_Nomen_Elemek_Kepzes
        x.ablak.setObjectName("Ui_Nomen_Elemek_Kepzes")
        x.ablak.resize(563, 379)
        x.parentablak=parentablak
        x.centralwidget = QtWidgets.QWidget(x.ablak)
        x.centralwidget.setObjectName("centralwidget")
        x.groupBox = QtWidgets.QGroupBox(x.centralwidget)
        x.groupBox.setGeometry(QtCore.QRect(20, 10, 531, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.groupBox.setFont(font)
        x.groupBox.setObjectName("groupBox")

        x.db=DbConnect()
        x.bal=bal
        x.jobb=jobb

        x.pushButton_csere = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_csere.setGeometry(QtCore.QRect(27, 70, 71, 21))
        x.pushButton_csere.setObjectName("pushButton_csere")

        x.label_bal = QtWidgets.QLabel(x.groupBox)
        x.label_bal.setGeometry(QtCore.QRect(261, 40, 121, 31))
        x.label_bal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        x.label_bal.setWordWrap(False)
        x.label_bal.setObjectName("label")
        x.label_jobb = QtWidgets.QLabel(x.groupBox)
        x.label_jobb.setGeometry(QtCore.QRect(261, 80, 121, 31))
        x.label_jobb.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        x.label_jobb.setWordWrap(False)
        x.label_jobb.setObjectName("label")
        x.label = QtWidgets.QLabel(x.groupBox)
        x.label.setGeometry(QtCore.QRect(40, 40, 121, 31))
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setWordWrap(False)
        x.label.setObjectName("label")
        # x.comboBox = QtWidgets.QComboBox(x.groupBox)
        # x.comboBox.setGeometry(QtCore.QRect(150, 50, 161, 21))
        # x.comboBox.setObjectName("comboBox")
        x.label_2 = QtWidgets.QLabel(x.groupBox)
        x.label_2.setGeometry(QtCore.QRect(40, 80, 121, 31))
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setWordWrap(False)
        x.label_2.setObjectName("label_2")
        x.label_3 = QtWidgets.QLabel(x.groupBox)
        x.label_3.setGeometry(QtCore.QRect(40, 125, 121, 31))
        x.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_3.setWordWrap(False)
        x.label_3.setObjectName("label_3")
        x.label_4 = QtWidgets.QLabel(x.groupBox)
        x.label_4.setGeometry(QtCore.QRect(20, 160, 141, 21))
        x.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_4.setObjectName("label_4")
        # x.lineEdit_lekerdezes = QtWidgets.QLineEdit(x.groupBox)
        # x.lineEdit_lekerdezes.setGeometry(QtCore.QRect(150, 80, 361, 31))
        # x.lineEdit_lekerdezes.setText("")
        # x.lineEdit_lekerdezes.setObjectName("lineEdit_lekerdezes")
        x.lineEdit_nev = QtWidgets.QLineEdit(x.groupBox)
        x.lineEdit_nev.setGeometry(QtCore.QRect(190, 130, 191, 21))
        x.lineEdit_nev.setText("")
        x.lineEdit_nev.setObjectName("lineEdit_nev")
        x.lineEdit_ertek = QtWidgets.QLineEdit(x.groupBox)
        x.lineEdit_ertek.setGeometry(QtCore.QRect(190, 160, 191, 21))
        x.lineEdit_ertek.setText("")
        x.lineEdit_ertek.setObjectName("lineEdit_ertek")
        x.pushButton_mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_mentes.setGeometry(QtCore.QRect(350, 290, 91, 41))
        x.pushButton_mentes.setObjectName("pushButton_mentes")
        x.pushButton_mentes.clicked.connect(lambda: x.db.nomen_kepzes(x.ablak,x.parentablak,x.lineEdit_nev.text(), x.lineEdit_ertek.text(),x.bal, x.jobb))
        x.pushButton_megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_megse.setGeometry(QtCore.QRect(460, 290, 91, 41))
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: x.ablak.close())
        # x.pushButton_mentes.clicked.connect(lambda: x.ablak.close())
        x.pushButton_megse.setObjectName("pushButton_megse")

        x.pushButton_csere.clicked.connect(lambda:x.csere())

        x.ablak.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(x.ablak)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        x.menubar.setObjectName("menubar")
        x.ablak.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(x.ablak)
        x.statusbar.setObjectName("statusbar")
        x.ablak.setStatusBar(x.statusbar)

        x.retranslateUi(x.ablak)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)

    def csere(self):
        self.jobb, self.bal = self.bal, self.jobb
        self.retranslateUi(self.ablak)

    def retranslateUi(x, Ui_Nomen_Elemek_Kepzes):
        _translate = QtCore.QCoreApplication.translate
        Ui_Nomen_Elemek_Kepzes.setWindowTitle(_translate("Ui_Nomen_Elemek_Kepzes", "Nómenklatúra képzési szabályok"))
        x.groupBox.setTitle(_translate("Ui_Nomen_Elemek_Kepzes", "Paraméterek"))
        x.label.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Baloldal:"))
        x.label_2.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Jobboldal:"))
        x.label_3.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Változónév:"))
        x.label_4.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Nyomtatási címke:"))
        x.label_bal.setText(_translate("Ui_Nomen_Elemek_Kepzes", x.bal))
        x.label_jobb.setText(_translate("Ui_Nomen_Elemek_Kepzes", x.jobb))
        x.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Mégse"))
        x.pushButton_csere.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Csere"))

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
        c.execute('insert into nomenklaturak (nev, cimke, leiras, hossz, tipus, csoport, kepzett_e, bal_kepzett_nev, jobb_kepzett_nev, utolso_modositas, kezdoidopont, vegidopont) '
                  'values(?,?,?,?,?,?,?,?,?,?,?,?);',(nev,cimke,"","","Szöveg","",1,bal,jobb,str(date.today()),str(date.today()),str(date.today())))
        if parentablak is not None:
            addNewRow(parentablak, [nev, cimke,"","","Szöveg","","Igen",str(date.today()),str(date.today()),str(date.today())])
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
            valtnev=ablak.tableWidget.item(index.row(),0).text()
            c.execute('delete from nomenklatura_elemek where ertek="'+valtnev+'";')
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
