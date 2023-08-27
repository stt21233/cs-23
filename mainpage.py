import tkinter as tk
from tkinter import ttk
  # Import ttk module for Treeview widget

# Create a new Tkinter window
window = tk.Tk()
window.title("Basketball Analysis Program")

# Create a title label with dark blue background and white text
title_label = tk.Label(window, text="Basketball Analysis Tracker", bg="darkblue", fg="white", font=("Helvetica", 14, "bold"))
title_label.pack(fill="x")

# Create a subheading label above the entry fields
subheading_label = tk.Label(window, text="Enter Team 1 Data", font=("Helvetica", 12, "bold"))
subheading_label.pack(pady=(10, 0))

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.quit)

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



# Create an empty list to store the entered data for both teams
teams_data = [[], []]

# Keep track of which team's data is being entered
current_team = 0

# Create a function to process the data entered by the user
def submit():
    global current_team
    
    # Get the data from the input fields
    team_data = (
        blocks_entry.get(), turnovers_entry.get(), steals_entry.get(),
        assists_entry.get(), free_throw_success_entry.get(), free_throw_failed_entry.get()
    )
    
    # Store the data in the appropriate team's data list
    teams_data[current_team].extend(team_data)
    
    # Clear the entry fields
    blocks_entry.delete(0, tk.END)
    turnovers_entry.delete(0, tk.END)
    steals_entry.delete(0, tk.END)
    assists_entry.delete(0, tk.END)
    free_throw_success_entry.delete(0, tk.END)
    free_throw_failed_entry.delete(0, tk.END)
    
    current_team += 1
    
    if current_team == 1:
        # Update the subheading label for the second cycle
        subheading_label.config(text="Enter Team 2 Data")
        
    if current_team == 2:
        # Call the display_results function with both teams' data
        display_results(teams_data[0], teams_data[1])
        
        # Reset the current_team counter and teams_data list
        current_team = 0
        teams_data[0].clear()
        teams_data[1].clear()
        
        # Reset the subheading label for the next first cycle
        subheading_label.config(text="Enter Team 1 Data")
         # Check if any of the input fields are empty
    
    # REFINING: STRING THAT CHECKS FOR MISSING DATA.    
    missing_indices = [i for i, data in enumerate(team_data) if data == '']
    if missing_indices:
        # Display "missing" in the entry boxes that lack data, and set the color to red
        for index in missing_indices:
            entry_boxes[index].delete(0, tk.END)
            entry_boxes[index].insert(0, "missing")
            entry_boxes[index].config(fg="red")  # Set the text color to red
        return

    # Restore the normal color of entry boxes
    for entry in entry_boxes:
        entry.config(fg="black")  # Set the text color back to black

    # Store the data in the appropriate team's data list
    teams_data[current_team].extend(team_data)
    
    # Clear the entry fields
    for entry in entry_boxes:
        entry.delete(0, tk.END)
    
    current_team += 1
    
    if current_team == 1:
        # Update the subheading label for the second cycle
        subheading_label.config(text="Enter Team 2 Data")
        
    if current_team == 2:
        # Call the display_results function with both teams' data
        display_results(teams_data[0], teams_data[1])
        
        # Reset the current_team counter and teams_data list
        current_team = 0
        teams_data[0].clear()
        teams_data[1].clear()
        
        # Reset the subheading label for the next first cycle
        subheading_label.config(text="Enter Team 1 Data")

# REFINING: for easier management. 
entry_boxes = [
    blocks_entry, turnovers_entry, steals_entry,
    assists_entry, free_throw_success_entry, free_throw_failed_entry
]

# Create a submit button
submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=6, columnspan=2, pady=10)  # Use columnspan to make the button span two columns

#yellow aesthetic - left side
yellow_square = tk.Label(window, text="", bg="yellow")
yellow_square.place(x=150, y=29, width=30, height=200) 

#yellow aesthetic - right side
yellow_square = tk.Label(window, text="", bg="yellow")
yellow_square.place(x=525, y=29, width=30, height=200) 

# Create a subheading for results (initially hidden)
results_label = tk.Label(frame, text="", font=("Helvetica", 12, "bold"))


# Create a function to display the results in a table
def display_results(team1_data, team2_data):
    global results_label
    
    # Create a frame to hold the table that will display the results
    result_frame = tk.Frame(window)
    result_frame.pack()

    # Show the RESULTS subheading between the Submit button and the generated table
    results_label.config(text="RESULTS")
    results_label.grid(row=7, columnspan=2, pady=10)  # Use columnspan to span two columns

    # Create a table using Treeview widget
    table = ttk.Treeview(result_frame, columns=("Metrics", "Team 1", "Team 2"), show='headings')
    table.heading("Metrics", text="Metrics")
    table.heading("Team 1", text="Team 1")
    table.heading("Team 2", text="Team 2")
    table.grid(row=0, column=0)

    metrics = ["Blocks", "Turnovers", "Steals", "Assists", "Free Throw Success", "Free Throw Failed"]
    for metric in metrics:
        table.insert("", "end", values=(metric, team1_data[metrics.index(metric)], team2_data[metrics.index(metric)]))

    # Create a button to close the window
    close_button = tk.Button(result_frame, text="Close", command=result_frame.destroy)
    close_button.grid(row=1, column=0)


# set window size
window.geometry("700x1000")

# Run the mainloop
window.mainloop()
