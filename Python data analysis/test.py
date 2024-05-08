import tkinter as tk

class DataPlotterApp:
    def __init__(self, master):
        self.master = master
        master.title("Data Plotter")

        '''Import frame'''
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

        # Listbox to display imported data
        self.data_listbox = tk.Listbox(self.import_frame, width=70, height=10)
        self.data_listbox.grid(row=1, column=0, columnspan=3)

        '''Plot type frame'''
        self.plot_type_frame = tk.Frame(master)
        self.plot_type_frame.grid(row=0, column=1, padx=10, pady=10)

        # Plot type drop down menu
        self.plot_type_var = tk.StringVar(self.plot_type_frame)
        self.plot_type_var.set("Absorption")  # Default option
        self.plot_type_menu = tk.OptionMenu(self.plot_type_frame, self.plot_type_var, "Absorption", "Single Voltage", "EA Series")#, command=self.plot_type_selected)
        self.plot_type_menu.pack(side=tk.RIGHT, padx=5, pady=10)

    def import_data(self):
        # Placeholder method for importing data
        pass

    def data_type_selected(self, selected_type):
        # Placeholder method for handling data type selection
        pass

def main():
    root = tk.Tk()
    app = DataPlotterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
