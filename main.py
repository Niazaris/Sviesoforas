class TrafficLight:
    def __init__(self, file_path, delimiter=','):
        self.red_values = []
        self.yellow_values = []
        self.green_values = []
        self.time_active_values = []
        self.time_values = []
        self.delimiter = delimiter
        self.load_data(file_path)

    def load_data(self, file_path):
        try:
            with open(file_path, "r") as file:
                next(file)
                for line in file:
                    values = line.strip().split(self.delimiter)
                    if len(values) == 5:
                        self.red_values.append(int(values[0]))
                        self.yellow_values.append(int(values[1]))
                        self.green_values.append(int(values[2]))
                        self.time_active_values.append(int(values[3]))
                        self.time_values.append(values[4])
                    else:
                        raise ValueError(f"Incomplete data record: {line}")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")

    def light_occurrence(self):
        red_occurrence = sum(1 for value in self.red_values if value == 1)
        yellow_occurrence = sum(1 for value in self.yellow_values if value == 1)
        green_occurrence = sum(1 for value in self.green_values if value == 1)
        return red_occurrence, yellow_occurrence, green_occurrence

    def total_active_time(self):
        red_time = sum(time for time, value in zip(self.time_active_values, self.red_values) if value == 1)
        yellow_time = sum(time for time, value in zip(self.time_active_values, self.yellow_values) if value == 1)
        green_time = sum(time for time, value in zip(self.time_active_values, self.green_values) if value == 1)
        return red_time, yellow_time, green_time

    def green_active_timestamps(self):
        return [timestamp for timestamp, value in zip(self.time_values, self.green_values) if value == 1]

    def total_complete_cycles(self):
        cycle_count = 0
        i = 0
        length = len(self.red_values)
        while i < length - 4:
            if (
                self.red_values[i] == 1 and
                self.yellow_values[i + 1] == 1 and
                self.green_values[i + 2] == 1 and
                self.yellow_values[i + 3] == 1 and
                self.red_values[i + 4] == 1
            ):
                cycle_count += 1
                i += 5
            else:
                i += 1
        return cycle_count
    def mistake_calculation(self):
        mistakes = sum(1 for red, yellow, green in zip(self.red_values, self.yellow_values, self.green_values) if
                       (red + yellow + green != 1))
        return mistakes
    
traffic_light = TrafficLight("data.txt")
print(f'There are {traffic_light.light_occurrence()[0]} red light, {traffic_light.light_occurrence()[1]} yellow light and {traffic_light.light_occurrence()[2]} green light occurrences')
print(f'Red light was active for {traffic_light.total_active_time()[0]} seconds, yellow for {traffic_light.total_active_time()[1]} seconds and green for {traffic_light.total_active_time()[2]} seconds')
print(f'Timestamps when green light was active are: {traffic_light.green_active_timestamps()}')
print(f'There are a total of {traffic_light.total_complete_cycles()} cycles completed')
print(f'There are a total of {traffic_light.mistake_calculation()} mistakes')