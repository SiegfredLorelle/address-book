"""CMPE 30052 Lab Activity No. 1 - Application of Python List"""

# Address Book

import cs50
import sys
import tkinter as tk

from helpers import get_name, get_house_number, get_street_vilage, get_city_municipality, get_province, get_country


def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
window.geometry("500x500")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


main_menu = tk.Frame(window, bg='#EFF5F5')
add_contact = tk.Frame(window, bg="gray")
edit_contact = tk.Frame(window, bg='#EFF5F5')
delete_contact = tk.Frame(window, bg="blue")
view_contact = tk.Frame(window, bg='#EFF5F5')
search_contact = tk.Frame(window, bg='#EFF5F5')

for frame in [main_menu, add_contact, edit_contact, delete_contact, view_contact, search_contact]:
        frame.grid(row=0, column=0, sticky="nsew")

# Main Menu

main_menu.grid_rowconfigure(0, weight=1)
main_menu.grid_rowconfigure(1, weight=1)
main_menu.grid_rowconfigure(2, weight=1)
main_menu.grid_rowconfigure(3, weight=1)
main_menu.grid_rowconfigure(4, weight=1)
main_menu.grid_rowconfigure(5, weight=1)
main_menu.grid_rowconfigure(6, weight=1)
main_menu.grid_rowconfigure(7, weight=1)
main_menu.grid_columnconfigure(0, weight=1)



main_menu_title = tk.Label(main_menu, text="Main Menu", font=("Arial", 24), fg="white", bg="#497174")
main_menu_title.grid(row=0, column=0, sticky="NESW")

main_menu_description = tk.Label(main_menu, text="What do you want to do?", font=("Arial", 18), bg="#EFF5F5")
main_menu_description.grid(row=1, column=0, sticky="NESW")

mm_add_btn = tk.Button(main_menu, text="1 - Add Contact", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(add_contact))
mm_add_btn.grid(row=2, column=0, sticky="NESW")

mm_edit_btn = tk.Button(main_menu, text="2 - Edit Contact", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(edit_contact))
mm_edit_btn.grid(row=3, column=0, sticky="NESW")

mm_del_btn = tk.Button(main_menu, text="3 - Delete Contact", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(delete_contact))
mm_del_btn.grid(row=4, column=0, sticky="NESW")

mm_view_btn = tk.Button(main_menu, text="4 - View Contacts", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(view_contact))
mm_view_btn.grid(row=5, column=0, sticky="NESW")

mm_search_btn = tk.Button(main_menu, text="5 - Search Address Book", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(search_contact))
mm_search_btn.grid(row=6, column=0, sticky="NESW")

mm_exit_btn = tk.Button(main_menu, text="6 - Exit", font=("Arial", 12), bg="#D6E4E5", command=lambda:show_frame(exit))
mm_exit_btn.grid(row=7, column=0, sticky="NESW")

show_frame(main_menu)


window.mainloop()






# This will import all the widgets
# and modules which are available in
# tkinter and ttk module

 
 
# class NewWindow(Toplevel):
     
#     def __init__(self, master = None):
         
#         super().__init__(master = master)
#         self.title("New Window")
#         self.geometry("200x200")
#         label = Label(self, text ="This is a new Window")
#         label.pack()
 
 
# # creates a Tk() object
# master = Tk()
 
# # sets the geometry of
# # main root window
# master.geometry("200x200")
 
# label = Label(master, text ="Main Menu")
# label.pack(side = TOP, pady = 10)
 
# label = Label(master, text ="What would you like to do?", font='arial 10 bold').pack()

# # a button widget which will
# # open a new window on button click
# btn = Button(master,
#              text ="Click to open a new window")
 
# # Following line will bind click event
# # On any click left / right button
# # of mouse a new window will be opened
# btn.bind("<Button>",
#          lambda e: NewWindow(master))
 
# btn.pack(pady = 10)
 
# # mainloop, runs infinitely
# mainloop()






















# ws = Tk()
# ws.title('Python Guides')
# ws.geometry('500x400')
# ws.config(bg="#447c84")
# ws.attributes('-fullscreen',True)

# functions

# from tkinter import ttk


# class Window(tk.Toplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.geometry('300x100')
#         self.title('Toplevel Window')

#         ttk.Button(self,
#                 text='Close',
#                 command=self.destroy).pack(expand=True)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.geometry('720x576')
#         self.title('Main Menu')

#         tk.Label(self, text = 'Main Menu', font='arial 16 bold').pack()
#         tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = '1 - Add Contacts', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()
#         # tk.Label(self, text = 'What would you like to do?', font='arial 12 bold').pack()

#         # place a button on the root window
#         ttk.Button(self,
#                 text = 'Add Contacts',
#                 command=self.open_window("add")).pack()

#         ttk.Button(self,
#                 text = 'Go',
#                 command=self.open_window).place(x="450", y="84")


#     def open_window(self, todo):
#         if todo == "add":
#             window = Window(self)
#             window.grab_set()
#         else:
#             pass




# if __name__ == "__main__":
#     app = App()
#     app.mainloop()













# def main_menu():

#     print("Main Menu\nWhat would you like  to do?")
#     print("1 - Add Contact\n2 - Edit Contact\n3 - Delete Contact\n4 - View Contacts\n5 - Search Address Book\n6 - Exit\n")
    
#     # Keep prompting the user until a valid answer is given
#     # (add counter for when user exceed 5 reask the question and give sggestions)
#     # accept string inputs like add contact or edit contact
#     options = [str(number) for number in range(1,7)]
#     while True:
#         option = input("Choose an option:  ").lstrip("0")
#         if option in options:
#             break

#     # Prompt again depending on what the user want to do
#     if option == options[0]:
#         add_contact()
    
#     elif option == options[1]:
#         edit_contact()
    
#     elif option == options[2]:
#         delete_contact()
    
#     elif option == options[3]:
#         view_contact()
    
#     elif option == options[4]:
#         search_address_book()
    
#     else:
#         sys.exit("The program is closing. Thank you!")

    
    
# def add_contact():
#     # Prompt for first name, last name, address, and contact number
#     print("\nFill up the details for the new contact")
    
#     # Get the names 
#     first_name = get_name("first_name")
#     last_name = get_name("last_name")

#     print(first_name, last_name)
#     print("successfully got the name")

#     # Get the full address

    
#     print("\nFill up the contact's full address (NA if not sure)")



#     # main_menu()






        
    

            
# def edit_contact():
#     pass

# def delete_contact():
#     pass

# def view_contact():
#     pass

# def search_address_book():
#     pass










# if __name__ == "__main__":
# 	main_menu()