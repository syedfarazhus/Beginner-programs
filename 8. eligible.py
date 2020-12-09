def eligible(CGPA:float, Year:int, program:str) -> bool:
    """
    function that determines if a student is eligible for PEY
    A student is eligible for PEY if their CGPA is at least 2, they are
    in year 2 or year 3, and they are in a CS program
    """
    return CGPA >= 2 and Year == (2 or 3) and program == "CS"
