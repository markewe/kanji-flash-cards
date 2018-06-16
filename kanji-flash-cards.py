import sys
import random
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class Kanji():
    value = ''
    next = None
    prev = None

    def __init__(self, val):
        self.value = val

class KanjiFlashCards(QtWidgets.QMainWindow):
    testKanji = ['一','二','三','四','五','六','七','八','九','十']
    kanjiPtr = None
    
    def __init__(self):
        super(KanjiFlashCards, self).__init__()
        loadUi('kanji-flash-cards.ui', self)

        #shuffle kanji array and create linked list for prev/next traversal
        random.shuffle(self.testKanji)
        nextKanji = None
        prevKanji = Kanji(self.testKanji[0])
        self.testKanji.pop(0)
        self.kanjiPtr = prevKanji
        
        for kanji in self.testKanji:
            nextKanji = Kanji(kanji)
            nextKanji.prev = prevKanji
            prevKanji.next = nextKanji
            prevKanji = nextKanji

        # bind events
        self.btnNext.clicked.connect(self.onBtnNextClicked)
        self.btnPrev.clicked.connect(self.onBtnPrevClicked)
        
        # show first Kanji
        self.onBtnNextClicked()
        self.onBtnPrevClicked()

        self.show()

    def onBtnNextClicked(self):
        if(self.kanjiPtr.next is not None):
            self.lblKanji.setText(self.kanjiPtr.value)
            self.kanjiPtr = self.kanjiPtr.next

    def onBtnPrevClicked(self):
        if(self.kanjiPtr.prev is not None):
            self.lblKanji.setText(self.kanjiPtr.value)
            self.kanjiPtr = self.kanjiPtr.prev

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = KanjiFlashCards()
    sys.exit(app.exec_())

run()