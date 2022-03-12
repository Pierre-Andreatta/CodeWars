def tower_builder(n_floors):
    floors = []
    wide = (n_floors*2)-1
    for r in range(n_floors):
        star = ((r+1)*2)-1
        edge = (wide-star)//2
        floors.append(" "*int(edge)+"*"*int(star)+" "*int(edge))
    return floors