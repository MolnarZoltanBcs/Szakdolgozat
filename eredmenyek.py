import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, QFileDialog, \
    QAction, QMdiArea, QMdiSubWindow, QLineEdit, QScrollArea, QButtonGroup
from PyQt5.QtCore import pyqtSlot
from app_modules import *

import os

class Eredmeny(QtWidgets.QMainWindow):
    def __init__(self, ablak, parentAblak):
        super(Eredmeny, self).__init__()
        #deklarációk
        self.ablak=ablak
        self.parentAblak=parentAblak
        self.centralwidget = QtWidgets.QWidget(self.ablak)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self._translate = QtCore.QCoreApplication.translate
        self.tab = QtWidgets.QWidget()
        # self.tab2 = QtWidgets.QWidget()
        self.font = QtGui.QFont()
        # self.pushButton_Mentes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Megse = QtWidgets.QPushButton(self.centralwidget)

        self.scrollbar = QScrollArea()
        self.form = QtWidgets.QFormLayout(self.scrollbar)



        #specifikus beállítások
        self.setup()

    def setup(self):
        self.ablak.setObjectName("Eredmények")
        # self.ablak.resize(484, 466)
        self.ablak.resize(618, 600)
        self.ablak.setWindowTitle(self.ablak.objectName())
        self.centralwidget.setObjectName("centralwidget")
        self.ablak.setCentralWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 585, 505))
        self.tab.setObjectName("tab")
        # self.tab2.setObjectName("tab2")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Attribútumok")
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), "Attribútumok2")


        # self.pushButton_Mentes.setGeometry(QtCore.QRect(270, 400, 91, 41))
        # self.pushButton_Mentes.setText("OK")

        self.scrollbar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollbar.setWidget(self.tab)
        self.scrollbar.setWidgetResizable(True)
        self.scrollbar.setEnabled(True)
        self.scrollbar.setFixedHeight(470)


        self.buttonGroup=QButtonGroup()
        self.buttonGroup.setExclusive(True)

        self.form_init()

        self.buttonGroup.buttonClicked.connect(lambda: self.fajlinditas())
        self.tab.setLayout(self.form)
        self.pushButton_Megse.setGeometry(QtCore.QRect(504, 534, 91, 41))
        self.pushButton_Megse.setDefault(True)
        self.pushButton_Megse.setObjectName("pushButton_Megse")
        self.pushButton_Megse.setText("Bezár")
        self.pushButton_Megse.clicked.connect(lambda: self.ablak.close())

        self.font.setPointSize(11)
        self.pushButton_Megse.setFont(self.font)
        # self.pushButton_Mentes.setFont(self.font)
        self.tab.setFont(self.font)
        # self.tab2.setFont(self.font)
        self.tabWidget.setFont(self.font)

    def form_init(self):
        index=0
        while(self.form.rowCount()>0):
            self.form.removeRow(0)
        # self.form=QtWidgets.QFormLayout(self.scrollbar)
        self.layoutElemLista = []
        self.fajlLista = []
        for fajl in os.listdir("eredmenyek"):
            self.fajlLista.append(fajl)
            layout = QtWidgets.QHBoxLayout()
            megtekint=QtWidgets.QPushButton(self.scrollbar)
            megtekint.setCheckable(True)
            megtekint.setText("Megtekintés")
            self.buttonGroup.addButton(megtekint)
            torol=QtWidgets.QPushButton(self.scrollbar)
            torol.setText("Törlés")
            torol.setCheckable(True)
            self.buttonGroup.addButton(torol)
            layout.addWidget(megtekint)
            layout.addWidget(torol)
            self.form.addRow(fajl, layout)
            self.layoutElemLista.append(LayoutElem(layout, index))
            index+=1

    def fajlinditas(self):
        # print(self.buttonGroup.checkedButton())
        for elem in self.layoutElemLista:
            # print(elem)
            if elem.layout.itemAt(0).widget().isChecked():
                os.system('start eredmenyek/'+'"'+self.fajlLista[elem.index]+'"')
                return
            if elem.layout.itemAt(1).widget().isChecked():
                os.remove("eredmenyek/"+self.fajlLista[elem.index])
                self.form_init()
                return

    # def alma(self):
    #     raise ValueError

class EredmenyekMegjelenitese(Eredmeny):
    def __init__(self, ablak, parentAblak):
        super(EredmenyekMegjelenitese, self).__init__(ablak, parentAblak)


        self.tabWidget.addTab(self.scrollbar, "Összes mentett eredmény")
        # self.tabWidget.addTab(self.tab2, "Összes mentett eredmény2")


class LayoutElem():

    def __init__(self, layout, index):
        self.layout=layout
        self.index=index


