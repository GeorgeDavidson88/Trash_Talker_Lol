import random
import threading
import time

import pynput


class Main:
    def __init__(self):
        self.F1_Phrase = "Trash Kid"
        self.F2_Phrase = "Easy :)"
        self.F3_Phrase = "DEAD LOL"
        self.F4_Phrase = "BAD XD"

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
        time.sleep(0.05)  # You have to wait a bit for the chat to open.
        pynput.keyboard.Controller().type(string)
        # You have to wait for the letters to be rendered before clicking Enter.
        time.sleep(0.05)
        pynput.keyboard.Controller().tap(pynput.keyboard.Key.enter)

    def on_press(self, key):
        if str(key) == "Key.f1":
            self.say(self.F1_Phrase)

        elif str(key) == "Key.f2":
            self.say(self.F2_Phrase)

        elif str(key) == "Key.f3":
            self.say(self.F3_Phrase)

        elif str(key) == "Key.f4":
            self.say(self.F4_Phrase)

        elif str(key) == "Key.f8":
            if len(self.phrases) != 0:
                # Selects a random index from the list of phrases.
                self.phrase_index = random.randint(0, len(self.phrases) - 1)

                # Set the current phrase to the random phrase index.
                phrase = self.phrases[self.phrase_index]

                if self.last_phrase.lower() == phrase.lower():
                    # We will not throw an error if there is only one phrase in phrases.txt.
                    if len(self.phrases) > 1:
                        if self.phrase_index == 0:  # We can't pick an index that is lower than 0.
                            phrase = self.phrases[self.phrase_index + 1]
                        # We can't choose an index greater than the length of phrases.txt.
                        elif self.phrase_index == len(self.phrases) - 1:
                            phrase = self.phrases[self.phrase_index - 1]
                        else:
                            # We will pick the phrase that is one index above the current phrase.
                            phrase = self.phrases[self.phrase_index + 1]

                # To add more variety to the phrases.
                random_number = random.randint(0, 2)

                if random_number == 0:
                    phrase = phrase.lower()
                elif random_number == 1:
                    phrase = phrase.upper()
                else:
                    phrase = phrase.title()

            else:
                phrase = ""

            if len(self.endings) != 0:
                # Selects a random index from the list of endings.
                self.ending_index = random.randint(0, len(self.endings) - 1)

                # Set the current ending to the random ending index.
                ending = self.endings[self.ending_index]

                if self.last_ending.lower() == ending.lower():  # The same logic as above.
                    if len(self.endings) > 1:
                        if self.ending_index == 0:
                            ending = self.endings[self.ending_index + 1]
                        elif self.ending_index == len(self.endings) - 1:
                            ending = self.endings[self.ending_index - 1]
                        else:
                            ending = self.endings[self.ending_index + 1]

            else:
                ending = ""

            self.say(f"{phrase} {ending}")

            self.last_phrase = phrase
            self.last_ending = ending

    def main_loop(self):
        while True:  # So the user can easily quit the program.
            command = input("Type 'quit' to quit or close the terminal -> ")

            if command == "quit":
                break


def keyboard_listener(main):
    # Listen for keys that the user pressed, and when a key is pressed, call the "on_press" function.
    with pynput.keyboard.Listener(on_press=lambda key: main.on_press(key)) as keyboard_listener:
        keyboard_listener.join()


def main():
    print("Program Started...")

    main = Main()

    # Create and start the keyboard_listener_thread.
    keyboard_listener_thred = threading.Thread(
        target=keyboard_listener, args=(main,))
    keyboard_listener_thred.daemon = True
    keyboard_listener_thred.start()

    main.main_loop()


if __name__ == "__main__":
    main()
