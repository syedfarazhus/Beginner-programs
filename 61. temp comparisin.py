from typing import List

def hotter_daily_temps(temps_then, temps_now):
    i = 0
    change = []
    while i < len(temps_then):
        if temps_then[i] < temps_now[i]:
            change.append("Hotter")
        else:
            change.append("Not Hotter")
    return change
