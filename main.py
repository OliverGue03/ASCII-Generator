
import glob
from generator import generate_ascii

# Image Files to look up in directory
DATA_TYPES = ["*.png", "*.jpg", "*.webp", "*.gif"]
SIZES = {"S": 100, "M": 200, "L": 400}

def main():
    # Get Pictures
    pictures = []
    choice = None
    size = 0
    
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
                print("Goodbye!")
                break
            elif choice > len(pictures) or choice < 0:
                print(f"Choose a number between 0 and {len(pictures)}")
                choice = None
        except:
            print("Input a correct value.")

    while size == 0:
        try:
            size = input("What size should your ASCII have? (S, M or L)\n").upper()
            if size in SIZES.keys:
                size = SIZES[size]
        except:
            print("Input a correct value.")

    # ASCII-fy the image
    generate_ascii(pictures[choice-1], size)
    
if __name__ == "__main__":
    main()