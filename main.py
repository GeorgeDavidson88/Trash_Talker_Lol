import random
import threading
import time

import pynput

exit_threads = threading.Event()

phrases = []

with open("phrases.txt") as phrases_file:
    for line in phrases_file:
        phrases.append(line.strip())


def say(string):
    pynput.keyboard.Controller().tap(key="/")
    time.sleep(0.05)
    pynput.keyboard.Controller().type(string)
    time.sleep(0.05)
    pynput.keyboard.Controller().tap(pynput.keyboard.Key.enter)


def on_press(key):
    if exit_threads.is_set():
        return False

    if str(key) == "Key.f1":
        say("Trash kid :(")

    elif str(key) == "Key.f2":
        say("Easy :)")

    elif str(key) == "Key.f3":
        say("DEAD LOL")

    elif str(key) == "Key.f4":
        say("sucks to suck :)")

    elif str(key) == "Key.f8":
        say(phrases[random.randint(0, len(phrases) - 1)])


def keyboard_listener():
    with pynput.keyboard.Listener(on_press=lambda key: on_press(key)) as keyboard_listener:
        keyboard_listener.join()


def main():
    print("Program Started.")

    keyboard_listener_thred = threading.Thread(target=keyboard_listener)
    keyboard_listener_thred.start()

    while True:
        command = input("Type 'quit' to quit>")

        if command == "quit":
            break

    exit_threads.set()
    pynput.keyboard.Controller().tap(pynput.keyboard.Key.esc)


if __name__ == "__main__":
    main()
