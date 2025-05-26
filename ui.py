import tkinter as tk
from tkinter import messagebox

# --- Tài khoản mẫu ---
USERS = {"admin": "123"}

# --- Hàm xử lý đăng nhập ---
def handle_login():
    username = username_entry.get()
    password = password_entry.get()

    if username in USERS and USERS[username] == password:
        show_dashboard()
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng")

# --- Hàm hiển thị dashboard ---
def show_dashboard():
    login_frame.pack_forget()
    dashboard_frame.pack(fill="both", expand=True)

# --- Cửa sổ chính ---
root = tk.Tk()
root.title("Login → Dashboard")
root.geometry("900x500")

# ======================= LOGIN FRAME =======================
login_frame = tk.Frame(root, bg="white")
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Đăng nhập", font=("Arial", 20), bg="white").pack(pady=30)
tk.Label(login_frame, text="Tên đăng nhập:", bg="white").pack()
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Mật khẩu:", bg="white").pack()
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

tk.Button(login_frame, text="Đăng nhập", command=handle_login, bg="#3498db", fg="white", width=20).pack(pady=20)

# ======================= DASHBOARD FRAME =======================
dashboard_frame = tk.Frame(root, bg="#ecf0f1")  # Ẩn lúc đầu

# Sidebar trái
sidebar = tk.Frame(dashboard_frame, width=200, bg="#2c3e50")
sidebar.pack(side="left", fill="y")

menu_items = ["Trang chủ", "Quản lý Proxy", "Báo cáo", "Cài đặt"]
for item in menu_items:
    tk.Button(sidebar, text=item, bg="#34495e", fg="white", bd=0, pady=10, font=("Arial", 12), anchor="w").pack(fill="x", padx=10, pady=2)

# Nội dung phải
content = tk.Frame(dashboard_frame, bg="#ecf0f1")
content.pack(side="right", expand=True, fill="both")

tk.Label(content, text="Chào mừng đến Dashboard!", font=("Arial", 24), bg="#ecf0f1", fg="#2c3e50").pack(pady=100)

# ======================= CHẠY =======================
root.mainloop()
