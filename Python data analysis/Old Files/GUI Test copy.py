import tkinter as tk
from tkinter import ttk

class DataPlotterApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Plotter")

        # Import frame
        self.import_frame = tk.Frame(master)
        self.import_frame.grid(row=0, column=0, padx=10, pady=10)

        # Select Data type label
        self.data_type_label = tk.Label(self.import_frame, text="Select Data Type:")
        self.data_type_label.grid(row=0, column=0)

        # Select Data Type dropdown menu
        self.data_type_var = tk.StringVar(self.import_frame)
        self.data_type_var.set("Transmission")  # Default option
        self.data_type_menu = tk.OptionMenu(self.import_frame, self.data_type_var, "Transmission", "Blank", "EA Voltage", command=self.data_type_selected)
        self.data_type_menu.grid(row=0, column=1)

        # Import Data button
        self.import_button = tk.Button(self.import_frame, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=2)

        # Treeview to display imported data
        self.data_tree = ttk.Treeview(self.import_frame, columns=('Data Type', 'File Path'), show='headings')
        self.data_tree.heading('Data Type', text='Data Type')
        self.data_tree.heading('File Path', text='File Path')
        self.data_tree.grid(row=1, column=0, columnspan=3, sticky="nsew")  # Set sticky to "nsew"

        # Configure grid weights to allow resizing
        self.import_frame.columnconfigure(0, weight=1)  # Make the first column expandable
        self.import_frame.rowconfigure(1, weight=1)     # Make the second row expandable

    def import_data(self):
        data_type = self.data_type_var.get()
        file_path = "Some file path"  # Replace this with the actual file path
        self.data_tree.insert('', 'end', values=(data_type, file_path))

    def data_type_selected(self, selected_type):
        pass  # Placeholder method for handling data type selection

def main():
    root = tk.Tk()
    app = DataPlotterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
