import random
import threading
import time

import pynput

phrases = []
endings = []
last_phrase = ""
last_ending = ""

with open("phrases.txt") as phrases_file:
    for line in phrases_file:
        phrases.append(line.strip())

with open("endings.txt") as endings_file:
    for line in endings_file:
        endings.append(line.strip())


def say(string):
    pynput.keyboard.Controller().tap(key="/")
    time.sleep(0.05)
    pynput.keyboard.Controller().type(string)
    time.sleep(0.05)
    pynput.keyboard.Controller().tap(pynput.keyboard.Key.enter)


def on_press(key):
    if str(key) == "Key.f1":
        say("Trash Kid")

    elif str(key) == "Key.f2":
        say("Easy :)")

    elif str(key) == "Key.f3":
        say("DEAD LOL")

    elif str(key) == "Key.f4":
        say("BAD XD")

    elif str(key) == "Key.f8":
        global last_phrase
        global last_ending

        phrase_index = random.randint(0, len(phrases) - 1)
        ending_index = random.randint(0, len(endings) - 1)

        phrase = phrases[phrase_index]
        ending = endings[ending_index]

        if last_phrase.lower() == phrase.lower():
            if len(phrases) != 1:
                if phrase_index == 0:
                    phrase = phrases[phrase_index + 1]
                elif phrase_index == len(phrases) - 1:
                    phrase = phrases[phrase_index - 1]
                else:
                    phrase = phrases[phrase_index + 1]

        if last_ending.lower() == ending.lower():
            if len(endings) != 1:
                if ending_index == 0:
                    ending = endings[ending_index + 1]
                elif ending_index == len(endings) - 1:
                    ending = endings[ending_index - 1]
                else:
                    ending = endings[ending_index + 1]

        random_number = random.randint(0, 2)

        if random_number == 0:
            phrase = phrase.lower()
        elif random_number == 1:
            phrase = phrase.upper()
        else:
            phrase = phrase.title()

        say(f"{phrase} {ending}")

        last_phrase = phrase
        last_ending = ending


def keyboard_listener():
    with pynput.keyboard.Listener(on_press=lambda key: on_press(key)) as keyboard_listener:
        keyboard_listener.join()


def main():
    print("Program Started...")

    keyboard_listener_thred = threading.Thread(target=keyboard_listener)
    keyboard_listener_thred.daemon = True
    keyboard_listener_thred.start()

    while True:
        command = input("Type 'quit' to quit or close the terminal -> ")

        if command == "quit":
            break


if __name__ == "__main__" and len(phrases) != 0:
    main()
