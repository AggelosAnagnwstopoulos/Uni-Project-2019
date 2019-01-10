##################### Group project for python courses 2018 ####################
"""A quick note about the code: In order to save ourselves from making multiple frames and switching back and forth
we decided it was better to erase and recreate all the contents inside the menu canvas i.e. Buttons,Labels,Images 
and then make the new menus from scratch."""
############################## Essential stuff that we have to add ###############################
"""What is left: Create the player pawns and make them move inside the canvas, add a background picture to level 1 and make level 2
(same as level 1 but smaller more or less)."""
########################## Optional but cool stuff to add to the application #########################
""" 1) Add the questions for player count and names on a separete text box after clicking to play.
2) Add animations and movement to the player's pawns. 3) Using threading in order to get tkinter and pygame to make out 
a little bit and have some musicfunctioality that tkinter cannot offer."""

##################### Imports section ####################
import tkinter as t
import random
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring

#################### Classes Creation ###################

class Menu():
    
    def __init__(self):
        """This method initialises the window and creates the main canvas"""
        self.window=t.Tk()
        self.window.geometry("400x400")
        self.window.title("Snakes n ladders")
        self.window.resizable(0,0)
        self.canvas1=t.Canvas(self.window, width = 400, height = 400)
        self.canvas1.pack()
        #Background picture
        self.photo=t.PhotoImage(file="Project\Images\snake.gif")
        self.canvas1.create_image(0,0, anchor=t.NW, image=self.photo)
        self.main_menu()
        self.window.mainloop()
    
    def main_menu(self):
        """This method takes care of the main menu construction with its buttons and functionality"""
        self.playbutton=t.Button(self.window,text = "Play",width = 10,bg="green",fg="white",command=self.level_1)
        self.playbutton.place(x=165,y=100)
        self.levelsbutton=t.Button(self.window,text = "Levels",width = 10,bg="green",fg="white",command=self.levels_menu)
        self.levelsbutton.place(x=165,y=180)
        self.exitbutton=t.Button(self.window,text = "Exit",width = 10,bg="green",fg="white",command=self.rip)
        self.exitbutton.place(x=165,y=260)
    
    def levels_menu(self):
        """This method creates the Level menu with 2 images and 2 buttons underneath each one.
        Pressing one of the buttons will result in playing that level"""
        self.main_menu_killer()
        #First level
        self.photo1=t.PhotoImage(file="Project\Images\level1.gif")
        self.canvas1.create_image(50,100, anchor=t.NW, image=self.photo1)
        self.level1=t.Button(self.window,text="Level 1",bg="green",fg="white",command=self.level_1)
        self.level1.place(x=80,y=210)
        self.text1=t.Label(self.window,text="The classic snakes n' ladders game",bg="green",fg="white")
        self.text1.place(x=15,y=240)
        #Second level
        self.photo2=t.PhotoImage(file="Project\Images\level2.gif")
        self.canvas1.create_image(250,100, anchor=t.NW, image=self.photo2)
        self.level2=t.Button(self.window,text="Level 2",bg="green",fg="white",command=self.level_2)
        self.level2.place(x=280,y=210)
        self.text2=t.Label(self.window,text="A small board for new players",bg="green",fg="white")
        self.text2.place(x=230,y=240)
        #Back button
        self.back=t.Button(self.window, text = 'Back',width=10,bg="green",fg="white",command=self.level_back)
        self.back.place(x=165,y=300)

    def level_back(self):
        """This method deletes the contents of the levels menu and returns the user to the main menu"""
        self.canvas1.delete("all")
        self.photo = t.PhotoImage(file="Project\Images\snake.gif")
        self.canvas1.create_image(0,0, anchor=t.NW, image=self.photo)
        self.level1.destroy()
        self.text1.destroy()
        self.level2.destroy()
        self.text2.destroy()
        self.back.destroy()
        self.main_menu()

    def back_button(self):
        """This method destroys the options menu and returns the user to the main menu"""
        self.music.destroy()
        self.back.destroy()
        self.musictext.destroy()
        self.main_menu()

    def main_menu_killer(self):
        """This method destroyes the main menu buttons and clears the canvas"""
        self.playbutton.destroy()
        self.levelsbutton.destroy()
        self.exitbutton.destroy()
        ''
        
        
    def level_1(self):
        """This method kills the main menu and starts the game at level 1  by making an object of the Game class"""
        self.window.destroy()
        self.app = Level1()
        self.app.setup_game()
        self.app.window.mainloop()

    def level_2(self):
        """This method kills the main menu and starts the game at level 2  by making an object of the Game2 class"""
        self.window.destroy()
        self.app = Level2()
        self.app.setup_game()
        self.app.window.mainloop()

    def rip(self):
        """This method exits the application when the exit button is pressed"""
        self.window.destroy()

class Player():

    def __init__(self,name):
        """Creates a player object and keeps track of its position on the board"""
        self.name=name
        self.position=t.IntVar()
        self.position.set(1)

class Level1():

    colors=["red","blue","green","black"]

    def __init__(self):
        """Creates the window,canvas,board and dice button and sets up the counter for the dice rolls"""
        self.window=t.Tk()
        self.window.geometry("1000x610")
        self.window.title("Snakes n ladders")
        self.window.resizable(0,0)
        self.canvas2=t.Canvas(self.window,width=1000,height=600)
        self.background=t.PhotoImage(file=r"C:\Users\aggel\Desktop\Python Exams\Project\Images\background1.gif")
        self.canvas2.create_image(0,0,anchor=t.NW,image=self.background)
        self.canvas2.pack()
        self.currentplayer = 0
        self.snl=t.Label(self.window,text="Snakes n Ladders",font=("Helvetica",22),fg="green")
        self.snl.place(x=700,y=30)
        self.canvas2.create_line(600,0,600,1000)
        self.dicebutton=t.Button(self.window,text="Roll the dice",command=self.movement)
        self.dicebutton.place(x=780,y=110)
        self.eventlabel=t.Label(self.window,text="Roll the die to begin")
        self.eventlabel.place(x=760,y=80)

    def movement(self): 
        """Returns a random number from 1 to 6 as to replicate a dice roll and simulates a turn between the players.
        It also keeps track of each player's position and moves them to the designated square if they landed on a snake
        of a ladder. Also takes care of moving each players' piece on the board accordingly."""
        self.diceroll = random.randint(1,6)
        self.eventlabel.configure(text="You rolled a {}".format(self.diceroll))
        self.eventlabel.place(x=780,y=80)
        self.oldposition = self.names[self.currentplayer].position.get() 
        self.names[self.currentplayer].position.set(self.names[self.currentplayer].position.get()+self.diceroll)
        if  self.names[self.currentplayer].position.get() in self.snake_squares:
            self.names[self.currentplayer].position.set(self.snake_squares.get(self.names[self.currentplayer].position.get()))
        elif self.names[self.currentplayer].position.get() in self.ladder_squares:
            self.names[self.currentplayer].position.set(self.ladder_squares.get(self.names[self.currentplayer].position.get()))
        self.newposition = self.names[self.currentplayer].position.get()

        ############################## NOT ODDS ############################
        
        #if (self.names[self.currentplayer].position.get() % 10) not in [1,3,5,7,9]:
        #    self.canvas2.move(self.pawns[self.currentplayer],((self.newposition - self.oldposition) % 10) *60) , ((self.newposition - self.oldposition) // 10) *60)
        
        ############################## ODDS ################################
        
        #elif (self.names[self.currentplayer].position.get() % 10) in [1,3,5,7,9]:
        #    self.canvas2.move(self.pawns[self.currentplayer],((10 - (self.newposition - self.oldposition) % 10) * 60), ((self.newposition - self.oldposition) // 10) *60)
        
        
        if self.names[self.currentplayer].position.get() >= 100:
            self.eventlabel.configure(text="{} won the game!!!".format(self.names[self.currentplayer]))
            self.dicebutton.configure(command="")

        self.currentplayer += 1
        if self.currentplayer >= len(self.names):
            self.currentplayer = 0

    def setup_game(self):
        """This method draws the players' pawns and presents
         their names and positions on the right"""
        self.snake_squares = {17: 7, 62: 18, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}
        self.ladder_squares = {4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 63: 81, 71: 91}
        self.players= askinteger("snakes n ladders","How many players are there?")
        #Draw the pawns of each player (They get deleted bottom up if less than 4 players are ingame)
        self.p0 = self.canvas2.create_oval(5,548,25,568,fill=Level1.colors[0])
        self.p1 = self.canvas2.create_oval(30,548,50,568,fill=Level1.colors[1])
        self.p2 = self.canvas2.create_oval(5,573,25,593,fill=Level1.colors[2])
        self.p3 = self.canvas2.create_oval(30,573,50,593,fill=Level1.colors[3])
        self.pawns = []
        Tip 
        
        self.pawns.append(self.p0)
        self.pawns.append(self.p1)
        self.pawns.append(self.p2)
        self.pawns.append(self.p3)
        if self.players>4 or self.players<1:
            raise Exception("Player count is between 2 and 4")
        if self.players == 2:
            self.canvas2.delete(self.p2,self.p3)
        elif self.players == 3:
            self.canvas2.delete(self.p3)
        if self.players>4 or self.players<1:
            raise Exception("Player count is between 2 and 4")
        self.names = []
        for i in range(0,self.players):
            name = askstring("snakes n ladders","What is the name of player {}".format(i+1))
            player = Player(name)
            self.names.append(player)
            playernames=t.Label(self.window,text="{0} is at square:".format(self.names[i].name),fg=Level1.colors[i])
            playernames.place(x=700,y=i*100+200)
            playerposition=t.Label(self.window,textvariable=self.names[i].position)
            playerposition.place(x=900,y=i*100+200)

class Level2():
    
    colors=["red","blue","green","black"]

    def __init__(self):
        """Creates the window,canvas,board and dice button and sets up the counter for the dice rolls"""
        self.window=t.Tk()
        self.window.geometry("900x510")
        self.window.title("Snakes n ladders")
        self.window.resizable(0,0)
        self.canvas2=t.Canvas(self.window,width=1000,height=510)
        self.background2=t.PhotoImage(file=r"C:\Users\aggel\Desktop\Python Exams\Project\Images\background2.gif")
        self.canvas2.create_image(0,0,anchor=t.NW,image=self.background2)
        self.canvas2.pack()
        self.currentplayer = 0
        self.snl=t.Label(self.window,text="Snakes n Ladders",font=("Helvetica",22),fg="green")
        self.snl.place(x=600,y=30)
        self.dicebutton=t.Button(self.window,text="Roll the dice",command=self.movement)
        self.dicebutton.place(x=680,y=110)
        self.eventlabel=t.Label(self.window,text="Roll the die to begin")
        self.eventlabel.place(x=660,y=80)

    def movement(self): 
        """Returns a random number from 1 to 6 as to replicate a dice roll and simulates a turn between the players.
        It also keeps track of each player's position and moves them to the designated square if they landed on a snake
        of a ladder. Also takes care of moving each players' piece on the board accordingly."""
        self.diceroll = random.randint(1,6)
        self.eventlabel.configure(text="You rolled a {}".format(self.diceroll))
        self.eventlabel.place(x=680,y=80)
        self.oldposition = self.names[self.currentplayer].position.get() 
        self.names[self.currentplayer].position.set(self.names[self.currentplayer].position.get()+self.diceroll)
        if  self.names[self.currentplayer].position.get() in self.snake_squares:
            self.names[self.currentplayer].position.set(self.snake_squares.get(self.names[self.currentplayer].position.get()))
        elif self.names[self.currentplayer].position.get() in self.ladder_squares:
            self.names[self.currentplayer].position.set(self.ladder_squares.get(self.names[self.currentplayer].position.get()))
        self.newposition = self.names[self.currentplayer].position.get()

        ############################## NOT ODDS ############################
        
        #if (self.names[self.currentplayer].position.get() % 10) not in [1,3,5,7,9]:
        #    self.canvas2.move(self.pawns[self.currentplayer],((self.newposition - self.oldposition) % 10) *60) , ((self.newposition - self.oldposition) // 10) *60)
        
        ############################## ODDS ################################
        
        #elif (self.names[self.currentplayer].position.get() % 10) in [1,3,5,7,9]:
        #    self.canvas2.move(self.pawns[self.currentplayer],((10 - (self.newposition - self.oldposition) % 10) * 60), ((self.newposition - self.oldposition) // 10) *60)
        
        if self.names[self.currentplayer].position.get() >= 30:
            self.eventlabel.configure(text="{0} won the game!!! Press the button to start over.".format(self.names[self.currentplayer]))
            self.dicebutton.configure(command=Menu.level_2)

        self.currentplayer += 1
        if self.currentplayer >= len(self.names):
            self.currentplayer = 0

    def setup_game(self):
        """This method draws the players' pawns and presents
         their names and positions on the right"""
        self.snake_squares = {27:1,21:9,19:7,17:4}
        self.ladder_squares = {3:22,5:8,11:26,20:29}
        self.players= askinteger("snakes n ladders","How many players are there?")
        #Draw the pawns of each player (They get deleted bottom up if less than 4 players are ingame)
        self.p0 = self.canvas2.create_oval(5,405,40,440,fill=Level2.colors[0])
        self.p1 = self.canvas2.create_oval(45,405,75,440,fill=Level2.colors[1])
        self.p2 = self.canvas2.create_oval(5,455,40,490,fill=Level2.colors[2])
        self.p3 = self.canvas2.create_oval(45,455,75,490,fill=Level2.colors[3])
        self.pawns = []
        self.pawns.append(self.p0)
        self.pawns.append(self.p1)
        self.pawns.append(self.p2)
        self.pawns.append(self.p3)
        if self.players>4 or self.players<1:
            raise Exception("Player count is between 2 and 4")
        if self.players == 2:
            self.canvas2.delete(self.p2,self.p3)
        elif self.players == 3:
            self.canvas2.delete(self.p3)
        if self.players>4 or self.players<1:
            raise Exception("Player count is between 2 and 4")
        self.names = []
        for i in range(0,self.players):
            name = askstring("snakes n ladders","What is the name of player {}".format(i+1))
            player = Player(name)
            self.names.append(player)
            playernames=t.Label(self.window,text="{0} is at square:".format(self.names[i].name),fg=Level1.colors[i])
            playernames.place(x=650,y=i*100+150)
            playerposition=t.Label(self.window,textvariable=self.names[i].position)
            playerposition.place(x=750,y=i*100+150)

def menu():
    menu = Menu()

if __name__ == "__main__":
    menu()