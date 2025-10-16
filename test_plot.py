from plot_parser import hstack, vstack, parse_recursive

pumpkins = (Entities.Pumpkin, 6, 6)
sunflowers = (Entities.Sunflower, 4, 4)
hay = (Entities.Carrot, 2, 4)
block1 = vstack([sunflowers, hay])
block2 = hstack([pumpkins, block1, pumpkins])
carrots = (Entities.Carrot, 2, 16)
block3 = vstack([block2, carrots])
maze = (Entities.Bush, 8, 8)
trees = (Entities.Tree, 3, 8)
cactus = (Entities.Cactus, 3, 8)
hay2 = (Entities.Grass, 2, 8)
block4 = vstack([trees, cactus, hay2])
block5 = hstack([maze, block4])
block6 = vstack([block3, block5])

plot_parsed, plot_pos_by_id = parse_recursive(block6, True)
