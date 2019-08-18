#!/usr/bin/env python3

import pynput.keyboard as kb
import pynput.mouse as mo

count = 0

def prt_count(*arg, **argv):
    global count
    print("[" + str(count).rjust(5, "0") + "]", *arg, **argv)

def inc_count(i):
    global count
    count += i

def rst_count():
    global count
    count = 0

def main():
    prt_count("R400ForVN started !")
    keyboard_controller = kb.Controller()
    mouse_controller = mo.Controller()

    def on_press(key):
        if key == kb.Key.page_up:
            mouse_controller.scroll(0, 1)
            inc_count(-1)
            prt_count("Scoll Up")
        elif key == kb.Key.page_down:
            mouse_controller.scroll(0, -1)
            inc_count(1)
            prt_count("Scoll Down")
        elif key == kb.Key.f5 or key == kb.Key.esc:
            rst_count()
            prt_count("Count reseted !")
        elif str(key) == "'.'":
            return False

    with kb.Listener(on_press=on_press) as listener:
        listener.join()

    prt_count("R400ForVN stopped !")


if __name__ == '__main__':
    main()
