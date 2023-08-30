import tkinter as tk

def on_button_click_F():
    value = entry.get()
    result = (float(value) - 32) * 5/9
    result_label.config(text=str(result))
    
def on_button_click_C():
    value = entry.get()
    result = (float(value) * 9/5) + 32
    result_label.config(text=str(result))
    
def on_switch_click():
    global is_farenheit
    is_farenheit = not is_farenheit
    
    if is_farenheit:
        print("Switching to Celsius")
        button.config(command=on_button_click_C)
        label.config(text="Enter temperature (Celsius):")
    else:
        print("Switching to Farenheit")
        button.config(command=on_button_click_F)
        label.config(text="Enter temperature (Farenheit):")

# main application window
root = tk.Tk()
root.title("Temperature Converter")

button_switch = tk.Button(root, text="Switch", command=on_switch_click)
button_switch.grid(row=0, column=0, columnspan=3)

# create the Fahrenheit entry frame with an Entry
label = tk.Label(root, text="Enter temperature (Farenheit):")
label.grid(row=1, column=0)

# create the Fahrenheit entry frame with an Entry
entry = tk.Entry(root)
entry.grid(row=1, column=1, sticky="EW")

# create the conversion buttons in a frame
button = tk.Button(root, text="Convert", command=on_button_click_F)
button.grid(row=1, column=2)

# create the result display label
result_label = tk.Label(root, text="Result")
result_label.grid(row=2, column=0, columnspan=3)

# set the initial state of the app
is_farenheit = True

# start the GUI
root.mainloop()