from tile_behavior import (
    prepare_plot,
    plant_crop,
    harvest_crop,
    plot_info,
    solve_maze,
    sort_cactus,
)
from farm_vars import plot_parsed, plot_pos_by_id

# ALL PASSED ARGS IN DRONESPACE


def move_drone():
    move(North)
    if get_pos_y() == 0:
        move(East)
        if get_pos_x() == 0:
            return True
    return False


def serpentine_path(height, width):
    path = []
    height_adj = height - 1
    width_adj = width - 1

    def flip_dir(dir):
        if dir == East:
            return West
        else:
            return East

    dir = East

    if width == 2:
        for i in range(height_adj):
            path.append(North)
        path.append(dir)
        for i in range(height_adj):
            path.append(South)
    else:
        for i in range(height_adj):
            path.append(North)
        for j in range(width_adj):
            path.append(dir)
        dir = flip_dir(dir)
        for i in range(height_adj):
            path.append(South)
            for j in range(width_adj - 1):
                path.append(dir)
            dir = flip_dir(dir)
        path.append(West)
    return path


def move_drone_to(target_r, target_c):
    while get_pos_y() != target_r or get_pos_x() != target_c:
        r_diff = target_r - get_pos_y()
        c_diff = target_c - get_pos_x()
        wrap_size = get_world_size() // 2
        if r_diff == 0:
            pass
        elif (r_diff > 0 and r_diff < wrap_size) or -r_diff > wrap_size:
            move(North)
        else:
            move(South)
        if c_diff == 0:
            pass
        elif (c_diff > 0 and c_diff < wrap_size) or -c_diff > wrap_size:
            move(East)
        else:
            move(West)


def drone_to_plot():
    return [get_world_size() - 1 - get_pos_y(), get_pos_x()]


def prepare_loop(path, crop):
    for dir in path:
        plot_r, plot_c = drone_to_plot()
        prepare_plot(crop, plot_r, plot_c)
        plant_crop(crop, plot_r, plot_c)
        move(dir)


def loop_farm(path, crop, plot_id):
    top, left, height, width = plot_pos_by_id[plot_id]
    if crop == Entities.Bush:
        solve_maze(height)
        return
    bottom = get_world_size() - top - height
    move_drone_to(bottom, left)
    run_info = plot_info(True, drone_to_plot())
    for dir in path:
        plot_r, plot_c = drone_to_plot()
        run_info = harvest_crop(crop, plot_r, plot_c, run_info)
        move(dir)
    if crop == Entities.Pumpkin and run_info["valid"]:
        harvest()
    if crop == Entities.Cactus:
        sort_cactus(height, width)
