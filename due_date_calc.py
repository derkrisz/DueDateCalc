days = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')

def get_am_pm(input):
    split_input = input.split()
    upper_am_pm = split_input[2]
    if (upper_am_pm != 'PM' and upper_am_pm != 'AM'):
        raise ValueError('Time of day should be AM or PM')
    return upper_am_pm

def get_time(input):
    split_input = input.split()
    time = split_input[1].split(':')
    if (1 <= int(time[0]) > 12):
        raise ValueError('Hours should be between 1 and 12')
    if (0 <= int(time[1]) > 59):
        raise ValueError('Minutes should be between 0 and 60')
    return time

def get_day(input):
    split_input = input.split()
    day_upper = split_input[0].upper()
    if (day_upper not in days):
        raise ValueError("Day should be a day of the week e.g. 'Monday', 'Tuesday'")
    return day_upper



