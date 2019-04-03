from tkinter import *

def frame(root, side):
   
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
   
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def label(root, side, text, command=None):
  
    w = Label(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

#**** Main Menu ****
class Quiz(Frame):


    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Welcome to Quiz Maker")
        theMenu = Menu(self.master)
        self.master.config(menu = theMenu)


        fileMenu = Menu(theMenu)
        
        theMenu.add_cascade(label = "File", menu = fileMenu, underline=0)
        fileMenu.add_command(label = "New File", command = self.NewFile, underline=0)
        fileMenu.add_command(label = "Open", command = self.OpenFile, underline=0)
        
        fileMenu.add_separator()
        
        fileMenu.add_command(label = "Save", command = self.doNothing, underline=0)
        fileMenu.add_command(label = "Save As", command = self.doNothing)
        
        fileMenu.add_separator()
        
        fileMenu.add_command(label = "Print", command = self.doNothing, underline=0)
        
        fileMenu.add_separator()
        
        fileMenu.add_command(label = "Close", command = self.doNothing)
        fileMenu.add_command(label = "Exit", command = self.onExit, underline=1)


        editMenu = Menu(theMenu)
        
        theMenu.add_cascade(label = "Edit", menu = editMenu, underline=0)
        editMenu.add_command(label = "Undo", command = self.doNothing)
        editMenu.add_command(label = "Redo", command = self.doNothing)
        
        editMenu.add_separator()

        editMenu.add_command(label = "Cut", command = self.doNothing, underline=2)
        editMenu.add_command(label = "Copy", command = self.doNothing, underline=0)
        editMenu.add_command(label = "Paste", command = self.doNothing)
        editMenu.add_command(label = "Select All", command = self.doNothing, underline=7)

        editMenu.add_separator()

        editMenu.add_command(label = "Find", command = self.doNothing, underline=0)
        editMenu.add_command(label = "Find Again", command = self.doNothing, underline=5)
        editMenu.add_command(label = "Find in Files", command = self.doNothing)
        editMenu.add_command(label = "Replace", command = self.doNothing, underline=0)


        quizMenu = Menu(theMenu)

        theMenu.add_cascade(label = "Quiz", menu = quizMenu, underline=0)
        quizMenu.add_command(label = "Add Question", command = self.doNothing)
        quizMenu.add_command(label = "Select Question", command = self.doNothing)
        quizMenu.add_command(label = "Undo", command = self.doNothing)


        setMenu = Menu(theMenu)

        theMenu.add_cascade(label = "Settings", menu = setMenu, underline=0)

        dispMenu = Menu(setMenu)
        setMenu.add_cascade(label = "Display", menu = dispMenu, underline=0)
        dispMenu.add_checkbutton(label = "Number Buttons", command = self.doNothing)
        dispMenu.add_checkbutton(label = "Question Bar", command = self.doNothing)
        dispMenu.add_checkbutton(label = "Time Bar", command = self.doNothing)

        setMenu.add_command(label = "Undo", command = self.doNothing)
        setMenu.add_command(label = "Redo", command = self.doNothing)


        actionMenu = Menu(theMenu)
        theMenu.add_cascade(label = "Action", menu = actionMenu, underline=4)

        timerMenu = Menu(actionMenu)
        actionMenu.add_cascade(label = "Timer", menu = timerMenu)
        timerMenu.add_command(label = "Start Timer", command = self.doNothing)
        timerMenu.add_command(label = "Stop Timer", command = self.doNothing)

        actionMenu.add_command(label = "Start Quiz", command = self.doNothing)
        actionMenu.add_command(label = "Stop Quiz", command = self.doNothing)


        resultMenu = Menu(theMenu)
        theMenu.add_cascade(label = "Results", menu = resultMenu, underline=3)
        resultMenu.add_command(label = "View Results", command = self.doNothing)


        surveyMenu = Menu(theMenu)
        theMenu.add_cascade(label = "Survey", menu = surveyMenu, underline=5)
        surveyMenu.add_command(label = "Survey Results", command = self.doNothing)


        helpMenu = Menu(theMenu)
        theMenu.add_cascade(label = "Help", menu = helpMenu, underline=0)
        helpMenu.add_command(label = "About Quiz Maker", command = self.About)



        m1 = PanedWindow()
        m1.pack(fill=BOTH, expand=1)

        left = Label(m1, text="Add/Remove Questions")
        m1.add(left)

        m2 = PanedWindow(m1, orient=VERTICAL)
        m1.add(m2)

        top = Label(m2, text=" Files Added")
        m2.add(top)

        bottom = Label(m2, text="                                                                                                                                                                                                                                                                   Client Pane")
        m2.add(bottom)


    def onExit(self):

        self.quit()

    def doNothing(self):

        print("I won't do anything")

    def NewFile(self):
        print("New File!")

    def OpenFile(self):

        name = askopenfilename()
        print(name)

    def About(self):

        print("This is Quiz Maker")



#**** Toolbar ****

"""theTool = Frame(win, bg = "white")
insertButton = Button(theTool, text = "Insert Image", command = self.doNothing)
insertButton.pack(side = LEFT, padx = 2, pady = 2)
printButton = Button(theTool, text = "Print", command = self.doNothing)
printButton.pack(side = LEFT, padx = 2, pady = 2)

theTool.pack(fill = X)"""

def main():

#**** Main Window ****

        win = Tk()
        app = Quiz()
        win.title("Welcome to Quiz Maker")
        win.mainloop()

if __name__ == '__main__':

    main()
