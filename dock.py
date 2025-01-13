import tkinter as tk
from tkinter import PhotoImage, filedialog

def open_app(path):
    """Abre um aplicativo no sistema operacional."""
    try:
        os.startfile(path)  # Para Windows
    except AttributeError:
        os.system(f'open "{path}"')  # Para macOS/Linux

def update_dock(root, apps):
    """Atualiza os botões exibidos na dock."""
    dock_frame = root.winfo_children()[0]
    dock_frame.config(bg=root.configure()["background"][-1])

    for widget in dock_frame.winfo_children():
        widget.destroy()

    for index, app in enumerate(apps):
        icon = PhotoImage(file=app["icon"]).subsample(root.icon_size)
        btn = tk.Button(
            dock_frame, image=icon, command=lambda p=app["path"]: open_app(p), bg=root.configure()["background"][-1], bd=0
        )
        btn.image = icon
        btn.pack(side=tk.LEFT if root.dock_layout == "horizontal" else tk.TOP, padx=10, pady=10)

        # Context menu para remover aplicativos
        def show_context_menu(event, app_index=index):
            context_menu = tk.Menu(root, tearoff=0)
            context_menu.add_command(label="Remover", command=lambda: remove_app(app_index, root, apps))
            context_menu.post(event.x_root, event.y_root)

        btn.bind("<Button-3>", show_context_menu)

def add_app(root, apps):
    """Abre o seletor de arquivos para adicionar aplicativos ao dock."""
    file_path = filedialog.askopenfilename(title="Selecione um aplicativo", filetypes=[("Executáveis", "*.exe")])
    if file_path:
        app_name = os.path.basename(file_path)
        apps.append({"name": app_name, "icon": "icons/default.png", "path": file_path})
        update_dock(root, apps)

def remove_app(app_index, root, apps):
    """Remove um aplicativo do dock."""
    del apps[app_index]
    update_dock(root, apps)
