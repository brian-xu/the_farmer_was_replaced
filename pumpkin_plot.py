from plot_parser import hstack, vstack, parse_recursive

pumpkins = (Entities.Pumpkin, 6, 6)
sunflowers = (Entities.Sunflower, 2, 6)
cactus2 = (Entities.Cactus, 2, 6)
block1 = vstack(
    [pumpkins, sunflowers, pumpkins, sunflowers, pumpkins, cactus2, pumpkins, cactus2]
)
maze = (Entities.Bush, 32, 2)
maze3 = (Entities.Bush, 32, 3)
maze2 = (Entities.Bush, 16, 4)
trees = (Entities.Tree, 8, 4)
cactus = (Entities.Cactus, 8, 4)
block3 = vstack([maze2, trees, cactus])
block4 = hstack([block1, maze, block1, maze, block1, maze3, block3, maze3])

farm_block = block4
