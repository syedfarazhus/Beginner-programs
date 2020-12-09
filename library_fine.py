def library_fine(status:str, days_late:int) -> float:
	if status == "child":
		fine = 0.1 * days_late
		if fine > 5.0:
			return "$" + str(5.00)
		else:
			return "$" + str(round(fine, 3))
	elif status == "adult":
		fine = 0.25 * days_late
		return "$" + str(round(fine, 3))
	else:
		if status == "senior":
			fine = 0.25 * days_late
		if fine > 5.0:
			return "$" + str(5.00)
		else:
			return "$" + str(round(fine, 3))
