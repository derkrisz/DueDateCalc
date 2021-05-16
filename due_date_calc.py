days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
hours = (1, 2, 3, 4, 5, 9, 10, 11, 12)

def get_am_pm(input):
    split_input = input.split()
    upper_am_pm = split_input[2]
    if upper_am_pm != 'PM' and upper_am_pm != 'AM':
        raise ValueError('Time of day should be AM or PM')
    return upper_am_pm

def get_time(input):
    split_input = input.split()
    time = list(map(int, split_input[1].split(':')))
    if time[0] not in hours:
        raise ValueError('Hours should fall between working hours: 9 AM to 5 PM')
    if 0 <= time[1] > 59:
        raise ValueError('Minutes should be between 0 and 60')
    if time[1] == 0:
        time.append(0)
    return time

def get_day(input):
    split_input = input.split()
    day = split_input[0]
    capitalized = day.capitalize()
    if capitalized not in days:
        raise ValueError("Day should be a day of the week e.g. 'Monday', 'Tuesday'")
    return capitalized

def calculate_turnaround_time(turnaround_time):
    return int(turnaround_time / 12), turnaround_time % 12

def calculate_due_date(date, turnaround_time):
    
    day = get_day(date)

    time = get_time(date)

    time_of_day = get_am_pm(date)

    turnaround = calculate_turnaround_time(turnaround_time)

    due_date_time = time[0] + turnaround[1]

    return f'{day} {due_date_time}:{time[1]}{time[2]} {time_of_day}'

    



    

    





