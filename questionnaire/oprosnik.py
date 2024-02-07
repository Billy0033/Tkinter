import tkinter
from tkinter import *
import sys
def button_result():

    windowQuestion3 = Tk()
    windowQuestion3.title("Результаты")  # Заголовок окна
    windowQuestion3.geometry("400x300+500+200")  # Размер окна и выравнивание по центру
    canvas = tkinter.Canvas(windowQuestion3)
    canvas['bg'] = 'black'
    canvas.pack()

    poetry = "Спасибули что прошли,\n хорошего дня вам!"
    btn = Label(windowQuestion3, text=poetry, justify=CENTER, fg="#F8FF00", bg="BLACK", font="Arial 11")
    btn.place(x=125, y=100)

    btnQuit = Button(windowQuestion3, text='Выход', bg="#F8FF00", border="5px", command=lambda:sys.exit())
    btnQuit.place(x= 180, y=175)
    


def button_next_block2():
    windowQuestion1 = Tk()
    windowQuestion1.title("Опросник")  # Заголовок окна
    windowQuestion1.geometry("800x400+300+50") # Размер окна и выравнивание по центру

    questionsblock2 = ['9) Вы помогаете бездомным животным?',
        '10) Вы были в приюте для животных?', '11) У вас есть дома животное из приюта?',
        '12) Хотели бы вы быть волонтером в приюте для животных?', '13) Вам понравился опросник?]']

    answer9 = IntVar()
    answer10 = IntVar()
    answer11 = IntVar()
    answer12 = IntVar()
    answer13 = IntVar()

    answers = [answer9, answer10, answer11, answer12, answer13]
    for i in range(5):
        vopros = Label(windowQuestion1, text=questionsblock2[i], font='Arial 9')
        vopros.pack()

        yes = Radiobutton(windowQuestion1, font='Arial 9', text='Да', value=1, variable=answers[i])
        no = Radiobutton(windowQuestion1, font='Arial 9', text='Нет', value=0, variable=answers[i])

        yes.pack()
        no.pack()

    btnSend = Button(windowQuestion1, text='Отправить', bg="#F8FF00", border="5px", command=button_result)
    btnSend.place(x=365, y=352)





def button_next_block1():
    windowQuestion1 = Tk()
    windowQuestion1.title("Опросник")  # Заголовок окна
    windowQuestion1.geometry("800x625+300+50")  # Размер окна и выравнивание по центру


    '''mainframe = Frame(window)
    mainframe.pack(fill=BOTH, expand=1)
    canvas = tkinter.Canvas(mainframe)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)'''

    '''scrollbar = tkinter.Scrollbar(mainframe, orient='vertical', command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=NW)'''

    questionsblock1 = ['1) Вы любите котиков?', '2) Вы живете один?', '3) У вас есть котик?',
        '4) У вас аллергия на котиков?', '5) Вы любите собак?', '6) Вы живете один?',
        '7) У вас есть собака?', '8) У вас есть аллергия на собак?', '9) Вы помогаете бездомным животным?',
        '10) Вы были в приюте для животных?', '11) У вас есть дома животное из приюта?',
        '12) Хотели бы вы быть волонтером в приюте для животных?', '13) Вам понравился опросник?']

    answer1 = IntVar()
    answer2 = IntVar()
    answer3 = IntVar()
    answer4 = IntVar()
    answer5 = IntVar()
    answer6 = IntVar()
    answer7 = IntVar()
    answer8 = IntVar()



    answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7,
               answer8]

    for i in range(8):
        vopros = Label(windowQuestion1, text=questionsblock1[i], font='Arial 9')
        vopros.pack()

        yes = Radiobutton(windowQuestion1, font='Arial 9', text='Да', value=1, variable=answers[i])
        no = Radiobutton(windowQuestion1, font='Arial 9', text='Нет', value=0, variable=answers[i])

        yes.pack()
        no.pack()

    btnNext = Button(windowQuestion1, text='Отправить', bg="#F8FF00", border="5px", command=button_next_block2)
    btnNext.place(x=360, y=575)


#Функция кнопки "Начать"
def button_start():
    #Создали второе окно для вопросов
    windowQuestion = Tk()
    windowQuestion.title("Опросник")  # Заголовок окна
    windowQuestion.geometry("400x300+500+200") #Размер окна и выравнивание по центру
    canvas = tkinter.Canvas(windowQuestion)
    canvas['bg'] = 'black'


    name = Label(windowQuestion, text='Имя', font="Arial 11", bg='black', fg='#F8FF00')
    name.pack()
    poleName = Entry(windowQuestion, width=25, bg='black', fg='#F8FF00')
    poleName.pack()
    surname = Label(windowQuestion, text="Фамилия", font="Arial 11", bg='black', fg='#F8FF00')
    surname.pack()
    poleSurname = Entry(windowQuestion, width=25, bg='black', fg='#F8FF00')
    poleSurname.pack()

    btnNext = Button(windowQuestion, text='Далее', bg ="#F8FF00", border="5px", command=button_next_block1)
    btnNext.place(x=175, y=225)
    #btnBack = Button(windowQuestion, text='Назад', bg ="#F8FF00", border="5px", command=button_back_mainmenu)
    #btnBack.place(x=75, y = 225)

    #questions = []
    canvas.pack()
    window.destroy()


    '''canvasTwo = tkinter.Canvas()
    canvasTwo['bg'] = 'black'
    canvasTwo.pack()'''

#кнопка выхода из опросника
def button_exit():
   window.destroy()


# Создаем начальное окно (Приветствие!)

window = Tk()   #Создание графического окна
window.title("Опросник")   #Заголовок окна
window.geometry("400x300+500+200") #Размер окна и выравнивание по центру
#window.entry(, bg="#000000")
canvas = tkinter.Canvas()
canvas['bg'] = 'black'

btnStart = Button(window, text="Начать", bg ="#F8FF00", border="5px", command=button_start)
btnExit = Button(window, text="Выход", bg = "#F8FF00", border="5px", command=button_exit)
btnStart.place(x = 175, y = 175) # мы сами задаем парметры X и Y на оси координат
btnExit.place(x = 175, y =225) # мы сами задаем парметры X и Y на оси координат

poetry = "Приветули!\n Сейчас вы пройдёте опросник\n связанный с вашей любовью к животным"
btn = Label(text=poetry, justify=CENTER, fg="#F8FF00", bg="BLACK", font="Arial 11")
btn.place(x = 55, y = 50)



canvas.pack() #чтобы заработал черный фон
window.mainloop() #запуск нашего окна