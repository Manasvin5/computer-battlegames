import time
import random
import sys
import termios
import tty

def get_user_reaction():
    print("Get ready to react to a change...")
    time.sleep(random.uniform(2, 5))  # Wait for a random time between 2 to 5 seconds
    print("Change!")
    start_time = time.time()
    tty.setcbreak(sys.stdin)  # Set terminal to cbreak mode
    sys.stdin.read(1)  # Wait for any key press
    end_time = time.time()
    reaction_time = end_time - start_time
    return reaction_time

def main():
    print("Welcome to Reaction Time Tester!")
    print("When you're ready, press any key to begin the test.")
    tty.setcbreak(sys.stdin)  # Set terminal to cbreak mode
    sys.stdin.read(1)  # Wait for any key press
    
    reaction_time = get_user_reaction()
    
    print("Your reaction time was: {:.2f} seconds".format(reaction_time))

if __name__ == "__main__":
    main()
