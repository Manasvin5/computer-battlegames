#Written By Manasvin Shrimali
#Book:Computer Battlegames(1982)(Usborne Publishing)
import random
import time
import os
import sys
def printt(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def main():
    os.system('clear')
    printt("VITAL MESSAGE")
    printt('''You are a laser communications operator. Your job is to intercept robot messages and relay them to Command HQ. A vital code message is expected. If you relay it correctly, the Robot attack will be crushed.

The computer will ask you for a difficulty from 4 to 10. When you have typed in your answer, letters will appear top left of your screen and disappear again fairly quickly. Memorize them and then type them into the computer and see if you were right.''')
    while True:
        difficulty = int(input("HOW DIFFICULT? (4-10): "))
        if difficulty < 4 or difficulty > 10:
            print("Invalid difficulty! Please enter a number between 4 and 10...Be Serious You Kiddo!!")
        else:
            break
    secret_message = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(difficulty))
    os.system('clear')
    printt("SEND THIS MESSAGE:")
    printt(secret_message)
    for _ in range(difficulty * 4):
        time.sleep(0.5) 
        os.system('clear') 
    os.system('clear')
    user_input = input("TYPE THE MESSAGE YOU REMEMBERED: ").upper()
    if user_input == secret_message:
        printt("MESSAGE CORRECT")
        printt("THE WAR IS OVER...THANK YOU SOLDIER....LONG LIVE SOVIET")
    else:
        printt("WRONG COMRADE............./ HQ HAS FALLEN BCS OF U......../ You INGLORIUS BASTARD")
        printt(f"YOU SHOULD HAVE SENT: {{secret_message}}")
        printt("YOU FOOL")

main()
