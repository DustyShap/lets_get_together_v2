import csv
import sys

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







    def run(self):
        self.load_input_file()
        self.csv_read_to_list()
        self.set_group_size()
