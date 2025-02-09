import random
import time

score = 0
level = 1
game_running = True

riddle1 = "L dp dq rgg qxpehu. Wdnh dzdb d ohwwhu dqg L ehfrph hyhq. Zkdw qxpehu dp L?"
answer1 = "SEVEN"
riddle2 = "V2hhdCBoYXMga2V5cywgYnV0IG5vIGxvY2tzOyBzcGFjZSwgYnV0IG5vIHJvb207IHlvdSBjYW4gZW50ZXIsIGJ1dCBub3QgZ28gaW4/"
answer2 = "KEYBOARD"
riddle3 = ".-- .... .- -   .... .- ...   -.-. .. - .. . ...    -... ..- -   -. ---   .... --- ..- ... . ...    ..-. --- .-. . ... - ...    -... ..- -   -. ---   - .-. . . ...    .-. .. ...- . .-. ...    -... ..- -   -. ---   .-- .- - . .-."
answer3 = "MAP"
riddle4 = "?I ma tahW .dniheb evael uoy erom eht ,ekat uoy erom ehT"
answer4 = "FOOTSTEPS"
riddle5 = "7cf6b9b8d7c0ea767416bcf7f77af31c"
answer5 = "M"

print("\n=== CRYPTO RIDDLE GAME ===")
print("Solve these 5 riddles to win!")
input("Press Enter to start...")

while game_running:
    print("\n=== LEVEL " + str(level) + " ===")
    print("\nScore: " + str(score))
    if level == 1:
        encrypted = riddle1
        print("\nDecrypt this message:")
        print(encrypted)
        print("\nHint: Caesar cipher with shift of 3")
        
        player_answer = input("\nYour answer: ").upper()
        if player_answer == answer1:
            print("\nCorrect! Moving to next level!")
            score = score + 100
            level = level + 1
        else:
            print("\nWrong! Try again!")
            score = score - 10
    elif level == 2:
        encrypted = riddle2
        print("\nDecrypt this message:")
        print(encrypted)
        print("\nHint: Base64 encoded")
        
        player_answer = input("\nYour answer: ").upper()
        if player_answer == answer2:
            print("\nCorrect! Moving to next level!")
            score = score + 100
            level = level + 1
        else:
            print("\nWrong! Try again!")
            score = score - 10
    elif level == 3:
        encrypted = riddle3
        print("\nDecrypt this message:")
        print(encrypted)
        print("\nHint: Morse code")
        
        player_answer = input("\nYour answer: ").upper()
        if player_answer == answer3:
            print("\nCorrect! Moving to next level!")
            score = score + 100
            level = level + 1
        else:
            print("\nWrong! Try again!")
            score = score - 10
    elif level == 4:
        encrypted = riddle4
        print("\nDecrypt this message:")
        print(encrypted)
        print("\nHint: Mirror mirror...")
        
        player_answer = input("\nYour answer: ").upper()
        if player_answer == answer4:
            print("\nCorrect! Moving to final level!")
            score = score + 100
            level = level + 1
        else:
            print("\nWrong! Try again!")
            score = score - 10
    elif level == 5:
        encrypted = riddle5
        print("\nDecrypt this message:")
        print(encrypted)
        print("\nHint: Final level - no encryption, just solve the riddle")
        
        player_answer = input("\nYour answer: ").upper()
        if player_answer == answer5:
            print("\nCorrect! You beat the game!")
            score = score + 100
            game_running = False
        else:
            print("\nWrong! Try again!")
            score = score - 10
    quit_check = input("\nPress Enter to continue or 'q' to quit: ").lower()
    if quit_check == 'q':
        game_running = False

print("\n=== GAME OVER ===")
print("Final Score: " + str(score))
if score >= 500:
    print("Perfect score! You're a master decoder!")
elif score >= 300:
    print("Great job! You've got skills!")
else:
    print("Keep practicing!")
print("\nThanks for playing!")
