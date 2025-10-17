# ALL ARGS IN PLOTSPACE


def plot_info(valid, coord):
    return {"valid": valid, "coord": coord}


def water_tile():
    if get_water() < 0.5:
        use_item(Items.Water)


def prepare_plot(crop_type, r, c):
    if crop_type == Entities.Grass:
        pass
    elif crop_type == Entities.Bush:
        pass
    else:
        till()


def plant_crop(crop_type, r, c):
    if crop_type == Entities.Grass:
        pass
    elif crop_type == Entities.Bush:
        pass
    elif crop_type == Entities.Tree:
        water_tile()
        if (r + c) % 2 == 0:
            plant(Entities.Tree)
        else:
            plant(Entities.Bush)
    else:
        water_tile()
        plant(crop_type)
    return


def spawn_maze(size):
    plant(Entities.Bush)
    substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)


def harvest_crop(crop_type, r, c, run_info):
    retval = plot_info(run_info["valid"], run_info["coord"])
    if crop_type == Entities.Grass:
        harvest()
        return retval
    elif crop_type == Entities.Tree:
        harvest()
        plant_crop(crop_type, r, c)
        return retval
    elif crop_type == Entities.Bush:
        quick_print("maze should never be passed to harvest_crop!")
        x = 5 / 0
    elif crop_type == Entities.Carrot:
        harvest()
        plant_crop(crop_type, r, c)
        return retval
    elif crop_type == Entities.Pumpkin:
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()
            retval["valid"] = False
        plant_crop(crop_type, r, c)
        return retval
    elif crop_type == Entities.Cactus:
        plant_crop(crop_type, r, c)
        return retval
    elif crop_type == Entities.Sunflower:
        harvest()
        plant_crop(crop_type, r, c)
        return retval
