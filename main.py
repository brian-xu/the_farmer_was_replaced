from drone_behavior import move_drone_to, loop_farm, reset_farm

reset_farm()
move_drone_to(0, 0)
while True:
    loop_farm()
