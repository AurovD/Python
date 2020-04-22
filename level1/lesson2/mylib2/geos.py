def area_of_disk(radius):
    return 3.14 * radius ** 2

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)
