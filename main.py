from random import randint
import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.create)
        self.setGeometry(600, 600, 800, 800)
        self.setFixedSize(self.size())
        self.paint = False

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
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
