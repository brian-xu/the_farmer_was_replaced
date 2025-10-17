from plot_parser import hstack, vstack

carrot = (Entities.Carrot, 8, 4)
sunflower = (Entities.Sunflower, 8, 4)
block1 = hstack([sunflower, carrot, carrot, carrot, carrot, carrot, carrot, carrot])
block2 = vstack([block1, block1, block1, block1])

farm_block = block2
