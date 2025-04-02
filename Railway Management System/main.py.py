import pandas as pd
from tkinter import *
from tkinter import Tk, Label, Entry, Button, Toplevel, Text
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Declare entry widgets as global variables
entry_admin_id = None
entry_admin_password = None
admin_window = None
train_choice_window = None
interstate_menu_window = None
update_window = None

def display_menu():
    print("\nMENU")
    print("1) Modify The Train Details ")
    print("2) View Train Details")
    print("3) View Passenger Details")
    print("4) Add a new admin")
    print("5) Display Statistics")
    print("6) Exit")

    admin_choice = int(input("Enter your choice:"))
    if admin_choice == 1:
        modify_train_details()
    elif admin_choice == 2:
        view_train_details()
    elif admin_choice == 3:
        view_passenger_details()
    elif admin_choice == 4:
        add_new_admin()
    elif admin_choice == 5:
        display_statistics()
        
    elif admin_choice == 6:
        exit()

def admin_login():
    global entry_admin_id, entry_admin_password, admin_window
    
    # Function to handle admin login
    admin_id = entry_admin_id.get()
    admin_password = entry_admin_password.get()
    
    # Load admin details from file
    df_admin = pd.read_csv("AdminDetails.txt")

    # Check if admin credentials are valid
    valid_admin = False
    for i in range(len(df_admin)):
        if admin_id == str(df_admin.iloc[i, 3]) and admin_password == str(df_admin.iloc[i, 4]):
            valid_admin = True
            break
    
    if valid_admin:
        print("Admin Login Successful")
        messagebox.showinfo("Login Successful", "Admin Login Successful")
        admin_window.destroy()  # Close login window
        display_menu_window()  # Open menu choice window
        # Perform actions for successful login (to be implemented)
    else:
        print("Invalid Admin ID or Password")
        messagebox.showerror("Login Failed", "Invalid Admin ID or Password. Please try again.")
        # Clear entry fields
        entry_admin_id.delete(0, END)
        entry_admin_password.delete(0, END)

def display_menu_window():
    global admin_window
    admin_window = Tk()
    admin_window.title("Admin Menu")
    admin_window.geometry("300x200")  # Adjusted geometry

    Button(admin_window, text="Modify The Train Details", command=modify_train_details).pack()
    Button(admin_window, text="View Train Details", command=view_train_details).pack()
    Button(admin_window, text="View Passenger Details", command=view_passenger_details).pack()
    Button(admin_window, text="Add a new admin", command=add_new_admin).pack()
    Button(admin_window, text="Display Statistics", command=execute_both_commands).pack()
    Button(admin_window, text="Exit", command=admin_window.quit).pack()

def modify_train_details():
    global train_choice_window
    train_choice_window = Tk()
    train_choice_window.title("Train Choice")
    train_choice_window.geometry("300x100")
    
    Label(train_choice_window, text="Choose the type of train:").pack()
    Button(train_choice_window, text="InterState Train", command=lambda: handle_train_choice("InterState Train")).pack()
    Button(train_choice_window, text="InterCity Train", command=lambda: handle_train_choice("InterCity Train")).pack()

def handle_train_choice(choice):
    global train_choice_window
    train_choice_window.destroy()
    if choice == "InterState Train":
        display_interstate_menu()
    elif choice == "InterCity Train":
        display_intercity_menu()

def display_interstate_menu():
    global interstate_menu_window
    interstate_menu_window = Tk()
    interstate_menu_window.title("InterState Train Menu")
    interstate_menu_window.geometry("300x200")
    
    Label(interstate_menu_window, text="InterState Train Menu").pack()
    Button(interstate_menu_window, text="Add New Train", command=add_new_train_interstate).pack()
    Button(interstate_menu_window, text="Remove a Train", command=remove_train_interstate).pack()
    Button(interstate_menu_window, text="Update Train Details", command=update_train_details).pack()
    Button(interstate_menu_window, text="Go Back", command=go_back).pack()
    
    #Button(interstate_menu_window, text="InterCity Train", command=lambda: handle_train_choice("InterCity Train")).pack()
    

def display_intercity_menu():
    global intercity_menu_window
    intercity_menu_window = Tk()
    intercity_menu_window.title("InterCity Train Menu")
    intercity_menu_window.geometry("300x200")

    Label(intercity_menu_window, text="InterCity Train Menu").pack()
    Button(intercity_menu_window, text="Add New Train", command=add_new_train_intercity).pack()
    Button(intercity_menu_window, text="Remove a Train", command=remove_train_intercity).pack()
    Button(intercity_menu_window, text="Update Train Details", command=update_intercitytrain_details).pack()
    Button(intercity_menu_window, text="Go Back", command=intercity_menu_window.destroy).pack()



def add_new_train_interstate():
    global interstate_menu_window, entry_train_id, entry_train_name, entry_start_state, entry_start_station, entry_end_state, entry_end_station, entry_distance, entry_dep_time, entry_arrival_time, entry_fare, entry_travel_time
    
    
    add_train_window = Tk()
    add_train_window.title("Add New Train - InterState")
    
    Label(add_train_window, text="Train ID:").grid(row=0, column=0, padx=5, pady=5)
    entry_train_id = Entry(add_train_window)
    entry_train_id.grid(row=0, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Train Name:").grid(row=1, column=0, padx=5, pady=5)
    entry_train_name = Entry(add_train_window)
    entry_train_name.grid(row=1, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Start State:").grid(row=2, column=0, padx=5, pady=5)
    entry_start_state = Entry(add_train_window)
    entry_start_state.grid(row=2, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Start Station:").grid(row=3, column=0, padx=5, pady=5)
    entry_start_station = Entry(add_train_window)
    entry_start_station.grid(row=3, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="End State:").grid(row=4, column=0, padx=5, pady=5)
    entry_end_state = Entry(add_train_window)
    entry_end_state.grid(row=4, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="End Station:").grid(row=5, column=0, padx=5, pady=5)
    entry_end_station = Entry(add_train_window)
    entry_end_station.grid(row=5, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Distance:").grid(row=6, column=0, padx=5, pady=5)
    entry_distance = Entry(add_train_window)
    entry_distance.grid(row=6, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Departure Time:").grid(row=7, column=0, padx=5, pady=5)
    entry_dep_time = Entry(add_train_window)
    entry_dep_time.grid(row=7, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Arrival Time:").grid(row=8, column=0, padx=5, pady=5)
    entry_arrival_time = Entry(add_train_window)
    entry_arrival_time.grid(row=8, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Fare:").grid(row=9, column=0, padx=5, pady=5)
    entry_fare = Entry(add_train_window)
    entry_fare.grid(row=9, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Travel Time:").grid(row=10, column=0, padx=5, pady=5)
    entry_travel_time = Entry(add_train_window)
    entry_travel_time.grid(row=10, column=1, padx=5, pady=5)
    
    Button(add_train_window, text="Submit", command=submit_new_train_interstate).grid(row=11, columnspan=2, padx=5, pady=5)

def submit_new_train_interstate():
    global entry_train_id, entry_train_name, entry_start_state, entry_start_station, entry_end_state, entry_end_station, entry_distance, entry_dep_time, entry_arrival_time, entry_fare, entry_travel_time
    
    trainID = entry_train_id.get()
    trainName = entry_train_name.get()
    startState = entry_start_state.get()
    startStation = entry_start_station.get()
    endState = entry_end_state.get()
    endStation = entry_end_station.get()
    distance = entry_distance.get()
    depTime = entry_dep_time.get()
    arrivalTime = entry_arrival_time.get()
    fare = entry_fare.get()
    travelTime = entry_travel_time.get()
    
    # Write train details to file
    state_train_file = open("trainBtwStates.txt", "a+")
    state_train_file.writelines(f"\n{trainID},{trainName},{startState},{startStation},{endState},{endStation},{distance},{depTime},{arrivalTime},{fare},{travelTime}")
    state_train_file.close()
    
    messagebox.showinfo("Success", "New train added successfully.")
    
    # Clear entry fields
    entry_train_id.delete(0, END)
    entry_train_name.delete(0, END)
    entry_start_state.delete(0, END)
    entry_start_station.delete(0, END)
    entry_end_state.delete(0, END)
    entry_end_station.delete(0, END)
    entry_distance.delete(0, END)
    entry_dep_time.delete(0, END)
    entry_arrival_time.delete(0, END)
    entry_fare.delete(0, END)
    entry_travel_time.delete(0, END)

def remove_train_interstate():
    global interstate_menu_window


    # Create a new window for train removal
    remove_train_window = Tk()
    remove_train_window.title("Remove Train - InterState")

    # Function to handle train removal
    def submit_remove_train():
        removeID = entry_remove_train_id.get()
        df = pd.read_csv("trainBtwStates.txt")
        flag = 0
        for i in range(len(df)):
            current_train_id = str(df.iloc[i, 0]).strip()  # Convert to string and strip leading and trailing whitespaces
            print("Checking train ID:", current_train_id)
            if str(removeID).strip() == current_train_id:
                df = df.drop(i)
                df = df.reset_index(drop=True)
                df.to_csv("trainBtwStates.txt", index=False)
                flag = 1
                break
        if flag == 0:
            print("\nTrain with ID {} is not found !".format(removeID))
        elif flag == 1:
            print("\nTrain with ID {} removed successfully\n".format(removeID))
        remove_train_window.destroy()  # Close remove train window

    # UI elements for train removal
    Label(remove_train_window, text="Enter the train ID to remove:").pack()
    entry_remove_train_id = Entry(remove_train_window)
    entry_remove_train_id.pack()
    Button(remove_train_window, text="Remove", command=submit_remove_train).pack()




'''def display_interstate_menu():
    global interstate_menu_window
    interstate_menu_window = Tk()
    interstate_menu_window.title("InterState Train Menu")
    interstate_menu_window.geometry("300x200")
    
    Label(interstate_menu_window, text="InterState Train Menu").pack()
    Button(interstate_menu_window, text="Add New Train", command=add_new_train_interstate).pack()
    Button(interstate_menu_window, text="Remove a Train", command=remove_train_interstate).pack()
    Button(interstate_menu_window, text="Update Train Details", command=update_train_details).pack()
    Button(interstate_menu_window, text="Go Back", command=go_back).pack()'''



def execute_both_commands():
    display_statistics()
    display_interstate_statistics()

def display_statistics():
    # Load the data
    df = pd.read_csv("trainBtwCities.txt")

    # Extract ticket fares
    ticket_fares = df['TICKET FARE']

    # Create a new tkinter window
    stats_window = Toplevel()
    stats_window.title("Statistics")
    stats_window.geometry("600x400")

    # Plot histogram
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(ticket_fares, bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Ticket Fare Distribution for Intercity Trains')
    ax.set_xlabel('Ticket Fare')
    ax.set_ylabel('Frequency')
    ax.grid(True)

    # Embed the plot into tkinter window
    canvas = FigureCanvasTkAgg(fig, master=stats_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add a button to close the window
    close_button = Button(stats_window, text="Close", command=stats_window.destroy)
    close_button.pack()
    display_interstate_statistics()
    # Run the tkinter event loop
    stats_window.mainloop()

def display_interstate_statistics():
    # Load the data
    df = pd.read_csv("trainBtwStates.txt")

    # Extract ticket fares
    ticket_fares = df['FARE']

    # Create a new tkinter window
    stats_window = Toplevel()
    stats_window.title("Interstate Train Statistics")
    stats_window.geometry("600x400")

    # Plot histogram
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(ticket_fares, bins=20, color='skyblue', edgecolor='black')
    ax.set_title('Ticket Fare Distribution for Interstate Trains')
    ax.set_xlabel('Ticket Fare (in Rs)')
    ax.set_ylabel('Frequency')
    ax.grid(True)

    # Embed the plot into tkinter window
    canvas = FigureCanvasTkAgg(fig, master=stats_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Add a button to close the window
    close_button = Button(stats_window, text="Close", command=stats_window.destroy)
    close_button.pack()

    # Run the tkinter event loop
    stats_window.mainloop()



def update_train_details():
    global interstate_menu_window

    def update_choice():
        global update_window  # Declare update_window as global
        update_window = Tk()
        update_window.title("Update Train Details")
        update_window.geometry("300x500")


        Label(update_window, text="\nWhat detail do you want to update?\n").pack()
        Label(update_window, text="1) Train ID").pack()
        Label(update_window, text="2) Train Name").pack()
        Label(update_window, text="3) Start Station").pack()
        Label(update_window, text="4) End Station").pack()
        Label(update_window, text="5) Start State").pack()  # Added
        Label(update_window, text="6) End State").pack()  # Added
        Label(update_window, text="7) Distance Between Stations").pack()
        Label(update_window, text="8) Departure Time").pack()
        Label(update_window, text="9) Arrival Time").pack()
        Label(update_window, text="10) General Fare").pack()
        Label(update_window, text="11) Total Travel Time").pack()

        entry_update_choice = Entry(update_window)
        entry_update_choice.pack()

        Button(update_window, text="Submit", command=lambda: handle_update_choice(int(entry_update_choice.get()))).pack()

    def handle_update_choice(choice):
        update_window.destroy()
        global update_train_window
        update_train_window = Tk()
        update_train_window.title("Update Train Details")
        update_train_window.geometry("400x200")

        Label(update_train_window, text="Enter the train ID to update:").pack()
        entry_train_id = Entry(update_train_window)
        entry_train_id.pack()

        Button(update_train_window, text="Submit", command=lambda: get_update_value(choice, entry_train_id.get())).pack()

    def get_update_value(choice, train_id):
        update_train_window.destroy()
        update_value_window = Tk()
        update_value_window.title("Enter New Value")
        update_value_window.geometry("400x200")

        Label(update_value_window, text="Enter the new value:").pack()
        entry_new_value = Entry(update_value_window)
        entry_new_value.pack()
    
        def submit_new_value():
            new_value = entry_new_value.get()
            update_train_detail(choice, train_id, new_value)
            update_value_window.destroy()
        Button(update_value_window, text="Submit", command=lambda: update_train_detail(choice, train_id, entry_new_value.get())).pack()

    def update_train_detail(choice, train_id, new_value):
        df = pd.read_csv("trainBtwStates.txt")
        train_id = str(train_id)


        if choice == 1:
            df.loc[df['TRAIN ID'] == train_id, 'TRAIN ID'] = int(new_value)
        elif choice == 2:
            df.loc[df['TRAIN ID'] == train_id, 'TRAIN NAME'] = new_value
        elif choice == 3:
            df.loc[df['TRAIN ID'] == train_id, 'START STATION'] = new_value
        elif choice == 4:
            df.loc[df['TRAIN ID'] == train_id, 'END STATION'] = new_value
        elif choice == 5:
            df.loc[df['TRAIN ID'] == train_id, 'START STATE'] = new_value
        elif choice == 6:
            df.loc[df['TRAIN ID'] == train_id, 'END STATE'] = new_value  
        elif choice == 7:
            df.loc[df['TRAIN ID'] == train_id, 'DISTANCE'] = str(new_value)
        elif choice == 8:
            df.loc[df['TRAIN ID'] == train_id, 'DEPARTURE'] = new_value
        elif choice == 9:
            df.loc[df['TRAIN ID'] == train_id, 'ARRIVAL'] = new_value
        elif choice == 10:
            df.loc[df['TRAIN ID'] == train_id, 'FARE'] = float(new_value)
        elif choice == 11:
            df.loc[df['TRAIN ID'] == train_id, 'TIME'] = new_value

        df.to_csv("trainBtwStates.txt", index=False)
        messagebox.showinfo("Success", "Train details updated successfully.")

    update_choice()

def update_intercitytrain_details():
    global intercity_menu_window

    def update_choice():
        global update_window  # Declare update_window as global
        update_window = Tk()
        update_window.title("Update Train Details")
        update_window.geometry("300x300")

        Label(update_window, text="\nWhat detail do you want to update?\n").pack()
        Label(update_window, text="1) Train ID").pack()
        Label(update_window, text="2) Train Name").pack()
        Label(update_window, text="3) Start Station").pack()
        Label(update_window, text="4) End Station").pack()
        Label(update_window, text="5) Departure Time").pack()
        Label(update_window, text="6) Arrival Time").pack()
        Label(update_window, text="7) Distance (km)").pack()
        Label(update_window, text="8) Ticket Fare").pack()
        Label(update_window, text="9) Total Travel Time").pack()

        entry_update_choice = Entry(update_window)
        entry_update_choice.pack()

        Button(update_window, text="Submit", command=lambda: handle_update_choice(int(entry_update_choice.get()))).pack()

    def handle_update_choice(choice):
        update_window.destroy()
        global update_train_window
        update_train_window = Tk()
        update_train_window.title("Update Train Details")
        update_train_window.geometry("400x200")

        Label(update_train_window, text="Enter the train ID to update:").pack()
        entry_train_id = Entry(update_train_window)
        entry_train_id.pack()

        Button(update_train_window, text="Submit", command=lambda: get_update_value(choice, entry_train_id.get())).pack()

    def get_update_value(choice, train_id):
        update_train_window.destroy()
        update_value_window = Tk()
        update_value_window.title("Enter New Value")
        update_value_window.geometry("400x200")

        Label(update_value_window, text="Enter the new value:").pack()
        entry_new_value = Entry(update_value_window)
        entry_new_value.pack()

        Button(update_value_window, text="Submit", command=lambda: submit_new_value(choice, train_id, entry_new_value.get())).pack()

    def submit_new_value(choice, train_id, new_value):
        update_train_detail(choice, train_id, new_value)

    def update_train_detail(choice, train_id, new_value):
        try:
            df = pd.read_csv("trainBtwCities.txt")
            train_id = str(train_id)

            if choice == 1:
                df.loc[df['TRAIN ID'] == train_id, 'TRAIN ID'] = str(new_value)
            elif choice == 2:
                df.loc[df['TRAIN ID'] == train_id, 'TRAIN NAME'] = str(new_value)
            elif choice == 3:
                df.loc[df['TRAIN ID'] == train_id, 'START STATION'] = str(new_value)
            elif choice == 4:
                df.loc[df['TRAIN ID'] == train_id, 'END STATION'] = str(new_value)
            elif choice == 5:
                df.loc[df['TRAIN ID'] == train_id, 'DEPARTURE TIME'] = str(new_value)
            elif choice == 6:
                df.loc[df['TRAIN ID'] == train_id, 'ARRIVAL TIME'] = str(new_value)
            elif choice == 7:
                df.loc[df['TRAIN ID'] == train_id, 'DISTANCE(km)'] = float(new_value)
            elif choice == 8:
                df.loc[df['TRAIN ID'] == train_id, 'TICKET FARE'] = float(new_value)
            elif choice == 9:
                df.loc[df['TRAIN ID'] == train_id, 'TIME'] = str(new_value)

            df.to_csv("trainBtwCities.txt", index=False)
            messagebox.showinfo("Success", "Train details updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    update_choice()

def go_back():
    interstate_menu_window.destroy()
    display_menu_window()
    
def view_train_details():
    global admin_window
    

    def handle_choice(train_choice):
        if train_choice == 1:
            display_interstate_trains()
        elif train_choice == 2:
            display_intercity_trains()

    # Function to create a window for choosing Interstate or InterCity trains
    def choose_train_type():
        choose_window = Tk()
        choose_window.title("Choose Train Type")
        choose_window.geometry("300x100")

        Label(choose_window, text="Choose the type of train:").pack()
        Button(choose_window, text="InterState Train", command=lambda: handle_choice(1)).pack()
        Button(choose_window, text="InterCity Train", command=lambda: handle_choice(2)).pack()

    choose_train_type()


def display_interstate_trains():
    # Function to display Interstate train details
    interstate_window = Tk()
    interstate_window.title("InterState Train Details")
    interstate_window.geometry("800x600")

    # Read Interstate train details from file
    with open("trainBtwStates.txt", "r") as file:
        interstate_data = file.readlines()

    # Display Interstate train details in a label
    Label(interstate_window, text="InterState Train Details").pack()
    for line in interstate_data:
        Label(interstate_window, text=line.strip()).pack()

def display_intercity_trains():
    # Function to display Intercity train details
    intercity_window = Tk()
    intercity_window.title("InterCity Train Details")
    intercity_window.geometry("700x600")

    # Read Intercity train details from file
    with open("trainBtwCities.txt", "r") as file:
        intercity_data = file.readlines()

    # Display Intercity train details in a label
    Label(intercity_window, text="InterCity Train Details").pack()
    for line in intercity_data:
        Label(intercity_window, text=line.strip()).pack()

def view_passenger_details():
    global admin_menu_window
    
    def view_choice():
        global view_window
        view_window = Tk()
        view_window.title("View Passenger Details")
        view_window.geometry("300x150")

        Label(view_window, text="\nChoose what details to view:\n").pack()
        Button(view_window, text="PNR Details", command=view_pnr_details).pack()
        Button(view_window, text="User Details", command=view_user_details).pack()

    def view_pnr_details():
        view_window.destroy()
        try:
            # Read the PNR details from file
            with open("pnrDetail.txt", "r") as file:
                pnr_details = file.read()

            # Create a new tkinter window
            pnr_window = Tk()
            pnr_window.title("PNR DETAILS")

            # Display PNR details in a label
            Label(pnr_window, text=pnr_details).pack()

            # Run the tkinter event loop
            pnr_window.mainloop()
        except FileNotFoundError:
            print("PNR Details file not found.")

    def view_user_details():
        view_window.destroy()
        try:
            # Read the user details from file
            with open("userCities.txt", "r") as file:
                user_details = file.read()

            # Create a new tkinter window
            user_window = Tk()
            user_window.title("USER DETAILS")

            # Display user details in a label
            Label(user_window, text=user_details).pack()

            # Run the tkinter event loop
            user_window.mainloop()
        except FileNotFoundError:
            print("User Details file not found.")


    view_choice()


def add_new_admin():
    global admin_window, entry_admin_firstname, entry_admin_lastname, entry_admin_mailid, entry_admin_idname, entry_admin_password
    
    admin_window = Tk()
    admin_window.title("Add New Admin")
    
    Label(admin_window, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
    entry_admin_firstname = Entry(admin_window)
    entry_admin_firstname.grid(row=0, column=1, padx=5, pady=5)
    
    Label(admin_window, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
    entry_admin_lastname = Entry(admin_window)
    entry_admin_lastname.grid(row=1, column=1, padx=5, pady=5)
    
    Label(admin_window, text="Mail ID:").grid(row=2, column=0, padx=5, pady=5)
    entry_admin_mailid = Entry(admin_window)
    entry_admin_mailid.grid(row=2, column=1, padx=5, pady=5)
    
    Label(admin_window, text="ID Name:").grid(row=3, column=0, padx=5, pady=5)
    entry_admin_idname = Entry(admin_window)
    entry_admin_idname.grid(row=3, column=1, padx=5, pady=5)
    
    Label(admin_window, text="Password:").grid(row=4, column=0, padx=5, pady=5)
    entry_admin_password = Entry(admin_window, show="*")
    entry_admin_password.grid(row=4, column=1, padx=5, pady=5)
    
    Button(admin_window,text="Submit", command=submit_new_admin).grid(row=5, columnspan=2, padx=5, pady=5)



def add_new_train_intercity():
    global intercity_menu_window, entry_train_id, entry_train_name, entry_start_station, entry_end_station, entry_dep_time, entry_arrival_time, entry_distance, entry_fare, entry_travel_time
    
    add_train_window = Tk()
    add_train_window.title("Add New Train - InterCity")
    
    Label(add_train_window, text="Train ID:").grid(row=0, column=0, padx=5, pady=5)
    entry_train_id = Entry(add_train_window)
    entry_train_id.grid(row=0, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Train Name:").grid(row=1, column=0, padx=5, pady=5)
    entry_train_name = Entry(add_train_window)
    entry_train_name.grid(row=1, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Start Station:").grid(row=2, column=0, padx=5, pady=5)
    entry_start_station = Entry(add_train_window)
    entry_start_station.grid(row=2, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="End Station:").grid(row=3, column=0, padx=5, pady=5)
    entry_end_station = Entry(add_train_window)
    entry_end_station.grid(row=3, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Departure Time:").grid(row=4, column=0, padx=5, pady=5)
    entry_dep_time = Entry(add_train_window)
    entry_dep_time.grid(row=4, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Arrival Time:").grid(row=5, column=0, padx=5, pady=5)
    entry_arrival_time = Entry(add_train_window)
    entry_arrival_time.grid(row=5, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Distance:").grid(row=6, column=0, padx=5, pady=5)
    entry_distance = Entry(add_train_window)
    entry_distance.grid(row=6, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Fare:").grid(row=7, column=0, padx=5, pady=5)
    entry_fare = Entry(add_train_window)
    entry_fare.grid(row=7, column=1, padx=5, pady=5)
    
    Label(add_train_window, text="Travel Time:").grid(row=8, column=0, padx=5, pady=5)
    entry_travel_time = Entry(add_train_window)
    entry_travel_time.grid(row=8, column=1, padx=5, pady=5)
    
    Button(add_train_window, text="Submit", command=submit_new_train_intercity).grid(row=9, columnspan=2, padx=5, pady=5)

def submit_new_train_intercity():
    global entry_train_id, entry_train_name, entry_start_station, entry_end_station, entry_dep_time, entry_arrival_time, entry_distance, entry_fare, entry_travel_time
    
    trainID = entry_train_id.get()
    trainName = entry_train_name.get()
    startStation = entry_start_station.get()
    endStation = entry_end_station.get()
    depTime = entry_dep_time.get()
    arrivalTime = entry_arrival_time.get()
    distance = entry_distance.get()
    fare = entry_fare.get()
    travelTime = entry_travel_time.get()
    
    # Write train details to file
    city_train_file = open("trainBtwCities.txt", "a+")
    city_train_file.writelines([f"{trainID},{trainName},{startStation},{endStation},{depTime},{arrivalTime},{distance},{fare},{travelTime}\n"])
    city_train_file.close()
    
    messagebox.showinfo("Success", "New train added successfully.")
    
    # Clear entry fields
    entry_train_id.delete(0, END)
    entry_train_name.delete(0, END)
    entry_start_station.delete(0, END)
    entry_end_station.delete(0, END)
    entry_dep_time.delete(0, END)
    entry_arrival_time.delete(0, END)
    entry_distance.delete(0, END)
    entry_fare.delete(0, END)
    entry_travel_time.delete(0, END)

def remove_train_intercity():
    global intercity_menu_window

    # Create a new window for train removal
    remove_train_window = Tk()
    remove_train_window.title("Remove Train - InterCity")

    # Function to handle train removal
    def submit_remove_train():
        removeID = entry_remove_train_id.get()
        df = pd.read_csv("trainBtwCities.txt")
        flag = 0
        for i in range(len(df)):
            current_train_id = str(df.iloc[i, 0]).strip()  # Convert to string and strip leading and trailing whitespaces
            print("Checking train ID:", current_train_id)
            if str(removeID).strip() == current_train_id:
                df = df.drop(i)
                df = df.reset_index(drop=True)
                df.to_csv("trainBtwCities.txt", index=False)
                flag = 1
                break
        if flag == 0:
            print("\nTrain with ID {} is not found !".format(removeID))
        elif flag == 1:
            print("\nTrain with ID {} removed successfully\n".format(removeID))
        remove_train_window.destroy()  # Close remove train window

    # UI elements for train removal
    Label(remove_train_window, text="Enter the train ID to remove:").pack()
    entry_remove_train_id = Entry(remove_train_window)
    entry_remove_train_id.pack()
    Button(remove_train_window, text="Remove", command=submit_remove_train).pack()



def go_back():
    # Function to go back to the main menu
    pass

def submit_new_admin():
    global entry_admin_firstname, entry_admin_lastname, entry_admin_mailid, entry_admin_idname, entry_admin_password
    
    firstName = entry_admin_firstname.get()
    lastName = entry_admin_lastname.get()
    mailID = entry_admin_mailid.get()
    IDName = entry_admin_idname.get()
    password = entry_admin_password.get()
    
    # Validation of password length
    if len(password) < 8:
        messagebox.showerror("Invalid Password", "Password should be at least 8 characters long.")
        return
    
    # Write admin details to file
    admin_file = open("AdminDetails.txt", "a+")
    admin_file.write(f"\n{firstName},{lastName},{mailID},{IDName},{password}")
    admin_file.close()
    
    messagebox.showinfo("Success", "New admin added successfully.")
    
    # Clear entry fields
    entry_admin_firstname.delete(0, END)
    entry_admin_lastname.delete(0, END)
    entry_admin_mailid.delete(0, END)
    entry_admin_idname.delete(0, END)
    entry_admin_password.delete(0, END)


        
class Fare:
    def __init__(self,fare,trainFare,coachFare,foodFare,a,c,pnr):
        self.fare=fare
        self.trainFare=trainFare
        self.coachFare=coachFare
        self.foodFare=foodFare
        self.a=a
        self.c=c
        self.pnr=pnr
    def setFare(self,fare):
        self.fare=fare

    def setTFare(self,trainFare):
        self.trainFare=trainFare

    def setCFare(self,coachFare):
        self.coachFare=coachFare
       
    def setFFare(self,foodFare):
        self.foodFare=foodFare
       
    def setAdult(self,a):
        self.a=a
   
    def setPNR(self,pnr):
        self.pnr=pnr
       
    def getPNR(self):
        return self.pnr
   
    def getNumOfPass(self):
        return self.a+self.c
   
    def setChild(self,c):
        self.c=c
       
    def total(self):
        return self.trainFare+self.foodFare+self.coachFare
   
    def getFare(self):
        return self.fare
   
       
obj = Fare(0,0,0,0,0,0,0)   #city
obj1 = Fare(0,0,0,0,0,0,0)   #state

   
def show_coach_selection_window():
    coach_selection_window = Toplevel(top)
    coach_selection_window.title("Coach Selection")


   
    df11 = pd.read_csv("coachDetails.txt")
    data11 = df11.iloc[0:6, 0:2]
    print(df11)
    for i in range(len(data11)):
        option_label = Label(coach_selection_window, text=data11.iloc[i, 0])
        option_label.grid(row=i, column=0)
       
        cost_label = Label(coach_selection_window, text=data11.iloc[i, 1])
        cost_label.grid(row=i, column=1)
    choice_label = Label(coach_selection_window, text="Your choice:")
    choice_label.grid(row=len(data11), column=0)
    choice_entry = Entry(coach_selection_window)
    choice_entry.grid(row=len(data11), column=1)
   
    submit_button = Button(coach_selection_window, text="Submit", command=lambda: process_coach_selection(choice_entry.get(), coach_selection_window))
    submit_button.grid(row=len(data11)+1, columnspan=2)


def show_coach_selection_window2():
    coach_selection_window = Toplevel(top)
    coach_selection_window.title("Coach Selection")

   
    df11 = pd.read_csv("coachDetails.txt")
    data11 = df11.iloc[0:6, 0:2]
    print(df11)
    for i in range(len(data11)):
        option_label = Label(coach_selection_window, text=data11.iloc[i, 0])
        option_label.grid(row=i, column=0)
       
        cost_label = Label(coach_selection_window, text=data11.iloc[i, 1])
        cost_label.grid(row=i, column=1)
    choice_label = Label(coach_selection_window, text="Your choice:")
    choice_label.grid(row=len(data11), column=0)
    choice_entry = Entry(coach_selection_window)
    choice_entry.grid(row=len(data11), column=1)
   
    submit_button = Button(coach_selection_window, text="Submit", command=lambda: process_coach_selection2(choice_entry.get(), coach_selection_window))
    submit_button.grid(row=len(data11)+1, columnspan=2)
   
   
def process_coach_selection(choice, window):
    coachChoice = int(choice)
    df11 = pd.read_csv("coachDetails.txt")
    data11 = df11.iloc[0:6, 0:2]
    coachFare = (int(data11.iloc[coachChoice,1]))*obj.getNumOfPass()
    obj.setCFare(coachFare)
    window.destroy()
    show_food_order_window()
   
       
def process_coach_selection2(choice, window):
    coachChoice = int(choice)
    df11 = pd.read_csv("coachDetails.txt")
    data11 = df11.iloc[0:6, 0:2]
    coachFare = (int(data11.iloc[coachChoice,1]))*obj1.getNumOfPass()
    obj1.setCFare(coachFare)
    print(coachFare)
    window.destroy()
    show_food_order_window2()

   
def show_food_order_window():
    food_order_window = Toplevel(top)
    food_order_window.title("Food Ordering")

    food_order_label = Label(food_order_window, text="Would you like to pre-order your food?")
    food_order_label.grid(row=0, column=0, columnspan=2)

    food_choice_label = Label(food_order_window, text="Enter your choice (1 for YES, 2 for NO):")
    food_choice_label.grid(row=1, column=0)

    foodCh=Entry(food_order_window)
    foodCh.grid(row=1, column=1)

    submit_button = Button(food_order_window, text="Submit", command=lambda: process_food_choice(foodCh.get(), food_order_window))
    submit_button.grid(row=2, columnspan=2)

   
def show_food_order_window2():
    food_order_window = Toplevel(top)
    food_order_window.title("Food Ordering")

    food_order_label = Label(food_order_window, text="Would you like to pre-order your food?")
    food_order_label.grid(row=0, column=0, columnspan=2)

    food_choice_label = Label(food_order_window, text="Enter your choice (1 for YES, 2 for NO):")
    food_choice_label.grid(row=1, column=0)

    foodCh=Entry(food_order_window)
    foodCh.grid(row=1, column=1)

    submit_button = Button(food_order_window, text="Submit", command=lambda: process_food_choice2(foodCh.get(), food_order_window))
    submit_button.grid(row=2, columnspan=2)

def process_food_choice(choice, window):
    if choice == "1":  # User wants to pre-order food
        df10 = pd.read_csv("foodDetails.txt")
        data10 = df10.iloc[0:7, 0:2]  # increase row

        for i in range(len(data10)):
            option_label = Label(window, text=data10.iloc[i, 0])
            option_label.grid(row=i+3, column=0)

            cost_label = Label(window, text=data10.iloc[i, 1])
            cost_label.grid(row=i+3, column=1)

        # Entry for food choice and quantity
        choice_label = Label(window, text="Food choice:")
        choice_label.grid(row=len(data10)+3, column=0)
        choice_entry = Entry(window)

        choice_entry.grid(row=len(data10)+3, column=1)

        quantity_label = Label(window, text="Quantity:")
        quantity_label.grid(row=len(data10)+4, column=0)
        quantity_entry = Entry(window)
        quantity_entry.grid(row=len(data10)+4, column=1)

        submit_button = Button(window, text="Submit", command=lambda: process_food_order(choice_entry.get(), quantity_entry.get(), window))
        submit_button.grid(row=len(data10)+5, columnspan=2)
    else:
        window.destroy()
        show_payment_window()


def process_food_choice2(choice, window):
    if choice == "1":  # User wants to pre-order food
        df10 = pd.read_csv("foodDetails.txt")
        data10 = df10.iloc[0:7, 0:2]  # increase row

        for i in range(len(data10)):
            option_label = Label(window, text=data10.iloc[i, 0])
            option_label.grid(row=i+3, column=0)

            cost_label = Label(window, text=data10.iloc[i, 1])
            cost_label.grid(row=i+3, column=1)

        # Entry for food choice and quantity
        choice_label = Label(window, text="Food choice:")
        choice_label.grid(row=len(data10)+3, column=0)
        choice_entry = Entry(window)
        choice_entry.grid(row=len(data10)+3, column=1)

        quantity_label = Label(window, text="Quantity:")
        quantity_label.grid(row=len(data10)+4, column=0)
        quantity_entry = Entry(window)
        quantity_entry.grid(row=len(data10)+4, column=1)

        submit_button = Button(window, text="Submit", command=lambda: process_food_order2(choice_entry.get(), quantity_entry.get(), window))
        submit_button.grid(row=len(data10)+5, columnspan=2)
    else:
        window.destroy()
        show_payment_window()


def process_food_order(choice, quantity, window):
    foodChoice = int(choice)
    number = int(quantity)
    df10 = pd.read_csv("foodDetails.txt")
    data10 = df10.iloc[0:7, 0:2]
    cost=(int(data10.iloc[foodChoice,1]))*number
   
    obj.setFFare(cost)
    file3=open("userCityFood.txt","a")
    #file3.write("PNR,FOOD CHOICE,QUANTITY\n")
    file3.writelines([str(obj.getPNR()),",",data10.iloc[foodChoice,0],",",str(number)])

    window.destroy()
   
    totalFare = obj.total()
    df12=pd.read_csv("pnrDetail.txt")
    df12.loc[0,"Ticket Fare"]=str(totalFare)
    df12.to_csv("pnrDetail.txt", index=False)
    show_payment_window(totalFare)




def process_food_order2(choice, quantity, window):
    foodChoice = int(choice)
    number = int(quantity)
    df10 = pd.read_csv("foodDetails.txt")
    data10 = df10.iloc[0:4, 0:2]
    cost=(int(data10.iloc[foodChoice,1]))*number
    print(cost)


    obj1.setFFare(cost)
    file3=open("userStateFood.txt","a")
    #file3.write("PNR,FOOD CHOICE,QUANTITY\n")
    file3.writelines([str(obj1.getPNR()),",",data10.iloc[foodChoice,0],",",str(number)])

    window.destroy()
   
    totalFare = obj1.total()
    print(totalFare)
    df12=pd.read_csv("pnrDetail.txt")
    df12.loc[0,"Ticket Fare"]=str(totalFare)
    df12.to_csv("pnrDetail.txt", index=False)
    show_payment_window2(totalFare)





def show_payment_window(totalFare):
    payment_window = Toplevel(top)
    payment_window.title("Payment")

    pnr_label = Label(payment_window, text="Your PNR Number: " + str(obj.getPNR()))
    pnr_label.pack()

    total_cost_label = Label(payment_window, text="Total Ticket Cost (including Convenience Fee + GST): ₹" + str(totalFare + 11.8))
    total_cost_label.pack()

    accNum_label = Label(payment_window, text="Enter your account number:")
    accNum_label.pack()
    accNum_entry = Entry(payment_window)
    accNum_entry.pack()

    password_label = Label(payment_window, text="Enter your password:")
    password_label.pack()
    password_entry = Entry(payment_window, show="*")  # Show asterisks for password
    password_entry.pack()

    payment_label = Label(payment_window, text="Would you like to proceed to pay (y/n):")
    payment_label.pack()

    payment_entry = Entry(payment_window)
    payment_entry.pack()

    submit_button = Button(payment_window, text="Submit", command=lambda: process_payment(payment_entry.get(), accNum_entry, password_entry, payment_window))
    submit_button.pack()


def show_payment_window2(totalFare):
    payment_window = Toplevel(top)
    payment_window.title("Payment")

    pnr_label = Label(payment_window, text="Your PNR Number: " + str(obj1.getPNR()))
    pnr_label.pack()
   

    total_cost_label = Label(payment_window, text="Total Ticket Cost (including Convenience Fee + GST): ₹" + str(totalFare + 11.8))
    total_cost_label.pack()

    accNum_label = Label(payment_window, text="Enter your account number:")
    accNum_label.pack()
    accNum_entry = Entry(payment_window)
    accNum_entry.pack()

    password_label = Label(payment_window, text="Enter your password:")
    password_label.pack()
    password_entry = Entry(payment_window, show="*")
    password_entry.pack()

    payment_label = Label(payment_window, text="Would you like to proceed to pay (y/n):")
    payment_label.pack()

    payment_entry = Entry(payment_window)
    payment_entry.pack()

    submit_button = Button(payment_window, text="Submit", command=lambda: process_payment2(payment_entry.get(), accNum_entry.get(), password_entry.get(), payment_window))
    submit_button.pack()


def process_payment(payment, accNum_entry, password_entry, payment_window):
    if payment.lower() == 'y':
        accNum = accNum_entry.get()
        password = password_entry.get()

        transID = random.randint(100000000000000, 100009999999999)

        confirmation_label1 = Label(payment_window, text="Payment done successfully for PNR Number: " + str(obj.getPNR()))
        confirmation_label1.pack()

        confirmation_label2 = Label(payment_window, text="Transaction Number: " + str(transID))
        confirmation_label2.pack()

    else:
        print("Payment cancelled.")
    payment_window.destroy()


def process_payment2(payment, accNum, password, payment_window):
    if payment.lower() == 'y':
        transID = random.randint(100000000000000, 100009999999999)

        confirmation_label1 = Label(payment_window, text="Payment done successfully for PNR Number: " + str(obj1.getPNR()))
        confirmation_label1.pack()

        confirmation_label2 = Label(payment_window, text="Transaction Number: " + str(transID))
        confirmation_label2.pack()

    else:
        print("Payment cancelled.")
    payment_window.destroy()



def view_ticket(pnr_num):
    ticket_window = Toplevel(top)
    ticket_window.title("Electronic Reservation Slip (ERS)")

    def get_passenger_details(pnr_num):
        passenger_details = []
        df = pd.read_csv("userCities.txt")
        for i in range(len(df)):
            if df.iloc[i, 3] == pnr_num:
                passenger_details.append([df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2]])
        return passenger_details

    passenger_details = get_passenger_details(pnr_num)

    ticket_details = None
    with open("pnrDetail.txt", "r") as file:
        for line in file:
            if line.startswith(str(pnr_num)):
                ticket_details = line.split(",")
                break

    if ticket_details:
        start = ticket_details[3]
        end = ticket_details[4]
        dept_time = ticket_details[5]
        arr_time = ticket_details[6]
        train_id = ticket_details[1]
        train_name = ticket_details[2]
        distance = ticket_details[7]
        fare = ticket_details[8]
        total_time = ticket_details[9]



        # Ticket Header
        header_label = Label(ticket_window, text="ELECTRONIC RESERVATION SLIP (ERS)", font=("Arial", 12, "bold"))
        header_label.pack()

        # Route Details
        route_label = Label(ticket_window, text="Booked from: {}      BOARDING AT: {}      To: {}".format(start, start + " JN", end), font=("Arial", 10))
        route_label.pack()
        dept_arr_label = Label(ticket_window, text="Departure: {}      Arrival: {}".format(dept_time, arr_time), font=("Arial", 10))
        dept_arr_label.pack()

        # Train Details
        train_info_label = Label(ticket_window, text="Train Number: {}      Train Name: {}".format(train_id, train_name), font=("Arial", 10))
        train_info_label.pack()
        distance_label = Label(ticket_window, text="Distance: {} km".format(distance), font=("Arial", 10))
        distance_label.pack()

        # Passenger Details
        passenger_header_label = Label(ticket_window, text="PASSENGER DETAILS", font=("Arial", 11, "bold"))
        passenger_header_label.pack()
        passenger_label = Label(ticket_window, text="#      Name      Age      Gender", font=("Arial", 10))
        passenger_label.pack()

        for i, passenger in enumerate(passenger_details):
            passenger_details_label = Label(ticket_window, text="{}      {}      {}      {}".format(i+1, *passenger), font=("Arial", 10))
            passenger_details_label.pack()

        # Transaction ID
        trans_id_label = Label(ticket_window, text="TRANSACTION ID: {}".format(random.randint(100000000000000, 100009999999999)), font=("Arial", 10))
        trans_id_label.pack()

        fare=int(obj.getFare())-11.80
        # Payment Details
        payment_header_label = Label(ticket_window, text="PAYMENT DETAILS", font=("Arial", 12, "bold"))
        payment_header_label.pack()
        payment_details_label1 = Label(ticket_window, text="Ticket Fare: ₹{}".format(fare), font=("Arial", 10))
        payment_details_label1.pack()
        payment_details_label2 = Label(ticket_window, text="Convenience Fee (incl. of GST): ₹11.80", font=("Arial", 10))
        payment_details_label2.pack()
        total_fare_label = Label(ticket_window, text="Total Fare (all inclusive): ₹{}".format(float(fare) + 11.8), font=("Arial", 10))
        total_fare_label.pack()

    else:
        error_label = Label(ticket_window, text="Invalid PNR. Please try again.", font=("Arial", 10))
        error_label.pack()



def view_ticket2(pnr_num):
    ticket_window = Toplevel(top)
    ticket_window.title("Electronic Reservation Slip (ERS)")

    def get_passenger_details(pnr_num):
        passenger_details = []
        df = pd.read_csv("userStates.txt")
        for i in range(len(df)):
            if df.iloc[i, 3] == pnr_num:
                passenger_details.append([df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2]])
        return passenger_details

    passenger_details = get_passenger_details(pnr_num)

    ticket_details = None
    with open("pnrDetail.txt", "r") as file:
        for line in file:
            if line.startswith(str(pnr_num)):
                ticket_details = line.split(",")
                break

    if ticket_details:
        start = ticket_details[3]
        end = ticket_details[4]
        dept_time = ticket_details[5]
        arr_time = ticket_details[6]
        train_id = ticket_details[1]
        train_name = ticket_details[2]
        distance = ticket_details[7]
        fare = ticket_details[8]
        total_time = ticket_details[9]



        header_label = Label(ticket_window, text="ELECTRONIC RESERVATION SLIP (ERS)", font=("Arial", 12, "bold"))
        header_label.pack()

        route_label = Label(ticket_window, text="Booked from: {}      BOARDING AT: {}      To: {}".format(start, start + " JN", end), font=("Arial", 10))
        route_label.pack()
        dept_arr_label = Label(ticket_window, text="Departure: {}      Arrival: {}".format(dept_time, arr_time), font=("Arial", 10))
        dept_arr_label.pack()

        train_info_label = Label(ticket_window, text="Train Number: {}      Train Name: {}".format(train_id, train_name), font=("Arial", 10))
        train_info_label.pack()
        distance_label = Label(ticket_window, text="Distance: {} km".format(distance), font=("Arial", 10))
        distance_label.pack()

        passenger_header_label = Label(ticket_window, text="PASSENGER DETAILS", font=("Arial", 11, "bold"))
        passenger_header_label.pack()
        passenger_label = Label(ticket_window, text="#      Name      Age      Gender", font=("Arial", 10))
        passenger_label.pack()

        for i, passenger in enumerate(passenger_details):
            passenger_details_label = Label(ticket_window, text="{}      {}      {}      {}".format(i+1, *passenger), font=("Arial", 10))
            passenger_details_label.pack()

        trans_id_label = Label(ticket_window, text="TRANSACTION ID: {}".format(random.randint(100000000000000, 100009999999999)), font=("Arial", 10))
        trans_id_label.pack()
        fare=int(objq.getFare())-11.80

        payment_header_label = Label(ticket_window, text="PAYMENT DETAILS", font=("Arial", 12, "bold"))
        payment_header_label.pack()
        payment_details_label1 = Label(ticket_window, text="Ticket Fare: ₹{}".format(fare), font=("Arial", 10))
        payment_details_label1.pack()
        payment_details_label2 = Label(ticket_window, text="Convenience Fee (incl. of GST): ₹11.80", font=("Arial", 10))
        payment_details_label2.pack()
        total_fare_label = Label(ticket_window, text="Total Fare (all inclusive): ₹{}".format(float(fare) + 11.8), font=("Arial", 10))
        total_fare_label.pack()

    else:
        error_label = Label(ticket_window, text="Invalid PNR. Please try again.", font=("Arial", 10))
        error_label.pack()

   
 
def get_user_details_from_entry(numberOfpersons, window):
    adults = 0
    children = 0
    user_details = []

    person_labels = []
    person_entries = []

    for i in range(numberOfpersons):
        person_frame = Frame(window)
        person_frame.grid(row=i+4, column=0, pady=5)

        person_label = Label(person_frame, text=f"PERSON {i+1}")
        person_label.grid(row=0, column=0)

        name_label = Label(person_frame, text="Name:")
        name_label.grid(row=1, column=0)
        name_entry = Entry(person_frame)
        name_entry.grid(row=1, column=1)
        person_entries.append(name_entry)

        age_label = Label(person_frame, text="Age:")
        age_label.grid(row=2, column=0)
        age_entry = Entry(person_frame)
        age_entry.grid(row=2, column=1)
        person_entries.append(age_entry)

        gender_label = Label(person_frame, text="Gender (M/F/O):")
        gender_label.grid(row=3, column=0)
        gender_entry = Entry(person_frame)
        gender_entry.grid(row=3, column=1)
        person_entries.append(gender_entry)

        person_labels.extend([name_label, age_label, gender_label])

    submit_button = Button(window, text="Submit", command=lambda: process_user_details(person_entries, adults, children, user_details, window))
    submit_button.grid(row=numberOfpersons+4, column=0, pady=5)
   
   
def get_user_details_from_entry2(numberOfpersons, window):
    adults = 0
    children = 0
    user_details = []

    person_labels = []
    person_entries = []

    for i in range(numberOfpersons):
        person_frame = Frame(window)
        person_frame.grid(row=i+4, column=0, pady=5)

        person_label = Label(person_frame, text=f"PERSON {i+1}")
        person_label.grid(row=0, column=0)

        name_label = Label(person_frame, text="Name:")
        name_label.grid(row=1, column=0)
        name_entry = Entry(person_frame)
        name_entry.grid(row=1, column=1)
        person_entries.append(name_entry)

        age_label = Label(person_frame, text="Age:")
        age_label.grid(row=2, column=0)
        age_entry = Entry(person_frame)
        age_entry.grid(row=2, column=1)
        person_entries.append(age_entry)

        gender_label = Label(person_frame, text="Gender (M/F/O):")
        gender_label.grid(row=3, column=0)
        gender_entry = Entry(person_frame)
        gender_entry.grid(row=3, column=1)
        person_entries.append(gender_entry)

        person_labels.extend([name_label, age_label, gender_label])

    submit_button = Button(window, text="Submit", command=lambda: process_user_details2(person_entries, adults, children, user_details, window))
    submit_button.grid(row=numberOfpersons+4, column=0, pady=5)


def process_user_details(entries, adults, children, user_details, window):
    for i in range(0, len(entries), 3):
        name = entries[i].get()
        age = int(entries[i+1].get())
        gender = entries[i+2].get()

        user_details.append({"Name": name, "Age": age, "Gender": gender})

        if age >= 12:
            adults += 1
        else:
            children += 1
        obj.setAdult(adults)
        obj.setChild(children)
       
    file2=open("userCities.txt","a")
    #file2.write("Name,Age,Gender,PNR,STATUS\n")
    for user in user_details:
        file2.writelines([user['Name'],",",str(user['Age']),",",user['Gender'],",",str(obj.getPNR()),",ACTIVE","\n"])

    obj.setTFare(int(obj.getFare())*adults+(int(obj.getFare())/2)*children)
    file2.close()
    file1=open("pnrDetail.txt","a")    
    file1.writelines([",",str(adults),",",str(children),",ACTIVE","\n"])
    file1.close()
    show_coach_selection_window()
       
def process_user_details2(entries, adults, children, user_details, window):
    for i in range(0, len(entries), 3):
        name = entries[i].get()
        age = int(entries[i+1].get())
        gender = entries[i+2].get()

        user_details.append({"Name": name, "Age": age, "Gender": gender})

        if age >= 12:
            adults += 1
        else:
            children += 1
        obj1.setAdult(adults)
        obj1.setChild(children)
       
    file2=open("userStates.txt","a")
    #file2.write("Name,Age,Gender,PNR,STATUS\n")
    for user in user_details:
        file2.writelines([user['Name'],",",str(user['Age']),",",user['Gender'],",",str(obj.getPNR()),",ACTIVE","\n"])

    obj1.setTFare(int(obj1.getFare())*adults+(int(obj1.getFare())/2)*children)
    file2.close()
    file1=open("pnrDetail.txt","a")    
    file1.writelines([",",str(adults),",",str(children),",ACTIVE","\n"])
    file1.close()
    show_coach_selection_window()
   
   
   
def show_user_menu():
    top.title("User Menu")    
    label.config(text="\n USER MENU")
    city = Radiobutton(top, text="Intercity Railways", variable=userChoice, value=1)
    city.pack(anchor='w')
    state = Radiobutton(top, text="InterState Railways", variable=userChoice, value=2)
    state.pack(anchor='w')
    submit_button.config(command=lambda: open_menu_window() if userChoice.get() == 1 else open_menu_window2())




def open_menu_window():
    menu_window = Toplevel(top)
    menu_window.title("Menu")

    menu_label = Label(menu_window, text="\n\tMENU\n")
    menu_label.pack()

    option = IntVar()

    book_button = Radiobutton(menu_window, text="Book Ticket", variable=option, value=1)
    book_button.pack(anchor='w')

    view_button = Radiobutton(menu_window, text="View Ticket", variable=option, value=2)
    view_button.pack(anchor='w')

    submit_menu_button = Button(menu_window, text="Submit", command=lambda: handle_menu_option(option.get(), menu_window))
    submit_menu_button.pack()




def open_menu_window2():
    menu_window = Toplevel(top)
    menu_window.title("Menu")

    menu_label = Label(menu_window, text="\n\tMENU\n")
    menu_label.pack()

    option = IntVar()

    book_button = Radiobutton(menu_window, text="Book Ticket", variable=option, value=1)
    book_button.pack(anchor='w')

    view_button = Radiobutton(menu_window, text="View Ticket", variable=option, value=2)
    view_button.pack(anchor='w')

    submit_menu_button = Button(menu_window, text="Submit", command=lambda: handle_menu_option2(option.get(), menu_window))
    submit_menu_button.pack()


def handle_menu_option(option, menu_window):
    if option == 1:  # Book Ticket
        book_ticket_window = Toplevel(top)
        book_ticket_window.title("Book Ticket")

        start_label = Label(book_ticket_window, text="Start City:")
        start_label.grid(row=0, column=0)
        start_entry = Entry(book_ticket_window)
        start_entry.grid(row=0, column=1)

        end_label = Label(book_ticket_window, text="End City:")
        end_label.grid(row=1, column=0)
        end_entry = Entry(book_ticket_window)
        end_entry.grid(row=1, column=1)

        train_info_text = Text(book_ticket_window, height=10, width=100)
        train_info_text.grid(row=2, columnspan=2)
   
        submit_button = Button(book_ticket_window, text="Submit", command=lambda: get_train_data(start_entry.get(), end_entry.get(), train_info_text, book_ticket_window))
        submit_button.grid(row=3, columnspan=2)
   
    elif option == 2:
        pnr_entry_label = Label(menu_window, text="Enter your PNR number:")
        pnr_entry_label.pack()
   
        pnr_entry = Entry(menu_window)
        pnr_entry.pack()
   
        view_ticket_button = Button(menu_window, text="View Ticket", command=lambda: view_ticket(int(pnr_entry.get())))
        view_ticket_button.pack()
       
       
def handle_menu_option2(option, menu_window):
    if option == 1:  # Book Ticket
        book_ticket_window = Toplevel(top)
        book_ticket_window.title("Book Ticket")

        start_label = Label(book_ticket_window, text="Start State:")
        start_label.grid(row=0, column=0)
        start_entry = Entry(book_ticket_window)
        start_entry.grid(row=0, column=1)

        end_label = Label(book_ticket_window, text="End State:")
        end_label.grid(row=1, column=0)
        end_entry = Entry(book_ticket_window)
        end_entry.grid(row=1, column=1)

        train_info_text = Text(book_ticket_window, height=10, width=150)
        train_info_text.grid(row=2, columnspan=2)
   
        submit_button = Button(book_ticket_window, text="Submit", command=lambda: get_train_data2(start_entry.get(), end_entry.get(), train_info_text, book_ticket_window))
        submit_button.grid(row=3, columnspan=2)
   
    elif option == 2:
        pnr_entry_label = Label(menu_window, text="Enter your PNR number:")
        pnr_entry_label.pack()
   
        pnr_entry = Entry(menu_window)
        pnr_entry.pack()
   
        view_ticket_button = Button(menu_window, text="View Ticket", command=lambda: view_ticket2(int(pnr_entry.get())))
        view_ticket_button.pack()    
             
       
def get_train_data(fromCity, toCity, train_info_text, window):
    df = pd.read_csv("trainBtwCities.txt")
    new_df = pd.DataFrame()
    for i in range(len(df)):
        if df.iloc[i, 2] == fromCity and df.iloc[i, 3] == toCity:
            extract_data = pd.DataFrame({"Train ID": [df.iloc[i, 0]], "Train Name": [df.iloc[i, 1]], "Departure Time": [df.iloc[i, 4]], "Arrival Time": [df.iloc[i, 5]], "Distance": [df.iloc[i, 6]], "Ticket Fare": [df.iloc[i, 7]], "Total Time": [df.iloc[i, 8]]})
            obj.setFare(df.iloc[i,7])
            new_df = pd.concat([new_df, extract_data])
    if new_df.empty:
        train_info_text.insert(END, "\nSorry, No trains available for your search")
    else:
        train_info_text.insert(END, "\nThe trains available are listed below, select your choice to proceed further\n\n")
        new_df.reset_index(drop=True, inplace=True)
        train_info_text.insert(END, new_df.to_string(index=False))
        choice_label = Label(window, text="Enter your choice:")
        choice_label.grid(row=3, column=0)
        choice_entry = Entry(window)
        choice_entry.grid(row=3, column=1)

        persons_label = Label(window, text="Enter number of persons:")
        persons_label.grid(row=5, column=0)
        persons_entry = Entry(window)
        persons_entry.grid(row=5, column=1)

        submit_button = Button(window, text="Submit", command=lambda: get_user_details(persons_entry, window, choice_entry,fromCity,toCity))
        submit_button.grid(row=6, columnspan=2)

def get_user_details(persons, window, choice_entry,fromCity,toCity):
    df = pd.read_csv("trainBtwCities.txt")
    new_df = pd.DataFrame()
    for i in range(len(df)):
       if df.iloc[i, 2] == fromCity and df.iloc[i, 3] == toCity:
           extract_data = pd.DataFrame({"Train ID": [df.iloc[i, 0]], "Train Name": [df.iloc[i, 1]], "Departure Time": [df.iloc[i, 4]], "Arrival Time": [df.iloc[i, 5]], "Distance": [df.iloc[i, 6]], "Ticket Fare": [df.iloc[i, 7]], "Total Time": [df.iloc[i, 8]]})
           new_df = pd.concat([new_df, extract_data])
    choice = int(choice_entry.get())
    pnr_num = random.randint(1000000001, 9999999999)
    obj.setPNR(pnr_num)
    c = choice

    #file1 = open("pnrDetail.txt", "w")
    #file1.write("PNR Number,Train ID,Train Name,From Station,End Station,Departure time,Arrival time,Distance,Ticket Fare,Time,Adults,Child,Status,Food choice\n")
    #file1.close()
    file1 = open("pnrDetail.txt", "a")
    c = choice
    file1.writelines([str(pnr_num), ",", str(new_df.iloc[c, 0]), ",", new_df.iloc[c, 1], ",", fromCity, ",", toCity, ",", str(new_df.iloc[c, 2]), ",", str(new_df.iloc[c, 3]), ",", str(new_df.iloc[c, 4]), ",", str(new_df.iloc[c, 5]), ",", str(new_df.iloc[c, 6])])
    file1.close()

    obj1.setFare(new_df.iloc[choice,5])
    get_user_details_from_entry(int(persons.get()), window)



def get_train_data2(fromState, toState, train_info_text, window):
    df = pd.read_csv("trainBtwStates.txt")
    new_df = pd.DataFrame()
    for i in range(len(df)):
        if df.iloc[i, 2] == fromState and df.iloc[i, 4] == toState:
            extract_data = pd.DataFrame({"Train ID": [df.iloc[i, 0]], "Train Name": [df.iloc[i, 1]],"From city":[df.iloc[i,3]],"To city":[df.iloc[i,5]],"Departure Time": [df.iloc[i, 7]], "Arrival Time": [df.iloc[i, 8]], "Distance": [df.iloc[i, 6]], "Ticket Fare": [df.iloc[i, 9]], "Total Time": [df.iloc[i,10]]})
            new_df = pd.concat([new_df, extract_data])
    if new_df.empty:
        train_info_text.insert(END, "\nSorry, No trains available for your search")
    else:
 
        train_info_text.insert(END, "\nThe trains available are listed below, select your choice to proceed further\n\n")
        new_df.reset_index(drop=True, inplace=True)
        train_info_text.insert(END, new_df.to_string(index=False))
       
       
        choice_label = Label(window, text="Enter your choice:")
        choice_label.grid(row=3, column=0)
        choice_entry = Entry(window)
        choice_entry.grid(row=3, column=1)

       
        persons_label = Label(window, text="Enter number of persons:")
        persons_label.grid(row=5, column=0)
        persons_entry = Entry(window)
        persons_entry.grid(row=5, column=1)
       
        submit_button = Button(window, text="Submit", command=lambda: get_user_details2(persons_entry, window, choice_entry,fromState,toState))
        submit_button.grid(row=6, columnspan=2)

def get_user_details2(persons, window, choice_entry,fromState,toState):

    df = pd.read_csv("trainBtwStates.txt")
    new_df = pd.DataFrame()
    for i in range(len(df)):
        if df.iloc[i, 2] == fromState and df.iloc[i, 4] == toState:
            extract_data = pd.DataFrame({"Train ID": [df.iloc[i, 0]], "Train Name": [df.iloc[i, 1]],"From city":[df.iloc[i,3]],"To city":[df.iloc[i,5]],"Departure Time": [df.iloc[i, 7]], "Arrival Time": [df.iloc[i, 8]], "Distance": [df.iloc[i, 6]], "Ticket Fare": [df.iloc[i, 9]], "Total Time": [df.iloc[i,10]]})
            new_df = pd.concat([new_df, extract_data])
    choice = int(choice_entry.get())
    pnr_num = random.randint(1000000001, 9999999999)
    obj1.setPNR(pnr_num)
    c = choice

    #file1 = open("pnrDetail.txt", "w")
    #file1.write("PNR Number,Train ID,Train Name,From State,From Station,End state,End Station,Departure time,Arrival time,Distance,Ticket Fare,Time,Adults,Child,Status,Food choice\n")
    #file1.close()
    file1 = open("pnrDetail.txt", "a")
    c = choice
    file1.writelines([str(pnr_num), ",", str(new_df.iloc[c, 0]), ",", new_df.iloc[c, 1], ",", fromState, ",",new_df.iloc[c,2],",", toState, ",",new_df.iloc[c,3],",", str(new_df.iloc[c, 4]), ",", str(new_df.iloc[c, 5]), ",", str(new_df.iloc[c, 6]), ",", str(new_df.iloc[c,7]), ",", str(new_df.iloc[c,8])])
    file1.close()
           
    obj1.setFare(new_df.iloc[choice,7])
    print(new_df.iloc[c,7])
    get_user_details_from_entry2(int(persons.get()), window)

def submit():
    global entry_admin_id, entry_admin_password, admin_window
    
    # Function to submit choice and open appropriate window
    if choice.get() == 1:
        # Open admin login window
        #top.destroy()  # Destroying the first window
        admin_window = Tk()
        admin_window.title("Admin Login")
        
        label_admin_id = Label(admin_window, text="ID Name:")
        label_admin_id.grid(row=0, column=0, padx=5, pady=5)
        entry_admin_id = Entry(admin_window)
        entry_admin_id.grid(row=0, column=1, padx=5, pady=5)

        label_admin_password = Label(admin_window, text="Password:")
        label_admin_password.grid(row=1, column=0, padx=5, pady=5)
        entry_admin_password = Entry(admin_window, show="*")
        entry_admin_password.grid(row=1, column=1, padx=5, pady=5)

        button_admin_login = Button(admin_window, text="Login", command=admin_login)
        button_admin_login.grid(row=2, columnspan=2, padx=5, pady=5)

        admin_window.mainloop()
    elif choice.get() == 2:
        top = Tk()
        userChoice = IntVar()
        city = Radiobutton(top, text="Intercity Railways", variable=userChoice, value=1)
        city.pack(anchor='w')
        state = Radiobutton(top, text="InterState Railways", variable=userChoice, value=2)
        state.pack(anchor='w')
        submit_button = Button(top, text="Submit", command=lambda: open_menu_window() if userChoice.get() == 1 else open_menu_window2())
        submit_button.pack()

        
top = Tk()
top.geometry("300x200")

label_choice = Label(top, text="Choose an option:")
label_choice.pack()

choice = IntVar()
Radiobutton(top, text="Admin", variable=choice, value=1).pack()
Radiobutton(top, text="User", variable=choice, value=2).pack()

button_submit = Button(top, text="Submit", command=submit)
button_submit.pack()
userChoice = IntVar() 
top.mainloop()