"""
These scripts are for testing out SQL Functions in python: https://www.geeksforgeeks.org/sql-using-python/
"""
#import sqlite3
#import logging
#import pandas as pd
import tkinter as tk



def application_init():
    def greet():
        label.config(text=f"Hello, {entry.get()}!")

    root = tk.Tk() #root is the main app
    root.title("SQL App")

    tk.Label(root, text="Enter your name:").pack(pady=5) #label
    entry = tk.Entry(root) #entry on the root application
    entry.pack(pady=5) #packs the gui for positioning
    tk.Button(root, text="Greet", command=greet).pack(pady=5)
    label = tk.Label(root, text="")
    label.pack(pady=5)

    return root

def app_mainloop(app_root=None):
    app_root.mainloop()






def main():
    my_app = application_init()
    app_mainloop(my_app)














main()