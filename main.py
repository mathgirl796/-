import pynput
import tkinter
import time
import threading
import tkinter.ttk

trigger_char = "q"

mouse = pynput.mouse.Controller()
loop_status = False

def on_press(key):
    global status
    global loop_status
    try:
        if hasattr(key, "char") and key.char == trigger_char:
            loop_status = True
            threading.Thread(target=loop_press_d).start()
    except Exception as e:
        print(e)

def on_release(key):
    global status
    global loop_status
    if hasattr(key, "char") and key.char == trigger_char:
        loop_status = False
        

listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

def loop_press_d():
    global status
    global loop_status
    while loop_status == True:
        mouse.press(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.left)
        print(loop_status)

def start_listener():
    global listener
    listener.stop()
    listener = pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

def stop_listener():
    global loop_status
    global listener
    listener.stop()


top = tkinter.Tk()
tk_button_start = tkinter.Button(top, text="start", command=start_listener)
tk_button_stop = tkinter.Button(top, text="stop", command=stop_listener)
combobox_var = tkinter.StringVar()
combobox = tkinter.ttk.Combobox(
    top, 
    textvariable=combobox_var, 
    value=("1", "2", "3", "[", "]", "\\", "q", "a", "z"))
combobox.current(0)
trigger_char = combobox['value'][0]
def set_trigger_char(event):
    global trigger_char
    trigger_char = combobox_var.get()
combobox.bind('<<ComboboxSelected>>', set_trigger_char)
combobox.configure(state="readonly")
varLabel = tkinter.StringVar()
label = tkinter.Label(top, textvariable=varLabel)
varLabel.set("触发字符：")

label.pack()
combobox.pack(padx=5, pady=10)
tk_button_start.pack()
tk_button_stop.pack()


# top.geometry("200x100")
top.mainloop()