##################### "Group" project for python courses 2018-19 ####################

"""Κάποια ακόμα σχόλια για τον κώδικα: 
1) Προτιμήθηκε η διαγραφή και επανασχεδίαση κάθε μενού αντί της δημιουργίας όλων μαζί και 
διαχείρηση του αντίστοιχου επιπέδου (μεταφορά στο προσκύνιο του εκάστοτε μενού)
2) Οι κλάσεις Level 1 , 2 είναι πανομοιότυπες στον κώδικα με διαφορά τον υπολογισμό της μεταβολής dx,dy για την κάθε μια.
Δεν μπορέσαμε να βρούμε τρόπο να μην γίνει ανακύκλωση κώδικα οπότε δεν είναι και το πιο efficient πρόγραμμα. Παρόλα αυτά δουλεύει ! Thats always nice...
3) Μετά από αρκετό testing νομίζω πως όλα τα δυνατά exceptions έχουν γίνει κατάλληλα handle, 
αυτό περιλαμβάνει είτε σχετικό μήνυμα, είτε loop το οποίο απαιτεί σωστό τύπο δεδομένων.
4) Το πρόγραμμα λειτουργεί και σε παλαιότερες εκδόσεις της python (2.x) (βλ. version control στo Imports Section)."""

##################### Imports section ####################

import random
import time
try:
    import tkinter as t
except ImportError:
    import Tkinter as t
try:
    from tkinter.simpledialog import askinteger
    from tkinter.simpledialog import askstring
except ImportError:
    from Tkinter.simpledialog import askinteger
    from Tkinter.simpledialog import askstring
    
#################### Level 1 Toolkit ###################

def YfromPosition(p):
    return (p - 1) // 10

def XfromPosition(p):
    x = p % 10 
    if x == 0: 
        x = 10
    if YfromPosition(p) % 2 == 0 : #even 
        return x
    else: #odd
        return 11 - x

#################### Level 2 Toolkit ###################

def YfromPosition2(p):
    return (p - 1) // 6

def XfromPosition2(p):
    x = p % 6
    if x == 0: 
        x = 6
    if YfromPosition2(p) % 2 == 0 : #even 
        if x == 0: 
            return 6
        else:
            return x
    else: #odd
        return 7 - x

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
        self.photo=t.PhotoImage(file="snake.gif")
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
        self.photo1=t.PhotoImage(file="level1.gif")
        self.canvas1.create_image(50,100, anchor=t.NW, image=self.photo1)
        self.level1=t.Button(self.window,text="Level 1",bg="green",fg="white",command=self.level_1)
        self.level1.place(x=80,y=210)
        self.text1=t.Label(self.window,text="The classic snakes n' ladders game",bg="green",fg="white")
        self.text1.place(x=15,y=240)
        #Second level
        self.photo2=t.PhotoImage(file="level2.gif")
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
        self.photo = t.PhotoImage(file="snake.gif")
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
        self.background=t.PhotoImage(file="b1.gif")
        self.canvas2.create_image(0,0,anchor=t.NW,image=self.background)
        self.canvas2.pack()
        self.currentplayer = 0
        self.snl=t.Label(self.window,text="Snakes n Ladders",font=("Helvetica",22),fg="green")
        self.snl.place(x=700,y=30)
        self.dicebutton=t.Button(self.window,text="Roll the dice",command=self.gameplay)
        self.dicebutton.place(x=780,y=110)
        self.eventlabel=t.Label(self.window,text="Roll the die to begin")
        self.eventlabel.place(x=760,y=80)
        self.rettomenu=t.Button(self.window,text="Return to menu",font=("Helvetica",10),command=self.quittomenu)
        self.rettomenu.place(x=650,y=560)
        self.resetbutton=t.Button(self.window,text="Reset the game",font=("Helvetica",10),command=self.resetgame)
        self.resetbutton.place(x=850,y=560)

    def gameplay(self): 
        """Returns a random number from 1 to 6 as to replicate a dice roll and simulates a turn between the players.
        It also keeps track of each player's position and moves them to the designated square if they landed on a snake
        of a ladder. Also takes care of moving each players' piece on the board accordingly."""
        diceroll = random.randint(1,6)
        self.eventlabel.configure(text="You rolled a {}".format(diceroll))
        self.eventlabel.place(x=780,y=80)
        oldposition = self.names[self.currentplayer].position.get()
        newposition = oldposition + diceroll
        while newposition in self.snake_squares or newposition in self.ladder_squares: 
            if  newposition in self.snake_squares:
                newposition = self.snake_squares[newposition]
            elif newposition in self.ladder_squares:
                newposition = self.ladder_squares[newposition]
        # Check if the player Won.
        # If he did, then reset his position to 100 to be still visible on the screen
        if newposition >= 100:
            newposition = 100
            self.eventlabel.config(text = "{} Wins!".format(self.names[self.currentplayer].name))
            self.canvas2.delete(self.names[self.currentplayer].pawn)
        self.names[self.currentplayer].position.set(newposition)
        # Calculate change in X and Y
        dy = - (YfromPosition(newposition) - YfromPosition(oldposition))
        dx = XfromPosition(newposition) - XfromPosition(oldposition)
        # Move the coresponding circle
        for i in range(15):
            time.sleep(0.020)
            self.canvas2.move(self.names[self.currentplayer].pawn, dx*4, dy*4)
            self.dicebutton.config(state="disabled")
            self.canvas2.update()
        self.dicebutton.config(state="normal")
        # Get the next player
        self.currentplayer += 1
        if self.currentplayer >= len(self.names):
            self.currentplayer = 0
        self.canvas2.update()

    def setup_game(self):
        """This method initialises the number and names of players,
        draws their pawns and presents their names and positions on the right"""

        self.snake_squares = {17: 7, 62: 18, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}
        self.ladder_squares = {4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 63: 81, 71: 91}
        self.players= askinteger("Snakes n Ladders","Enter a player number between 1 and 4")
        #Η μέρα της μαρμότας
        while self.players < 1 or self.players > 4:
            self.players= askinteger("Snakes n Ladders","Enter a player number between 1 and 4")    
        self.starting_locations = [(5,548,25,568), (30,548, 50,568), (5,573,25,593), (30,573, 50, 593)]
        self.names = []
        for i in range(0,self.players):
            name = askstring("Snakes n Ladders","What is the name of player {}".format(i+1))
            player = Player(name)
            player.pawn = self.canvas2.create_oval(self.starting_locations[i][0],
                                                   self.starting_locations[i][1],
                                                   self.starting_locations[i][2],
                                                   self.starting_locations[i][3],
                                                   fill = Level1.colors[i])
            self.names.append(player)
            playernames=t.Label(self.window,text="{0} is at square:".format(self.names[i].name),fg=Level1.colors[i])
            playernames.place(x=700,y=i*100+200)
            playerposition=t.Label(self.window,textvariable=self.names[i].position)
            playerposition.place(x=900,y=i*100+200)

    def quittomenu(self):
        """This method is called upon on the menu button while ingame and returns the players to the main menu"""
        self.window.destroy()
        self.app = Menu()
        self.app.main_menu()
        self.app.window.mainloop()
    
    def resetgame(self):
        """This method resets the board for the players to start anew"""
        for i in range(0,self.players):
            self.names[i].position.set(1)
            self.canvas2.delete(self.names[i].pawn)
            self.names[i].pawn = self.canvas2.create_oval(self.starting_locations[i][0],
                                                   self.starting_locations[i][1],
                                                   self.starting_locations[i][2],
                                                   self.starting_locations[i][3],
                                                   fill = Level2.colors[i])
        self.eventlabel.config(text="Game reset.Replay?")  

class Level2():
    
    colors=["red","blue","green","black"]

    def __init__(self):
        """Creates the window,canvas,board and dice button and sets up the counter for the dice rolls"""
        self.window=t.Tk()
        self.window.geometry("900x510")
        self.window.title("Snakes n ladders")
        self.window.resizable(0,0)
        self.canvas2=t.Canvas(self.window,width=1000,height=510)
        self.background2=t.PhotoImage(file="b2.gif")
        self.canvas2.create_image(0,0,anchor=t.NW,image=self.background2)
        self.canvas2.pack()
        self.currentplayer = 0
        self.snl=t.Label(self.window,text="Snakes n Ladders",font=("Helvetica",22),fg="green")
        self.snl.place(x=600,y=30)
        self.dicebutton=t.Button(self.window,text="Roll the dice",command=self.gameplay)
        self.dicebutton.place(x=680,y=110)
        self.eventlabel=t.Label(self.window,text="Roll the die to begin")
        self.eventlabel.place(x=660,y=80)
        self.rettomenu=t.Button(self.window,text="Return to menu",font=("Helvetica",10),command=self.quittomenu)
        self.rettomenu.place(x=550,y=480)
        self.resetbutton=t.Button(self.window,text="Reset the game",font=("Helvetica",10),command=self.resetgame)
        self.resetbutton.place(x=750,y=480)

    def gameplay(self): 
        """Returns a random number from 1 to 6 as to replicate a dice roll and simulates a turn between the players.
        It also keeps track of each player's position and moves them to the designated square if they landed on a snake
        of a ladder. Also takes care of moving each players' piece on the board accordingly."""
        diceroll = random.randint(1,6)
        self.eventlabel.configure(text="You rolled a {}".format(diceroll))
        self.eventlabel.place(x=680,y=80)
        oldposition = self.names[self.currentplayer].position.get()
        newposition = oldposition + diceroll
        while newposition in self.snake_squares or newposition in self.ladder_squares: 
            if  newposition in self.snake_squares:
                newposition = self.snake_squares[newposition]
            elif newposition in self.ladder_squares:
                newposition = self.ladder_squares[newposition]
        # Check if the player Won.
        # If he did, then reset his position to 100 to be still visible on the screen
        if newposition >= 30:
            newposition = 30
            self.eventlabel.config(text = "{} Wins!".format(self.names[self.currentplayer].name))
            self.canvas2.delete(self.names[self.currentplayer].pawn)
        self.names[self.currentplayer].position.set(newposition)
        # Calculate change in X and Y
        dy = - (YfromPosition2(newposition) - YfromPosition2(oldposition))
        dx = XfromPosition2(newposition) - XfromPosition2(oldposition)
        # Move the coresponding circle 
        for i in range (25):
            time.sleep(0.025)
            self.canvas2.move(self.names[self.currentplayer].pawn, dx * (20/6) , dy * 4)
            self.dicebutton.config(state="disabled")
            self.canvas2.update()
        self.dicebutton.config(state="normal")
        # Get the next player
        self.currentplayer += 1
        if self.currentplayer >= len(self.names):
            self.currentplayer = 0
        self.canvas2.update()

    def setup_game(self):
        """This method initialises the number and names of players,
        draws their pawns and presents their names and positions on the right"""
        self.snake_squares = {27:1,21:9,19:7,17:4}
        self.ladder_squares = {3:22,5:8,11:26,20:29}
        self.players= askinteger("Snakes n Ladders","Enter a player number between 1 and 4")    
        #Η μέρα της μαρμότας
        while self.players < 1 or self.players > 4:
            self.players= askinteger("Snakes n Ladders","Enter a player number between 1 and 4")    
        self.starting_locations = [(5,448,25,468), (30,448, 50,468), (5,473,25,493), (30,473, 50, 493)]
        self.names = []
        for i in range(0,self.players):
            self.name = askstring("Snakes n Ladders","What is the name of player {}".format(i+1))
            player = Player(self.name)
            player.pawn = self.canvas2.create_oval(self.starting_locations[i][0],
                                                   self.starting_locations[i][1],
                                                   self.starting_locations[i][2],
                                                   self.starting_locations[i][3],
                                                   fill = Level2.colors[i])
            self.names.append(player)
            playernames=t.Label(self.window,text="{0} is at square:".format(self.names[i].name),fg=Level1.colors[i])
            playernames.place(x=600,y=i*100+150)
            playerposition=t.Label(self.window,textvariable=self.names[i].position)
            playerposition.place(x=700,y=i*100+150)
    
    def quittomenu(self):
        """This method is called upon on the menu button while ingame and returns the players to the main menu"""
        self.window.destroy()
        self.app = Menu()
        self.app.main_menu()
        self.app.window.mainloop()
    
    def resetgame(self):
        """This method resets the board for the players to start anew"""
        for i in range(0,self.players):
            self.names[i].position.set(1)
            self.canvas2.delete(self.names[i].pawn)
            self.names[i].pawn = self.canvas2.create_oval(self.starting_locations[i][0],
                                                   self.starting_locations[i][1],
                                                   self.starting_locations[i][2],
                                                   self.starting_locations[i][3],
                                                   fill = Level2.colors[i])
        self.eventlabel.config(text="Game reset. Replay ?")  

def menu():
    try:
        menu = Menu()
    except EnvironmentError:
        print("Are you seriously running on a vm with no $DISPLAY variable dude... What is this, a joke ?")

if __name__ == "__main__":
    menu()
    #Νταξ καλούλι βγήκε
