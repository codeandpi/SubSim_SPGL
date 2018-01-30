# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import math

# Create Classes
# Changes

class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):

        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        self.score = 0
        self.pendown()
        self.pencolor('yellow')
        self.setheading(90)
        self.heading = 90
        self.position()
        #self.setheading(90)     # Turtle faces North
        #self.setheading(180)   # Turtle faces West
        #self.setheading(270)    # Turtle faces South
        # self.setheading(360)    # Turtle faces East
        #self.home()

    def tick(self):
        self.move()

    def move(self):
        # Draw a trail behind player


        self.fd(self.speed)
        # Wrap back to the other side of the screen
        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)


    def rotate_left(self):
        self.lt(30)
        self.heading -= 30
        if self.heading < 0:
            self.heading += 360

    def rotate_right(self):
        self.rt(30)
        self.heading += 30
        if self.heading > 360:
            self.heading -= 360

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
        if self.speed < 1:
            self.speed = 0.5
# Create Functions

# Initial Game setup

game = spgl.Game(1200, 900, "black", "SPGL Minimum Code Example by /u/wynand1004 AKA @TokyoEdTech",splash_time=3)


game.highscore = 110
heading = Player.heading
position = Player.position

# Create Sprites

# Create Player
player = Player("triangle", "white", 0, 0)

# Create Labels
score_label = spgl.Label("Score: 0 Highscore: {}".format(game.highscore), "white", -570, 324)

# Create Buttons


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_DOWN, player.decelerate)
game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)


while True:
    # Call the game tick method
    game.tick()

    speed_string = "-" * int(player.speed)
    # speed_string2 =  int(player.speed)
    speed_string2 = int(player.heading)
    position_string = str(player.pos())

    score_label.update( " Position:{} \n High Score:{} \n Speed:{} \n Heading:{}".format(position_string,
                                                                            game.highscore,speed_string,
                                                                                           speed_string2))
