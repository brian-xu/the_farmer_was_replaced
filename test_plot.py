from plot_parser import hstack, vstack

maze = (Entities.Bush, 8, 8)
block1 = hstack([maze, maze, maze, maze])
block2 = vstack([block1, block1, block1, block1])

farm_block = block2
