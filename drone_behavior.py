from tile_behavior import prepare_plot, plant_crop, harvest_crop, plot_info
from farm_vars import plot_parsed, plot_pos_by_id

# ALL PASSED ARGS IN DRONESPACE


def move_drone():
    move(North)
    if get_pos_y() == 0:
        move(East)
        if get_pos_x() == 0:
            return True
    return False


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


def reset_farm():
    clear()
    for _ in range(get_world_size() * get_world_size()):
        plot_r, plot_c = drone_to_plot()
        crop, plot_id = plot_parsed[plot_r][plot_c]
        prepare_plot(crop, plot_r, plot_c, plot_id)
        plant_crop(crop, plot_r, plot_c, plot_id)
        move_drone()


def loop_farm():
    run_info = {}
    for plot_id in plot_pos_by_id:
        run_info[plot_id] = plot_info(True, drone_to_plot())
    for _ in range(get_world_size() * get_world_size()):
        plot_r, plot_c = drone_to_plot()
        crop, plot_id = plot_parsed[plot_r][plot_c]
        run_info[plot_id] = harvest_crop(
            crop, plot_r, plot_c, plot_id, run_info[plot_id]
        )
        move_drone()
