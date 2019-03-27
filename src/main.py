# Import all the contents of the classes file
import classes as classfile

# Import the listed contents from functions file
from functions import function, number

if __name__ == "__main__":

    print("Function only run if file is run directly from this file.")
    print("E.g. python main.py")

    print(function())

    print(number(1))
