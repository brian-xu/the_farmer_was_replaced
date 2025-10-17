from farm_vars import plot_parsed, plot_pos_by_id
from drone_behavior import move_drone_to, loop_farm, prepare_loop, serpentine_path

clear()

for plot_id in plot_pos_by_id:
    top, left, height, width = plot_pos_by_id[plot_id]
    crop, _ = plot_parsed[top][left]
    bottom = get_world_size() - top - height
    path = serpentine_path(height, width)

    def task():
        move_drone_to(bottom, left)
        prepare_loop(path, crop)
        while True:
            loop_farm(path, crop, plot_id)

    if not spawn_drone(task):
        quick_print("all drones used :)")
        task()

quick_print(num_drones(), "drones used")
