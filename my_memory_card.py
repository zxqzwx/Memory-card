
from PyQt5.QtCore import Qt
from random import shuffle, randint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QPushButton, QButtonGroup

class Question():
    def __init__(self,question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2    
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В каком году началась Великая Отечественная война?','в 1941','в 1951','в 1931','в 1942'))
question_list.append(Question('Какая из сестёр в романе Александра Сергеевича Пушкина «Евгений Онегин» была старше: Ольга, Татьяна, Наташа, Василиса','Татьяна','Ольга','Наташа','Василиса'))
question_list.append(Question('Как назывался первый музей России, учреждённый Петром Великим?','Кунтскамера','Канцелярия','Верховный','Центральный'))
question_list.append(Question('Какой класс животных самый многочисленный и распространённый на Земле?','насекомые','животные','змеи','грибы'))
question_list.append(Question('Какие бытовые предметы китайцы дарят молодожёнам, чтобы те были вместе и всегда помогали друг другу?','Куайцзы','вилку','ложку','палочки'))
question_list.append(Question('Сколько цветов в радуге','7','6','8','5'))
question_list.append(Question('Сколько колец на ауди','4','5','3','2'))
question_list.append(Question('В каком году распался СССР','в 1991','в 1981','в 1992','в 1995'))
question_list.append(Question('Какую максимальную скорость развивает гепард','130 км/ч','150км/ч','70км/ч','160км/ч'))
question_list.append(Question('Сколько лет длилась северная война','21 год','5 лет','30 лет','14 лет'))
question_list.append(Question('Какая самая ядовитая рыба в мире','рыба-камень','фуга','сельдь','щука'))

app = QApplication([])
main_win = QWidget()
main_win.resize(450, 300)
main_win.setWindowTitle('Memory Card')

btn_OK = QPushButton('Ответить')
question = QLabel('В каком году началась Великая Отечественная война?')

RadioGroupBox = QGroupBox('Варианты ответов')
btn1 = QRadioButton('В 1940')
btn2= QRadioButton('В 1945')
btn3 = QRadioButton('В 1841')
btn4 = QRadioButton('В 1941')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans4 = QHBoxLayout()

layout_ans2.addWidget(btn1)
layout_ans2.addWidget(btn2)
layout_ans3.addWidget(btn3)
layout_ans3.addWidget(btn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_result = QLabel('Прав ты или нет')
lb_correct = QLabel('Ответ будет тут')
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lb_result, alignment =(Qt.AlignLeft | Qt.AlignTop))
layout_ans4.addWidget(lb_correct, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_ans4)

layout_line = QVBoxLayout()
layout_line.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line.addWidget(btn_OK, stretch=2)
main_win.setLayout(layout_line)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Продолжить')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn1, btn2, btn3, btn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Верно!')
        main_win.score += 1
        print('Статистика:\nВсего вопросов - ', main_win.total, '\nКоличество правильных ответов - ',main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    main_win.total += 1
    print('Статистика\nВсего вопросов - ', main_win.total, '\nКоличество правильных ответов - ',main_win.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


main_win.total = 0
main_win.score = 0
btn_OK.clicked.connect(click_OK)
next_question()



main_win.show()
app.exec_()

