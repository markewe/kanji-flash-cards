import sys
import random
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class Kanji():
    value = ''
    onyomi = ''
    kunyomi = ''

    next = None
    prev = None

    def __init__(self, val, onyomi, kunyomi):
        self.value = val
        self.onyomi = onyomi
        self.kunyomi = kunyomi

class KanjiFlashCards(QtWidgets.QMainWindow):
    testKanji = {
        '一': 'ichi'
        ,'二': 'ni'
        ,'三': 'san'
        ,'四': 'shi'
        ,'五': 'go'
        ,'六': 'roku'
        ,'七': 'nana'
        ,'八': 'hachi'
        ,'九': 'kyuu'
        ,'十': 'jyuu'
    }
    kanjiPtr = None
    
    def __init__(self):
        super(KanjiFlashCards, self).__init__()
        loadUi('kanji-flash-cards.ui', self)

        #shuffle kanji array and create linked list for prev/next traversal
        randomKeys = list(self.testKanji.keys())
        random.shuffle(randomKeys)
        nextKanji = None
        prevKanji = Kanji(randomKeys[0], '', self.testKanji[randomKeys[0]])
        randomKeys.pop(0)
        self.kanjiPtr = prevKanji
        
        for kanji in randomKeys:
            nextKanji = Kanji(kanji, '', self.testKanji[kanji])
            nextKanji.prev = prevKanji
            prevKanji.next = nextKanji
            prevKanji = nextKanji

        # bind events
        self.btnNext.clicked.connect(self.onBtnNextClicked)
        self.btnPrev.clicked.connect(self.onBtnPrevClicked)

        self.show()

    def onBtnNextClicked(self):
        self.lblKanji.setText(self.kanjiPtr.value)
        
        if(self.kanjiPtr.next is not None):
            self.kanjiPtr = self.kanjiPtr.next

    def onBtnPrevClicked(self):
        self.lblKanji.setText(self.kanjiPtr.value)

        if(self.kanjiPtr.prev is not None):
            self.kanjiPtr = self.kanjiPtr.prev

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = KanjiFlashCards()
    sys.exit(app.exec_())

run()