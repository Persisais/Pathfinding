#Калюжный Максим ИТ-11
#Л-п №4 Творческое задание
from  tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
global Shelf,Bookcase,Room,NumberShelf,NumberBookcase,AllEntriesPressed,Language
Shelf=3;Bookcase=1;Room=1;NumberShelf=3;NumberBookcase=1;AllEntriesPressed=0;Language='ru-RU'

root=Tk()
root.title('Библиотека')
root.geometry("735x440")
root.resizable(width=False,height=False)
root.config(bg='#e1dee6')

def AddBook():
    Window1=Toplevel(root)
    Window1.geometry('640x80')
    Window1.config(bg='#e1dee6')
    Window1.resizable(width=False,height=False)
    Window1.title('Добавление книги')
    Window1.grab_set()
    Lbl1=Label(Window1,text='Название',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
    Lbl1.place(x=55,y=0)
    Lbl2=Label(Window1,text='Автор',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
    Lbl2.place(x=220,y=0)
    Lbl3=Label(Window1,text='Жанр',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
    Lbl3.place(x=325,y=0)
    Lbl4=Label(Window1,text='Дата издания',width=110,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
    Lbl4.place(x=400,y=0)
    Lbl5=Label(Window1,text='Наличие',width=110,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
    Lbl5.place(x=520,y=0)
    Name=Entry(Window1,width=30,font='Times 10')
    Name.place(x=0,y=20)
    Author=Entry(Window1,width=20,font='Times 10')
    Author.place(x=190,y=20)
    Genre=Entry(Window1,width=13,font='Times 10')
    Genre.place(x=320,y=20)
    Date=Entry(Window1,width=4,font='Times 10')
    Date.place(x=440,y=20)
    Availability=Combobox(Window1,font='Times 10',state='readonly',width=3,values=['Да', 'Нет'])
    Availability.place(x=555,y=20)
    if Language=='ru-RU':
        Window1.title('Добавление книги')
        Lbl1.config(text='Название')
        Lbl2.config(text='Автор')
        Lbl3.config(text='Жанр')
        Lbl4.config(text='Дата издания')
        Lbl5.config(text='Наличие')
        Availability.config(values=['Да','Нет'])
    elif Language=='en-GB':
        Window1.title('Adding a book')
        Lbl1.config(text='Title')
        Lbl2.config(text='Author')
        Lbl3.config(text='Genre')
        Lbl4.config(text='Date of publication')
        Lbl5.config(text='Availability')
        Availability.config(values=['Yes','No'])
    elif Language=='de-DE':
        Window1.title('Hinzufügen einer Arbeitsmappe')
        Lbl1.config(text='Titel')
        Lbl2.config(text='Der Autor')
        Lbl3.config(text='Das Genre')
        Lbl4.config(text='Datum der Ausgabe')
        Lbl5.config(text='Das Vorhandensein')
        Availability.config(values=['Ja','Nein'])
    def AddBookButton():
        global Shelf,Bookcase,Room,NumberShelf,NumberBookcas
        if Shelf==5:
            Bookcase+=1
            Shelf=1
        elif Bookcase==5:
            Room+=1
            Bookcase=1
        elif NumberShelf==5:
            Shelf+=1
            NumberShelf=1
        elif NumberShelf<5:
            NumberShelf+=1
        elif NumberBookcase<5:
            NumberBookcase+=1
        Tableinformation.append([Name.get(),Author.get(),Genre.get(),Date.get(),Availability.get()])
        table1.insert("","end",values=(Room,Bookcase,Shelf))
        table2.insert("","end",values=(Tableinformation[len(Tableinformation)-1]))
        Window1.destroy()
    Button1=Button(Window1,bg='#e1dee6',text='Добавить книгу',font='Times 12',command=AddBookButton)
    Button1.place(x=265,y=45)
    if Language=='ru-RU':
        Button1.config(text='Добавить книгу')
    elif Language=='en-GB':
        Button1.config(text='Add a book')
    elif Language=='de-DE':
        Button1.config(text='Buch hinzufügen')
    
def EditBook():
    try:
        Window1=Toplevel(root)
        Window1.geometry('640x80')
        Window1.config(bg='#e1dee6')
        Window1.resizable(width=False,height=False)
        Window1.title('Изменение книги')
        Window1.grab_set()
        Lbl1=Label(Window1,text='Название',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
        Lbl1.place(x=55,y=0)
        Lbl2=Label(Window1,text='Автор',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
        Lbl2.place(x=220,y=0)
        Lbl3=Label(Window1,text='Жанр',width=65,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
        Lbl3.place(x=325,y=0)
        Lbl4=Label(Window1,text='Дата издания',width=110,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
        Lbl4.place(x=400,y=0)
        Lbl5=Label(Window1,text='Наличие',width=110,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
        Lbl5.place(x=520,y=0)
        Nom=table2.item(table2.selection())["values"]
        Name=Entry(Window1,width=30,font='Times 10')
        Name.place(x=0,y=20)
        Name.insert(END,Nom[0])
        Author=Entry(Window1,width=20,font='Times 10')
        Author.insert(END,Nom[1])
        Author.place(x=190,y=20)
        Genre=Entry(Window1,width=13,font='Times 10')
        Genre.place(x=320,y=20)
        Genre.insert(END,Nom[2])
        Date=Entry(Window1,width=4,font='Times 10')
        Date.place(x=440,y=20)
        Date.insert(END,Nom[3])
        Availability=Combobox(Window1,font='Times 10',state='readonly',width=3,values=['Да', 'Нет'])
        Availability.place(x=555,y=20)
        Availability.value=Nom[4]
        def EditBookButton():
            currInd=table2.focus()
            Index=table2.index(currInd)
            table2.delete(currInd)
            Tableinformation.pop(Index)
            Tableinformation.insert(Index,[Name.get(),Author.get(),Genre.get(),Date.get(),Availability.get()])
            table2.insert("",Index,values=(Tableinformation[Index]))
            Window1.destroy()  
        Button1=Button(Window1,bg='#e1dee6',text='Изменить книгу',font='Times 12',command=EditBookButton)
        Button1.place(x=205,y=45)
        if Language=='ru-RU':
            Window1.title('Изменение книги')
            Lbl1.config(text='Название')
            Lbl2.config(text='Автор')
            Lbl3.config(text='Жанр')
            Lbl4.config(text='Дата издания')
            Lbl5.config(text='Наличие')
            Availability.config(values=['Да','Нет'])
            Button1.config(text='Изменить книгу')
        elif Language=='en-GB':
            Window1.title('Changing a book')
            Lbl1.config(text='Title')
            Lbl2.config(text='Author')
            Lbl3.config(text='Genre')
            Lbl4.config(text='Date of publication')
            Lbl5.config(text='Availability')
            Availability.config(values=['Yes','No'])
            Button1.config(text='Edit a book')
        elif Language=='de-DE':
            Window1.title('Arbeitsmappe ändern')
            Lbl1.config(text='Titel')
            Lbl2.config(text='Der Autor')
            Lbl3.config(text='Das Genre')
            Lbl4.config(text='Datum der Ausgabe')
            Lbl5.config(text='Das Vorhandensein')
            Availability.config(values=['Ja','Nein'])
            Button1.config(text='Arbeitsmappe Bearbeiten')
        
    except:
        Window1.destroy()
        if Language=='ru-RU':
            messagebox.showerror('Ошибка!','Выделите нужную книгу')
        elif Language=='en-GB':
            messagebox.showerror('Error!','Select the desired book')
        elif Language=='de-DE':
            messagebox.showerror('Fehler!','Wählen Sie die gewünschte Arbeitsmappe aus')
        
def DeleteBook():
    global EditBookPressed
    Window2=Toplevel(root)
    Window2.geometry('250x60')
    Window2.config(bg='#e1dee6')
    Window2.resizable(width=False,height=False)
    Window2.title('Подтвердите удаление книги')
    Window2.grab_set()
    Lbl1=Label(Window2,text='Вы действительно хотите удалить книгу?',width=250,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
    Lbl1.place(x=0,y=0)
    def DeleteBookButton():
        try:
            Nom=table2.focus()
            Index=table2.index(Nom)
            table2.delete(Nom)
            Tableinformation.pop(Index)
            if AllEntriesPressed==0:
                table1.delete('I00'+str(Index+1))
            elif AllEntriesPressed==1:
                table1.delete(Nom)
            Window2.destroy()
        except:
            if Language=='ru-RU':
                messagebox.showerror('Ошибка!','Выделите нужную книгу')
            elif Language=='en-GB':
                messagebox.showerror('Error!','Select the desired book')
            elif Language=='de-DE':
                messagebox.showerror('Fehler!','Wählen Sie die gewünschte Arbeitsmappe aus')
            Window2.destroy()
    def NotDeleteBookButton():
        Window2.destroy()
    Button1=Button(Window2,bg='#e1dee6',text='Да',font='Times 12',command=DeleteBookButton)
    Button1.place(x=40,y=20)
    Button2=Button(Window2,bg='#e1dee6',text='Нет',font='Times 12',command=NotDeleteBookButton)
    Button2.place(x=160,y=20)
    if Language=='ru-RU':
        Window2.title('Подтвердите удаление книги')
        Lbl1.config(text='Вы действительно хотите удалить книгу?')
        Button1.config(text='Да')
        Button2.config(text='Нет')
    elif Language=='en-GB':
        Window2.title('Confirm the deletion of the book')
        Lbl1.config(text='Do you really want to delete the book?')
        Button1.config(text='Yes')
        Button2.config(text='No')
    elif Language=='de-DE':
        Window2.title('Bestätigen Sie das löschen der Arbeitsmappe')
        Lbl1.config(text='Möchten Sie das Buch wirklich löschen?')
        Button1.config(text='Ja')
        Button2.config(text='Nein')
        
def ChooseLanguage():
    global Language
    Window3=Toplevel(root)
    Window3.geometry('260x50')
    Window3.config(bg='#3d4a5b')
    Window3.iconphoto(True,PhotoImage(file="Logo.png"))
    Window3.resizable(width=False,height=False)
    Window3.title('Выбор языка')
    Window3.grab_set()
    Lbl1=Label(Window3,text='Выберите язык',width=150,height=8,fg='white',bg='#3d4a5b',font='century 12',image=pixelVirtual,compound='c')
    Lbl1.place(x=0,y=0)
    if Language=='ru-RU':
        Window3.title('Выбор языка')
        Lbl1.configure(text='Выберите язык')
    elif Language=='en-GB':
        Window3.title('Language selection')
        Lbl1.configure(text='Select a language')
    elif Language=='de-DE':
        Window3.title('Sprache auswählen')
        Lbl1.configure(text='Sprache auswählen')
    List1=Combobox(Window3,state='readonly')
    List1.place(x=0,y=20, width=145,height=21)
    List1['values']=('Русский','English','Deutsch')
    List1.current(0)
    def LanguageChosen():
        global Language
        if List1.get()=='Русский':
            Language='ru-RU'
            BAdd=Button(F1,bg='#e1dee6',text='Добавить книгу',image=p1,compound=LEFT,width=128,height=27,command=AddBook).grid(row=0,column=0,padx=3,pady=3)
            BRed=Button(F1,bg='#e1dee6',text='Редактировать',image=p2,compound=LEFT,width=128,height=27,command=EditBook).grid(row=0,column=1,padx=3,pady=3)
            BDel=Button(F1,bg='#e1dee6',text='Удалить книгу',image=p3,compound=LEFT,width=128,height=27,command=DeleteBook).grid(row=0,column=2,padx=3,pady=3)
            BAll=Button(F1,bg='#e1dee6',text='Все записи',image=p4,compound=LEFT,width=128,height=27,command=AllEntries).grid(row=0,column=3,padx=3,pady=3)
            BLan=Button(F1,bg='#e1dee6',text='Язык',image=p5,compound=LEFT,width=128,height=27,command=ChooseLanguage).grid(row=0,column=4,padx=3,pady=3)
            L1.configure(text='Поле поиска')
            List['values']=('Название','Автор','Жанр','Дата издания','Наличие')
            L2.configure(text='Искомое значение')
            BSearch.configure(image=p6)
            L3.configure(text='Расположение')
            L4.configure(text='Книги')
            table1.heading('1',text='Комната')
            table1.heading('2',text='Шкаф')
            table1.heading('3',text='Полка')
            table2.heading('1',text='Название')
            table2.heading('2',text='Автор')
            table2.heading('3',text='Жанр')
            table2.heading('4',text='Дата издания')
            table2.heading('5',text='Наличие')
        elif List1.get()=='English':
            Language='en-GB'
            BAdd=Button(F1,bg='#e1dee6',text='Add a book',image=p1,compound=LEFT,width=128,height=27,command=AddBook).grid(row=0,column=0,padx=3,pady=3)
            BRed=Button(F1,bg='#e1dee6',text='Edit',image=p2,compound=LEFT,width=128,height=27,command=EditBook).grid(row=0,column=1,padx=3,pady=3)
            BDel=Button(F1,bg='#e1dee6',text='Delete a book',image=p3,compound=LEFT,width=128,height=27,command=DeleteBook).grid(row=0,column=2,padx=3,pady=3)
            BAll=Button(F1,bg='#e1dee6',text='All entries',image=p4,compound=LEFT,width=128,height=27,command=AllEntries).grid(row=0,column=3,padx=3,pady=3)
            BLan=Button(F1,bg='#e1dee6',text='Language',image=p5,compound=LEFT,width=128,height=27,command=ChooseLanguage).grid(row=0,column=4,padx=3,pady=3)
            L1.configure(text='The search box')
            List['values']=('Title','Author','Genre','Date of publication','Availability')
            L2.configure(text='The desired value')
            BSearch.configure(image=p6en)
            L3.configure(text='Location')
            L4.configure(text='Books')
            table1.heading('1',text='Room')
            table1.heading('2',text='Bookcase')
            table1.heading('3',text='Shelf')
            table2.heading('1',text='Title')
            table2.heading('2',text='Author')
            table2.heading('3',text='Genre')
            table2.heading('4',text='Date of publication')
            table2.heading('5',text='Availability')
        elif List1.get()=='Deutsch':
            Language='de-DE'
            BAdd=Button(F1,bg='#e1dee6',text='Buch hinzufügen',image=p1,compound=LEFT,width=128,height=27,command=AddBook).grid(row=0,column=0,padx=3,pady=3)
            BRed=Button(F1,bg='#e1dee6',text='Redigieren',image=p2,compound=LEFT,width=128,height=27,command=EditBook).grid(row=0,column=1,padx=3,pady=3)
            BDel=Button(F1,bg='#e1dee6',text='Arbeitsmappe löschen',image=p3,compound=LEFT,width=128,height=27,command=DeleteBook).grid(row=0,column=2,padx=3,pady=3)
            BAll=Button(F1,bg='#e1dee6',text='Alle Einträge',image=p4,compound=LEFT,width=128,height=27,command=AllEntries).grid(row=0,column=3,padx=3,pady=3)
            BLan=Button(F1,bg='#e1dee6',text='Sprache',image=p5,compound=LEFT,width=128,height=27,command=ChooseLanguage).grid(row=0,column=4,padx=3,pady=3)
            L1.configure(text='Suchfeld')
            List['values']=('Titel','Der Autor','Das Genre','Datum der Ausgabe','Das Vorhandensein')
            L2.configure(text='Suchwert')
            BSearch.configure(image=p6de)
            L3.configure(text='Lage')
            L4.configure(text='Die Bücher')
            table1.heading('1',text='Das Zimmer')
            table1.heading('2',text='Schrank')
            table1.heading('3',text='Regal')
            table2.heading('1',text='Titel')
            table2.heading('2',text='Der Autor')
            table2.heading('3',text='Das Genre')
            table2.heading('4',text='Datum der Ausgabe')
            table2.heading('5',text='Das Vorhandensein') 
        Window3.destroy()
    ButtonLanguage=Button(Window3,bg='#313b47',text='Выбрать',fg='white',font='century 12',command=LanguageChosen)
    ButtonLanguage.place(x=150,y=20,height=22)
    if Language=='ru-RU':
        ButtonLanguage.config(text='Выбрать')
    elif Language=='en-GB':
        ButtonLanguage.config(text='Select')
    elif Language=='de-DE':
        ButtonLanguage.config(text='Wählen')

def AllEntries():
    global Shelf,Bookcase,Room,NumberShelf,NumberBookcase,AllEntriesPressed
    AllEntriesPressed=1
    Shelf=1;Bookcase=1;Room=1;NumberShelf=0;NumberBookcase=1
    table2.delete(*table2.get_children())
    table1.delete(*table1.get_children())
    for i in range (0,len(Tableinformation)):
        table2.insert("","end", values=(Tableinformation[i]))
        if Shelf==5:
            Bookcase+=1
            Shelf=1
        elif Bookcase==5:
            Room+=1
            Bookcase=1
        elif NumberShelf==5:
            Shelf+=1
            NumberShelf=1
        elif NumberShelf<5:
            NumberShelf+=1
        elif NumberBookcase<5:
            NumberBookcase+=1
        table1.insert("","end",values=(Room,Bookcase,Shelf))
        
def Search():
    Shelf=1;Bookcase=1;Room=1;NumberShelf=0;NumberBookcase=1
    Value=E1.get()
    if (List.get()=='Название')or(List.get()=='Title')or(List.get()=='Titel'):
        Value2=0
    elif (List.get()=='Автор')or(List.get()=='Author')or(List.get()=='Der Autor'):
        Value2=1
    elif (List.get()=='Жанр')or(List.get()=='Genre')or(List.get()=='Das Genre'):
        Value2=2
    elif (List.get()=='Дата издания')or(List.get()=='Date of publication')or(List.get()=='Datum der Ausgabe'):
        Value2=3
    elif (List.get()=='Наличие')or(List.get()=='Availability')or(List.get()=='Das Vorhandensein'):
        Value2=4
    if Value=='':
        if Language=='ru-RU':
            messagebox.showerror('Ошибка!','Введите значение для поиска')
        elif Language=='en-GB':
            messagebox.showerror('Error!','Enter a value for the search')
        elif Language=='de-DE':
            messagebox.showerror('Fehler!','Geben Sie einen Wert für die Suche ein')
    else:
        table2.delete(*table2.get_children())
        table1.delete(*table1.get_children())
        for i in range(0,len(Tableinformation)):
            if Value in Tableinformation[i][Value2]:
                table2.insert("","end", values=(Tableinformation[i]))
                if Shelf==5:
                    Bookcase+=1
                    Shelf=1
                elif Bookcase==5:
                    Room+=1
                    Bookcase=1
                elif NumberShelf==5:
                    Shelf+=1
                    NumberShelf=1
                elif NumberShelf<5:
                    NumberShelf+=1
                elif NumberBookcase<5:
                    NumberBookcase+=1
                table1.insert("","end",values=(Room,Bookcase,Shelf))
                
                
        

pixelVirtual=PhotoImage(width=1,height=1)

F1=LabelFrame(root,height=52,width=712,bg='#e1dee6')
F1.place(x=8,y=8)

p1=PhotoImage(file='1.png')
p2=PhotoImage(file='2.png')
p3=PhotoImage(file='3.png')
p4=PhotoImage(file='4.png')
p5=PhotoImage(file='5.png')
p6=PhotoImage(file='6.png')
p6en=PhotoImage(file='6en.png')
p6de=PhotoImage(file='6de.png')


BAdd=Button(F1,bg='#e1dee6',text='Добавить книгу',image=p1,compound=LEFT,width=128,height=27,command=AddBook).grid(row=0,column=0,padx=3,pady=3)
BRed=Button(F1,bg='#e1dee6',text='Редактировать',image=p2,compound=LEFT,width=128,height=27,command=EditBook).grid(row=0,column=1,padx=3,pady=3)
BDel=Button(F1,bg='#e1dee6',text='Удалить книгу',image=p3,compound=LEFT,width=128,height=27,command=DeleteBook).grid(row=0,column=2,padx=3,pady=3)
BAll=Button(F1,bg='#e1dee6',text='Все записи',image=p4,compound=LEFT,width=128,height=27,command=AllEntries).grid(row=0,column=3,padx=3,pady=3)
BLan=Button(F1,bg='#e1dee6',text='Язык',image=p5,compound=LEFT,width=128,height=27,command=ChooseLanguage).grid(row=0,column=4,padx=3,pady=3)


F2=LabelFrame(root,width=712,height=59,text='Параметры поиска',bg='#e1dee6',fg='black',font='arial 12')
F2.place(x=8,y=68)
L1=Label(F2,text='Поле поиска',width=80,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L1.place(x=0,y=6)
List=Combobox(F2,state='readonly')
List.place(x=95,y=5, width=145,height=21)
List['values']=('Название','Автор','Жанр','Дата издания','Наличие')
List.current(0)
L2=Label(F2,text='Искомое значение',width=100,height=9,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L2.place(x=248,y=6)
E1=Entry(F2)
E1.place(x=356,y=5,width=165,heigh=21)
BSearch=Button(F2,width=169,height=33,bg='#e1dee6',image=p6,compound='c',command=Search)
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
table1.insert("","end",values=(1,1,1))
table1.insert("","end",values=(1,1,1))
table1.insert("","end",values=(1,1,1))
table1.insert("","end",values=(1,1,1))
table1.insert("","end",values=(1,1,1))
table1.insert("","end",values=(1,1,2))
table1.insert("","end",values=(1,1,2))
table1.insert("","end",values=(1,1,2))
table1.insert("","end",values=(1,1,2))
table1.insert("","end",values=(1,1,2))
table1.insert("","end",values=(1,1,3))
table1.insert("","end",values=(1,1,3))

Sc1=Scrollbar(root,bg='white',command=table1.yview)
Sc1.place(x=206,y=165,height=226)
table1.config(yscrollcommand=Sc1.set)

L4=Label(root,text='Книги',width=80,height=9,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
L4.place(x=230,y=147)

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
Tableinformation=[]
Tableinformation.append(['Белая перчатка','Рид Майн','Приключения','1982','Нет'])
Tableinformation.append(['Как закалялалсь сталь','Николай Островский','Роман','1934','Да'])
Tableinformation.append(['Молодая гвардия','А.А.Фадеев','Роман','1946','Да'])
Tableinformation.append(['Понедельник начинается в субботу','Б.Н.Стругацкий','Повесть','1965','Да'])
Tableinformation.append(['Война и мир','Л.Н.Толстой','Роман','1867','Да'])
Tableinformation.append(['Преступление и наказание','Ф.М. Достоевский','Роман','1866','Да'])
Tableinformation.append(['Идиот','Ф.М.Достоевский','Роман','1869','Да'])
Tableinformation.append(['Евгений Онегин','А.С.Пушкин','Роман','1833','Да'])
Tableinformation.append(['Мёртвые души','Н.В.Гоголь','Поэма','1842','Нет'])
Tableinformation.append(['Мастер и Маргарита','М.А.Булгаков','Роман','1966','Да'])
Tableinformation.append(['Собачье сердце','М.А.Булгаков','Повесть','1968','Да'])
Tableinformation.append(['Сотников','В.В.Быков','Повесть','1970','Нет'])
for i in range (0,len(Tableinformation)):
    table2.insert("","end", values=(Tableinformation[i]))


Sc2=Scrollbar(root,bg='white',command=table2.yview)
Sc2.place(x=701,y=166,height=226)
table2.config(yscrollcommand=Sc2.set)


root.mainloop()


