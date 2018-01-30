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
    depth = 100

    def __init__(self, shape, color, x, y):

        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        self.score = 0
        self.pendown()
        self.pencolor('yellow')
        self.setheading(90)
        self.heading = 90
        self.position()
        self.rudder = 5 # default rudder setting


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

    # This keypress will alter the course to Port by using the default rudder
    # value of 5 degrees per press.
    """Would like to improve this so that when the key is pressed the rudder setting
     is constantly added to the heading until the wheel is set to amidships.  Would 
     also like to see the label updated to show how much rudder is set"""

    def rotate_left(self):
        self.heading -= self.rudder
        self.lt(self.rudder)
        if self.heading < 0:
            self.heading += 360

    # This keypress will alter the course to Stb by using the default rudder
    # value of 5 degrees per press.

    def rotate_right(self):
        self.heading += self.rudder
        self.rt(self.rudder)
        if self.heading > 360:
            self.heading -= 360

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
        if self.speed < 1:
            self.speed = 0.5



# Create Functions
    def depth_up(self):
        Player.depth += 50

    def depth_down(self):
        Player.depth -= 50
# Initial Game setup
game = spgl.Game(1200, 900, "black", "SPGL Minimum Code Example by /u/wynand1004 AKA @TokyoEdTech",splash_time=3)
game.highscore = 110
heading = Player.heading
position = Player.position
depth = Player.depth

# Create Sprites

# Create Player
player = Player("triangle", "white", 0, 0)

# Create Labels
score_label = spgl.Label("Score: 0 Highscore: {}".format(Player.heading), "Yellow", -570, 324)

# Create Buttons


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_DOWN, player.decelerate)
game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)

game.set_keyboard_binding(spgl.KEY_ALT_LEFT, player.depth_up)
game.set_keyboard_binding(spgl.KEY_ALT_RIGHT, player.depth_down)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)


while True:
    # Call the game tick method
    game.tick()

    # speed_string = "-" * int(player.speed)
    speed_string2 =  str(player.speed)
    heading_string = int(player.heading)
    position_string = str(player.pos())

    score_label.update( " Position:{} \n Depth:{} \n Speed:{} \n Heading:{}".format(position_string,
                                                                            Player.depth,speed_string2,
                                                                                           heading_string))
