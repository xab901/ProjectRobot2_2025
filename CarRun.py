def on_forever():
    basic.show_arrow(ArrowNames.SOUTH)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_RUN)
    basic.pause(1000)
    basic.show_arrow(ArrowNames.NORTH)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_BACK)
    basic.pause(1000)
    basic.show_arrow(ArrowNames.EAST)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_SPINLEFT)
    basic.pause(1000)
    basic.show_arrow(ArrowNames.WEST)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_SPINRIGHT)
    basic.pause(1000)
    basic.show_leds("""
                    . . # . .
                    . # # # .
                    # # # # #
                    # # # # #
                    . # . # .
                    """)
    Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
    basic.pause(1000)
basic.forever(on_forever)