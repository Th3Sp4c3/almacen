import tkinter as tk

def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar, width = 300, height = 300)

    menu_inicio = tk.Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label='Inicio', menu = menu_inicio)
    menu_bar.add_cascade(label='Consulta')
    menu_bar.add_cascade(label='Configuración')
    menu_bar.add_cascade(label='Ayuda')

    menu_inicio.add_command(label='Registrar producto en BD')
    menu_inicio.add_command(label='Eliminar producto en BD')
    menu_inicio.add_command(label='Salir', command = root.destroy)


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        #self.config( bg='green')
        self.Campos_productos()

    def Campos_productos(self):
        # labbels campos del producto
        self.labbel_nombre = tk.Label(self, text='Nombre: ')
        self.labbel_nombre.config(font = ('Arial', '12', 'bold'))
        self.labbel_nombre.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.labbel_descripcion = tk.Label(self, text='Descripcion: ')
        self.labbel_descripcion.config(font = ('Arial', '12', 'bold'))
        self.labbel_descripcion.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.labbel_cantidad = tk.Label(self, text='Cantidad: ')
        self.labbel_cantidad.config(font = ('Arial', '12', 'bold'))
        self.labbel_cantidad.grid(row = 2, column = 0, padx = 10, pady = 10)

        #Entrys de cada campo
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width = 50, state = 'disable', font = ('Arial', '12'))
        self.entry_nombre.grid(row=0,column=1, padx = 10, pady = 10)

        self.entry_descrip = tk.Entry(self)
        self.entry_descrip.config(width = 50, state = 'disable', font = ('Arial', '12'))
        self.entry_descrip.grid(row=1,column=1, padx = 10, pady = 10)

        self.entry_cant = tk.Entry(self)
        self.entry_cant.config(width = 50, state = 'disable', font = ('Arial', '12'))
        self.entry_cant.grid(row=2,column=1, padx = 10, pady = 10)