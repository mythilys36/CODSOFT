import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize an empty dictionary to store contacts
contacts = {}

# Function to add or update a contact (with scrollable popup for input)
def contact_form(action, selected_name=None):
    form_window = tk.Toplevel(root)
    form_window.title(f"{action} Contact")
    form_window.geometry("350x300")
    
    # Create a canvas and a scrollbar for the popup
    canvas = tk.Canvas(form_window, borderwidth=0)
    scroll_frame = tk.Frame(canvas)
    scrollbar = tk.Scrollbar(form_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    
    # Frame inside the canvas
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    
    # Ensure canvas resizes to the size of the frame
    scroll_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    # Contact details input fields
    tk.Label(scroll_frame, text="Name:").pack(pady=5)
    name_entry = tk.Entry(scroll_frame, width=30)
    name_entry.pack(pady=5)

    tk.Label(scroll_frame, text="Phone:").pack(pady=5)
    phone_entry = tk.Entry(scroll_frame, width=30)
    phone_entry.pack(pady=5)

    tk.Label(scroll_frame, text="Email:").pack(pady=5)
    email_entry = tk.Entry(scroll_frame, width=30)
    email_entry.pack(pady=5)

    tk.Label(scroll_frame, text="Address:").pack(pady=5)
    address_entry = tk.Entry(scroll_frame, width=30)
    address_entry.pack(pady=5)

    # Pre-fill form fields if updating a contact
    if action == "Update" and selected_name:
        name_entry.insert(0, selected_name)
        name_entry.config(state='disabled')  # Prevent changing the name
        phone_entry.insert(0, contacts[selected_name]['phone'])
        email_entry.insert(0, contacts[selected_name]['email'])
        address_entry.insert(0, contacts[selected_name]['address'])

    # Save contact (for both Add and Update)
    def save_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        
        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required fields!")
            return
        
        if action == "Add":
            if name in contacts:
                messagebox.showwarning("Duplicate Contact", "Contact with this name already exists.")
            else:
                contacts[name] = {'phone': phone, 'email': email, 'address': address}
                messagebox.showinfo("Success", f"Contact for {name} added successfully!")
        elif action == "Update":
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact for {name} updated successfully!")
        
        view_contacts()
        form_window.destroy()
    
    # Save button
    tk.Button(scroll_frame, text="Save", command=save_contact).pack(pady=10)

# Function to view all contacts in the listbox
def view_contacts():
    contact_list.delete(0, tk.END)
    if contacts:
        for name, details in contacts.items():
            contact_list.insert(tk.END, f"{name} - {details['phone']}")
    else:
        contact_list.insert(tk.END, "No contacts found.")

# Function to delete a selected contact
def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contact_info = contact_list.get(selected)
        name = contact_info.split(" - ")[0]
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete {name}'s contact?")
        if confirm:
            del contacts[name]
            messagebox.showinfo("Success", f"Contact for {name} deleted.")
            view_contacts()
    else:
        messagebox.showwarning("Warning", "No contact selected.")

# Function to search for a contact
def search_contact():
    search_term = simpledialog.askstring("Input", "Enter name or phone number to search:")
    if search_term:
        found = False
        contact_list.delete(0, tk.END)
        for name, details in contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                contact_list.insert(tk.END, f"{name} - {details['phone']}")
                found = True
        if not found:
            messagebox.showinfo("Search Result", "No contact found.")

# Function to update a selected contact (opens form pre-filled)
def update_contact():
    selected = contact_list.curselection()
    if selected:
        contact_info = contact_list.get(selected)
        name = contact_info.split(" - ")[0]
        contact_form("Update", selected_name=name)
    else:
        messagebox.showwarning("Warning", "No contact selected.")

# Main application window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x400")
root.config(bg='#F0F8FF')

# Title label
title_label = tk.Label(root, text="Contact Manager", font=("Arial", 18, "bold"), bg='#F0F8FF', fg='#333333')
title_label.pack(pady=10)

# Contact listbox
contact_list = tk.Listbox(root, height=10, width=50, font=("Arial", 12))
contact_list.pack(pady=10)

# Button frame
button_frame = tk.Frame(root, bg='#F0F8FF')
button_frame.pack(pady=10)

# Buttons for actions
add_button = tk.Button(button_frame, text="Add Contact", width=15, command=lambda: contact_form("Add"), bg='#4682B4', fg='white', font=("Arial", 10))
add_button.grid(row=0, column=0, padx=10)

view_button = tk.Button(button_frame, text="View Contacts", width=15, command=view_contacts, bg='#32CD32', fg='white', font=("Arial", 10))
view_button.grid(row=0, column=1, padx=10)

search_button = tk.Button(button_frame, text="Search Contact", width=15, command=search_contact, bg='#FFA500', fg='white', font=("Arial", 10))
search_button.grid(row=1, column=0, padx=10, pady=5)

update_button = tk.Button(button_frame, text="Update Contact", width=15, command=update_contact, bg='#1E90FF', fg='white', font=("Arial", 10))
update_button.grid(row=1, column=1, padx=10, pady=5)

delete_button = tk.Button(button_frame, text="Delete Contact", width=15, command=delete_contact, bg='#FF6347', fg='white', font=("Arial", 10))
delete_button.grid(row=2, column=0, padx=10, pady=5)

exit_button = tk.Button(button_frame, text="Exit", width=15, command=root.quit, bg='#696969', fg='white', font=("Arial", 10))
exit_button.grid(row=2, column=1, padx=10, pady=5)

# Start the main event loop
root.mainloop()
