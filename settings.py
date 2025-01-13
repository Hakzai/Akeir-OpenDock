from tkinter import colorchooser
from dock import update_dock

def set_dock_size(size, root, apps):
    """Define o tamanho dos ícones do dock."""
    root.icon_size = size
    update_dock(root, apps)

def set_dock_layout(layout, root, apps):
    """Define o layout do dock (horizontal ou vertical)."""
    root.dock_layout = layout
    update_dock(root, apps)

def change_dock_color(root):
    """Permite alterar a cor de fundo da dock."""
    color = colorchooser.askcolor(title="Escolha uma cor para a dock")[1]
    if color:
        root.configure(bg=color)
        update_dock(root, apps)
