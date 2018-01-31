# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

# Import SPGL
import spgl
import math
import random

# Create Classes
class Player(spgl.Sprite):
    depth = 100

    def __init__(self, shape, color, x, y):

        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        # self.score = 0
        self.pendown()
        self.pencolor('yellow')
        self.setheading(90)
        self.heading = 90
        self.position()
        self.rudder = 10 # default rudder setting


    def tick(self):
        self.move()

    def move(self):
        # Draw a trail behind player
        self.fd(self.speed)

        # Wrap back to the other side of the screen
        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())
            self.clear()
        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())
            self.clear()
        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)
            self.clear()
        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)
            self.clear()
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
        """ The depth up function """
        Player.depth -= 50
        if Player.depth < 0:
            Player.depth = 0

    def depth_down(self):
        """ The depth down function, this needs to include some check
        for the crush depth and seabed """
        Player.depth += 50

class Enemy(spgl.Sprite):
    depth = 150
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 2
        self.setheading(180)
        self.heading = 180
        self.rudder = 30
        self.depth = 100
        self.name = "Crazy Ivan"
        self.pendown()
        self.pencolor('red')

    def tick(self):
        self.move()

    def move(self):
        self.fd(self.speed)

        # Calls crazy ivan random maneuvers though would like it to be more random
        coin = random.randrange(0, 100)
        if coin == 0:  # heads
            self.crazy_ivan()
        elif coin == 1:
            pass


        # Wrap back to the other side of the screen
        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())
            self.clear()
        if self.xcor() < -game.SCREEN_WIDTH / 2:
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())
            self.clear()
        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)
            self.clear()
        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)
            self.clear()

    def rotate_left(self):
        self.heading -= self.rudder
        self.lt(90)
        if self.heading < 0:
            self.heading += 360

    def rotate_right(self):
        self.heading += self.rudder
        self.rt(90)
        if self.heading > 360:
            self.heading -= 360

    def crazy_ivan(self):
    # This does a random# change of course leaping 30 degrees left or right off original course
        toss = random.randrange(10, 30, 5)
        coin = random.randrange(0, 2)
        if coin == 0:  # heads
            self.heading -= toss
            self.lt(toss)
        elif coin == 1:  # tails
            self.heading += self.rudder
            self.rt(self.rudder)
        else:
            self.heading = self.setheading(180)

        if self.heading < 0:
            self.heading += 360
        if self.heading > 360:
            self.heading -= 360


# Initial Game setup
game = spgl.Game(1200, 1200, "black", "SPGL Minimum Code Example by /u/wynand1004 AKA @TokyoEdTech",splash_time=3)
heading = Player.heading
#position = Player.position
depth = Player.depth
enemy_heading = Enemy.heading

# Create Sprites
# Create Enemy
enemy = Enemy("square", "brown", 300, 500)
# Create Player
player = Player("triangle", "white", 0, 0)

# Create Labels
navigation_label = spgl.Label("Current: \nHeading: Heading: {}".format(Player.heading), "Green", -550, 450)
orders_label = spgl.Label("Ordered: \nHeading:  {}".format(heading), "Yellow",400, 450)
tracking_label = spgl.Label("Contact Data: \nHeading: Heading  {}".format(Enemy.heading), "Red", -400, -450)
# Create Buttons


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_DOWN, player.decelerate)
game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)

game.set_keyboard_binding(spgl.KEY_U, player.depth_up)
game.set_keyboard_binding(spgl.KEY_D, player.depth_down)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)


while True:
    # Call the game tick method
    game.tick()


    # position_string = str(player.pos())
    # speed_string = "-" * int(player.speed)

    speed_string2 = str(player.speed)
    heading_string = int(player.heading)
    enemy_speed_string = str(enemy.speed)
    enemy_heading = int(enemy.heading)
    #navigation_label.update(" Current: \n Position:{} \n Depth:{} \n Speed:{} \n Heading:{}"
                            #.format(position_string, Player.depth, speed_string2, heading_string))

    navigation_label.update(" Current:  \n Depth:{} \n Speed:{} \n Heading:{}"
                            .format(Player.depth, speed_string2, heading_string))
    orders_label.update(" Ordered: \n Depth:{} \n Speed:{} \n Heading:{}"
                        .format(Player.depth, speed_string2, heading_string))

    tracking_label.update(" Contact Data: \n Depth:{} \n Speed:{} \n Heading:{}"
                        .format(Enemy.depth, enemy_speed_string, enemy_heading))

    # show game info in terminal

    game.clear_terminal_screen()
    game.print_game_info()