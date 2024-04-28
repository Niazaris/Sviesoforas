with open("data.txt", "r") as file:
    lines = file.readlines()

red_values = []
yellow_values = []
green_values = []
time_active_values = []
time_values = []

for line in lines [1:]:
    values = line.strip().split(",")
    red_values.append(int(values[0]))
    yellow_values.append(int(values[1]))
    green_values.append(int(values[2]))
    time_active_values.append(int(values[3]))
    time_values.append(values[4])

def light_occurrence():
    red_occurrence = 0
    yellow_occurrence = 0
    green_occurrence = 0
    for value in red_values:
        if value == 1:
            red_occurrence += 1
    for value in yellow_values:
        if value == 1:
            yellow_occurrence += 1
    for value in green_values:
        if value == 1:
            green_occurrence += 1
    return red_occurrence, yellow_occurrence, green_occurrence

def total_active_time():
    red_time = 0
    yellow_time = 0
    green_time = 0
    for i in range(len(red_values)):
        if red_values[i] == 1:
            red_time += time_active_values[i]
        if yellow_values[i] == 1:
            yellow_time += time_active_values[i]
        if green_values[i] == 1:
            green_time += time_active_values[i]
    return red_time, yellow_time, green_time

def green_atcive_timestamps():
    green_timestamps = []
    for i in range(len(green_values)):
        if green_values[i] == 1:
            green_timestamps.append(time_values[i])
    return green_timestamps

def total_complete_cycles():
    cycle_count = 0
    i = 0
    while i < len(red_values) - 4:
        if (
            red_values[i] == 1
            and yellow_values[i + 1] == 1
            and green_values[i + 2] == 1
            and yellow_values[i + 3] == 1
            and red_values[i + 4] == 1
        ):
            cycle_count += 1
            i += 5  
        else:
            i += 1
    return cycle_count

def mistake_calculation():
    mistakes = 0
    for i in range(len(red_values)):
        if (red_values[i] == 1 and (yellow_values[i] == 1 or green_values[i] == 1)):
            mistakes += 1
        elif (yellow_values[i] == 1 and (red_values[i] == 1 or green_values[i] == 1)):
            mistakes += 1
        elif (green_values[i] == 1 and (red_values[i] == 1 or yellow_values[i] == 1)):
            mistakes += 1
        elif (red_values[i] == 0 and yellow_values[i] == 0 and green_values[i] == 0):
            mistakes += 1
    return mistakes

#print(f'There are {light_occurrence()[0]} red light, {light_occurrence()[1]} yellow light and {light_occurrence()[2]} green light occurrences')
#print(f'Red light was active for {total_active_time()[0]} seconds, yellow for {total_active_time()[1]} seconds and green for {total_active_time()[2]} seconds')
#print(f'Timestamps when green light was active are: {green_atcive_timestamps()}')
#print(f'There are a total of {total_complete_cycles()} cycles completed')
#print(f'There are a total of {mistake_calculation()} mistakes')