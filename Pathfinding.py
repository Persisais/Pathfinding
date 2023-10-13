from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
from functools import partial

rows = 0
columns = 0
setMode = 0


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
height = max(100 + tileSize[1] * rows, 300)
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
    def __init__(self, button, x, y):
        self.button = button
        self.x = x
        self.y = y
        self.cost = 0
        self.heuristic = 0
        self.totalCost = 0
        self.type = 0
        """
        0 - Не посещено
        1 - Стартовая точка
        2 - Конечная точка
        3 - Стена
        4 - Посещено
        5 - Путь
        """


tilesArray = [[0] * columns] * rows
startPoint=0
endPoint=0


def changeTile(position):
    global setMode,startPoint,endPoint
    tile = tilesArray[position[0]][position[1]]
    if startPoint==tile:
        startPoint.button.config(bg="#FFF")
        startPoint.type=0
        startPoint=0
    if endPoint==tile:
        endPoint.button.config(bg="#FFF")
        endPoint.type=0
        endPoint=0

    if setMode == 0:
        tile.type=0
        tile.button.config(bg="#FFF")
    elif setMode == 1:
        if startPoint!=0:
            startPoint.button.config(bg="#FFF")
            startPoint.type=0
            startPoint=0
        startPoint=tile
        tile.type=1
        tile.button.config(background="#009900")
    elif setMode == 2:
        if endPoint!=0:
            endPoint.button.config(bg="#FFF")
            endPoint.type=0
            endPoint=0
        endPoint=tile
        tile.type=2
        tile.button.config(background="#990000")
    elif setMode==3:
        tile.type=3
        tile.button.config(bg="#000")


for i in range(rows):
    tilesLine = [0] * columns
    for j in range(columns):
        button = Button(leftLabelFrame, text=str(i) + " " + str(j) + "\n" + str(i + j), width=tileSize[0],
                        height=tileSize[0],
                        image=pixelVirtual, compound="c", command=partial(changeTile, (i, j)))
        button.grid(row=i, column=j)
        tile = Tile(button, i, j)
        print("tile ",tile.x,tile.y)
        tilesLine[j]=tile
        #tilesArray[i][j] = tile
    tilesArray[i]=tilesLine

"""
for tileList in tilesArray:
    for tile in tileList:
        print(tile.x, tile.y)
"""

"""
        0 - Не посещено
        1 - Стартовая точка
        2 - Конечная точка
        3 - Стена
        4 - Посещено
        5 - Путь
        """
def buttonStartPoint():
    global setMode,startPoint
    setMode = 1
    if startPoint!=0:
        startPoint.button.config(bg="#FFF")
        startPoint.type=0
        startPoint=0

def buttonEndPoint():
    global setMode,endPoint
    setMode = 2
    if endPoint!=0:
        endPoint.button.config(bg="#FFF")
        endPoint.type=0
        startPoint=0

def buttonUnseenPoint():
    global setMode
    setMode=0

def buttonWallPoint():
    global setMode
    setMode=3

rightLabelFrame = LabelFrame(root, height=height, width=rightPanelWidth, bg="#FFF")
rightLabelFrame.pack(side=RIGHT)

legendLabelFrame = LabelFrame(rightLabelFrame, text="Легенда", bg="#FFF")
legendLabelFrame.place(x=0, y=0)

legendLeftFrame = Frame(legendLabelFrame)
legendLeftFrame.pack(side=LEFT)

frameStartPoint = Frame(legendLeftFrame)
frameStartPoint.pack()
buttonStartPoint = Button(frameStartPoint, text="1 1\n2", width=tileSize[0], height=tileSize[0],
                          background="#009900", image=pixelVirtual, compound="c", command=buttonStartPoint)
buttonStartPoint.pack(side=LEFT)
labelStartPoint = Label(frameStartPoint, text="Стартовая точка")
labelStartPoint.pack(side=RIGHT)

frameEndPoint = Frame(legendLeftFrame)
frameEndPoint.pack()
buttonLegendEndPoint = Button(frameEndPoint, text="1 1\n2", width=tileSize[0], height=tileSize[0], background="#990000",
                              image=pixelVirtual, compound="c",command=buttonEndPoint)
buttonLegendEndPoint.pack(side=LEFT)
labelLegendEndPoint = Label(frameEndPoint, text="Конечная точка ")
labelLegendEndPoint.pack(side=RIGHT)

frameUnseen = Frame(legendLeftFrame, width=400)
frameUnseen.pack()
buttonUnseenPoint = Button(frameUnseen, text="1 1\n1", width=tileSize[0], height=tileSize[0], image=pixelVirtual,
                           compound="c",command=buttonUnseenPoint)
buttonUnseenPoint.pack(side=LEFT)
labelUnseenPoint = Label(frameUnseen, text="Не посещено     ")
labelUnseenPoint.pack(side=RIGHT)

legendRightFrame = Frame(legendLabelFrame)
legendRightFrame.pack(side=RIGHT)

frameWallPoint = Frame(legendRightFrame)
frameWallPoint.pack()
buttonWallPoint = Button(frameWallPoint, text="1 1\n2", width=tileSize[0], height=tileSize[0], background="#000",
                         image=pixelVirtual, compound="c",command=buttonWallPoint)
buttonWallPoint.pack(side=LEFT)
labelWallPoint = Label(frameWallPoint, text="Стена                   ")
labelWallPoint.pack(side=RIGHT)

frameSeenPoint = Frame(legendRightFrame)
frameSeenPoint.pack()
buttonSeenPoint = Button(frameSeenPoint, text="1+1\n2", width=tileSize[0], height=tileSize[0], background="#42aaff",
                         image=pixelVirtual, compound="c")
buttonSeenPoint.pack(side=LEFT)
labelSeenPoint = Label(frameSeenPoint, text="Посещено          ")
labelSeenPoint.pack(side=RIGHT)

framePathPoint = Frame(legendRightFrame, width=400)
framePathPoint.pack()
buttonPathPoint = Button(framePathPoint, text="1+ 1\n2", width=tileSize[0], height=tileSize[0], background="#1133FF",
                         fg="#FF4444", image=pixelVirtual, compound="c")
buttonPathPoint.pack(side=LEFT)
labelPathPoint = Label(framePathPoint, text="Путь                     ")
labelPathPoint.pack(side=RIGHT)

buttonStart = Button(rightLabelFrame, text="Начать", width=31, height=2, font=12)
buttonStart.place(x=1, y=164)

root.mainloop()
