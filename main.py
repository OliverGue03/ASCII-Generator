import numpy
import pandas
import glob

# Image Files to look up in directory
DATA_TYPES = ["*.png", "*.jpg", "*.webp", "*.gif"]

# Get Pictures
pictures = []

for type in DATA_TYPES:
    pictures += glob.glob(type)


# Present scanned pictures to User 
print("-------LIST OF ALL PICTURES-------")
for i, picture in enumerate(pictures, start=1):
    print(f"{i}.    {picture}")