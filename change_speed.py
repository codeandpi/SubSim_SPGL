max_speed = 30
min_speed = .1
desired_speed = int(input('>> Set Speed >>>  '))
current_speed = 10
count = 0
while current_speed != desired_speed:
    count += 1
    if desired_speed > max_speed:
        desired_speed = max_speed
    if desired_speed < min_speed:
        desired_speed = min_speed

    if desired_speed != current_speed:
        current_speed += 0.45


    print (current_speed," ",desired_speed, " ", count)
