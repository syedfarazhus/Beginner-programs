from typing import List

def enrolled_teams(teams:List[List[int]], enrolled_students:List[int]) -> bool:
    """
    students uniquely identified by integers are broken into
    teams. Write a function to check that all team members are
    enrolled students.
    """
    for team in teams:
        for member in team:
            if member not in enrolled_students:
                return False
    return True
