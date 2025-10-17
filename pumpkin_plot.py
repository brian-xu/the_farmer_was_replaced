from plot_parser import hstack, vstack

pumpkin = (Entities.Pumpkin, 6, 6)
cactus = (Entities.Cactus, 2, 6)
block1 = vstack([pumpkin, cactus, pumpkin, cactus, pumpkin, cactus, pumpkin, cactus])
sunflower = (Entities.Sunflower, 32, 2)
block2 = hstack([block1, sunflower, block1, sunflower, block1, sunflower])
cactus2 = (Entities.Cactus, 8, 8)
maze = (Entities.Bush, 8, 8)
block3 = vstack([cactus2, maze, cactus2, maze])
block4 = hstack([block2, block3])

farm_block = block4
