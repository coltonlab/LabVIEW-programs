import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import matplotlib.pyplot as plt
import pandas as pd
import plot_colton_graphs as pcg
import read_colton_files as rcf
import numpy as np

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
        self.data_type_menu = tk.OptionMenu(self.import_frame, self.data_type_var, "Transmission", "Blank", "EA Voltage", "EA Voltage Series")#, command=self.data_type_selected)
        self.data_type_menu.grid(row=0, column=1)

        # Import Data button
        self.import_button = tk.Button(self.import_frame, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=2)

        # Listbox to display imported data
        self.data_listbox = tk.Listbox(self.import_frame, width=70, height=10)
        self.data_listbox.grid(row=1, column=0, columnspan=3)


        ''' Delete Selected items '''
        self.delete_button = tk.Button(self.import_frame, text="Delete Selected", command=self.delete_selected_items)
        self.delete_button.grid(row=2, column=0)


        # '''Plot type frame'''
        # self.plot_type_frame = tk.Frame(self.import_frame)
        # self.plot_type_frame.grid(row=2, column=2) 

        # Plot type drop down menu
        self.plot_type_var = tk.StringVar(self.import_frame)
        self.plot_type_var.set("Absorption")  # Default option
        self.plot_type_menu = tk.OptionMenu(self.import_frame, self.plot_type_var, "Absorption", "Single Voltage", "EA Series")#, command=self.plot_type_selected)
        self.plot_type_menu.grid(row=2, column=1)
        # self.plot_type_menu.pack(side=tk.RIGHT, padx=5, pady=10)

        
        # Plot Data button on the right
        self.plot_button = tk.Button(self.import_frame, text="Plot Data")#, command=self.plot_data)
        self.plot_button.grid(row=2, column=2) 

        # # Close Program button on the right
        # self.close_button = tk.Button(master, text="Close Program", command=master.quit)
        # self.close_button.pack(side=tk.RIGHT, padx=5, pady=10)

        
        print('test')
        # Dictionary to store imported data
        self.imported_data = {}



    def import_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("xls files", "*.xls")])
        
        if file_path:
            try:
                data_type = self.data_type_var.get()


                # EA Voltage
                if data_type == "EA Voltage":
                    voltage = simpledialog.askinteger("EA Voltage", "Enter voltage used:")
                    if voltage is None:
                        return  # If user cancels, return without importing
                    

                    # self.imported_data["EA Voltage"] = (file_path, voltage)

                    self.data_listbox_insert_replace("EA Voltage", f"{voltage}V: {file_path}")
                

                # EA Voltage Series
                if data_type == "EA Voltage Series":
                    voltage_range_string = simpledialog.askstring("Voltage Range", "Enter the range of voltages (start-end):")
                    if voltage_range_string is None:
                        return  # If user cancels, return without importing
                    
                    # self.imported_data["EA Voltage"] = (file_path, voltage)
                    self.data_listbox_insert_replace("EA Voltage Series", f"{voltage_range_string}V: {file_path}")
                    

                # Transmission
                if data_type == "Transmission":
                    pass


                # Blank Scan
                if data_type == "Blank":
                    pass

                else:
                    self.imported_data[data_type] = file_path
                    self.data_listbox_insert_replace(data_type, f"{data_type}: {file_path}")
                # messagebox.showinfo("Success", "Data imported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def delete_selected_items(self):
        # Get selected indices
        selected_indices = self.data_listbox.curselection()

        # Delete selected items from the list box
        for idx in reversed(selected_indices):
            self.data_listbox.delete(idx)


    def plot_data(self):
        selected_type = self.data_type_var.get()
        if selected_type in self.imported_data:
            file_path = self.imported_data[selected_type]
            data = pd.read_csv(file_path)
            data.plot()
            plt.title(selected_type)
            plt.show()
        else:
            messagebox.showerror("Error", "No data imported yet!")

    def data_type_selected(self, selected_type):
        if selected_type == "EA Voltage":
            messagebox.showinfo("EA Voltage", "Please enter the voltage used when prompted.")

    def data_listbox_insert_replace(self, data_type, data_entry):
        # Remove previous entry of the same data_type if it exists
        indices = self.data_listbox.curselection()
        for index in indices:
            entry_text = self.data_listbox.get(index)
            if data_type in entry_text:
                self.data_listbox.delete(index)
                break
        self.data_listbox.insert(tk.END, data_entry)

###################################################################################################################################################

    def Absorption_template(self):
        fig, ax = plt.subplots()

        # date where the data is stored
        file_path = 'C:/Data/2024-02-22/'

        blank_file = file_path + 'Trans Blank 350-650nm 15K.xls'
        trans_file = file_path + 'Trans 2-CF3 PESI 350-650nm 15K.xls'

        # Dictionary that holds all of the data with input voltages
        self.data = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        self.data['blank'] = rcf.read_trans_data(blank_file)
        self.data['trans'] = rcf.read_trans_data(trans_file)

        # plot data
        pcg.plot_absorption(self.data, ax=ax)
        
        plt.show()


    def EA_voltage_template(self):
        # date where the data is stored
        file_path = 'C:/Data/2024-02-22/'

        blank_file = file_path + 'Blank 2-MePESI 16K 300-700nm.xls'
        trans_file = file_path + 'Trans 2-MePESI 16K 300-700nm.xls'
        voltage_file = file_path + 'EA 250V 2-MePESI 295K fast 2.xls'
        voltage = 250
        voltage_file = file_path + '300V EA 2-CF3 PESI 350-650nm 15K.xls'
        # fig_name = 'Y6 data.png' 

        # Dictionary that holds all of the self.self.data with input voltages
        self.data = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        self.data['blank'] = rcf.read_trans_data(blank_file)
        self.data['trans'] = rcf.read_trans_data(trans_file)
        self.data['voltage'] = rcf.read_trans_data(voltage_file) # For a single voltage

        # Create the first plot with the first y-axis
        fig, ax1 = plt.subplots()

        pcg.plot_EA_voltage(self.data, ax=ax1, voltage=voltage)
        # ax1.set_ylabel('Y1', color='blue')

        ax2 = ax1.twinx()
        ABS_color = 'red'
        pcg.plot_absorption(self.data, ax=ax2, color=ABS_color)


        # make the right ABS color

        ax2.set_ylabel('Absorption (OD)', color=ABS_color)

        # Set the color of the right y-axis line
        ax2.spines['right'].set_color(ABS_color)

        # Set the color of the right y-axis ticks to ABS color
        ax2.yaxis.set_tick_params(color=ABS_color)

        # Set the color of the tick labels on the right y-axis to ABS color
        for label in ax2.get_yticklabels():
            label.set_color(ABS_color)

        
        # plt.savefig(fig_name, format='png', dpi=300)
        plt.show()

    def EA_series_template(self):
        # date where the data is stored
        file_path = 'C:/Data/2024-01-10/'

        blank_file = file_path + 'Blank 2-MePESI 16K 300-700nm.xls'
        trans_file = file_path + 'Trans 2-MePESI 16K 300-700nm.xls'
        voltage_series_file = file_path + 'EA 2-MePESI 16K 300-700nm 100-300V.xls'

        # Dictionary that holds all of the data with input voltages
        self.data = {}

        # trans and blank will have strings as their voltage value, but each voltage will be an integer
        self.data['blank'] = rcf.read_trans_data(blank_file)
        self.data['trans'] = rcf.read_trans_data(trans_file)
        self.data['voltages'] = {}
        self.data['voltages'] = rcf.read_voltage_series_data(voltage_series_file) # This returns a dictionary with the values
        
        # for i in voltages:
        #     data['voltages'][i] = rcf.read_trans_data(file_path+str(i)+end_of_filename) # For a single voltage

        # Create the first plot with the first y-axis
        fig, ax1 = plt.subplots()

        pcg.plot_EA_series(self.data, ax=ax1, color_map_name='plasma')

        ax2 = ax1.twinx()
        ABS_color = 'green'
        pcg.plot_absorption(self.data, ax=ax2, color=ABS_color)


        # make the right axis ABS color

        ax2.set_ylabel('Absorption (OD)', color=ABS_color)

        # Set the color of the right y-axis line
        ax2.spines['right'].set_color(ABS_color)

        # Set the color of the right y-axis ticks to ABS color
        ax2.yaxis.set_tick_params(color=ABS_color)

        # Set the color of the tick labels on the right y-axis to ABS color
        for label in ax2.get_yticklabels():
            label.set_color(ABS_color)

        
        # plt.savefig(fig_name, format='png', dpi=300)
        plt.show()



###################################################################################################################################################

def main():
    root = tk.Tk()
    app = DataPlotterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
