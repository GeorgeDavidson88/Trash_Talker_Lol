import random
import threading
import time

import pynput

class Main:
    def __init__(self):
        self.phrases = []
        self.endings = []
        self.last_phrase = ""
        self.last_ending = ""

        with open("phrases.txt") as phrases_file:
            for line in phrases_file:
                self.phrases.append(line.strip())

        with open("endings.txt") as endings_file:
            for line in endings_file:
                self.endings.append(line.strip())


    def say(self, string):
        pynput.keyboard.Controller().tap(key="/")
        time.sleep(0.05)
        pynput.keyboard.Controller().type(string)
        time.sleep(0.05)
        pynput.keyboard.Controller().tap(pynput.keyboard.Key.enter)


    def on_press(self, key):
        if str(key) == "Key.f1":
            self.say("Trash Kid")

        elif str(key) == "Key.f2":
            self.say("Easy :)")

        elif str(key) == "Key.f3":
            self.say("DEAD LOL")

        elif str(key) == "Key.f4":
            self.say("BAD XD")

        elif str(key) == "Key.f8":
            self.phrase_index = random.randint(0, len(self.phrases) - 1)
            self.ending_index = random.randint(0, len(self.endings) - 1)

            phrase = self.phrases[self.phrase_index]
            ending = self.endings[self.ending_index]

            if self.last_phrase.lower() == phrase.lower():
                if len(self.phrases) != 1:
                    if self.phrase_index == 0:
                        phrase = self.phrases[self.phrase_index + 1]
                    elif self.phrase_index == len(self.phrases) - 1:
                        phrase = self.phrases[self.phrase_index - 1]
                    else:
                        phrase = self.phrases[self.phrase_index + 1]

            if self.last_ending.lower() == ending.lower():
                if len(self.endings) != 1:
                    if self.ending_index == 0:
                        ending = self.endings[self.ending_index + 1]
                    elif self.ending_index == len(self.endings) - 1:
                        ending = self.endings[self.ending_index - 1]
                    else:
                        ending = self.endings[self.ending_index + 1]

            random_number = random.randint(0, 2)

            if random_number == 0:
                phrase = phrase.lower()
            elif random_number == 1:
                phrase = phrase.upper()
            else:
                phrase = phrase.title()

            self.say(f"{phrase} {ending}")

            last_phrase = phrase
            last_ending = ending

    def main_loop(self):
        while True:
            command = input("Type 'quit' to quit or close the terminal -> ")

            if command == "quit":
                break


def keyboard_listener(main):
    with pynput.keyboard.Listener(on_press=lambda key: main.on_press(key)) as keyboard_listener:
        keyboard_listener.join()


def main():
    print("Program Started...")

    main = Main()

    if len(main.phrases) != 0:
        keyboard_listener_thred = threading.Thread(target=keyboard_listener, args=(main,))
        keyboard_listener_thred.daemon = True
        keyboard_listener_thred.start()

        main.main_loop()


if __name__ == "__main__":
    main()
