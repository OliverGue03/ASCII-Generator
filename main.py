
import glob

# Image Files to look up in directory
DATA_TYPES = ["*.png", "*.jpg", "*.webp", "*.gif"]

# Get Pictures
pictures = []
choice = None
for type in DATA_TYPES:
        pictures += glob.glob(type)
if not pictures:
    raise FileNotFoundError("No image files found.\nPlease put the file(s) you want to turn into an ASCII into this folder.")


# Present scanned pictures to User 
print("-------LIST OF ALL PICTURES-------\n")
for i, picture in enumerate(pictures, start=1):
    print(f"{i}.    {picture}")
    print("0.    EXIT")
print("----------------------------------\n")
print("---------CHOOSE A PICTURE---------\n")
while not choice:
    try:
        choice = int(input("Input the number of the picture you want to turn into an ASCII:\n"))
        if choice == 0:
             break
        elif choice > len(pictures) or choice < 0:
            print(f"Choose a number between 0 and {len(pictures)}")
            choice = None
    except:
        print("Input a correct value.")
print(choice)
print("Goodbye!")