 
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys 
  
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
  
        # set the title 
        self.setWindowTitle("Python") 
  
        # setting geometry 
        self.setGeometry(100, 100, 600, 400) 
  
        # creating a label widget 
        self.label_1 = QLabel("old label ", self) 
  
        # getting the content of label 
        content = self.label_1.text() 
          
        # printing the content of label 
        print(content) 
  
        # moving the label 
        self.label_1.move(10, 100) 
  
        # creating a new label widget 
        self.label_2 = QLabel("new Label ", self) 
  
       # moving the label 
        self.label_2.move(110, 110) 
          
        # printing the content of label 
        print(self.label_2.text()) 
  
        # show all the widgets 
        self.show() 
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 