import tkinter as tk
from tkinter import messagebox
from auth import register_user, login_user, delete_user, get_all_users
from files import create_file, view_file, delete_file
from logs import view_logs, clear_logs


root = tk.Tk()
root.title("Secure File Access - GUI")
root.geometry("800x450")

# --- GUI Components ---

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Label(root, text="Role (for registration only)").pack()
role_var = tk.StringVar()
role_dropdown = tk.OptionMenu(root, role_var, "admin", "user")
role_dropdown.pack()

def gui_register():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    role = role_var.get()

    if not username or not password or not role:
        messagebox.showerror("Error", "All fields are required.")
        return

    success, msg = register_user(username, password, role)
    if success:
        messagebox.showinfo("Success", msg)
    else:
        messagebox.showerror("Error", msg)

def gui_login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Username and password required.")
        return

    user, msg = login_user(username, password)

    if user:
        messagebox.showinfo("Welcome", msg)
        open_file_menu(user)
    else:
        messagebox.showerror("Login Failed", msg)

def open_file_menu(user):
    menu = tk.Toplevel(root)
    menu.title("File Menu")
    menu.geometry("850x450")

    tk.Label(menu, text=f"Logged in as {user['username']} ({user['role']})").pack(pady=10)

    btn_create = tk.Button(menu, text="Create File", command=lambda: create_file_gui(user))
    btn_create.pack(pady=5)

    btn_view = tk.Button(menu, text="View File", command=lambda: view_file_gui(user))
    btn_view.pack(pady=5)

    btn_delete = tk.Button(menu, text="Delete File", command=lambda: delete_file_gui(user))
    btn_delete.pack(pady=5)

    if user["role"] == "admin":
        btn_logs = tk.Button(menu, text="View Logs", command=view_logs_gui)
        btn_logs.pack(pady=5)

        btn_clear_logs = tk.Button(menu, text="Clear Logs", command=clear_logs_gui)
        btn_clear_logs.pack(pady=5)

        btn_del_user = tk.Button(menu, text="Delete User", command=lambda: delete_user_gui(user))
        btn_del_user.pack(pady=5)

def create_file_gui(user):
    win = tk.Toplevel(root)
    win.title("Create File")

    tk.Label(win, text="Filename:").pack()
    entry_filename = tk.Entry(win)
    entry_filename.pack()

    tk.Label(win, text="Content:").pack()
    text_content = tk.Text(win, height=7, width=40)
    text_content.pack()

    def submit():
        filename = entry_filename.get().strip()
        content = text_content.get("1.0", tk.END).strip()

        if not filename or not content:
            messagebox.showerror("Error", "Filename and content required.")
            return

        success, msg = create_file(user["username"], filename, content)
        if success:
            messagebox.showinfo("Success", msg)
            win.destroy()
        else:
            messagebox.showerror("Error", msg)

    tk.Button(win, text="Create", command=submit).pack(pady=5)

def view_file_gui(user):
    win = tk.Toplevel(root)
    win.title("View File")

    tk.Label(win, text="Filename (without .txt):").pack()
    entry_filename = tk.Entry(win)
    entry_filename.pack()

    output_text = tk.Text(win, height=15, width=60)
    output_text.pack()

    def submit():
        filename = entry_filename.get().strip()
        if not filename:
            messagebox.showerror("Error", "Enter a filename.")
            return

        success, content = view_file(user["username"], user["role"], filename)
        if success:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, content)
        else:
            messagebox.showerror("Error", content)

    tk.Button(win, text="View", command=submit).pack(pady=5)

def delete_file_gui(user):
    win = tk.Toplevel(root)
    win.title("Delete File")

    tk.Label(win, text="Filename (without .txt):").pack()
    entry_filename = tk.Entry(win)
    entry_filename.pack()

    def submit():
        filename = entry_filename.get().strip()
        if not filename:
            messagebox.showerror("Error", "Enter a filename.")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{filename}'?")
        if not confirm:
            return

        success, msg = delete_file(user["username"], user["role"], filename)
        if success:
            messagebox.showinfo("Success", msg)
            win.destroy()
        else:
            messagebox.showerror("Error", msg)

    tk.Button(win, text="Delete", command=submit).pack(pady=5)

def view_logs_gui():
    win = tk.Toplevel(root)
    win.title("View Logs")

    success, logs = view_logs()
    if not success:
        messagebox.showinfo("Logs", logs)
        return

    log_text = tk.Text(win, height=20, width=70)
    log_text.pack()
    log_text.insert(tk.END, logs)

def clear_logs_gui():
    confirm = messagebox.askyesno("Confirm Clear Logs", "Are you sure you want to clear all logs?")
    if confirm:
        clear_logs()
        messagebox.showinfo("Success", "All logs have been cleared.")

def delete_user_gui(current_user):
    users = get_all_users()
    usernames = list(users.keys())

    win = tk.Toplevel(root)
    win.title("Delete User")

    tk.Label(win, text="Select user to delete:").pack()
    user_var = tk.StringVar(win)
    user_var.set(usernames[0] if usernames else "")

    user_dropdown = tk.OptionMenu(win, user_var, *usernames)
    user_dropdown.pack()

    def submit():
        username_to_delete = user_var.get()
        if not username_to_delete:
            messagebox.showerror("Error", "Select a user.")
            return

        if username_to_delete == current_user["username"]:
            messagebox.showerror("Error", "Cannot delete your own account.")
            return

        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{username_to_delete}'?")
        if not confirm:
            return

        success, msg = delete_user(current_user, username_to_delete)
        if success:
            messagebox.showinfo("Success", msg)
            win.destroy()
        else:
            messagebox.showerror("Error", msg)

    tk.Button(win, text="Delete", command=submit).pack(pady=5)

# Buttons on main window
tk.Button(root, text="Register", command=gui_register).pack(pady=10)
tk.Button(root, text="Login", command=gui_login).pack(pady=5)

root.mainloop()
