from tkinter import *
from tkinter import messagebox

ventana_principal = Tk()

ventana_principal.title("Siuuuuu")

ventana_principal.geometry("1000x500")

ventana_principal.config(bg="white")

def borrar():
    messagebox.showinfo("Datos", "Los datos serán borrados")
    caja_informacion.set("")
    caja_informacion.delete("1.0","end")





frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="DodgerBlue3" , width=1000, height=500)
frame_entrada.place(x=300, y=0)

caja_informacion = Entry(frame_entrada)
caja_informacion.config(bg="white", fg="Black", font=("Times New Roman", 10), width=25)
caja_informacion.focus_set()
caja_informacion.place(x=250,y=25)

lineas_texto = Label(frame_entrada, text = "Dirección de correo electronico:")
lineas_texto.config(bg ="DodgerBlue3", fg="white", font=("Arial", 10))
lineas_texto.place(x=45, y=25)

caja_informacion = Entry(frame_entrada)
caja_informacion.config(bg="white", fg="Black", font=("Times New Roman", 10), width=25)
caja_informacion.focus_set()
caja_informacion.place(x=250, y=65)

lineas_texto = Label(frame_entrada, text = "Nombre del estudiante:")
lineas_texto.config(bg ="DodgerBlue3", fg="white", font=("Arial", 10))
lineas_texto.place(x=45, y=65)

caja_informacion = Entry(frame_entrada)
caja_informacion.config(bg="white", fg="Black", font=("Times New Roman", 10), width=25)
caja_informacion.focus_set()
caja_informacion.place(x=250, y=105)

lineas_texto = Label(frame_entrada, text = "Especialidad tecnica:")
lineas_texto.config(bg ="DodgerBlue3", fg="white", font=("Arial", 10))
lineas_texto.place(x=45, y=105)

caja_informacion = Entry(frame_entrada)
caja_informacion.config(bg="white", fg="Black", font=("Times New Roman", 10), width=25)
caja_informacion.focus_set()
caja_informacion.place(x=250, y=145)

lineas_texto = Label(frame_entrada, text = "Grado:")
lineas_texto.config(bg ="DodgerBlue3", fg="white", font=("Arial", 10))
lineas_texto.place(x=45, y=145)

# boton para borrar
bt_borrar = Button(frame_entrada, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)











logo = PhotoImage(file="img/images.png")
lb_logo = Label(ventana_principal, image=logo, bg="white")
lb_logo.place(x=0,y=0)

Imagen = PhotoImage(file="img/Hala (1).png")
lb_Imagen = Label(frame_entrada, image=Imagen, bg="DodgerBlue3")
lb_Imagen.place(x=500,y=275)































ventana_principal.mainloop()
