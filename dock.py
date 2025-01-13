import tkinter as tk
from tkinter import PhotoImage, Menu
import os

# Função para abrir aplicativos
def open_app(path):
    try:
        os.startfile(path)  # Para Windows
    except AttributeError:
        os.system(f'open "{path}"')  # Para macOS/Linux

# Função para ajustar o tamanho dos ícones
def set_dock_size(size):
    global icon_size
    icon_size = size
    update_dock()

# Função para ajustar o tamanho da janela
def set_window_size(width, height):
    root.geometry(f"{width}x{height}")

# Função para atualizar os botões da dock
def update_dock():
    for widget in dock_frame.winfo_children():
        widget.destroy()

    for app in apps:
        icon = PhotoImage(file=app["icon"]).subsample(icon_size)
        btn = tk.Button(dock_frame, image=icon, command=lambda p=app["path"]: open_app(p), bg="black", bd=0)
        btn.image = icon
        btn.pack(side=tk.LEFT, padx=10)

# Lista de aplicativos e ícones
apps = [
    {"name": "Navegador", "icon": "icons/test.png", "path": "C:\\Program Files\\Mozilla Firefox\\firefox.exe"},
    {"name": "Editor de Texto", "icon": "icons/test.png", "path": "notepad.exe"},
]

# Tamanho inicial dos ícones
icon_size = 5

# Cria a janela principal
root = tk.Tk()
root.title("Meu Dock")
root.geometry("600x100")
root.resizable(False, False)
root.configure(bg="black")

# Cria o menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Menu para alterar o tamanho
size_menu = Menu(menu_bar, tearoff=0)
size_menu.add_command(label="Pequeno", command=lambda: set_dock_size(10))  # Ícones menores
size_menu.add_command(label="Médio", command=lambda: set_dock_size(5))    # Ícones médios
size_menu.add_command(label="Grande", command=lambda: set_dock_size(2))   # Ícones maiores
menu_bar.add_cascade(label="Tamanho da Dock", menu=size_menu)

# Menu para alterar o tamanho da janela
window_menu = Menu(menu_bar, tearoff=0)
window_menu.add_command(label="Pequeno (600x100)", command=lambda: set_window_size(600, 100))
window_menu.add_command(label="Médio (800x150)", command=lambda: set_window_size(800, 150))
window_menu.add_command(label="Grande (1000x200)", command=lambda: set_window_size(1000, 200))
menu_bar.add_cascade(label="Tamanho da Janela", menu=window_menu)

# Cria o frame da dock
dock_frame = tk.Frame(root, bg="black")
dock_frame.pack(expand=True, fill=tk.BOTH)

# Inicializa a dock
update_dock()

root.mainloop()
