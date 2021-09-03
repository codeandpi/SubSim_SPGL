# SPGL Minimal Code by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Use this as the starting point for your own games

import math
import random
from turtle import towards
import spgl
import numpy as np

rudder_multiplier = 4
# Create Classes
class Player(spgl.Sprite):
    depth = 100
    rudder = 0
    desired_speed = 0
    max_speed = 30
    min_speed = .1

    def __init__(self, shape, color, x, y):

        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 1
        # self.score = 0
        self.pendown()
        self.pencolor('yellow')
        self.setheading(90)
        self.heading = 90
        self.position()
        self.rudder = 0 # default rudder setting should remain at 0 at game start

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

    # Key binding "c".
    # This produces a reasonable turning circle though not sure on its accuracy
    def change_course(self):

        while self.rudder != 0 :
            self.heading -= self.rudder / rudder_multiplier
            self.lt(self.rudder / rudder_multiplier)
            if self.heading < 0:
                self.heading += 360

            break

    # Key binding "r"
    # This changes the setting of the rudder by 5 degrees each press
    def set_rudder(self):
        self.rudder += 5

    # Key binding "a"
    # This sets the rudder back to zero ie 'Wheel amidships'
    def set_amidshps(self):
        self.rudder = 0

    def rotate_left(self):

            self.heading -= self.rudder / rudder_multiplier
            self.lt(self.rudder / rudder_multiplier)
            if self.heading < 0:
                self.heading += 360



    def rotate_right(self):

            self.heading += self.rudder / rudder_multiplier
            self.rt(self.rudder / rudder_multiplier)
            if self.heading > 360:
                self.heading -= 360




    def accelerate(self):
        if self.speed == 0.1:
            self.speed = 1
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
        if self.speed < 1:
            self.speed = 0.1


# Create Functions

    def depth_up(self):
        Player.depth -= 50
        if Player.depth < 0:
            Player.depth = 0

    def depth_down(self):
        Player.depth += 50

    def desired_knots(self):

        self.desired_speed += 1
        if self.desired_speed > self.max_speed:
            self.desired_speed = self.max_speed
        if self.desired_speed < self.min_speed:
            self.desired_speed = self.min_speed
        if self .desired_speed > self.speed:
            self.speed += 0.45
            if self.speed > self.desired_speed:
                self.speed = self.desired_speed
class Enemy(spgl.Sprite):
    depth = 150

    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 0
        self.setheading(180)
        self.heading = 180
        self.rudder = 10
        self.depth = 100
        self.name = "Crazy Ivan"
        self.pendown()
        self.pencolor('red')

    def tick(self):
        self.move()

    def move(self):
        self.fd(self.speed)

        #Calls crazy ivan random maneuvers though would like it to be more random
        #coin = random.randrange(0, 100)
        #if coin == 0:  # heads
                # self.crazy_ivan()
        #elif coin == 1:
            #pass

        """ Wrap back to the other side of the screen.  Not sure I like this as the wrap at top 
         corners looks silly.  My just drop the contact when  the go off screen"""
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
game = spgl.Game(800, 600, "black", "SPGL Minimum Code Example by /u/wynand1004 AKA @TokyoEdTech",splash_time=3)
heading = Player.heading
depth = Player.depth
enemy_heading = Enemy.heading
rudder = Player.rudder
desired = Player.desired_speed

# Create Sprites
# Create Enemy
enemy = Enemy("square", "brown", 0, 0)
# Create Player
player = Player("triangle", "white", 0 , 0)
#player = Player("triangle", "white", -game.SCREEN_WIDTH / 2 , game.SCREEN_HEIGHT / 2 -1000)

# Create Labels

navigation_label = spgl.Label("Current: \nHeading: Heading: {}".format(Player.heading), "Green"
                              , -game.SCREEN_WIDTH / 2 + 10, game.SCREEN_HEIGHT / 2 - 100)

tracking_label = spgl.Label("Contact Data: \nHeading: Heading  {}".format(Enemy.heading), "Red", -game.SCREEN_WIDTH
                            /2 + 10, game.SCREEN_HEIGHT / 2 - 300)
# Create Buttons


# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_DOWN, player.decelerate)

game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(spgl.KEY_C, player.change_course)
game.set_keyboard_binding(spgl.KEY_R, player.set_rudder)
game.set_keyboard_binding(spgl.KEY_A, player.set_amidshps)
game.set_keyboard_binding(spgl.KEY_S, player.desired_speed)


game.set_keyboard_binding(spgl.KEY_U, player.depth_up)
game.set_keyboard_binding(spgl.KEY_D, player.depth_down)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)


while True:
    # Call the game tick method
    game.tick()

    # Calculate the distance between two objects need to put this in a function
    # def contact_range(contact.xcor, player.xcor):
       # vx = enemy.xcor() - player.xcor()
        #if vx == 0:
            #vx = 0.01
        #vy = enemy.ycor() - player.ycor()
        #distance = int(math.sqrt((vx ** 2) + (vy ** 2)))

    vx = enemy.xcor() - player.xcor()
    if vx == 0:
        vx = 0.01
    vy = enemy.ycor() - player.ycor()
    distance = int(math.sqrt((vx**2) + (vy**2)))

    # Calculate the bearing of target from player
    # Problems when ship in SE quadrant bearing way out
    
    myradians = math.atan2(vy, vx) - math.pi/2
    
    #target_bearing = int(abs(math.degrees(myradians)))
    target_bearing = towards(vx,vy)
    print (myradians ,target_bearing)

    if distance > 1200:
        enemy.color('blue')
        pass


    speed_string2 = int(player.speed)
    heading_string = int(player.heading)
    enemy_speed_string = str(enemy.speed)
    enemy_heading = int(enemy.heading)
    rudder = int(player.rudder)
    desired = int(player.desired_speed)

    navigation_label.update(" Current:  \n Depth:{} \n Speed:{} \n Heading:{} \n Rudder:{} "
                            .format(Player.depth, speed_string2, heading_string, rudder))
    tracking_label.update(" Contact Data: \n Depth:{} \n Speed:{} \n Heading:{} \n Desired {} \n Distance {} \n "
                          "Bearing {} \n "
                        .format(Enemy.depth, enemy_speed_string, enemy_heading, desired, distance, target_bearing))

# show game info in terminal

#game.clear_terminal_screen()
# game.print_game_info()

# Tried but not used stuff
# position_string = str(player.pos())
# speed_string = "-" * int(player.speed)
# orders_label.update(" Ordered: \n Depth:{} \n Speed:{} \n Heading:{} \n Rudder:{} "
# .format(Player.depth, speed_string2, heading_string, rudder))

#navigation_label.update(" Current: \n Position:{} \n Depth:{} \n Speed:{} \n Heading:{}"
#.format(position_string, Player.depth, speed_string2, heading_string))

#orders_label = spgl.Label("Ordered: \nHeading:  {}".format(heading), "Yellow"
                          #,-game.SCREEN_WIDTH / 2 + 10, game.SCREEN_HEIGHT / 2 - 200)