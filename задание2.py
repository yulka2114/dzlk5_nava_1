import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 630, 640)
        self.setWindowTitle("Приветствие")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        hello_label = QLabel(self)
        hello_label.setText("Здравствуйте")
        hello_label.move(250, 23)

        image = r"C:\Users\valer\OneDrive\Рабочий стол\1.jpg"
        try:
            with open(image):
                world_label = QLabel(self)
                pixmap = QPixmap(image)
                world_label.setPixmap(pixmap)
                world_label.move(0, 40)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")


class MainWindo(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(550, 100, 1000, 1000)  
        self.setWindowTitle("Профиль пользователя")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = r"C:\Users\valer\OneDrive\Рабочий стол\юля.jpg"
        try:
            with open(images):
                world_label = QLabel(self)
                pixmap = QPixmap(images)
                world_label.setPixmap(pixmap)
                world_label.move(300, 150)
        except FileNotFoundError as error:
            print(f"Image not found.\nError: {error}")
    
    def setUpMainWindow(self):
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText("Навричевская Юлия")
        user_label.setFont(QFont("Montserrat", 28))
        user_label.move(300, 60)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Montserrat", 24))
        bio_label.move(40, 600)

        about_label = QLabel(self)
        about_label.setText("Студентка 2 курса МАИ, М3О-237БВ-24")
        about_label.setWordWrap(True)
        about_label.setFont(QFont("Montserrat", 18))
        about_label.move(40, 635)

        skills_label = QLabel(self)
        skills_label.setText("Навыки")
        skills_label.setFont(QFont("Montserrat", 24))
        skills_label.move(40, 700)

        languages_label = QLabel(self)
        languages_label.setText("работа с детьми")
        languages_label.setFont(QFont("Montserrat", 18))
        languages_label.move(40, 725)

        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Montserrat", 24))
        experience_label.move(40, 755)

        developer_label = QLabel(self)
        developer_label.setText("вожатая")
        developer_label.setFont(QFont("Montserrat", 18))
        developer_label.move(40, 780)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("сентябрь-октябрь 25")
        dev_dates_label.setFont(QFont("Montserrat", 18))
        dev_dates_label.move(40, 800)

        driver_label = QLabel(self)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window1 = MainWindo()
    sys.exit(app.exec())