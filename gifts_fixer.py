# Creating a function to fix gifts
def toy_fixer(toys):
    fixed_toy = []
    for toy in toys:
        if "#" not in toy:
            fixed_toy.append(toy)
    return fixed_toy


