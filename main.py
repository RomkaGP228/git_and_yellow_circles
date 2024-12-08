from random import randint
import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create)
        self.setGeometry(600, 600, 800, 800)
        self.setFixedSize(self.size())
        self.paint = False

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(0, 400)
            qp.drawEllipse(randint(0, 800 - r), randint(0, 600 - r), r, r)
            self.paint = False
            qp.end()

    def create(self):
        self.paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
