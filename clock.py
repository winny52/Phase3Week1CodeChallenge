def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)

    return f"{hour_str}{minute_str}"

# Test cases
hour = 8
minute = 30
period = "am"
print(convert_to_24_hour(hour, minute, period))  

hour = 3
minute = 45
period = "pm"
print(convert_to_24_hour(hour, minute, period))  
