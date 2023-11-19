from PyQt5.QtWidgets import QApplication
from random import choice,shuffle
app = QApplication([])

from main_window import *


class Question:
    def __init__(self,q_tex,ans,wrong1,wrong2,wrong3) :
        self.question_tex = q_tex
        self.answer = ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    ...
q1 = Question("Дім",  "house","hose","horse","mouse")
q2 = Question("Миша",  "mouse","mouth","maise","mikie")
q3 = Question("Яблуко",  "apple ","apply","ape","application")
q4 = Question("Хмара",  "cloud","clode","chaos","chome")


radio_list = [rb_answer_1, rb_answer_2, rb_answer_3, rb_answer_4 ]
questionas_list = [q1,q2,q3,q4]

def next_question():
    current_question = choice(questionas_list)
    question.setText(current_question.question_tex)
    shuffle(radio_list)
    radio_list[0].setText(current_question.answer)
    radio_list[1].setText(current_question.wrong1)
    radio_list[2].setText(current_question.wrong2)
    radio_list[3].setText(current_question.wrong3)

    correct_answer.setText(current_question.answer)

next_question()

def check_result():
    RadioGroup.setExclusive(False)
    for b in radio_list:
        if b.isChecked():
            if b.text() == correct_answer.text():
                result_text.setText("Правильно!")
            else:
                result_text.setText("Ниправельно!")
            b.setChecked(False)
    RadioGroup.setExclusive(True)
def switch_box():
    if btn_next.text() == "Відповісти":
        check_result()
        RadioGroupBox.hide()
        AnswerGroupBox.show()
        btn_next.setText("Наступне питання")

    elif btn_next.text() == "Наступне питання":
        RadioGroupBox.show()
        AnswerGroupBox.hide()
        btn_next.setText("Відповісти")
        next_question()
btn_next.clicked.connect(switch_box)



window.show()
app.exec()