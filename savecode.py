# Save this code in a file named main_program.py
from my_module import greet

def main():
    name = input("Enter your name: ")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()

python main_program.py

