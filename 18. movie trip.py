def movie_trip(adult:int, child:int, is_matinee:bool) -> int:
    if is_matinee:
        if adult > child:
            deal = adult - child
            cost = deal * 10
            return cost
        elif child > adult:
            deal = child - adult
            cost = deal * 8
            return cost
        else:
            cost = adult * 10 + child * 8
            return cost
    else:
        if adult > child:
            deal = adult - child
            cost = deal * 12
            return cost
        elif child > adult:
            deal = child - adult
            cost = deal * 8
            return cost
        else:
            cost = adult * 12 + child * 8
            return cost
            
