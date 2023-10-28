import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role

class SystemAdminManagementSystem:
    def __init__(self):
        self.users = []

    def add_user(self, username, email, role):
        user = User(username, email, role)
        self.users.append(user)
        messagebox.showinfo("Success", f"User '{username}' added successfully.")

    def update_user(self, username, new_email, new_role):
        for user in self.users:
            if user.username == username:
                user.email = new_email
                user.role = new_role
                messagebox.showinfo("Success", f"User '{username}' updated successfully.")
                return
        messagebox.showerror("Error", f"User '{username}' not found.")

    def delete_user(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                messagebox.showinfo("Success", f"User '{username}' deleted successfully.")
                return
        messagebox.showerror("Error", f"User '{username}' not found.")

    def list_users(self):
        if self.users:
            user_list = "\n".join([f"Username: {user.username}, Email: {user.email}, Role: {user.role}" for user in self.users])
            messagebox.showinfo("User List", user_list)
        else:
            messagebox.showinfo("User List", "No users found.")

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Admin Management System")

        self.system = SystemAdminManagementSystem()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.role_label = tk.Label(root, text="Role:")
        self.role_label.pack()
        self.role_entry = tk.Entry(root)
        self.role_entry.pack()

        self.add_button = tk.Button(root, text="Add User", command=self.add_user)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update User", command=self.update_user)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete User", command=self.delete_user)
        self.delete_button.pack()

        self.list_button = tk.Button(root, text="List Users", command=self.list_users)
        self.list_button.pack()

    def add_user(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        role = self.role_entry.get()
        self.system.add_user(username, email, role)

    def update_user(self):
        username = self.username_entry.get()
        new_email = self.email_entry.get()
        new_role = self.role_entry.get()
        self.system.update_user(username, new_email, new_role)

    def delete_user(self):
        username = self.username_entry.get()
        self.system.delete_user(username)

    def list_users(self):
        self.system.list_users()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()