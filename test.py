def walk_r(steps):
    if steps == 5:
        return steps
    return walk_r(steps + 1) + 1


print(walk_r(1))