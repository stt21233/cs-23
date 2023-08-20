import tkinter as tk

from tkinter import ttk  # Import ttk module for Treeview widget


# Create a new Tkinter window
window = tk.Tk()
window.title("Basketball Analysis Program")

# Create a frame to hold the input fields and the submit button
frame = tk.Frame(window)
frame.pack()

# Create a label for each of the input fields
tk.Label(frame, text="Blocks").grid(row=0, column=0)
tk.Label(frame, text="Turnovers").grid(row=0, column=1)
tk.Label(frame, text="Steals").grid(row=2, column=0)
tk.Label(frame, text="Assists").grid(row=2, column=1)
tk.Label(frame, text="Free Throw Success").grid(row=4, column=0)
tk.Label(frame, text="Free Throw Failed").grid(row=4, column=1)

# Create an entry field for users to enter their data
blocks_entry = tk.Entry(frame)
blocks_entry.grid(row=1, column=0)
turnovers_entry = tk.Entry(frame)
turnovers_entry.grid(row=1, column=1)
steals_entry = tk.Entry(frame)
steals_entry.grid(row=3, column=0)
assists_entry = tk.Entry(frame)
assists_entry.grid(row=3, column=1)
free_throw_success_entry = tk.Entry(frame)
free_throw_success_entry.grid(row=5, column=0)
free_throw_failed_entry = tk.Entry(frame)
free_throw_failed_entry.grid(row=5, column=1)

# Create a function to process the data entered by the user
def submit():
    # Get the data from the input fields
    blocks = blocks_entry.get()
    turnovers = turnovers_entry.get()
    steals = steals_entry.get()
    assists = assists_entry.get()
    free_throw_success = free_throw_success_entry.get()
    free_throw_failed = free_throw_failed_entry.get()
    
    # Call the display_results function with the entered data
    display_results(blocks, turnovers, steals, assists, free_throw_success, free_throw_failed)

# Create a submit button
submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=6, columnspan=2)  # Use columnspan to make the button span two columns




# Create a function to display the results in a table
def display_results(blocks, turnovers, steals, assists, free_throw_success, free_throw_failed):
    # Create a frame to hold the table that will display the results
    result_frame = tk.Frame(window)
    result_frame.pack()

    # Create a table using Treeview widget
    table = ttk.Treeview(result_frame, columns=("Blocks", "Turnovers", "Steals", "Assists", "Free Throw Success", "Free Throw Failed"))

    table.heading("#1", text="Blocks")
    table.heading("#2", text="Turnovers")
    table.heading("#3", text="Steals")
    table.heading("#4", text="Assists")
    table.heading("#5", text="Free Throw Success")
    table.heading("#6", text="Free Throw Failed")
    
    table.grid(row=0, column=0)

    # Add data to the table
    table.insert("", "end", values=(blocks, turnovers, steals, assists, free_throw_success, free_throw_failed))

    # Create a button to close the window
    close_button = tk.Button(result_frame, text="Close", command=result_frame.destroy)
    close_button.grid(row=1, column=0)
     
     
     


# set window size
window.geometry("500x200")

# Run the mainloop
window.mainloop()