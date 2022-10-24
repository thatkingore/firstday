monthCoversionbs = {
     "Jan": "January",
     "Feb": "February",
     "Mar": "March",
     "Apr": "April",
     "May": "May",
     "Jun": "June",
     "Jul": "July",
     "Aug": "August",
    "Sept": "September",
     "Oct": "October",
     "Nov": "November",
     "Dec": "December",
}

print(monthCoversionbs["Aug"])
print(monthCoversionbs.get("Dec"))
print(monthCoversionbs.get("Luv", "Not a valid key."))