from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()

        
    def create_menubar(self):
        # Actions for menuBar
        
        # File menu
        open_file_action = QAction('Open file', self)
        open_file_action.setShortcut('Ctrl+O')
        open_file_action.triggered.connect(self.open_file)

        save_file_action = QAction('Save file', self)
        save_file_action.setShortcut('Ctrl+S')
        save_file_action.triggered.connect(self.save_file)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close_app)
        
        # Help menu
        help_action = QAction('Support', self)
        help_action.setShortcut('Ctrl+H')
        help_action.triggered.connect(self.show_support_info)

        about_program_action = QAction('About Me', self)
        about_program_action.setShortcut('Ctrl+I')
        about_program_action.triggered.connect(self.show_about_info)

        # Themes colors
        themes = {
            'dark' : 'QTextEdit { \
                        background-color: #53545d; \
                        color: #bec9ca; \
                    } \
                    QMainWindow { \
                        background-color:#bec9ca; \
                    }',

            'light' : 'QTextEdit { \
                        background-color: #bec9ca; \
                        color: #53545d; \
                    } \
                    QMainWindow { \
                        background-color:#53545d; \
                    }',

            'fernando' : 'QTextEdit { \
                            background-color: #eddcd2; \
                            color: #7f5539; \
                    } \
                    QMainWindow { \
                        background-color:#7f5539; \
                    }',

            'marisol' : 'QTextEdit { \
                            background-color: #F5F5DC; \
                            color: #73a6e0; \
                    } \
                    QMainWindow { \
                        background-color:#e9e7db; \
                    }',
            'boung' : 'QTextEdit { \
                            background-color: #293241; \
                            color: #ee6c4d; \
                    } \
                    QMainWindow { \
                        background-color:#ee6c4d; \
                    }',
            'kineto' : 'QTextEdit { \
                            background-color: #b7b7a4; \
                            color: #606c38; \
                    } \
                    QMainWindow { \
                        background-color:#606c38; \
                    }',
            
        }
        # Themes Actions
        dark_action = QAction('Dark', self)
        dark_action.triggered.connect(lambda x: self.setStyleSheet(themes['dark']))
        
        light_action = QAction('Light', self)
        light_action.triggered.connect(lambda x: self.setStyleSheet(themes['light']))
        
        fernando_action = QAction('Fernando', self)
        fernando_action.triggered.connect(lambda x: self.setStyleSheet(themes['fernando']))

        marisol_action = QAction('Marisol', self)
        marisol_action.triggered.connect(lambda x: self.setStyleSheet(themes['marisol']))

        boung_action = QAction('Boung', self)
        boung_action.triggered.connect(lambda x: self.setStyleSheet(themes['boung']))

        kineto_action = QAction('Kineto', self)
        kineto_action.triggered.connect(lambda x: self.setStyleSheet(themes['kineto']))
        

    # Connection the actions with menuBar
        menu_bar = self.menuBar()
       
        # Add actions to file_menu
        file_menu = menu_bar.addMenu('&File')   
        file_menu.addAction(open_file_action)
        file_menu.addAction(save_file_action)
        file_menu.addAction(exit_action)

        # Parameters
        settings_menu = menu_bar.addMenu('&Settings')

        # Themes
        themes_menu = settings_menu.addMenu('Themes')
        themes_menu.addAction(dark_action)
        themes_menu.addAction(light_action)
        themes_menu.addAction(fernando_action)
        themes_menu.addAction(marisol_action)
        themes_menu.addAction(boung_action)
        themes_menu.addAction(kineto_action)

        # Add actions to help_menu
        help_menu = menu_bar.addMenu('&Help')
        help_menu.addAction(help_action)
        help_menu.addAction(about_program_action)

    
    # Create TextField 
        self.text_box = QTextEdit()
        self.setCentralWidget(self.text_box)


    # Method saves file    
    def save_file(self):
        text = self.text_box.toPlainText()
        if len(text) > 0:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, type = QFileDialog.getSaveFileName(self, 'Сохранить файл', '',
            'All Files (*);; Text Files (*.txt);; Python Files (*.py)', options=options)
            if fileName:
                if type == 'Python Files (*.py)':
                    with open(f'{fileName}.py', 'w') as file:
                        file.write(text)    
                    print(f'{fileName} записан')
                    QMessageBox.about(self, 'Уведомление', 'Файл успешно сохранен')
                else:
                    with open(f'{fileName}.txt', 'w') as file:
                        file.write(text)    
                    print(f'{fileName} записан')
                    QMessageBox.about(self, 'Уведомление', 'Файл успешно сохранен')
            self.close()
        else:
            QMessageBox.about(self, 'Ошибка при сохранении файла', 'Вы пытаетесь сохранить пустой файл! Так нельзя...')


    # Method open the file
    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
        'All Files (*);; Text Files (*.txt);; Python Files (*.py)', options=options)
        if fileName:
            self.text_box.clear()
            with open(fileName, 'r') as file:
                for line in file:
                    self.text_box.append(line)
            self.statusBar().showMessage(f'Открыт {fileName}')
    

    # Method quit the program
    def close_app(self):
        if len(self.text_box.toPlainText()) > 0:
            answer = QMessageBox.question(self, 'Напоминание', 'Сохранить перед закрытием?', QMessageBox.Yes, QMessageBox.No)

            if answer == QMessageBox.Yes:
                self.save_file()
            else:
                self.close()
        else:
            self.close()


    # Support info method
    def show_support_info(self):
        message = '<h3 align=center>Вас приветствует приложение для создания заметок и текстовых файлов.</h3>\
                    <p>1. Приложение готово работать уже после запуска. Просто начните вводить нужнй текст </p>\
                     <p>2. После окончания работы вы можете нажать горячую клавишу <b>Ctrl + S</b>  для сохранения файла.</p>\
                <p>3. Чтобы открыть уже существующий файл - нажмите горячую клавишу <b>Ctrl + O</b> и выберите в файловом менеджере нужный файл</p> <hr>\
                <h4 align=center>Рекомендуем после завершения работы использовать для выхода горячую клавишу <b>Ctrl + Q</b> для выхода из программы. \
                    Таким выход будет безопаснее</h4>'

        QMessageBox.about(self, 'Руководство', message)
    

    # About program info method
    def show_about_info(self):
        message = '<div align=center> \
                        <h2> Rosya Notebook </h2>\
                        <h5> Copyrigth © Yunoshev Yaroslav</h5> \
                        <h4> Version 1.0.0. Stable. <h4> </div>'

        QMessageBox.about(self, 'О программе', message)
