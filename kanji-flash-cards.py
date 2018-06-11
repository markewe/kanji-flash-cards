import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class KanjiFlashCards(QtWidgets.QMainWindow):
    def __init__(self):
        super(KanjiFlashCards, self).__init__()
        loadUi('kanji-flash-cards.ui', self)
        self.btnNext.clicked.connect(self.onBtnNextClicked)
        self.show()

    def onBtnNextClicked(self):
        self.lblKanji.setText('一')

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = KanjiFlashCards()
    sys.exit(app.exec_())

run()