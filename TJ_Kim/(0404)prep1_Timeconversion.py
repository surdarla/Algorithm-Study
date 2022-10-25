def timeConversion(s):
    hour = int(s[:2])
    min_sec = s[2:8]
    if s[-2:] == 'AM':
        hour = hour % 12
    else :
        hour = hour % 12 + 12

    return f"{hour:02}{min_sec}"
