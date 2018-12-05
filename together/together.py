import csv
import sys
import random

class Together:

    def __init__(self, input_file):
        self.input_file = input_file
        self.name_list = []
        self.output_list = []
        self.group_size = None

    def load_input_file(self):
        """Load input CSV File"""
        try:
            open(self.input_file)
        except FileNotFoundError:
            print('No file found for {}'.format(self.input_file))
            print('Usage: scripts/generate <input_file.csv>')
            sys.exit()

    def csv_read_to_list(self):
        with open(self.input_file) as f:
            reader = csv.reader(f)
            self.name_list = [n[0].strip() for n in list(reader)]

    def set_group_size(self):
        valid_input = False
        while not valid_input:
            r = input('Group Size: ')
            if r.isdigit() and r != '0':
                self.group_size = int(r)
                valid_input = True
            else:
                print('Please enter a valid number')

    def process_list(self):
        new_list = list(set(self.name_list))
        random.shuffle(new_list)
        for i in range(0, len(new_list), self.group_size):
            self.output_list.append(new_list[i:i+self.group_size])

    def write_list_to_csv(self):
        with open('{}.output'.format(self.input_file), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow([i for i in self.output_list])








    def run(self):
        self.load_input_file()
        self.csv_read_to_list()
        self.set_group_size()
        self.process_list()
        self.write_list_to_csv()
