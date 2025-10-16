from farm_vars import plot_parsed, plot_pos_by_id

# ALL ARGS IN PLOTSPACE


def plot_info(valid, coord):
    return {"valid": valid, "coord": coord}


def water_tile():
    if get_water() < 0.5:
        use_item(Items.Water)


def prepare_plot(crop_type, r, c, plot_id):
    if crop_type == Entities.Grass:
        pass
    else:
        till()


def plant_crop(crop_type, r, c, plot_id):
    if crop_type == Entities.Grass:
        pass
    elif crop_type == Entities.Tree:
        water_tile()
        if (r + c) % 2 == 0:
            plant(Entities.Tree)
        else:
            plant(Entities.Bush)
    elif crop_type == Entities.Cactus:
        water_tile()
        plant(Entities.Cactus)
    elif crop_type == Entities.Bush:
        if (r + c) % 2 == 0:
            plant(Entities.Bush)
            use_item(Items.Weird_Substance)
            harvest()
        else:
            plant(Entities.Carrot)
    else:
        water_tile()
        plant(crop_type)
    return


def harvest_crop(crop_type, r, c, plot_id, run_info):
    retval = plot_info(run_info["valid"], run_info["coord"])
    if crop_type == Entities.Grass:
        harvest()
        return retval
    elif crop_type == Entities.Tree:
        harvest()
        plant_crop(crop_type, r, c, plot_id)
        return retval
    elif crop_type == Entities.Bush:
        plant_crop(crop_type, r, c, plot_id)
        return retval
    elif crop_type == Entities.Carrot:
        harvest()
        plant_crop(crop_type, r, c, plot_id)
        return retval
    elif crop_type == Entities.Pumpkin:
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()
            plant_crop(crop_type, r, c, plot_id)
            retval["valid"] = False
        elif run_info["valid"]:
            top, left, width, height = plot_pos_by_id[plot_id]
            if r == top and c == left + width - 1:
                harvest()
        if not can_harvest():
            plant_crop(crop_type, r, c, plot_id)
        return retval
    elif crop_type == Entities.Cactus:
        harvest()
        plant_crop(crop_type, r, c, plot_id)
        return retval
    elif crop_type == Entities.Sunflower:
        harvest()
        plant_crop(crop_type, r, c, plot_id)
        return retval
