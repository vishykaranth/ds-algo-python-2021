# Given and array representing heights of buildings.
# The array has buildings from left to right.
# Count number of building facing sunset.
# It is assumed that heights of all buildings are distinct.


def buildingFacingSunset(buildings):
    count = 1
    current = buildings[0]
    for index in range(1, len(buildings)):
        if buildings[index] > current:
            current = buildings[index]
            count += 1

    return count


print(buildingFacingSunset([7, 4, 8, 2, 9]))