from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview

rows = 0
columns = 0


def confirmEntry():
    global rows, columns
    rows = int(entryRows.get())
    columns = int(entryColumns.get())
    if (rows == 0 or columns == 0):
        messagebox.showerror('Ошибка!', 'Введите размеры')
    elif (rows < 3 or columns < 3):
        messagebox.showerror('Ошибка!', 'Размеры должны быть больше 3')
    else:
        popUpWindow.destroy()


popUpWindow = Tk()
popUpWindow.title("Pathfinding A*")
popUpWindow.geometry("320x100")
popUpWindow.resizable(width=False, height=False)
popUpWindow.config()
labelTextPopUp = Label(popUpWindow, text="Введите размерность поля (не меньше 3)", font=12)
labelTextPopUp.pack()
entryRows = Entry(popUpWindow, width=3)
entryRows.pack()
entryColumns = Entry(popUpWindow, width=3)
entryColumns.pack()
buttonConfirmEntry = Button(popUpWindow, text="Начать", command=confirmEntry)
buttonConfirmEntry.pack()



# Button1=Button(Window2,bg='#e1dee6',text='Да',font='Times 12',command=DeleteBookButton)
# Lbl5=Label(Window1,text='Наличие',width=110,height=8,bg='#e1dee6',font='arial 9',image=pixelVirtual,compound='c')
# Lbl5.place(x=520,y=0)
# Name=Entry(Window1,width=30,font='Times 10')
# Name.place(x=0,y=20)
popUpWindow.mainloop()

tileSize = (40, 40)
rightPanelWidth = 360

width = rightPanelWidth + tileSize[0] * columns
height = max(100+tileSize[1] * rows,300)
windowSize = str(width) + "x" + str(height)

root = Tk()
root.title('Pathfinding A*')
root.geometry(windowSize)
root.resizable(width=False, height=True)
root.config()
pixelVirtual = PhotoImage(width=1, height=1)

leftLabelFrame = LabelFrame(root, height=height, width=width - rightPanelWidth, bg="#009900")
leftLabelFrame.pack(side=LEFT)

class Tile(object):
    def __init__(self,button,x,y):
        self.button=button
        self.x=x
        self.y=y
        self.cost=0
        self.heuristic=0
        self.totalCost=0
        self.type=0
        """
        0 - Не посещено
        1 - Стартовая точка
        2 - Конечная точка
        3 - Стена
        4 - Посещено
        5 - Путь
        """



tilesArray = [[0] * columns] * rows
for i in range(rows):
    for j in range(columns):
        button = Button(leftLabelFrame, text=str(i) + " " + str(j) + "\n" + str(i + j), width=tileSize[0],
                        height=tileSize[0],
                        image=pixelVirtual, compound="c")
        button.grid(row=i, column=j)
        tile=Tile(button,i,j)
        tilesArray[i][j] = tile

rightLabelFrame = LabelFrame(root, height=height, width=rightPanelWidth,bg="#FFF")
rightLabelFrame.pack(side=RIGHT)

legendLabelFrame = LabelFrame(rightLabelFrame, text="Легенда", bg="#FFF")
legendLabelFrame.place(x=0, y=0)

legendLeftFrame = Frame(legendLabelFrame)
legendLeftFrame.pack(side=LEFT)


def buttonStartPoint():
    

frameStartPoint = Frame(legendLeftFrame)
frameStartPoint.pack()
buttonLegendStartPoint = Button(frameStartPoint, text="1 1\n2", width=tileSize[0], height=tileSize[0],background="#009900", image=pixelVirtual, compound="c")
buttonLegendStartPoint.pack(side=LEFT)
labelLegendStartPoint = Label(frameStartPoint, text="Стартовая точка")
labelLegendStartPoint.pack(side=RIGHT)


frameEndPoint = Frame(legendLeftFrame)
frameEndPoint.pack()
buttonLegendEndPoint = Button(frameEndPoint, text="1 1\n2", width=tileSize[0], height=tileSize[0], background="#990000",image=pixelVirtual, compound="c")
buttonLegendEndPoint.pack(side=LEFT)
labelLegendEndPoint = Label(frameEndPoint, text="Конечная точка ")
labelLegendEndPoint.pack(side=RIGHT)

frameUnseen = Frame(legendLeftFrame,width=400)
frameUnseen.pack()
buttonUnseenPoint =Button(frameUnseen, text="1 1\n1", width=tileSize[0],height=tileSize[0],image=pixelVirtual, compound="c")
buttonUnseenPoint.pack(side=LEFT)
labelUnseenPoint = Label(frameUnseen, text="Не посещено     ")
labelUnseenPoint.pack(side=RIGHT)

legendRightFrame = Frame(legendLabelFrame)
legendRightFrame.pack(side=RIGHT)

frameWallPoint = Frame(legendRightFrame)
frameWallPoint.pack()
buttonWallEndPoint = Button(frameWallPoint, text="1 1\n2", width=tileSize[0], height=tileSize[0], background="#000",image=pixelVirtual, compound="c")
buttonWallEndPoint.pack(side=LEFT)
labelWallEndPoint = Label(frameWallPoint, text="Стена                   ")
labelWallEndPoint.pack(side=RIGHT)


frameSeenPoint = Frame(legendRightFrame)
frameSeenPoint.pack()
buttonSeenEndPoint = Button(frameSeenPoint, text="1+1\n2", width=tileSize[0], height=tileSize[0], background="#42aaff",image=pixelVirtual, compound="c")
buttonSeenEndPoint.pack(side=LEFT)
labelSeenEndPoint = Label(frameSeenPoint, text="Посещено          ")
labelSeenEndPoint.pack(side=RIGHT)


framePathPoint = Frame(legendRightFrame,width=400)
framePathPoint.pack()
buttonPathEndPoint = Button(framePathPoint, text="1+ 1\n2", width=tileSize[0], height=tileSize[0], background="#1133FF",fg="#FF4444",image=pixelVirtual, compound="c")
buttonPathEndPoint.pack(side=LEFT)
labelPathEndPoint = Label(framePathPoint, text="Путь                     ")
labelPathEndPoint.pack(side=RIGHT)




buttonStart=Button(rightLabelFrame,text="Начать",width=31,height=2,font=12)
buttonStart.place(x=1,y=164)


root.mainloop()
