#
#  This is a code of a simple automated Tertis game on Micorbit v1.5 . This version of the code just shows how it runs+ explanation.
#  You can re-edit the script and use it yourself for your own project on the microbit piece
#
#  To run this code on the microbit website (https://python.microbit.org/v/2), use the code that is in this file: AutomatedTetris_Microbit.
#  

from random import choice, randint

# score of the game
score = 0

# The grid that we will be playing with
currents = ["00000",
            "00000",
            "00000",
            "00000",
            "00000"]

# Available blocks:
#           99    99    9
#           99          9
blocks = [[2,2],[2,1],[1,2]]


# The main class that defines a piece of a block and have specific functions
class Piece:
    global currents


#    Globaling couple of variables
    def __init__(self,x,y):
        self.lost = False
        self.x = x
        self.y = y
        self.spawn()


# This function fills a specific row in currents with 9's
# next_y is next y
# x is the amount of the x's
# i is the first index (index of first 9 in the block)
# moving is if it's moving or not
# ys checks if the block uses two y's (two rows, y is > 1)
    def fill(self,next_y,x,i,moving=False,ys=False):
            if next_y > 4:
                return False

            # Defining the next row we dealing with and the last one.
            row = [x for x in currents[next_y]]
            if moving and ys:
                old_row = [x for x in currents[next_y-2]]
            elif moving and not ys:
                old_row = [x for x in currents[next_y-1]]
            else:
                old_row = []

            # Adding the 9's to the rows
            if row[i] == '9':
                self.lost = True
                return False
            elif x == 2 and row[i+1] == '9':
                self.lost = True
                return False
            else:
                row[i] = '9'

                if moving:
                    old_row[i] = '0'
                if x == 2:
                    row[i+1] = '9'
                    if moving:
                        old_row[i+1] = '0'

                return ''.join(row),''.join(old_row)


    def spawn(self):
        #
        #  Spawning the piece
        #
        self.block = []
        self.first_index = randint(0,3)
        
        if currents[0][self.first_index] == '9':
            self.lost = True
        
        for r in range(self.y):
            rows = self.fill(r,self.x,self.first_index)
            try:
                if not rows:
                    return
            except:
                pass
            currents[r] = rows[0]
            self.block.append([r,self.first_index,self.x])
        self.last_y = self.block[-1][0]     
        return
    
    def move(self):
        self.last_y += 1
        info = self.fill(self.last_y,self.x,self.first_index,moving=True,ys=bool(self.block[-1][0]))
        if not info:
            return False
        currents[self.last_y] = info[0]
        if len(self.block) > 1:
            currents[self.last_y-2] = info[1]
        else:
            currents[self.last_y-1] = info[1]

#
# Function to remove full row and add a point to the score
#
def check_removation():
    global score
    for _ in currents:
        full = '99999' in currents
        if full:
            score += 1
            currents.remove('99999')
            currents.insert(0,'00000')

# That code will continue playing till you lose
while True:
    chosen_block = choice(blocks)     
    The_Piece = Piece(chosen_block[0],chosen_block[1])  
    print(currents) 
    for i in currents:
        print(i)
    
    if The_Piece.lost:
        print("Game Over: Score: " + str(score))
        score = 0
        break

    run = True
    while run:
        res = The_Piece.move()
        if res == False:
            run = False
        print('-----------------------')
        for i in currents:
            print(i)
    check_removation()

