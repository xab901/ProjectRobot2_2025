def on_button_pressed_a():
    global a
    a += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global b
    b = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

b = 0
a = 0
b = 0

def on_forever():
    global a
    if a == 5:
        a = 1
basic.forever(on_forever)

def on_forever2():
    global b
    if a == 4:
        basic.show_leds("""
            # # # # #
            . . . # .
            . . # . .
            . # . . .
            # # # # #
            """)
        if b == 1:
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1100)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 55)
            basic.pause(600)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1300)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 60)
            basic.pause(850)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 60)
            basic.pause(1300)
            b = 0
basic.forever(on_forever2)

def on_forever3():
    global b
    if a == 3:
        basic.show_leds("""
            # # . . .
            # . # . .
            # . . # .
            # . . . #
            # # # # #
            """)
        if b == 1:
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 65)
            basic.pause(400)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 55)
            basic.pause(800)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1200)
            b = 0
basic.forever(on_forever3)

def on_forever4():
    global b
    if a == 2:
        basic.show_leds("""
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            """)
        if b == 1:
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 65)
            basic.pause(400)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 65)
            basic.pause(400)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 65)
            basic.pause(400)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
            b = 0
basic.forever(on_forever4)

def on_forever5():
    global b
    if a == 1:
        basic.show_leds("""
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # # # # #
            """)
        if b == 1:
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 65)
            basic.pause(400)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 80)
            basic.pause(1000)
            Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
            b = 0
basic.forever(on_forever5)