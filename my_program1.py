import os

def greet():
    print(f"Hello ! I'm in {os.getcwd()}")
def say_bye():
    print("Leaving bye")

def main():
    greet()
    say_bye()
    print("I'm in the python code progrma file")
main()
if __name__ == "__main__":
    print(__name__)
    main()