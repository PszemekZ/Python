from random import randint
import tkinter as tk
import threading
from time import sleep


def change_text(continue_running, label):
    while continue_running.is_set():
        label['text'] = randint(1,100)
        sleep(30)


def main():
    root = tk.Tk()

    label = tk.Label(root, text='')

    continue_thread = threading.Event()
    continue_thread.set()
    change_text_thread = threading.Thread(target=change_text, kwargs={'continue_running': continue_thread, 'label': label})
    change_text_thread.start()

    label.pack()
    root.mainloop()

    continue_thread.clear()
    change_text_thread.join()


if __name__ == '__main__':
    main()