from plot_parser import hstack, vstack, parse_recursive

pumpkins = (Entities.Pumpkin, 6, 6)
sunflowers = (Entities.Sunflower, 4, 4)
hay = (Entities.Grass, 2, 4)
block5 = vstack([sunflowers, hay])
block1 = hstack([pumpkins, block5, pumpkins])
maze = (Entities.Bush, 4, 16)
trees = (Entities.Tree, 4, 4)
block2 = vstack([hay, trees])
block3 = hstack([pumpkins, block2, pumpkins])
block4 = vstack([block1, maze, block3])

plot_parsed, plot_pos_by_id = parse_recursive(block4, True)
