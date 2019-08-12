#!/usr/bin/env python3

import pynput.keyboard as kb
import pynput.mouse as mo

def main():
    print("R400ForVN started !")
    keyboard_controller = kb.Controller()
    mouse_controller = mo.Controller()

    def on_press(key):
        if key == kb.Key.page_up:
            print("Scoll Up")
            mouse_controller.scroll(0, 1)

        if key == kb.Key.page_down:
            print("Scoll Down")
            mouse_controller.scroll(0, -1)

        if str(key) == "'.'":
            return False

    with kb.Listener(on_press=on_press) as listener:
        listener.join()

    print("R400ForVN stopped !")

if __name__ == '__main__':
    main()
