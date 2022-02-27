import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *
from mutatok import Ui_Mutatok_UJ, Ui_Mutatok


class Ui_Nomenklatura(QtWidgets.QMainWindow):
    def setupUi(x,  Ui_Nomenklatura):
         x.ablak=Ui_Nomenklatura
         x.ui=Ui_Mutatok()
         x.ui.setupUi(x.ablak, nomen=True)
         x.ui.ablak.setWindowTitle("Nomenklaturák kezelése")
         x.ui.pushButton_elemek = QtWidgets.QPushButton(x.ui.ablak)
         x.ui.pushButton_elemek.setGeometry(QtCore.QRect(302, 26, 130, 23))
         x.ui.pushButton_elemek.setObjectName("pushButton_elemek") #nomeklatura elemek
         x.ui.pushButton_elemek.setText("Nómenklatúra Elemek") #nomeklatura elemek
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
         x.ui.pushButton_kepzes.clicked.connect(x.open_Nomen_Elemek_Kepzes)
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
         x.ui =  Ui_Mutatok_UJ()
         x.ui.setupUi(x.window, x.ablak, nomen=True) #az ablak a parentje az új windownak
         x.ui.comboBox.addItem("Karakteres")
         x.ui.csoportLabel.deleteLater()
         x.ui.lineEdit_csoport.deleteLater()
         x.ui.ervenyessegVegeLabel.setGeometry(QtCore.QRect(40, 200, 161, 51))
         x.ui.dateEdit_kezdet.setGeometry(QtCore.QRect(220, 210, 201, 31))
         x.ui.ervenyessegVegeLabel.setGeometry(QtCore.QRect(40, 250, 161, 31))
         x.ui.dateEdit_veg.setGeometry(QtCore.QRect(220, 250, 151, 31))
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
             nev=x.ui.tableWidget.item(elem.row(),0).text()
         x.window = QtWidgets.QMainWindow()
         x.ui_uj =  Ui_Nomen_Elemek()
         x.ui_uj.setupUi(x.window, nev)
         x.window.show()
    
    def open_Nomen_Elemek_Kepzes(x):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Kepzes()
         x.ui.setupUi(x.window)
         x.window.show()
    




class Ui_Nomen_Elemek(object):
    def setupUi(x, Ui_Nomen_Elemek, nev):
        x.ablak=Ui_Nomen_Elemek
        x.nev=nev
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
        x.pushButton_aktualizal.setGeometry(QtCore.QRect(310, 20, 151, 41))
        x.pushButton_aktualizal.setObjectName("pushButton_aktualizal")
        x.pushButton_torol = QtWidgets.QPushButton(x.frame)
        x.pushButton_torol.setGeometry(QtCore.QRect(490, 20, 121, 41))
        x.pushButton_torol.setObjectName("pushButton_torol")
        x.pushButton_frissit = QtWidgets.QPushButton(x.frame)
        x.pushButton_frissit.setGeometry(QtCore.QRect(640, 20, 121, 41))
        x.pushButton_frissit.setObjectName("pushButton_frissit")
        x.tableWidget = QtWidgets.QTableWidget(x.frame)
        x.tableWidget.setGeometry(QtCore.QRect(50, 100, 650, 311))
        x.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        x.tableWidget.setDragEnabled(False)
        x.tableWidget.setAlternatingRowColors(True)
        x.tableWidget.setRowCount(9)
        x.tableWidget.setColumnCount(2)
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

        x.retranslateUi(nev)
        QtCore.QMetaObject.connectSlotsByName(x.ablak)
        
        #ez nyitja meg az uj elemek ablakot
        x.pushButton_uj.clicked.connect(lambda: x.open_Nomen_Elemek_Uj(nev))
         
        #ez nyitja meg a modosit elemek ablakot
        x.pushButton_modosit.clicked.connect(x.open_Nomen_Elemek_Modosit)
        
        #ez nyitja meg az aktualizal ablakot
        x.pushButton_aktualizal.clicked.connect(x.open_Nomen_Elemek_Akt)
        
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
        x.pushButton_frissit.setText(_translate("Ui_Nomen_Elemek", "Frissítés"))
        x.nevButton.setText(_translate(x.nevButton.objectName(), nev))
        item = x.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Ui_Nomen_Elemek", "Pozíció"))
        item = x.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Ui_Nomen_Elemek", "Név"))

    def open_Nomen_Elemek_Uj(x, nev):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Ujfelvetel()
         x.window.setWindowTitle("Új nómenklatúra elem felvétele")
         x.ui.setupUi(x.window, nev)
         x.window.show()
         
    def open_Nomen_Elemek_Modosit(x, nev):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Ujfelvetel()
         x.window.setWindowTitle("Nómenklatúra elem módosítása")
         x.ui.setupUi(x.window, nev, modosit=True)
         x.window.show()
    
    def open_Nomen_Elemek_Akt(x):
         x.window = QtWidgets.QMainWindow()
         x.ui =  Ui_Nomen_Elemek_Akt()
         x.ui.setupUi(x.window)
         x.window.show()
         
   


class Ui_Nomen_Elemek_Ujfelvetel(object):
    def setupUi(x, Ui_Nomen_Elemek_Ujfelvetel, nev, modosit=False):
        x.ablak =  Ui_Nomen_Elemek_Ujfelvetel
        x.ablak.setObjectName("Ui_Nomen_Elemek_Ujfelvetel")
        x.ablak.resize(459, 267)
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
        x.pushButton_mentes.clicked.connect(lambda: x.db.insert_nomen_elem(nev, str(x.lineEdit.text()), str(x.lineEdit_2.text())))
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
    def setupUi(x, Ui_Nomen_Elemek_Akt):
        Ui_Nomen_Elemek_Akt.setObjectName("Ui_Nomen_Elemek_Akt")
        Ui_Nomen_Elemek_Akt.resize(459, 267)
        x.centralwidget = QtWidgets.QWidget(Ui_Nomen_Elemek_Akt)
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
        x.pushButton_mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_mentes.setGeometry(QtCore.QRect(230, 170, 91, 41))
        x.pushButton_mentes.setObjectName("pushButton_mentes")
        x.pushButton_megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_megse.setGeometry(QtCore.QRect(340, 170, 91, 41))
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: Ui_Nomen_Elemek_Akt.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        Ui_Nomen_Elemek_Akt.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Nomen_Elemek_Akt)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 459, 21))
        x.menubar.setObjectName("menubar")
        Ui_Nomen_Elemek_Akt.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Nomen_Elemek_Akt)
        x.statusbar.setObjectName("statusbar")
        Ui_Nomen_Elemek_Akt.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Nomen_Elemek_Akt)
        QtCore.QMetaObject.connectSlotsByName(Ui_Nomen_Elemek_Akt)

    def retranslateUi(x, Ui_Nomen_Elemek_Akt):
        _translate = QtCore.QCoreApplication.translate
        Ui_Nomen_Elemek_Akt.setWindowTitle(_translate("Ui_Nomen_Elemek_Akt", "Adatállomány kiválasztása"))
        x.groupBox.setTitle(_translate("Ui_Nomen_Elemek_Akt", "Input állomány"))
        x.label.setText(_translate("Ui_Nomen_Elemek_Akt", "Rendelkezésre álló adatok:"))
        x.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Akt", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Akt", "Mégse"))

class Ui_Nomen_Elemek_Kepzes(object):
    def setupUi(x, Ui_Nomen_Elemek_Kepzes):
        Ui_Nomen_Elemek_Kepzes.setObjectName("Ui_Nomen_Elemek_Kepzes")
        Ui_Nomen_Elemek_Kepzes.resize(563, 379)
        x.centralwidget = QtWidgets.QWidget(Ui_Nomen_Elemek_Kepzes)
        x.centralwidget.setObjectName("centralwidget")
        x.groupBox = QtWidgets.QGroupBox(x.centralwidget)
        x.groupBox.setGeometry(QtCore.QRect(20, 10, 531, 271))
        font = QtGui.QFont()
        font.setPointSize(11)
        x.groupBox.setFont(font)
        x.groupBox.setObjectName("groupBox")
        x.label = QtWidgets.QLabel(x.groupBox)
        x.label.setGeometry(QtCore.QRect(20, 40, 121, 31))
        x.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label.setWordWrap(False)
        x.label.setObjectName("label")
        x.comboBox = QtWidgets.QComboBox(x.groupBox)
        x.comboBox.setGeometry(QtCore.QRect(150, 50, 161, 21))
        x.comboBox.setObjectName("comboBox")
        x.label_2 = QtWidgets.QLabel(x.groupBox)
        x.label_2.setGeometry(QtCore.QRect(20, 80, 121, 31))
        x.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_2.setWordWrap(False)
        x.label_2.setObjectName("label_2")
        x.label_3 = QtWidgets.QLabel(x.groupBox)
        x.label_3.setGeometry(QtCore.QRect(20, 125, 121, 31))
        x.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_3.setWordWrap(False)
        x.label_3.setObjectName("label_3")
        x.label_4 = QtWidgets.QLabel(x.groupBox)
        x.label_4.setGeometry(QtCore.QRect(20, 160, 121, 21))
        x.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        x.label_4.setObjectName("label_4")
        x.lineEdit_lekerdezes = QtWidgets.QLineEdit(x.groupBox)
        x.lineEdit_lekerdezes.setGeometry(QtCore.QRect(150, 80, 361, 31))
        x.lineEdit_lekerdezes.setText("")
        x.lineEdit_lekerdezes.setObjectName("lineEdit_lekerdezes")
        x.lineEdit_nev = QtWidgets.QLineEdit(x.groupBox)
        x.lineEdit_nev.setGeometry(QtCore.QRect(150, 130, 191, 21))
        x.lineEdit_nev.setText("")
        x.lineEdit_nev.setObjectName("lineEdit_nev")
        x.lineEdit_ertek = QtWidgets.QLineEdit(x.groupBox)
        x.lineEdit_ertek.setGeometry(QtCore.QRect(150, 160, 191, 21))
        x.lineEdit_ertek.setText("")
        x.lineEdit_ertek.setObjectName("lineEdit_ertek")
        x.pushButton_mentes = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_mentes.setGeometry(QtCore.QRect(350, 290, 91, 41))
        x.pushButton_mentes.setObjectName("pushButton_mentes")
        x.pushButton_megse = QtWidgets.QPushButton(x.centralwidget)
        x.pushButton_megse.setGeometry(QtCore.QRect(460, 290, 91, 41))
        x.pushButton_megse.setDefault(True)
        x.pushButton_megse.clicked.connect(lambda: Ui_Nomen_Elemek_Kepzes.close())
        x.pushButton_megse.setObjectName("pushButton_megse")
        Ui_Nomen_Elemek_Kepzes.setCentralWidget(x.centralwidget)
        x.menubar = QtWidgets.QMenuBar(Ui_Nomen_Elemek_Kepzes)
        x.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        x.menubar.setObjectName("menubar")
        Ui_Nomen_Elemek_Kepzes.setMenuBar(x.menubar)
        x.statusbar = QtWidgets.QStatusBar(Ui_Nomen_Elemek_Kepzes)
        x.statusbar.setObjectName("statusbar")
        Ui_Nomen_Elemek_Kepzes.setStatusBar(x.statusbar)

        x.retranslateUi(Ui_Nomen_Elemek_Kepzes)
        QtCore.QMetaObject.connectSlotsByName(Ui_Nomen_Elemek_Kepzes)

    def retranslateUi(x, Ui_Nomen_Elemek_Kepzes):
        _translate = QtCore.QCoreApplication.translate
        Ui_Nomen_Elemek_Kepzes.setWindowTitle(_translate("Ui_Nomen_Elemek_Kepzes", "Nómenklatúra képzési szabályok"))
        x.groupBox.setTitle(_translate("Ui_Nomen_Elemek_Kepzes", "Paraméterek"))
        x.label.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Adatforrások:"))
        x.label_2.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Lekérdezés:"))
        x.label_3.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Név:"))
        x.label_4.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Érték:"))
        x.pushButton_mentes.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Mentés"))
        x.pushButton_megse.setText(_translate("Ui_Nomen_Elemek_Kepzes", "Mégse"))



class DbConnect(object):
    def __init__(self):
        pass

    def insert_nomen_elem(self, valtnev, ertek, cimke):
        conn = sqlite3.connect('datagov.db')
        conn.isolation_level = None
        c = conn.cursor()
        c.execute('insert into nomenklatura_elemek values("'+valtnev+'", "'+ertek+'", "'+cimke+'")')
        conn.commit()
        conn.close()