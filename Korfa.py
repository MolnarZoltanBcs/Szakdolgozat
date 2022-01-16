import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, QAction, QMdiArea, QMdiSubWindow, QLineEdit
from PyQt5.QtCore import pyqtSlot
from app_modules import *
from PIL import Image

import seaborn as sns


class Korfa(QtWidgets.QMainWindow):

    def __init__(self, ablak, parentAblak):
        super(Korfa, self).__init__()
        #deklarációk
        self.ablak=ablak
        self.parentAblak=parentAblak
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self._translate = QtCore.QCoreApplication.translate
        self.tab = QtWidgets.QWidget()
        self.font = QtGui.QFont()
        self.pushButton_Mentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Megse = QtWidgets.QPushButton(self.centralwidget)
        #specifikus beállítások
        self.setup()

    def setup(self):
        self.ablak.setObjectName("Korfa")
        self.ablak.resize(484, 466)
        self.ablak.setWindowTitle(self.ablak.objectName())
        self.centralwidget.setObjectName("centralwidget")
        self.ablak.setCentralWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 371))
        self.tab.setObjectName("tab")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Attribútumok")


        self.pushButton_Mentes.setGeometry(QtCore.QRect(270, 400, 91, 41))
        self.pushButton_Mentes.setText("Generálás")

        self.pushButton_Megse.setGeometry(QtCore.QRect(370, 400, 91, 41))
        self.pushButton_Megse.setDefault(True)
        self.pushButton_Megse.setObjectName("pushButton_Megse")
        self.pushButton_Megse.setText("Mégse")
        self.pushButton_Megse.clicked.connect(lambda: self.ablak.close())

        self.font.setPointSize(11)
        self.pushButton_Megse.setFont(self.font)
        self.pushButton_Mentes.setFont(self.font)
        self.tab.setFont(self.font)
        self.tabWidget.setFont(self.font)


class KorfaGeneralas(Korfa):

    def __init__(self, ablak, parentAblak):
        super(KorfaGeneralas, self).__init__(ablak, parentAblak)
        self.adatallomanyLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_adatallomany = QtWidgets.QLineEdit(self.tab)
        self.adatallomany_tallozPushButton = QtWidgets.QPushButton(self.tab)
        self.adatallomany_eleresi_ut=""

        self.korcsoportLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_korcsoport = QtWidgets.QLineEdit(self.tab)
        self.int_validator=QIntValidator(0,9)
        self.lineEdit_korcsoport.setValidator(self.int_validator)

        self.ferfiLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_ferfi = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_ferfi.setValidator(self.int_validator)

        self.noLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_no = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_no.setValidator(self.int_validator)

        self.yTengelyLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_yTengely = QtWidgets.QLineEdit(self.tab)

        self.xTengelyLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_xTengely = QtWidgets.QLineEdit(self.tab)

        self.plotNevLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_plotNev = QtWidgets.QLineEdit(self.tab)

        self.plotFajlNevLabel = QtWidgets.QLabel(self.tab)
        self.lineEdit_plotFajlNev = QtWidgets.QLineEdit(self.tab)

        self.pngLabel = QtWidgets.QLabel(self.tab)

        self.setup_korfa()

    def setup_korfa(self):
        self.ablak.setWindowTitle("Korfa")


        labelSetUp(self.adatallomanyLabel, 40, 10, 161, 31, "Adatállomány:")
        self.lineEdit_adatallomany.setGeometry(QtCore.QRect(220, 10, 140, 31))
        self.lineEdit_adatallomany.setReadOnly(True)
        self.lineEdit_adatallomany.setObjectName("lineEdit_adatallomany")
        self.lineEdit_adatallomany.setStyleSheet("QLineEdit"
                                            "{"
                                            "background : lightgray;"
                                            "}")
        self.adatallomany_tallozPushButton.setGeometry(QtCore.QRect(370, 10, 70, 31))
        self.adatallomany_tallozPushButton.setText("Tallózás")
        self.adatallomany_tallozPushButton.clicked.connect(lambda: self.getadatallomany())

        labelSetUp(self.korcsoportLabel, 40, 50, 161, 31, "Korcsoport indexe:")
        self.lineEdit_korcsoport.setGeometry(QtCore.QRect(220, 50, 210, 31))
        self.lineEdit_korcsoport.setText("0")

        labelSetUp(self.ferfiLabel, 40, 90, 161, 31, "Férfiak indexe:")
        self.lineEdit_ferfi.setGeometry(QtCore.QRect(220, 90, 210, 31))
        self.lineEdit_ferfi.setText("1")

        labelSetUp(self.noLabel, 40, 130, 161, 31, "Nők indexe:")
        self.lineEdit_no.setGeometry(QtCore.QRect(220, 130, 210, 31))
        self.lineEdit_no.setText("2")

        labelSetUp(self.yTengelyLabel, 40, 170, 161, 31, "Y tengely neve:")
        self.lineEdit_yTengely.setGeometry(QtCore.QRect(220, 170, 210, 31))
        self.lineEdit_yTengely.setText("y")

        labelSetUp(self.xTengelyLabel, 40, 200, 161, 51, "X tengely neve:")
        self.lineEdit_xTengely.setGeometry(QtCore.QRect(220, 210, 210, 31))
        self.lineEdit_xTengely.setText("x")

        labelSetUp(self.plotNevLabel, 40, 250, 161, 31, "Korfa címe:")
        self.lineEdit_plotNev.setGeometry(QtCore.QRect(220, 250, 210, 31))
        self.lineEdit_plotNev.setText("Korfa")

        labelSetUp(self.plotFajlNevLabel, 40, 290, 161, 31, "Eredmény fájl neve:")
        self.lineEdit_plotFajlNev.setGeometry(QtCore.QRect(220, 290, 150, 31))
        self.lineEdit_plotFajlNev.setText("eredmeny")

        labelSetUp(self.pngLabel, 370, 290, 40, 31, ".png")

        self.tabWidget.addTab(self.tab, "Új korfa generálása")

        self.pushButton_Mentes.clicked.connect(lambda: self.generalas())

    def getadatallomany(self):
        self.adatallomany_eleresi_ut = QtWidgets.QFileDialog.getOpenFileUrl(caption="Adatállomány betöltése", filter="CSV fájl (*.csv)", initialFilter="CSV fájl (*.csv)")
        try:
            self.lineEdit_adatallomany.setText(self.adatallomany_eleresi_ut[0].fileName())
        except:
            print("nem lett megadva szabályosan az útvonal")

    def generalas(self):
        if(self.lineEdit_adatallomany.text() != ""):
            if(self.lineEdit_korcsoport.text()==""):
                korcsoport=0
            else:
                korcsoport=int(self.lineEdit_korcsoport.text())
            if (self.lineEdit_ferfi.text() == ""):
                ferfi = 1
            else:
                ferfi = int(self.lineEdit_ferfi.text())
            if (self.lineEdit_no.text() == ""):
                no = 2
            else:
                no = int(self.lineEdit_no.text())
            df = pd.read_csv(self.adatallomany_eleresi_ut[0].toString())
            try:
                self.generateAgeTree(df, ageGroups=korcsoport, menColumn=ferfi, womenColumn=no, ylabelText=self.lineEdit_yTengely.text(), xlabelText=self.lineEdit_xTengely.text(), titleText=self.lineEdit_plotNev.text())
            except:
                QtWidgets.QMessageBox.question(self.ablak, "Nem megfelelő a megadott fájl korfa generálására", "Kérlek válassz ki egy fájlt amely alkalmas korfa generálására!", QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.question(self.ablak, "Hibás útvonal", "Kérlek válassz ki egy fájlt a generáláshoz!", QtWidgets.QMessageBox.Ok)

    def generateAgeTree(self, dataFrame, ageGroups=0, menColumn=1, womenColumn=2, xlabelText="Population", ylabelText="Age-Group", titleText="Age Tree"):
        if not dataFrame.empty:
            groups = dataFrame.iloc[:, ageGroups].values
            men = dataFrame.iloc[:, menColumn].values
            women = dataFrame.iloc[:, womenColumn].values
            if not (0 != groups[0][1]):
                groups = groups[::-1]
                men = men[::-1]
                women = women[::-1]

            data = {'Male': men, 'Female': women, 'Age': groups}
            new_df = pd.DataFrame(data)

            self.korfa = sns.barplot(x='Male', y='Age', data=new_df, order=groups)
            self.korfa = sns.barplot(x='Female', y='Age', data=new_df, order=groups)
            self.korfa.set(xlabel=xlabelText, ylabel=ylabelText, title=titleText)
            try:
                # self.korfa_eredmeny_eleresi_utvonal = QtCore.QUrl.toLocalFile(QtWidgets.QFileDialog.getSaveFileUrl(caption="Eredmény mentése", filter="PNG fájl (*.png)", initialFilter="PNG fájl (*.png)")[0])
                # if self.korfa_eredmeny_eleresi_utvonal=="": # hibakezelés, ha bezárják a fájlmentéses ablakot, vagy a mégse gombra kattintanak
                #     return
                self.korfa.figure.savefig("eredmenyek/"+self.lineEdit_plotFajlNev.text()+".png")
                self.korfa_img=Image.open("eredmenyek/"+self.lineEdit_plotFajlNev.text()+".png")
                self.korfa_img.show()
            except:
                print("nem lett megadva útvonal a generáláshoz")
                # self.korfa.figure.savefig("output.png")
            self.ablak.close()



def labelSetUp(label, kezdopont_x, kezdopont_y, hossz_x, hossz_y, nev):
    label.setGeometry(QtCore.QRect(kezdopont_x, kezdopont_y, hossz_x, hossz_y))
    label.setLayoutDirection(QtCore.Qt.LeftToRight)
    label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    label.setObjectName(nev)
    label.setText(nev)
