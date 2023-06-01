# generate_commit_dates.py

import os
import datetime
from art import *

def generate_dates(start_date, text):
    ascii_art = text2art(text) # Generate ASCII art from text
    ascii_art = ascii_art.split('\n')
    
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = start_date + datetime.timedelta(weeks=53)
    
    dates_to_commit = []
    
    # For each pixel in the ASCII art
    for row in range(len(ascii_art)):
        for col in range(len(ascii_art[row])):
            # If the pixel is "on", add this date to the commit dates
            if ascii_art[row][col] != ' ':
                date = start_date + datetime.timedelta(weeks=col, days=row)
                if start_date <= date < end_date:
                    # Add the date multiple times to create different intensities
                    intensity = 255 - ord(ascii_art[row][col])
                    dates_to_commit.extend([date] * intensity)
    
    return dates_to_commit

if __name__ == "__main__":
    import sys

    start_date = sys.argv[1]
    text = sys.argv[2]

    dates_to_commit = generate_dates(start_date, text)

    # Write dates to a file
    with open('dates.txt', 'w') as file:
        for date in dates_to_commit:
            file.write(f"{date}\n")
