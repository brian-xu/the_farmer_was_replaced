from plot_parser import hstack, vstack

maze = (Entities.Bush, 7, 7)
block1 = hstack([maze, maze, maze, maze])
block2 = vstack([block1, block1, block1, block1])
left = (Entities.Grass, 28, 4)
bottom = (Entities.Grass, 4, 32)
block3 = hstack([block2, left])
block4 = vstack([block3, bottom])

farm_block = hstack([(Entities.Bush, 32, 32)])
