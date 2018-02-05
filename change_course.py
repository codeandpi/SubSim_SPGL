rudder = 0
heading = 90
wheel_over = int(input(">> Enter Wheel Setting "))
port_stbd = input('>> p or s')
desired_heading = int(input ('>> Desired Heading '))
rudder = wheel_over
count = 0
while rudder != 0 and heading != desired_heading:
    count += 1
    if port_stbd == 'p':
        heading -= rudder / 2

    if port_stbd == 's':
        heading += rudder / 2

    if heading < 0:
        heading += 360

    print (rudder, " ", heading, " ", count)




