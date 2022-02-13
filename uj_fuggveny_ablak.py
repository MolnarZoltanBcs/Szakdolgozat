import datetime
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QTabWidget, QLabel, QLineEdit, QScrollArea, QFormLayout
from PyQt5 import QtCore, QtGui, Qt
from app_modules import *

class Fuggveny:
    def __init__(self, fuggveny, cim :str, argumentumok :dict, letrehozo :str, leiras :str):
        self.fuggveny = fuggveny
        self.argumentumok = argumentumok
        self.letrehozas_datuma = datetime.datetime.today()
        self.letrehozo = letrehozo
        self.leiras = leiras
        self.cim = cim

ABLAK_MERET=[540, 540]
line_edit_lista=[]

class Fuggveny_ablak:
    def __init__(self, fuggveny :Fuggveny, parentAblak :QMainWindow):
        self.fuggveny = fuggveny
        self.ablak = QMainWindow()
        self.ablak.resize(ABLAK_MERET[0], ABLAK_MERET[1])
        self.parentAblak = parentAblak
        self.font = QtGui.QFont()
        self.font.setPointSize(11)

        self.central_widget = QWidget(self.ablak)
        self.pushButton_Mentes = QPushButton(self.central_widget)
        self.pushButton_Megse = QPushButton(self.central_widget)

        self.tabWidget = QTabWidget(self.central_widget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, ABLAK_MERET[0] - 20, ABLAK_MERET[1] - 90))

        self.tab = QWidget()

        self.scrollbar = QScrollArea()
        self.scrollbar.setVerticalScrollBarPolicy(2) # always on
        self.scrollbar.setWidgetResizable(True)
        self.scrollbar.setEnabled(True)
        # self.scrollbar.setFixedHeight(ABLAK_MERET[1]-40)
        self.form = QFormLayout(self.scrollbar)

        self.setup()

    def setup(self):
        self.ablak.setObjectName(self.fuggveny.cim)
        self.ablak.setWindowTitle(self.fuggveny.cim)
        self.central_widget.setObjectName("centralwidget")
        self.pushButton_Mentes.setGeometry(QtCore.QRect(ABLAK_MERET[0]-200, ABLAK_MERET[1]-60, 91, 41))
        self.pushButton_Mentes.setObjectName("Mentes")
        self.pushButton_Megse.setGeometry(QtCore.QRect(ABLAK_MERET[0]-100, ABLAK_MERET[1]-60, 91, 41))
        self.pushButton_Megse.setObjectName("Megse")
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_Mentes.setText(_translate(self.pushButton_Mentes.objectName(), "Mentés"))
        self.pushButton_Mentes.clicked.connect(lambda: self.start_function())
        self.pushButton_Megse.setText(_translate(self.pushButton_Megse.objectName(), "Mégse"))
        self.pushButton_Megse.clicked.connect(lambda: self.ablak.close())


        #argumentumok megjelenítése
        i=0
        global line_edit_lista

        for key, value in self.fuggveny.argumentumok.items():
            layout = QtWidgets.QHBoxLayout()
            label = QLabel(self.scrollbar)
            label.setObjectName("label")
            label.setText(_translate(label.objectName(), key+":"))
            layout.addWidget(label)


            lineEdit = QLineEdit(self.scrollbar)
            lineEdit.setObjectName("lineEdit_csoport")
            layout.addWidget(lineEdit)
            line_edit_lista.append(lineEdit)
            i+=1
            self.form.addRow("",layout)
        self.tab.setLayout(self.form)
        self.tabWidget.addTab(self.tab, "Első oldal")
        self.tabWidget.setFont(self.font)
        self.tabWidget.setCurrentIndex(0)
        self.ablak.setCentralWidget(self.central_widget)

    def start_function(self):
        eredmeny_lista=[]
        global line_edit_lista
        for elem in line_edit_lista:
            eredmeny_lista.append(elem.text())
        self.fuggveny.fuggveny(eredmeny_lista)
        self.ablak.close()


def labelSetUp( label, kezdopont_x, kezdopont_y, hossz_x, hossz_y, nev):
    label.setGeometry(QtCore.QRect(kezdopont_x, kezdopont_y, hossz_x, hossz_y))
    label.setLayoutDirection(QtCore.Qt.LeftToRight)
    label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
    label.setObjectName(nev)