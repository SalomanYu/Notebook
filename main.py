import sys
from PyQt5.QtWidgets import QApplication
from app_logic import Notebook


class App(Notebook):
    def __init__(self):
        super().__init__()
        
        self.initGUI()
    
    def initGUI(self):
    
        self.create_menubar()
        self.statusBar().showMessage('Откройте файл или создайте новый')

   #Window parameters
        self.setGeometry(300,400, 1000, 650)
        self.setWindowTitle('Notebook')
        self.show()

if __name__ == '__main__':
    run_app = QApplication(sys.argv)
    style = ' '
    with open('style.css', 'r') as file:
        for line in file:
            style += line
    run_app.setStyleSheet(style)
    main = App()
    sys.exit(run_app.exec_())
