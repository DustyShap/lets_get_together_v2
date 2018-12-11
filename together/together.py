import csv
import sys
import random
from faker import Faker
fake = Faker()

class Together:

    def __init__(self, input):
        self.input = input
        self.name_list = []
        self.output_list = []
        self.group_size = None
        self.faker_names_amount = None

    def load_input_file(self):
        """Load input CSV File"""
        try:
            open(self.input)
        except FileNotFoundError:
            print('No file found for {}'.format(self.input))
            print('Usage: scripts/generate <input_file.csv>')
            sys.exit()

    def file_read_to_list(self):
        with open(self.input) as f:
            self.name_list = [n.strip() for n in list(f)]

    def set_group_size(self):
        valid_input = False
        while not valid_input:
            r = input('Group Size: ')
            if r.isdigit() and r != '0':
                self.group_size = int(r)
                valid_input = True
            else:
                print('Please enter a valid number')

    def set_faker_names_length(self):
        valid_input = False
        while not valid_input:
            r = input('How many names to generate?: ')
            if r.isdigit() and r != 0:
                self.faker_names_amount = int(r)
                valid_input = True
            else:
                print('Please enter a valid number!')

    def set_faker_names_list(self):
        for _ in range(self.faker_names_amount):
            self.name_list.append(fake.name())

    def process_list(self):
        self.output_list = []
        new_list = list(set(self.name_list))
        random.shuffle(new_list)
        for i in range(0, len(new_list), self.group_size):
            self.output_list.append(new_list[i:i+self.group_size])

    def print_list(self):
        for group in self.output_list:
            print('-----------')
            print('Group {}: {}'.format(self.output_list.index(group)+1,
                                       [name for name in group]))


    def reshuffle_or_exit(self):
        """Method to allow reshuffle list"""
        valid_input = False
        while not valid_input:
            r = input('Reshuffle Groups? [Y/N]: ').strip().lower()
            if r in ['yes', 'y']:
                self.process_list()
                self.print_list()
            if r in ['no', 'n']:
                sys.exit()


    def run(self):
        """Main method that kicks off the program"""
        if self.input != 'faker':
            self.load_input_file()
            self.file_read_to_list()
        else:
            self.set_faker_names_length()
            self.set_faker_names_list()
        self.set_group_size()
        self.process_list()
        self.print_list()
        self.reshuffle_or_exit()
