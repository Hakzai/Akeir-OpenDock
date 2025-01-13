import tkinter as tk
from tkinter import Menu
from dock import update_dock, add_app, remove_app
from settings import set_dock_size, set_dock_layout, change_dock_color

# Configurações da janela principal
root = tk.Tk()
root.title("Meu Dock")
root.geometry("600x100")
root.resizable(False, False)
root.configure(bg="black")

# Inicializando propriedades
root.icon_size = 5  # Tamanho inicial dos ícones
root.dock_layout = "horizontal"  # Layout inicial do dock

# Lista de aplicativos
apps = [
    {"name": "Navegador", "icon": "icons/test.png", "path": "C:\\Program Files\\Mozilla Firefox\\firefox.exe"},
    {"name": "Editor de Texto", "icon": "icons/test.png", "path": "notepad.exe"},
    {"name": "Calculadora", "icon": "icons/test.png", "path": "calc.exe"},
]

# Menu principal
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Menu para alterar o tamanho dos ícones
size_menu = Menu(menu_bar, tearoff=0)
size_menu.add_command(label="Pequeno", command=lambda: set_dock_size(10, root, apps))
size_menu.add_command(label="Médio", command=lambda: set_dock_size(5, root, apps))
size_menu.add_command(label="Grande", command=lambda: set_dock_size(2, root, apps))
menu_bar.add_cascade(label="Tamanho da Dock", menu=size_menu)

# Menu para alterar o layout
layout_menu = Menu(menu_bar, tearoff=0)
layout_menu.add_command(label="Horizontal", command=lambda: set_dock_layout("horizontal", root, apps))
layout_menu.add_command(label="Vertical", command=lambda: set_dock_layout("vertical", root, apps))
menu_bar.add_cascade(label="Layout da Dock", menu=layout_menu)

# Menu para alterar a cor de fundo
color_menu = Menu(menu_bar, tearoff=0)
color_menu.add_command(label="Alterar Cor de Fundo", command=lambda: change_dock_color(root, apps))
menu_bar.add_cascade(label="Cor da Dock", menu=color_menu)

# Menu para adicionar novos aplicativos
menu_bar.add_command(label="Adicionar Aplicativo", command=lambda: add_app(root, apps))

# Cria o frame da dock
dock_frame = tk.Frame(root, bg="black")
dock_frame.pack(expand=True, fill=tk.BOTH)

# Inicializa a dock
update_dock(root, apps)

root.mainloop()
