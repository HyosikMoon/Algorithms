def date_time(time: str) -> str:
    # replace this for solution
    # date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    day = str(int(time[:2]))
    month = int(time[3:5])
    year = str(int(time[6:10]))
    hour = str(int(time[11:13]))
    min = str(int(time[14:]))

    dictMonth = {1:'January', 2:"Feburary", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"Octobor", 11:"November", 12:"December"}
    strhour, strmin = '', ''

    # 1 hour
    if hour == '1': strhour = ' hour '
    else: strhour = ' hours ' 

    # 1 minute
    if min == '1': strmin = ' minute'
    else: strmin = ' minutes'  

    return day + ' ' + dictMonth[month] + ' ' + year + ' year ' + hour + strhour + min + strmin

print(date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes")