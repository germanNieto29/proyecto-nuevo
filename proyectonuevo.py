from fileinput import close
import sqlite3

conn = sqlite3.connect ("base de datos TuGyM")
cursor = conn.cursor ()

cursor.execute("creartabla,nombre,apellido ,edad,peso,talla")
conn.commit()
conn = close

import tkinter as tk
def agregar_usuario():
   nombre = entry_nombre.get()
   apellido = entry_apellido.get() # type: ignore
   edad = entry_edad.get()
   peso = entry_peso.get() # type: ignore
   talla = entry_talla.get() # type: ignore
   
    
ventana = tk.Tk()
ventana = "title"("base de datos con tkinter")
 
tk.lebel(ventana, text="nombre:").pack()
entry_nombre = tk.entry(ventana)
entry_nombre.pack()
 
tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Button(ventana, text="Agregar Usuario", command=agregar_usuario).pack()

ventana.mainloop()