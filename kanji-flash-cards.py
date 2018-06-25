import sys
import random
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sqlite3

class KanjiFlashCards(QtWidgets.QMainWindow):
    prevKanjiStack = []
    
    def __init__(self):
        super(KanjiFlashCards, self).__init__()
        loadUi('kanji-flash-cards.ui', self)

        # bind events
        self.btnNext.clicked.connect(self.onBtnNextClicked)
        self.btnPrev.clicked.connect(self.onBtnPrevClicked)

        self.show()

    def onBtnNextClicked(self):
        #select random from db
        try:
            db = sqlite3.connect('kanji-flash-cards.sqlite')
            db.row_factory = sqlite3.Row
            cursor = db.cursor()
            cursor.execute('SELECT * FROM kanji ORDER BY RANDOM() LIMIT 1;')
            row = cursor.fetchone()
            self.lblKanji.setText(row['kanji'])
            self.prevKanjiStack.append(row)
            print(self.prevKanjiStack)
        except sqlite3.Error as e:
            print(e)

    def onBtnPrevClicked(self):
        if(len(self.prevKanjiStack)):
            self.prevKanjiStack.pop()
            print(self.prevKanjiStack)

        if(len(self.prevKanjiStack)):
            self.lblKanji.setText(self.prevKanjiStack[0]['Kanji'])

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = KanjiFlashCards()
    sys.exit(app.exec_())

run()