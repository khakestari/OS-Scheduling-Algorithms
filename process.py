# taking input from csv
import csv

class Process:
    def __init__(self, process_id, arrival_time, cpu_burst_time_1, io_time, cpu_burst_time_2):
        self.process_id = int(process_id)
        self.arrival_time = int(arrival_time)
        self.cpu_burst_time_1 = int(cpu_burst_time_1)
        self.io_time = int(io_time)
        self.cpu_burst_time_2 = int(cpu_burst_time_2)
        self.finish_time = 0
    
    def __repr__(self):
        return f"Process(process_id={self.process_id}, arrival_time={self.arrival_time}, " \
               f"cpu_burst_time_1={self.cpu_burst_time_1}, io_time={self.io_time}, " \
               f"cpu_burst_time_2={self.cpu_burst_time_2}, finish_time={self.finish_time})"

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(Process(*row))
    return data

filename = 'inputFile.csv'  # Replace with the actual filename or path to the CSV file
csv_data = read_csv(filename)
for row in csv_data:
    print(row)