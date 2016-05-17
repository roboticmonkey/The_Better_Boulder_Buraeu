"""Utility file to seed boulders database from data_seed_files/"""
import csv

from model import Location, Sub_location, Boulders, Routes, connect_to_db, db
from server import app





with open('data_seed_files/sub_locations.csv', 'r,') as csvfile:
    my_file = csv.reader(csvfile, delimiter=',')

    for row in my_file:
        print row[1],"\n", row[3], "\n"
