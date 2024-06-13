#!/usr/bin/env python

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import threading
import time
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox, Style
from PIL import Image, ImageTk
from eyecrypt import encryption
from eyecrypt import is_valid_hex, eyecrypt
from encryption import *

SELECTOR_COLOR = '#e8e8e8'
WARNING_COLOR = '#ff8f4a'
ERROR_COLOR = 'red'
SUCCESS_COLOR = 'green'
PREVIEW_BACKGROUND_COLOR = '#dbdbdb'

DISPLAY_HEIGHT = 300
DISPLAY_WIDTH = 400

NO_FILE_SELECTED = "(none)"

LOAD_FILE_TYPES = [("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp *.apng")]
SAVE_FILE_TYPES = [("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp *.apng"), ("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", ".jpeg"), ("BMP, *.bmp"), ("BMP, *.bmp"), ("GIF", ".gif"), ("WEBP", "*.webp"), ("APNG", "*.apng")]
ECB_ALGORITHMS = list({k:v for k,v in encryption.methods.items() if v.get('mode') == Mode.ECB}.keys())
ALL_ALGORITHMS = list(encryption.methods.keys())

TIMEOUT = 60

class RaiseThread(threading.Thread):
    """
    A thread class that is capable of raising an exception that can be caught.
    """
    def run(self):
        self._exc = None
        try:
            super().run()
        except Exception as e:
            self._exc = e
    
    def join(self):
        super().join()
        if self._exc:
            raise self._exc

class ImageData:
    """
    A class that handles image data.
    """
    def __init__(self):
        self.file_path = None
        self.image = None

def get_icon_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

def resize(image_path, width, height):
    """
    Given an image path and a target width and height, resizes the image to fit.
    This function maintains the aspect ratio of the image, and does not stretch it.
    """
    image = Image.open(image_path)

    if (image.height >= image.width):
        image = image.resize((int(image.width*(height/image.height)),height))
    else:
        image = image.resize((width,int(image.height*(width/image.width))))

    if (image.height > height):
        image = image.resize((int(image.width*(height/image.height)),height))
    
    return ImageTk.PhotoImage(image)

def set_display(label, display, data):
    """
    Sets an image display with the given data.
    """
    try:
        data.image = resize(data.file_path, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        display.configure(image = data.image, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)
        label.configure(text=os.path.basename(data.file_path))
    except:
        reset_display(label, display)

def reset_display(label, display):
    """
    Resets an image display.
    """
    display.configure(image="", height=20)
    label.configure(text="")

def write_action(action, args):
    """
    Writes the current program action to the log.
    """
    log = args['log']
    if (log):
        log.configure(text=action)

def main():

    def invoke_go():
        """
        Wrapper function to invoke the go function in a separate thread.
        """
        go_thread = threading.Thread(target=go)
        go_thread.start()

    def go():
        """
        Executes the eyecrypt process with the given parameters.
        """
        log.configure(text="Starting...", fg="blue")
        go_button["state"] = "disabled"
        log.update()
        try:

            # Validation
            if (not input.file_path):
                raise Exception("Please select a file to encrypt.")
            if (not output.file_path):
                raise Exception("Please choose a save location.")
            if (not is_valid_hex(key.get())):
                raise Exception("Please enter a valid key.")

            thread = RaiseThread(target = eyecrypt, kwargs={'input_image_path': input.file_path, 'output_image_path': output.file_path, 'algo': algorithm.get(), 'key': key.get(), 'iv': defaults.IV, 'log_action': write_action, 'log': log})
            thread.daemon = True
            time_started = time.time()
            thread.start()

            try:
                thread.join()
            except Exception as e:
                raise Exception(e)
            
            while thread.is_alive():
                time.sleep(1)
                if (time.time() > time_started + TIMEOUT):
                    raise TimeoutError("Timed out. Please try a smaller file.")

            log.configure(text="Finished! (Saved to "+output.file_path+")", fg=SUCCESS_COLOR)    
            set_display(output_label, output_display, output)

        except Exception as e:
            log.configure(text=e, fg="red")
        go_button["state"] = "normal"


    def get_input_file():
        """
        Promps the user to provide an file to use as input.
        """
        input.file_path = filedialog.askopenfilename(filetypes=LOAD_FILE_TYPES)

        if (not input.file_path):
            input_button.configure(text=NO_FILE_SELECTED)
        else:
            input_button.configure(text = input.file_path)
 
        set_display(input_label, input_display, input)
    
    def get_output_file():
        """
        Promps the user to provide an file to save the output to.
        """
        output.file_path = filedialog.asksaveasfilename(filetypes=SAVE_FILE_TYPES, defaultextension="*.*")

        if (not output.file_path):
            output_button.configure(text=NO_FILE_SELECTED)
        else:
            output_button.configure(text = output.file_path)
        
        reset_display(output_label, output_display)

    def random_hex():
        """
        Sets the key to a random hexadeimal string.
        """
        key.set(os.urandom(16).hex())
    
    def check_key(*args):
        """
        Checks whether a key is a valid hexidecimal. Warns the user if not.
        """
        if (is_valid_hex(key.get())):
            key_tooltip.configure(text="")
        else:
            key_tooltip.configure(text="Please enter a valid hexadecimal.", fg=ERROR_COLOR)

    def check_algo(*args):
        """
        Checks whether an algorithm is an ECB algorithm. Warns the user if not.
        """
        method_data = encryption.methods.get(algorithm.get())
        mode = method_data.get('mode')

        if mode != Mode.ECB:
            algorithm_tooltip.configure(text="ECB algorithms are reccomended for more discernable results.", fg="orange")
        else:
            algorithm_tooltip.configure(text="")
        return
    
    def update_algo_menu(*args):
        if (algorithm_advanced.get()):
            algorithm_menu.configure(values=ALL_ALGORITHMS)
        else:
            algorithm_menu.configure(values=ECB_ALGORITHMS)
    
    # Window, root, and style setup
    window = Tk()
    window.title("EYECRYPT")
    window.resizable(False, False)
    try:
        icon_path = get_icon_path('eyecrypt-icon.ico')
        window.iconbitmap(icon_path)
    except:
        pass

    root = Frame(window)
    root.grid(column=0, row=0)

    style = Style()
    style.theme_create('combostyle', parent="winnative", settings = {
            'TCombobox': {
                'configure': {
                    'selectbackground': 'white',
                    'selectforeground': 'black',
                }
            },
        }
    )
    style.theme_use('combostyle')

    # Objects to hold image data
    input = ImageData()
    output = ImageData()

    # FILE SELECTORS
    file_selectors = Frame(root, padx=10, pady=10)
    file_selectors.grid(column=0, row=0)

    # Input selector
    Label(file_selectors, text = "Select file to encrypt:", anchor=E, pady=5).grid(column=0, row=0, sticky=E)
    input_button = Button(file_selectors, text = NO_FILE_SELECTED, width=100, command=get_input_file, bg=SELECTOR_COLOR, activebackground=SELECTOR_COLOR)
    input_button.grid(column=1, row=0)

    # Output selector
    Label(file_selectors, text = "Save to:", anchor=E, pady=5).grid(column=0, row=1, sticky=E)
    output_button = Button(file_selectors, text = NO_FILE_SELECTED, width=100, command=get_output_file, bg=SELECTOR_COLOR, activebackground=SELECTOR_COLOR)
    output_button.grid(column=1, row=1)

    # OPTIONS
    options = Frame(root)
    options.grid(column=0, row=1)

    # Key selector
    key = StringVar(root)
    key.set(defaults.KEY)
    key_selector = Frame(options)
    key_selector.grid(column=0, row=0, sticky = W)
    Label(key_selector, text = "Key:").grid(column=0, row=0)

    key_entry_frame = Frame(key_selector)
    key_entry_frame.grid(column=1, row=0)
    Label(key_entry_frame, text="0x").grid(column=0, row=0)
    key_entry = Entry(key_entry_frame, textvariable=key, width=35)
    key_entry.grid(column=1, row=0)
    key_random = Button(key_entry_frame, text="random", command=random_hex)
    key_random.grid(column=2, row=0, padx=(5,0))

    key_tooltip = Label(options, text="", width=50)
    key_tooltip.grid(column=0, row=1)
    key.trace_add('write', check_key)

    # Algorithm selector
    algorithm = StringVar(root)
    algorithm.set(defaults.ALGORITHM)
    algorithm_selector = Frame(options)
    algorithm_selector.grid(column=1, row=0)
    Label(algorithm_selector, text = "Encryption Algorithm:").grid(column=0, row=0)

    algorithm_menu_frame = Frame(algorithm_selector)
    algorithm_menu_frame.grid(column=1, row=0)
    algorithm_menu = Combobox(algorithm_menu_frame, textvariable = algorithm, state="readonly", values = ECB_ALGORITHMS, width=20)
    algorithm_menu.grid(column=0, row=0)

    algorithm_advanced = IntVar()
    algorithm_check = Checkbutton(algorithm_selector, text = "Show non-ECB", variable = algorithm_advanced, onvalue = 1, offvalue = 0, command=update_algo_menu)
    algorithm_check.grid(column = 2, row = 0)

    algorithm_tooltip = Label(options, text="", width=50)
    algorithm_tooltip.grid(column=1, row=1, pady=(0,5))
    algorithm.trace_add('write', check_algo)

    # IMAGE VIEW
    image_view = Frame(root, width=820, height=370)
    image_view.grid_propagate(False)
    image_view.grid(column=0, row=2)
    image_view.columnconfigure(0, minsize=410)
    image_view.columnconfigure(1, minsize=410)

    # Input view
    input_view_wrapper = Frame(image_view, width=400, height=370, bg=PREVIEW_BACKGROUND_COLOR)
    input_view_wrapper.grid_propagate(False)
    input_view_wrapper.grid(column=0, row=0)
    input_view = Frame(input_view_wrapper, bg=PREVIEW_BACKGROUND_COLOR)
    input_view.grid(column=0, row=0)

    input_title = Label(input_view, text="INPUT", font='SegoeUI 10 bold', bg=PREVIEW_BACKGROUND_COLOR)
    input_title.grid(column=0, row=0, pady=5)
    input_display = Label(input_view, text="Select an image to preview.", height=20, bg=PREVIEW_BACKGROUND_COLOR)
    input_display.grid(column=0, row=1)
    input_label = Label(input_view, text="", bg=PREVIEW_BACKGROUND_COLOR)
    input_label.grid(column=0, row=2, pady=5)
    input_view.place(in_=input_view_wrapper, anchor=N, relx=.5)

    # Output view
    output_view_wrapper = Frame(image_view, width=400, height=370, bg=PREVIEW_BACKGROUND_COLOR)
    output_view_wrapper.grid_propagate(False)
    output_view_wrapper.grid(column=1, row=0)
    output_view = Frame(output_view_wrapper, bg=PREVIEW_BACKGROUND_COLOR)
    output_view.grid(column=0, row=0)
    
    output_title = Label(output_view, text="OUTPUT", font='SegoeUI 10 bold', bg=PREVIEW_BACKGROUND_COLOR)
    output_title.grid(column=0, row=0, pady=5)
    output_display = Label(output_view, text="Result will be displayed here.", height=20, bg=PREVIEW_BACKGROUND_COLOR)
    output_display.grid(column=0, row=1)
    output_label = Label(output_view, text="", bg=PREVIEW_BACKGROUND_COLOR)
    output_label.grid(column=0, row=2, pady=5)
    output_view.place(in_=output_view_wrapper, anchor=N, relx=.5)

    # EXECUTE BUTTON
    go_button = Button(root, text="GO!", font='SegoeUI 10 bold', width=10, command=invoke_go)
    go_button.grid(column=0, row=3, pady=(8, 0))

    # LOG
    log = Label(root, text="")
    log.grid(column=0, row=4, pady=(0,5))

    window.mainloop()
    return

main()