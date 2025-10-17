import re

def parse_time_expression(expression: str) -> tuple:
    print(expression)

    hour = 0
    hour_offset = 0
    minute = 0
    minute_offset = 0
    
    if type(expression) != str:
        raise Exception
    
    numbers_to_words = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
        }

    words_to_numbers = {value:key for key, value in numbers_to_words.items()}

    #Edge Cases:
    if expression[0:4] == 'noon':
        hour = 12
        return (hour, minute)
    elif expression[0:9] == 'midnight':
        return (hour, minute)
    
    # Time words
    expression = expression.lower()
    words = expression.split(' ')
    if len(words) == 3:
        if words[0] == 'quarter':
            minute_offset = 15
        elif words[0] == 'half':
            minute_offset = 30
        else:
            pass
        
        if words[1] == 'to':
            minute_offset *= -1
        
        minute += minute_offset
        try:
            hour = int(words[2])
        except:
            
            try:
                hour = words_to_numbers[words[2]]
            except:
                
                if words[2] == 'midnight':
                    hour = 0
                elif words[2] == 'noon':
                    hour = 12
        
        if minute < 0:
            hour -= 1
            minute += 60
            
        if hour < 0:
            hour += 24

        return (hour, minute)

    # Explicit 12AM statement
    if expression == '12 am' or expression == '12am':
        return (0, 0)

    time = re.split(r'[\:| ]', expression)
    print(time)

    if time[-1] == 'am':
        time.pop()

    if time[-1] == 'pm':  
        time.pop() 

     
        hour_offset = 12
        print(hour_offset)

    

    try:
        hour = int(time[0])
        if hour >= 24:
            return None

        hour += hour_offset
    except:
        return None

    if hour >= 24:
        hour -= 12
    if hour < 0:
        return None
    

    if len(time) == 2:
        
        minute = int(time[-1])

    if minute < 0:
        return None
    if minute >= 60:
        return None

    return (hour, minute)

    
    


"""print(parse_time_expression('noon'))
print(parse_time_expression('midnight'))
print(parse_time_expression('quarter to midnight'))
print(parse_time_expression('quarter to noon'))
print(parse_time_expression('quarter past midnight'))
print(parse_time_expression('quarter past noon'))
print(parse_time_expression('half past midnight'))
print(parse_time_expression('half past noon'))
print(parse_time_expression('quarter past 8'))
print(parse_time_expression('quarter past seven'))

print(parse_time_expression('12 PM'))
print(parse_time_expression('12 AM'))
print(parse_time_expression('12AM'))

print(parse_time_expression('3:30 PM'))
print(parse_time_expression('14:45'))
print(parse_time_expression('3 pm'))

print(parse_time_expression('3'))
print(parse_time_expression('14'))
print(parse_time_expression('three'))

print(parse_time_expression('Quarter Past midnight PM'))


print(parse_time_expression('-34:65'))
print(parse_time_expression('0'))
print(parse_time_expression('2:60 pm'))
print(parse_time_expression('25:40'))"""

