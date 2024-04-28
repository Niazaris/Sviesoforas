import math

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

