import tkinter as t
import random
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring

#################### Tool             ###################
def YfromPosition(p):
    return (p - 1) // 10

def XfromPosition(p):
    x = p % 10 
    if YfromPosition(p) % 2 == 0 : #even 
        if x == 0 : return 10
        return x 
    else: #odd
        return 10 - x
        
class Player():

    def __init__(self,name):
        """Creates a player object and keeps track of its position on the board"""
        self.name=name
        self.position=t.IntVar()
        self.position.set(1)

class Game():

    colors=["red","blue","green","black"]

    def __init__(self):
        """Creates the window,canvas,board and dice button and sets up the counter for the dice rolls"""
        self.window=t.Tk()
        self.window.geometry("1000x600")
        self.window.title("Snakes n ladders")
        self.window.resizable(0,0)
        self.canvas2=t.Canvas(self.window,width=1000,height=600)
        self.canvas2.pack()
        self.currentplayer = 0
        #self.background=t.PhotoImage(file="Project\board.gif")
        #self.canvas2.create_image(self.window,0,0,anchor=t.NW,image=self.background)
        for i in range(0,11):
            self.canvas2.create_line(i*60,0,i*60,600)
            self.canvas2.create_line(0,i*60,600,i*60)    
        self.dicebutton=t.Button(self.window,text="Roll the dice",command=self.roll_dice)
        self.dicebutton.place(x=900,y=60)
        self.dicelabel=t.Label(self.window,text="Roll the die to begin")
        self.dicelabel.place(x=880,y=30)

    def roll_dice(self): 
        """Returns a random number from 1 to 6 as to replicate a dice roll and simulates a turn between the players.
        It also keeps track of each player's position and moves them to the designated square if they landed on a snake
        of a ladder."""
        diceroll = random.randint(1,6)
        self.dicelabel.configure(text="You rolled a {}".format(diceroll))
        self.dicelabel.place(x=900,y=30)
        oldposition = self.names[self.currentplayer].position.get()
        

        newposition = oldposition + diceroll

        # Check for collision against snake or ladder multiple times

        while newposition in self.snake_squares or newposition in self.ladder_squares: 
            if  newposition in self.snake_squares:
                newposition = self.snake_squares[newposition]
            elif newposition in self.ladder_squares:
                newposition = self.ladder_squares[newposition]

        # Check if the player Won.
        # If he did, then reset his position to 100 to be still visible on the screen
            
        if newposition >= 100:
            newposition = 100
            self.dicelabel.config(text = "{} Wins!".format(self.names[self.currentplayer].name))
        

        self.names[self.currentplayer].position.set(newposition)

        # Calculate change in X and Y

        dy = - (YfromPosition(newposition) - YfromPosition(oldposition))
        dx = XfromPosition(newposition) - XfromPosition(oldposition)

        # Move the coresponding circle 
        self.canvas2.move(self.names[self.currentplayer].pawn, dx * 60, dy * 60)
        
        
        # Get the next player
        self.currentplayer += 1
        if self.currentplayer >= len(self.names):
            self.currentplayer = 0





    def setup_game(self):
        """This method initialises the number and names of players,
        draws their pawns and presents their names and positions on the right"""

        self.snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
        self.ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
    
        ################ Make this into a textbox right after the menu! #################

        self.players= askinteger("Snakes n Ladders","How many players are there?")
        #Draw the pawns of each player (They get deleted bottom up if less than 4 players are ingame)

        starting_locations = [(5,548,25,568), (30,548, 50,568), (5,573,25,593), (30,573, 50, 593)]

        self.names = []
    
        for i in range(0,self.players):
            name = askstring("Snakes n Ladders","What is the name of player {}".format(i+1))
            player = Player(name)
            player.pawn = self.canvas2.create_oval(starting_locations[i][0],
                                                   starting_locations[i][1],
                                                   starting_locations[i][2],
                                                   starting_locations[i][3],
                                                   fill = Game.colors[i])
            self.names.append(player)
            playernames=t.Label(self.window,text="{0} is at square:".format(self.names[i].name),fg=Game.colors[i])
            playernames.place(x=700,y=i*100+200)
            playerposition=t.Label(self.window,textvariable=self.names[i].position)
            playerposition.place(x=900,y=i*100+200)