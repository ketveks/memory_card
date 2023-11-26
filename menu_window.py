from PyQt5.QtWidgets import ( QWidget,
                             QLabel,QPushButton,
                             QLineEdit,
                             QVBoxLayout,QHBoxLayout
                             )
menu_window = QWidget()

ld_question = QLabel("Ввудіть питання")
le_question = QLineEdit()

ld_answer = QLabel("Ііедіть правилtьний варіант ")
le_answer = QLineEdit()

ld_wrong1 = QLabel("Ііедіть неправилtьний варіант 1")
le_wrong1 = QLineEdit()

ld_wrong2 = QLabel("Ііедіть неправилtьний варіант 3")
le_wrong2 = QLineEdit()

ld_wrong3 = QLabel("Ііедіть неправилtьний варіант 3")
le_wrong3 = QLineEdit()

btn_add = QPushButton("Додати питання")
btn_clear = QPushButton("Очистити")
btn_back =QPushButton("Назад")

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_v_line = QVBoxLayout()

menu_h_line_1.addWidget(ld_question)
menu_h_line_1.addWidget(le_question)

menu_h_line_2.addWidget(ld_answer)
menu_h_line_2.addWidget(le_answer)

menu_h_line_3.addWidget(ld_wrong1)
menu_h_line_3.addWidget(le_wrong1)

menu_h_line_4.addWidget(ld_wrong2)
menu_h_line_4.addWidget(le_wrong2)

menu_h_line_5.addWidget(ld_wrong3)
menu_h_line_5.addWidget(le_wrong3)

menu_h_line_6.addWidget(btn_add)
menu_h_line_6.addWidget(btn_clear)

menu_v_line.addLayout(menu_h_line_1)
menu_v_line.addLayout(menu_h_line_2)
menu_v_line.addLayout(menu_h_line_3)
menu_v_line.addLayout(menu_h_line_4)
menu_v_line.addLayout(menu_h_line_5)
menu_v_line.addLayout(menu_h_line_6)

menu_v_line.addWidget(btn_back)
                      
menu_window.setLayout(menu_v_line)