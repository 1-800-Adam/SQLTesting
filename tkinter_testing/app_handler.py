import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SQL Testing App")
        self.geometry("400x300")
        
        # Create a container for all frames
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        # Create a dictionary to hold references to frames
        self.frames = {}
        
        # Initialize the pages
        self.initialize_pages()

        # Show the initial page
        self.show_page("SettingsPage")

    def initialize_pages(self):
        # Create and add frames to the container
        for Page in (SettingsPage, InitializedPage):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_page(self, page_name):
        # Show the specified page
        frame = self.frames[page_name]
        frame.tkraise()

    # def on_initialize(self):
    #     # Move to InitializedPage after initialization
    #     self.show_page("InitializedPage")

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Button to trigger initialization
        tk.Button(self, text="Connect to db", command=self.initialize).pack(pady=20)

    def initialize(self):
        # Perform any initialization tasks here
        # Then switch to the InitializedPage
        self.controller.show_page("InitializedPage")

class InitializedPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Text box and button on the initialized page
        self.text_box = tk.Entry(self)
        self.text_box.pack(pady=10, padx=10)
        
        tk.Button(self, text="Submit", command=self.submit).pack(pady=10)

    def submit(self):
        # Handle text box submission
        text_value = self.text_box.get()
        print(f"Text box value: {text_value}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
