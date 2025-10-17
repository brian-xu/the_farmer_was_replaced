from plot_parser import hstack, vstack

sunflower = (Entities.Sunflower, 8, 8)
block1 = hstack(
    [
        sunflower,
        sunflower,
        sunflower,
        sunflower,
        # sunflower,
        # sunflower,
        # sunflower,
        # sunflower,
    ]
)
block2 = vstack([block1, block1, block1, block1])

farm_block = block2
