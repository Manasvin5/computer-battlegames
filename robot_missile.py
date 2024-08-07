#Written By Manasvin Shrimali
#Book:Computer Battlegames(1982)(Usborne Publishing)
import random
import sys
import time
def printt(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
printt("ROBOT MISSILE")
printt('''The year is 2582 and the people of Earth are in the
midst of battle against the Robots. A lethal Robot
Missile has just landed and everyone is depending
on you to find the secret code which unlocks its
defuse mechanism. If you fail, the entire Earth
Command Headquarters(EHQ) will be blown up. ''')
printt("")
printt("TYPE THE CORRECT CODE")
printt("LETTER (A-Z) TO")
printt("DEFUSE THE MISSILE.")
printt("YOU HAVE 4 CHANCES")
printt("")
printt("Good Luck Soldier......MAKE STALIN PROUD")
secret_code = chr(64 + random.randint(1, 26))
for guess_count in range(4):
    guess = input("Enter your guess (a letter from A to Z):: ").upper()
    if guess == secret_code:
        printt("YOU DID IT! CLICKK....RESPECT+++")
        break
    elif guess < secret_code:
        printt("LATER THAN", guess)
    else:
        printt("EARLIER THAN", guess)
else:
    printt("BOOOOOOOOMMM! YOU BLEW IT. EHQ HAS FALLEN BCS OF U........You INGLORIUS BASTARD")
    print('''          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
_____________/_ __ \_____________               _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
_____________/_ __ \_____________          _ ._  _ , _ ._
     
          
                 /\     |\**/|      
                /  \    \ == /
                |  |     |  |
                |  |     |  |
                / == \   \  /
                |/**\|    \/
          
          ''')
    print("THE CORRECT CODE WAS", secret_code)
