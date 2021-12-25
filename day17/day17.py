x_bounds = (139, 187)
y_bounds = (-148, -89)

def get_positions(initial_x_velocity, initial_y_velocity):
    step = 0
    x, y = 0, 0
    stop = False
    found = []
    positions = []
    x_velocity = initial_x_velocity
    y_velocity = initial_y_velocity
    while not stop:
        x += x_velocity
        y += y_velocity

        positions.append((x,y))

        if x >= x_bounds[0] and x <= x_bounds[1] and y >= y_bounds[0] and y <= y_bounds[1]:
            stop = True
            if x == x_bounds[0] and y == y_bounds[0]:
                print("x bounds" + str(x_bounds[0]))
                print("y bounds" + str(y_bounds[0]))
                print((initial_x_velocity, initial_y_velocity))
            elif x == x_bounds[1] and y == y_bounds[0]:
                print("x bounds" + str(x_bounds[1]))
                print("y bounds" + str(y_bounds[0]))
                print((initial_x_velocity, initial_y_velocity))
            elif x == x_bounds[0] and y == y_bounds[1]:
                print("x bounds" + str(x_bounds[0]))
                print("y bounds" + str(y_bounds[1]))
                print((initial_x_velocity, initial_y_velocity))
            elif x == x_bounds[1] and y == y_bounds[1]:
                print("x bounds" + str(x_bounds[1]))
                print("y bounds" + str(y_bounds[1]))
                print((initial_x_velocity, initial_y_velocity))
            found.append((x,y))
        # drag
        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1

        # gravity
        y_velocity -= 1

        # current position
        # print((x,y))

        step += 1
        if step > 1000:
            stop = True
    if found != []:
        return (found, sorted(positions, key = lambda x: x[1])[::-1][0][1])
    else:
        return None

def find_velocities():
    all_found = []

    for x in range(189):
        for y in range(-149, 200):
            found = get_positions(x, y)
            if found:
                all_found.append((x, y, found))

    # part 1
    # print(sorted(all_found, key = lambda x: x[2][1])[::-1][0])

    # part 2
    print(len(all_found))

find_velocities()
#print(get_positions(18, 147))

# my part 1 answer - 10878
# my part 2 answer - 4716
