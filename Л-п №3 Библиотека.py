from  tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview

root=Tk()
root.title('Библиотека')
root.geometry("735x440")
root.resizable(width=False,height=False)
root.config(bg='#e1dee6')

pixelVirtual=PhotoImage(width=1,height=1)

F1=LabelFrame(root,height=52,width=712,bg='#e1dee6')
F1.place(x=8,y=8)

p1=PhotoImage(file='1.png')
p2=PhotoImage(file='2.png')
p3=PhotoImage(file='3.png')
p4=PhotoImage(file='4.png')
p5=PhotoImage(file='5.png')
p6=PhotoImage(file='6.png')
b1=PhotoImage(file='b1.png')
b2=PhotoImage(file='b2.png')
b3=PhotoImage(file='b3.png')
b4=PhotoImage(file='b4.png')
b5=PhotoImage(file='b5.png')

BAdd=Button(F1,bg='#e1dee6',text='Добавить книгу',image=p1,compound=LEFT,width=128,height=27).grid(row=0,column=0,padx=3,pady=3)
BAdd=Button(F1,bg='#e1dee6',text='Редактировать',image=p2,compound=LEFT,width=128,height=27).grid(row=0,column=1,padx=3,pady=3)
BAdd=Button(F1,bg='#e1dee6',text='Удалить книгу',image=p3,compound=LEFT,width=128,height=27).grid(row=0,column=2,padx=3,pady=3)
BAdd=Button(F1,bg='#e1dee6',text='Все записи',image=p4,compound=LEFT,width=128,height=27).grid(row=0,column=3,padx=3,pady=3)
BAdd=Button(F1,bg='#e1dee6',text='Язык',image=p5,compound=LEFT,width=128,height=27).grid(row=0,column=4,padx=3,pady=3)

"""
BAdd=Button(F1,image=b1)
BAdd.place(x=6,y=6)
BRed=Button(F1,image=b2)
BRed.place(x=150,y=6)
BDel=Button(F1,image=b3)
BDel.place(x=294,y=6)
BAll=Button(F1,image=b4)
BAll.place(x=435,y=6)
BLan=Button(F1,image=b5)
BLan.place(x=571,y=6)
"""
"""
BAdd=Button(F1, text='Добавить книгу',image=pixelVirtual,width=130,height=27,fg='black',font='arial 12',compound='c');
BAdd.place(x=6,y=6)
BRed=Button(F1, text='Редактировать',image=pixelVirtual,width=130,height=27,fg='black',font='arial 12',compound='c')
BRed.place(x=150,y=6)
BDel=Button(F1, text='Удалить книгу',image=pixelVirtual,width=130,height=27,fg='black',font='arial 12',compound='c')
BDel.place(x=294,y=6)
BAll=Button(F1, text='Все записи',image=pixelVirtual,width=124,height=27,fg='black',font='arial 12',compound='c')
BAll.place(x=435,y=6)
BLan=Button(F1, text='Язык',image=pixelVirtual,width=124,height=27,fg='black',font='arial 12',compound='c')
BLan.place(x=571,y=6)
"""

F2=LabelFrame(root,width=712,height=59,text='Параметры поиска',bg='#e1dee6',fg='black',font='arial 12')
F2.place(x=8,y=68)
L1=Label(F2,text='Поле поиска',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L1.place(x=15,y=6)
List=Combobox(F2)
List.place(x=95,y=5, width=145,height=21)
List['values']=('Автор','Название')
List.current(0)
L2=Label(F2,text='Искомое значение',width=100,height=9,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L2.place(x=248,y=6)
E1=Entry(F2)
E1.place(x=356,y=5,width=165,heigh=21)
BSearch=Button(F2,width=169,height=33,bg='#e1dee6',image=p6,compound='c')
BSearch.place(x=530,y=-6)

L3=Label(root,text='Расположение',width=80,height=9,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L3.place(x=8,y=147)

table1=Treeview()
table1.place(x=8,y=165)
table1['show']='headings'
table1['columns']=('1','2','3')
table1.column('1',width=65,minwidth=50)
table1.heading('1',text='Комната')
table1.column('2',width=65,minwidth=50)
table1.heading('2',text='Шкаф')
table1.column('3',width=65,minwidth=50)
table1.heading('3',text='Полка')
table1.insert("","end",values=(3,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(2,1,1))
table1.insert("","end",values=(4,1,1))

Sc1=Scrollbar(root,bg='white',command=table1.yview)
Sc1.place(x=206,y=165,height=226)
table1.config(yscrollcommand=Sc1.set)

L3=Label(root,text='Книги',width=29,height=9,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L3.place(x=230,y=147)

table2=Treeview()
table2.place(x=230,y=165,width=470)
table2['show']='headings'
table2['columns']=('1','2','3','4','5')
table2.column('1',width=125,minwidth=125)
table2.heading('1',text='Название')
table2.column('2',width=95,minwidth=95)
table2.heading('2',text='Автор')
table2.column('3',width=95,minwidth=95)
table2.heading('3',text='Жанр')
table2.column('4',width=85,minwidth=76)
table2.heading('4',text='Дата издания')
table2.column('5',width=80,minwidth=60)
table2.heading('5',text='Наличие')

table2.insert("","end", values=('Белая перчатка','Рид Майн','Приключения','1982','Нет'))
table2.insert("","end", values=('Как закалялалсь сталь','Николай Островский','Роман','1934','Да'))
table2.insert("","end", values=('Молодая гвардия','А.А.Фадеев','Роман','1946','Да'))
table2.insert("","end", values=('Понедельник начинается в субботу','Б.Н.Стругацкий','Повесть','1965','Да'))
table2.insert("","end", values=('Война и мир','Л.Н.Толстой','Роман','1867','Да'))
table2.insert("","end", values=('Преступление и наказание','Ф.М. Достоевский','Роман','1866','Да'))
table2.insert("","end", values=('Идиот','Ф.М.Достоевский','Роман','1869','Да'))
table2.insert("","end", values=('Евгений Онегин','А.С.Пушкин','Роман','1833','Да'))
table2.insert("","end", values=('Мёртвые души','Н.В.Гоголь','Поэма','1842','Нет'))
table2.insert("","end", values=('Мастер и Маргарита','М.А.Булгаков','Роман','1966','Да'))
table2.insert("","end", values=('Собачье сердце','М.А.Булгаков','Повесть','1968','Да'))
table2.insert("","end", values=('Сотников','В.В.Быков','Повесть','1970','Нет'))

Sc2=Scrollbar(root,bg='white',command=table2.yview)
Sc2.place(x=701,y=166,height=226)
table2.config(yscrollcommand=Sc2.set)


root.mainloop()


