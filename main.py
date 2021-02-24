import sys
from PyQt5 import QtCore, QtGui, QtWidgets  
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow
from app_modules import *

class Ui_foWindow(object):
    def setupUi(self, foWindow):
        foWindow.setObjectName("foWindow")
        foWindow.resize(860, 600)
        self.centralwidget = QtWidgets.QWidget(foWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        #nem jottem ra meg hogy kell mdi-t osszekapcsolni a tobbi ablakkal
        """self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(-10, 0, 871, 601))
        self.mdiArea.setDocumentMode(True)
        self.mdiArea.setTabsClosable(True)
        self.mdiArea.setTabsMovable(True)
        self.mdiArea.setObjectName("mdiArea")"""
        
        #self.mdiArea.addSubWindow(self.mutatok_window)
        
        
        foWindow.setCentralWidget(self.centralwidget)       
        self.menubar = QtWidgets.QMenuBar(foWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        self.menuFelhasznalok_kezelese = QtWidgets.QMenu(self.menubar)
        self.menuFelhasznalok_kezelese.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.menuFelhasznalok_kezelese.setObjectName("menuFelhasznalok_kezelese")
        self.menuMeta_kezeles = QtWidgets.QMenu(self.menubar)
        self.menuMeta_kezeles.setObjectName("menuMeta_kezeles")
        self.menuAdatimport = QtWidgets.QMenu(self.menubar)
        self.menuAdatimport.setObjectName("menuAdatimport")        
        self.menuAdattisztitas = QtWidgets.QMenu(self.menubar)
        self.menuAdattisztitas.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.menuAdattisztitas.setObjectName("menuAdattisztitas")       
        self.menuAdatkezeles = QtWidgets.QMenu(self.menubar)
        self.menuAdatkezeles.setObjectName("menuAdatkezeles")
        self.menuAdatelemzes = QtWidgets.QMenu(self.menubar)
        self.menuAdatelemzes.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.menuAdatelemzes.setObjectName("menuAdatelemzes")
        self.menuEredmenyek = QtWidgets.QMenu(self.menubar)
        self.menuEredmenyek.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.menuEredmenyek.setObjectName("menuEredmenyek")
        self.menuAdat_export = QtWidgets.QMenu(self.menubar)
        self.menuAdat_export.setObjectName("menuAdat_export")
        self.menuFoSugo = QtWidgets.QMenu(self.menubar)
        self.menuFoSugo.setObjectName("menuFoSugo")
        self.menuRendszerbeallitas = QtWidgets.QMenu(self.menubar)
        self.menuRendszerbeallitas.setObjectName("menuRendszerbeallitas")
        self.menuSzinvalasztas = QtWidgets.QMenu(self.menuRendszerbeallitas)
        self.menuSzinvalasztas.setObjectName("menuSzinvalasztas")
        self.menuNyelvbeallitas = QtWidgets.QMenu(self.menuRendszerbeallitas)
        self.menuNyelvbeallitas.setObjectName("menuNyelvbeallitas")
        
        foWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(foWindow)
        self.statusbar.setObjectName("statusbar")
        foWindow.setStatusBar(self.statusbar)
        
        self.actionFelhasznalok = QtWidgets.QAction(foWindow)
        self.actionFelhasznalok.setObjectName("actionFelhasznalok")
        self.actionCsoportok = QtWidgets.QAction(foWindow)
        self.actionCsoportok.setObjectName("actionCsoportok")
        self.actionJogosultsagok = QtWidgets.QAction(foWindow)
        self.actionJogosultsagok.setObjectName("actionJogosultsagok")
        self.actionSzervezetek = QtWidgets.QAction(foWindow)
        self.actionSzervezetek.setObjectName("actionSzervezetek")        
        self.actionMutatok = QtWidgets.QAction(foWindow)
        self.actionMutatok.setObjectName("actionMutatok")
        self.actionNomen = QtWidgets.QAction(foWindow)
        self.actionNomen.setObjectName("actionNomen")
        self.actionRekord = QtWidgets.QAction(foWindow)
        self.actionRekord.setStatusTip("")
        self.actionRekord.setObjectName("actionRekord")
        self.actionAdatall = QtWidgets.QAction(foWindow)
        self.actionAdatall.setObjectName("actionAdatall")        
        self.actionFajlimport= QtWidgets.QAction(foWindow)
        self.actionFajlimport.setObjectName("actionFajlimport")
        self.actionImport_adatbazisbol = QtWidgets.QAction(foWindow)
        self.actionImport_adatbazisbol.setObjectName("actionImport_adatbazisbol")
        self.actionMeta_import = QtWidgets.QAction(foWindow)
        self.actionMeta_import.setObjectName("actionMeta_import")
        self.actionParositas = QtWidgets.QAction(foWindow)
        self.actionParositas.setObjectName("actionParositas")
        self.actionAggregalas = QtWidgets.QAction(foWindow)
        self.actionAggregalas.setObjectName("actionAggregalas")
        self.actionSzelekcio = QtWidgets.QAction(foWindow)
        self.actionSzelekcio.setObjectName("actionSzelekcio")
        self.actionMintavetel = QtWidgets.QAction(foWindow)
        self.actionMintavetel.setObjectName("actionMintavetel")
        self.actionLeiro_statisztika = QtWidgets.QAction(foWindow)
        self.actionLeiro_statisztika.setObjectName("actionLeiro_statisztika")
        self.actionStatisztikai_tabla = QtWidgets.QAction(foWindow)
        self.actionStatisztikai_tabla.setObjectName("actionStatisztikai_tabla")
        self.actionGrafikus_megjelenites = QtWidgets.QAction(foWindow)
        self.actionGrafikus_megjelenites.setObjectName("actionGrafikus_megjelenites")
        self.actionTobbv_elemzes = QtWidgets.QAction(foWindow)
        self.actionTobbv_elemzes.setObjectName("actionTobbv_elemzes")
        self.actionMikroszimulacio = QtWidgets.QAction(foWindow)
        self.actionMikroszimulacio.setObjectName("actionMikroszimulacio")
        self.actionMI = QtWidgets.QAction(foWindow)
        self.actionMI.setObjectName("actionMI")     
        self.actionSugo = QtWidgets.QAction(foWindow)
        self.actionSugo.setObjectName("actionSugo")
        self.actionNevjegy = QtWidgets.QAction(foWindow)
        self.actionNevjegy.setObjectName("actionNevjegy")
        self.actionMagyar = QtWidgets.QAction(foWindow)
        self.actionMagyar.setObjectName("actionMagyar")
        self.actionAngol = QtWidgets.QAction(foWindow)
        self.actionAngol.setObjectName("actionAngol")
        self.actionGray = QtWidgets.QAction(foWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionBlack = QtWidgets.QAction(foWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionWhite = QtWidgets.QAction(foWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.actionJelszovaltas = QtWidgets.QAction(foWindow)
        self.actionJelszovaltas.setObjectName("actionJelszovaltas")
        self.actionJelszovaltas.setObjectName("actionJelszovaltas")
        
       
        self.menuFelhasznalok_kezelese.addAction(self.actionFelhasznalok)
        self.menuFelhasznalok_kezelese.addAction(self.actionCsoportok)
        self.menuFelhasznalok_kezelese.addAction(self.actionJogosultsagok)
        self.menuFelhasznalok_kezelese.addAction(self.actionSzervezetek)  
        self.menuMeta_kezeles.addAction(self.actionMutatok)
        self.menuMeta_kezeles.addAction(self.actionNomen)
        self.menuMeta_kezeles.addAction(self.actionRekord)
        self.menuMeta_kezeles.addAction(self.actionAdatall)
        self.menuAdatimport.addAction(self.actionFajlimport)
        self.menuAdatimport.addAction(self.actionImport_adatbazisbol)
        self.menuAdatimport.addAction(self.actionMeta_import)       
        self.menuAdatkezeles.addAction(self.actionParositas)
        self.menuAdatkezeles.addAction(self.actionAggregalas)
        self.menuAdatkezeles.addAction(self.actionSzelekcio)
        self.menuAdatkezeles.addAction(self.actionMintavetel)
        self.menuAdatelemzes.addAction(self.actionLeiro_statisztika)
        self.menuAdatelemzes.addAction(self.actionStatisztikai_tabla)
        self.menuAdatelemzes.addAction(self.actionGrafikus_megjelenites)
        self.menuAdatelemzes.addAction(self.actionTobbv_elemzes)
        self.menuAdatelemzes.addAction(self.actionMikroszimulacio)
        self.menuAdatelemzes.addAction(self.actionMI)
        self.menuFoSugo.addAction(self.actionSugo)
        self.menuFoSugo.addAction(self.actionNevjegy)
        self.menuNyelvbeallitas.addAction(self.actionMagyar)
        self.menuNyelvbeallitas.addAction(self.actionAngol)
        self.menuSzinvalasztas.addAction(self.actionBlack)
        self.menuSzinvalasztas.addAction(self.actionGray)
        self.menuSzinvalasztas.addAction(self.actionWhite)         
        self.menuRendszerbeallitas.addAction(self.menuNyelvbeallitas.menuAction())
        self.menuRendszerbeallitas.addAction(self.menuSzinvalasztas.menuAction())
        self.menuRendszerbeallitas.addAction(self.actionJelszovaltas)
        self.menubar.addAction(self.menuFelhasznalok_kezelese.menuAction())
        self.menubar.addAction(self.menuMeta_kezeles.menuAction())
        self.menubar.addAction(self.menuAdatimport.menuAction())
        self.menubar.addAction(self.menuAdattisztitas.menuAction())
        self.menubar.addAction(self.menuAdatkezeles.menuAction())
        self.menubar.addAction(self.menuAdatelemzes.menuAction())
        self.menubar.addAction(self.menuEredmenyek.menuAction())
        self.menubar.addAction(self.menuAdat_export.menuAction())
        self.menubar.addAction(self.menuFoSugo.menuAction())
        self.menubar.addAction(self.menuRendszerbeallitas.menuAction())
        
        self.retranslateUi(foWindow)
        QtCore.QMetaObject.connectSlotsByName(foWindow)
        
        self.actionMutatok.triggered.connect(self.window_mutatok)
        #ezzel nyitja meg a menüből a Ui_Mutatok ablakot
        self.actionNomen.triggered.connect(self.window_nomenklatura)
        self.actionRekord.triggered.connect(self.window_rekordleiras)
        self.actionAdatall.triggered.connect(self.window_adatallomanyok)
        self.actionParositas.triggered.connect(self.window_parositas)
        self.actionAggregalas.triggered.connect(self.window_aggregalas)
        self.actionSzelekcio.triggered.connect(self.window_szelekcio)
        self.actionMintavetel.triggered.connect(self.window_mintavetel)
        self.actionFajlimport.triggered.connect(self.window_import)

        #az adott menu osszes actionja megnyitja a felugro ablakot
        self.menuFelhasznalok_kezelese.triggered.connect(self.show_popup)
        self.menuAdatelemzes.triggered.connect(self.show_popup)
        self.actionJelszovaltas.triggered.connect(self.show_popup)
        self.actionGray.triggered.connect(self.change_color_gray)
        self.actionWhite.triggered.connect(self.change_color_white)
        self.actionBlack.triggered.connect(self.change_color_black)
        


        #kellene meg adattisztitas is, es eredmeny is, mert azok sem a DG feladatköre
        #self.menuAdattisztitas.menuAction(self.show_popup) #ez igy nem reagal a kattintasra
        #self.menuAdattisztitas.clicked.triggered[QAction].connect(self.show_popup)
        #self.menuEredmenyek.triggered.connect(self.show_popup)
        
     
        
     #itt megprobalkoztam a fajlok adatimportjaval, de egyik sem sikerult
        #self.actionFajlimport.triggered.connect(self.showDialogBox)
        #self.openFileNameDialog()
            
        """   
    def showDialogBox(self):
        home_directory = str(Path.home())
        file_name = QFileDialog.getOpenFileName(self, 'Open file', home_directory)
        if file_name[0]:
            file = open(file_name[0], 'r')
        with file:
            data = file.read()
            self.text_edit.setText(data)
        
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName) 
                
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if files:
            print(files)               

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)
       """      
    def addTableRow(self, table, row_data): #v2
            row = table.rowCount()
            table.setRowCount(row+1)
            col = 0
            for item in row_data:
                cell = QTableWidgetItem(str(item))
                table.setItem(row, col, cell)
                col += 1        

    def change_color_gray(self):
        self.centralwidget.setStyleSheet("background-color: gray;")
    
    def change_color_black(self):
        self.centralwidget.setStyleSheet("background-color: black;")

    def change_color_white(self):
        self.centralwidget.setStyleSheet("background-color: white;") 

    def retranslateUi(self, foWindow):
        _translate = QtCore.QCoreApplication.translate
        foWindow.setWindowTitle(_translate("foWindow", "U projekt - Data Governance"))
        self.menuFelhasznalok_kezelese.setTitle(_translate("MainWindow", "Felhasználó kezelése"))        
        self.menuMeta_kezeles.setTitle(_translate("foWindow", "Meta kezelés"))
        self.menuAdatimport.setTitle(_translate("foWindow", "Adatimport"))
        self.menuAdattisztitas.setTitle(_translate("MainWindow", "Adattisztítás"))
        self.menuAdatkezeles.setTitle(_translate("foWindow", "Adatkezelés"))
        self.menuAdatelemzes.setTitle(_translate("MainWindow", "Adatelemzés"))  
        self.menuEredmenyek.setTitle(_translate("MainWindow", "Eredmények"))
        self.menuAdat_export.setTitle(_translate("MainWindow", "Adat export"))
        self.menuFoSugo.setTitle(_translate("MainWindow", "Súgó"))
        self.menuRendszerbeallitas.setTitle(_translate("MainWindow", "Rendszerbeállítás"))
        self.menuNyelvbeallitas.setTitle(_translate("MainWindow", "Nyelv beállítása"))
        self.menuSzinvalasztas.setTitle(_translate("MainWindow", "Szín választása"))

        self.actionFelhasznalok.setText(_translate("MainWindow", "Felhasználók"))
        self.actionCsoportok.setText(_translate("MainWindow", "Csoportok"))
        self.actionJogosultsagok.setText(_translate("MainWindow", "Jogosultságok"))
        self.actionSzervezetek.setText(_translate("MainWindow", "Szervezetek"))
        self.actionFajlimport.setText(_translate("foWindow", "Fájlok importálása"))
        self.actionFajlimport.setStatusTip(_translate("foWindow", "CSV., SAS., XLSX. fájlok importálása"))
        self.actionImport_adatbazisbol.setText(_translate("MainWindow", "Importálás adatbázisból"))
        self.actionImport_adatbazisbol.setStatusTip(_translate("foWindow","Adatok importálása ODBC.-ből"))
        self.actionMeta_import.setText(_translate("MainWindow", "Meta import"))
        self.actionMutatok.setText(_translate("foWindow", "Mutatók"))
        self.actionMutatok.setStatusTip(_translate("foWindow", "Érték adataink kezelése"))
        self.actionNomen.setText(_translate("foWindow", "Nómenklatúrák"))
        self.actionNomen.setStatusTip(_translate("foWindow", "Kód adataink kezelése"))
        self.actionRekord.setText(_translate("foWindow", "Rekordleírások"))
        self.actionAdatall.setText(_translate("foWindow", "Adatállományok"))
        self.actionAdatall.setStatusTip(_translate("foWindow", "Fizikailag tárolt adatkatalógusunk kezelése"))
        self.actionParositas.setText(_translate("foWindow", "Párosítás"))
        self.actionAggregalas.setText(_translate("foWindow", "Aggregálás"))
        self.actionSzelekcio.setText(_translate("foWindow", "Szelekció"))
        self.actionMintavetel.setText(_translate("foWindow", "Mintavétel"))
        self.actionLeiro_statisztika.setText(_translate("MainWindow", "Leíró statisztika"))
        self.actionStatisztikai_tabla.setText(_translate("MainWindow", "Statisztikai tábla"))
        self.actionGrafikus_megjelenites.setText(_translate("MainWindow", "Grafikus megjelenítés"))
        self.actionTobbv_elemzes.setText(_translate("MainWindow", "Többváltozós elemzés"))
        self.actionMikroszimulacio.setText(_translate("MainWindow", "Mikroszimuláció"))
        self.actionMI.setText(_translate("MainWindow", "Mesterséges intelligencia"))       
        self.actionSugo.setText(_translate("MainWindow", "Súgó"))
        self.actionNevjegy.setText(_translate("MainWindow", "Névjegy"))
        self.actionMagyar.setText(_translate("MainWindow", "Magyar"))
        self.actionAngol.setText(_translate("MainWindow", "Angol"))
        self.actionGray.setText(_translate("MainWindow", "Szürke"))
        self.actionBlack.setText(_translate("MainWindow", "Fekete"))
        self.actionWhite.setText(_translate("MainWindow", "Fehér"))
        self.actionJelszovaltas.setText(_translate("MainWindow", "Jelszóváltás"))

    #ez nyitja meg a mutatok ablakot
    def window_mutatok(self):
        #self.window = QtWidgets.QMdiSubWindow()
        self.window = QtWidgets.QMainWindow()
        self.ui =  Ui_Mutatok()
        self.ui.setupUi(self.window)
        self.window.show()
    #ez nyitja meg a nomenklatura ablakot
    def window_nomenklatura(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Nomenklatura()
        self.ui.setupUi(self.window)
        self.window.show()
     #ez nyitja meg a rekordleiras ablakot   
    def window_rekordleiras(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Rekordleirasok()
        self.ui.setupUi(self.window)
        self.window.show()    
  #ezzel nyitjuk meg az adatallomanyok ablakot
    def window_adatallomanyok(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Adatallomanyok()
        self.ui.setupUi(self.window)
        self.window.show()         
    
    def window_parositas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Parositas()
        self.ui.setupUi(self.window)
        self.window.show()  
    
    def window_aggregalas(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Aggregalas()
        self.ui.setupUi(self.window)
        self.window.show() 
    def window_szelekcio(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Szelekcio()
        self.ui.setupUi(self.window)
        self.window.show() 
    def window_mintavetel(self):
        self.window=QtWidgets.QMainWindow()
        self.ui = Ui_Mintavetel()
        self.ui.setupUi(self.window)
        self.window.show() 
        
    def window_import(self):
        self.dialogs = list()
        dialog = DataMain()
        self.dialogs.append(dialog)
        dialog.show()
    
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Data Governance információ")
        msg.setText("Külön projekt foglalkozik ezzel a menüponttal!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

#az ablak bezárásának felülírásához új osztály kell, mert a closeEvent a QMainWindow metódusa
class MyWindow(QtWidgets.QMainWindow):  
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                      "Kilépés megerősítése...",
                      "Biztosan be szeretnád zárni az összes ablakot?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
            app.closeAllWindows()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    foWindow = MyWindow()
    #foWindow = QtWidgets.QMainWindow()
    ui = Ui_foWindow()
    ui.setupUi(foWindow)
    foWindow.show()
    sys.exit(app.exec_())