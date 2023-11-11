from PyQt5.QtWidgets import (
    QWidget,QHBoxLayout,QVBoxLayout,
    QLabel,QPushButton,QRadioButton,
    QButtonGroup,QGroupBox
)

window = QWidget()

win_width,win_heigh = 700, 400
window.resize(win_width, win_heigh)
window.setWindowTitle('Memory Card')
question = QLabel()
btn_menu = QPushButton("Меню")
btn_next = QPushButton("Відповісти")


rb_answer_1 = QRadioButton()
rb_answer_2 = QRadioButton()
rb_answer_3 = QRadioButton()
rb_answer_4 = QRadioButton()




RadionGroup = QButtonGroup()

RadionGroup.addButton(rb_answer_1)
RadionGroup.addButton(rb_answer_2)
RadionGroup.addButton(rb_answer_3)
RadionGroup.addButton(rb_answer_4)


RadionGroupBox = QGroupBox("Варіанти відповідей")

box_h_line =QHBoxLayout()
box_v_line1 =QVBoxLayout()
box_v_line2 =QVBoxLayout()


box_v_line1.addWidget(rb_answer_1)
box_v_line1.addWidget(rb_answer_2)
box_v_line2.addWidget(rb_answer_3)
box_v_line2.addWidget(rb_answer_4)


box_h_line.addLayout(box_v_line1)
box_h_line.addLayout(box_v_line2)




RadionGroupBox.setLayout(box_h_line)


main_v_line = QVBoxLayout()

main_v_line.addWidget(question)
main_v_line.addWidget(RadionGroupBox)
main_v_line.addWidget(btn_next)



window.setLayout(main_v_line)





window.show()