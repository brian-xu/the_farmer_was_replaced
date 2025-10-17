from plot_parser import hstack, vstack

cactus = (Entities.Cactus, 7, 7)
row = (Entities.Grass, 1, 7)
block1 = vstack([cactus, row, cactus])
col = (Entities.Grass, 15, 1)
block2 = hstack([block1, col, block1])
row2 = (Entities.Grass, 2, 15)
block3 = vstack([block2, row2, block2])
col2 = (Entities.Grass, 32, 2)
block4 = hstack([block3, col2, block3])

farm_block = block4

# cactus = (Entities.Cactus, 8, 8)
# farm_block = hstack([cactus])
