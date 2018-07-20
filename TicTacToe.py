# Tic Tac Toe

from tkinter import *

class TTT_Game(Frame):
    """ Play Tic Tac Toe """

    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("500x600")
        self.master.title("Tic Tac Toe Game")
        self.initUI()

    def initUI(self):
        canvas1 = Canvas(width=500, height=500, bg="lavender")
        canvas1.grid()

        #Title
        canvas1.create_text(250, 50, text = "Tic Tac Toe", font=("Arial", 24))
        canvas1.create_text(75, 30, text="X O X O", font=("Arial", 20))
        canvas1.create_text(425, 30, text="O X O X", font=("Arial", 20))
        canvas1.create_text(75, 470, text="O X O X", font=("Arial", 20))
        canvas1.create_text(425, 470, text="X O X O", font=("Arial", 20))
                            

        #Game board square
        canvas1.create_rectangle(100,100,400,400, fill = "floral white")

        #Game board lines
        canvas1.create_line(100,200,400,200, width=5)
        canvas1.create_line(100,300,400,300, width=5)
        canvas1.create_line(200,100,200,400, width=5)
        canvas1.create_line(300,100,300,400, width=5)

        #X or O radio button
        self.X_O = StringVar()
        check_X = Radiobutton(canvas1, text="X", font=("Arial", 24), value="X", variable=self.X_O, width=3, bg="lavender", indicatoron=0, activebackground="azure", selectcolor="lavender blush")
        check_O = Radiobutton(canvas1, text="O", font=("Arial", 24), value="O", variable=self.X_O, width=3, bg="lavender", indicatoron=0, activebackground="lavender blush", selectcolor="azure")

        #X or O windows
        canvas1.create_window(200,450, anchor="center", window=check_X)
        canvas1.create_window(300,450, anchor="center", window=check_O)
        
        
        #Buttons
        self.button_XO = []

        for i in range(9):
            self.button_XO.append(StringVar())

        #buttons = [button_A1, button_A2, button_A3, button_B1, button_B2, button_B3, button_C1, button_C2, button_C3]
        self.buttons = []
        
        for i in range(9):
            self.buttons.append(Button(canvas1, textvariable=self.button_XO[i], command= lambda i=i: self.XO(i), font=("Arial",35), anchor="center", relief="flat", bg="floral white", activebackground="old lace"))

        #Button windows
        button_windows = []

        A1 = canvas1.create_window(150, 150, anchor="center", window=self.buttons[0])
        A2 = canvas1.create_window(250, 150, anchor="center", window=self.buttons[1])
        A3 = canvas1.create_window(350, 150, anchor="center", window=self.buttons[2])
        B1 = canvas1.create_window(150, 250, anchor="center", window=self.buttons[3])
        B2 = canvas1.create_window(250, 250, anchor="center", window=self.buttons[4])
        B3 = canvas1.create_window(350, 250, anchor="center", window=self.buttons[5])
        C1 = canvas1.create_window(150, 350, anchor="center", window=self.buttons[6])
        C2 = canvas1.create_window(250, 350, anchor="center", window=self.buttons[7])
        C3 = canvas1.create_window(350, 350, anchor="center", window=self.buttons[8])

        #Rows values

        self.rows = []

        for i in range(9):
            self.rows.append(100)

        
    def XO(self,i):
                
        self.button_XO[i].set(self.X_O.get())

        if self.X_O.get() == "X":
            self.rows[i] = 1
        elif self.X_O.get() == "O":
            self.rows[i] = 0
        
        # Horizontal calc
        for m in [0,3,6]:
            self.total = 0
            for r in range(3):
                self.total += self.rows[r + m]

            self.win_canvas()
                                                  
        # Vertical calc
        for r in range(3):
            self.total = 0
            for m in [0,3,6]:
                self.total += self.rows[r+m]

            self.win_canvas()

        # Diagonal calc
        self.total = self.rows[0] + self.rows[4] + self.rows[8]
        self.win_canvas()
        
        self.total = self.rows[2] + self.rows[4] + self.rows[6]
        self.win_canvas()


    # Create win canvas

    def win_canvas(self):
        if self.total == 3:
            canvas2 = Canvas(width=500, height=100)
            canvas2.grid()
            win_X_rect = canvas2.create_rectangle(100, 20, 300, 80, fill="lavender blush")
            win_X = canvas2.create_text(200, 50, text="X Wins!", font=("Arial", 20))
            #play_again_button = Button(canvas2, text="Play Again", font=("Arial", 16), command=self.destroy, bg="bisque")
            #play_again_window = canvas2.create_window(400, 50, window=play_again_button)
        elif self.total == 0:
            canvas2 = Canvas(width=500, height=100)
            canvas2.grid()
            win_O_rect = canvas2.create_rectangle(100, 20, 300, 80, fill="azure")
            win_O = canvas2.create_text(200, 50, text="O Wins!", font=("Arial", 20))
            #play_again_button = Button(canvas2, text="Play Again", font=("Arial", 16), command=self.destroy, bg="bisque")
            #play_again_window = canvas2.create_window(400, 50, window=play_again_button)
        
   

        

game01 = TTT_Game()
game01.mainloop()


