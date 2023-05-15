import tkinter as tk
import ttkbootstrap as ttk
import pyperclip
from convert import Converter


class GenarateWindow:
    def __init__(self):
        # -----------------------------------Window=========================================================#
        self.window = ttk.Window(title="Text-Morse Converter",
                                 themename="flatly",
                                 size=(600, 450),
                                 resizable=(False, False),)

        self.style = ttk.Style("darkly")

        # -----------------------------------Entry =========================================================#
        self.text_var = ttk.StringVar()
        self.data_input = ttk.Entry(self.window, textvariable=self.text_var,font=("Arial", 15),)
        self.data_input.focus()
        self.data_input.bind("<Return>", lambda event: self.config_label())
        self.data_input.grid(row=0, column=1, pady=15)

        # -----------------------------------Radio Buttons===================================================#
        self.selected_option = tk.StringVar()
        self.option1 = tk.Radiobutton(self.window,
                                      text="Text to Morse Code",
                                      font=("Arial", 14),
                                      variable=self.selected_option,
                                      value="Text to Morse Code")

        self.option2 = tk.Radiobutton(self.window,
                                      text="Morse Code to Text",
                                      font=("Arial", 14),
                                      variable=self.selected_option,
                                      value="Morse Code to Text")

        self.option1.grid(row=1, column=1)
        self.option2.grid(row=2, column=1,padx=180,)
        self.selected_option.set("Text to Morse Code")

        # -----------------------------------Label=========================================================#

        self.output_label = ttk.Label(self.window, text="Enter Text", font=("Arial", 20), wraplength=500,)
        self.output_label.grid(row=3, column=1,)

        self.text_var.trace_add("write", lambda *args: self.config_label())

        # -----------------------------------Button=========================================================#
        self.copy_button = ttk.Button(self.window, text="Copy to Clipboard", command=self.CopytoClipboard)
        # self.copy_button.grid(row=4, column=1, padx=225,pady=200)
        self.copy_button.place(x=225, y=390)

        # -----------------------------------------------------------------------------------------------#
        self.window.mainloop()

    def config_label(self):
        '''Update output_label with the text in the data_input entry'''


        value = self.selected_option.get()
        # convert = str(self.data_input.get())
        convert = self.text_var.get()


        if len(convert) > 70:
            self.text_var.set(convert[:70])
        #limit the text in the entry to 70 characters

        if value == "Text to Morse Code":
            conversion = Converter().convert_text(convert)
        elif value == "Morse Code to Text":
            conversion = Converter().convert_morsecode(convert)
        else:
            conversion = "An Error Occured. Pleasse Try Again"

        self.output_label.config(text= conversion)

    def CopytoClipboard(self):
        '''Copy text in output_label to clipboard'''
        clipboard_text = self.output_label.cget("text")
        # clipboard_text = self.data_input.get()
        pyperclip.copy(clipboard_text)











