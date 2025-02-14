from ui import conjugationLevelPage, conjugationMenuPage
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import os
import database.dbDriver as database


class ConjugationMenuScreen(QMainWindow):
    def __init__(self):
        super(ConjugationMenuScreen, self).__init__()
        self.ui = conjugationMenuPage.Ui_MainWindow()
        self.ui.setupUi(self)

        # creating button groups
        self.gr1_buttons = QButtonGroup()
        self.gr2_buttons = QButtonGroup()
        self.gr3_buttons = QButtonGroup()

        # adding buttons to groups
        self.gr1_buttons.addButton(self.ui.btn_gr1_pr, 0)
        self.gr1_buttons.addButton(self.ui.btn_gr1_fu, 1)
        self.gr1_buttons.addButton(self.ui.btn_gr1_im, 2)
        self.gr1_buttons.addButton(self.ui.btn_gr1_ps, 3)
        self.gr1_buttons.addButton(self.ui.btn_gr1_pc, 4)

        self.gr2_buttons.addButton(self.ui.btn_gr2_pr, 0)
        self.gr2_buttons.addButton(self.ui.btn_gr2_fu, 1)
        self.gr2_buttons.addButton(self.ui.btn_gr2_im, 2)
        self.gr2_buttons.addButton(self.ui.btn_gr2_ps, 3)
        self.gr2_buttons.addButton(self.ui.btn_gr2_pc, 4)

        self.gr3_buttons.addButton(self.ui.btn_gr3_pr, 0)
        self.gr3_buttons.addButton(self.ui.btn_gr3_fu, 1)
        self.gr3_buttons.addButton(self.ui.btn_gr3_im, 2)
        self.gr3_buttons.addButton(self.ui.btn_gr3_ps, 3)
        self.gr3_buttons.addButton(self.ui.btn_gr3_pc, 4)


class ConjugationLevelScreen(QMainWindow):
    def __init__(self):
        super(ConjugationLevelScreen, self).__init__()
        self.ui = conjugationLevelPage.Ui_MainWindow()
        self.ui.setupUi(self)

        self.words_guess_spaces = [self.ui.word1_guess, self.ui.word2_guess,
                                   self.ui.word3_guess, self.ui.word4_guess, self.ui.word5_guess, self.ui.word6_guess]
        self.level = None


class ConjugationLevel:
    def __init__(self, temp, groupe):
        self.driver = database.JSONDriver()
        self.groupe = groupe
        self.temp = temp
        self.verb = self.get_verb(self.groupe)
        self.answer = self.driver.getConjAnswer(temp, groupe)
        self.title = self.get_title(self.groupe)
        self.question = f"conjuguer {self.verb} au {self.temp}"

    def get_verb(self, groupe):
        match groupe:
            case 0: return "acheter"
            case 1: return "finir"
            case 2: return "pouvoir"

    def get_title(self, groupe):
        match groupe:
            case 0: return "1ère groupe"
            case 1: return "2éme groupe"
            case 2: return "3éme groupe"
