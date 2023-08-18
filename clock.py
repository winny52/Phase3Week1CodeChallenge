def convert_to_24_hour(hour, minute, period):
    if period == "am" and hour == 12:
        hour_24 = 0
    elif period == "pm" and hour != 12:
        hour_24 = hour + 12
    else:
        hour_24 = hour
        
    return f"{hour_24:02d}{minute:02d}"

# Test cases
print(convert_to_24_hour(8, 30, "am"))   
print(convert_to_24_hour(8, 30, "pm"))  
print(convert_to_24_hour(12, 15, "am"))  
print(convert_to_24_hour(12, 15, "pm"))  
