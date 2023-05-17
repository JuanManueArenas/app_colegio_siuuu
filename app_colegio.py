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

# abrir toplevel a notas
def abrir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title("Notas_Madrid")
    toplevel_notas.resizable(False, False)
    toplevel_notas.geometry("500x500")
    toplevel_notas.config(bg="white")

#frame toplevel
    frame_notas = Frame(toplevel_notas)
    frame_notas.config(bg="white", width=500, height=500)
    frame_notas.place(x=0, y=0)

    frame_madri = Frame(toplevel_notas)
    frame_madri.config(bg="gold2", width=450    , height=450)
    frame_madri.place(x=0, y=0)
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Procedimental 30%:")
    lineas_texto_toplevel .config(bg ="gold2", fg="white", font=("Arial", 14))
    lineas_texto_toplevel .place(x=45, y=25)
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Cognitivo 30%:")
    lineas_texto_toplevel.config(bg ="gold2", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=65)
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Bimestral 20%:")
    lineas_texto_toplevel.config(bg ="gold2", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=105)

    lineas_texto_toplevel = Label(toplevel_notas, text = "Autoevaluacion 10%:")
    lineas_texto_toplevel.config(bg ="gold2", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=145)

    lineas_texto_toplevel = Label(toplevel_notas, text = "Actitudinal 10%:")
    lineas_texto_toplevel.config(bg ="gold2", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=185)

    caja_informacion_toplevel = Entry(toplevel_notas)
    caja_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=10)
    caja_informacion_toplevel.focus_set()
    caja_informacion_toplevel.place(x=250,y=25)

    caja_informacion_toplevel = Entry(toplevel_notas)
    caja_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=10)
    caja_informacion_toplevel.focus_set()
    caja_informacion_toplevel.place(x=250,y=65)

    caja_informacion_toplevel = Entry(toplevel_notas)
    caja_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=10)
    caja_informacion_toplevel.focus_set()
    caja_informacion_toplevel.place(x=250,y=105)

    caja_informacion_toplevel = Entry(toplevel_notas)
    caja_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=10)
    caja_informacion_toplevel.focus_set()
    caja_informacion_toplevel.place(x=250,y=145)

    caja_informacion_toplevel = Entry(toplevel_notas)
    caja_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=10)
    caja_informacion_toplevel.focus_set()
    caja_informacion_toplevel.place(x=250,y=185)




#entrada       
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

#boton para entrar 
blocksito = PhotoImage(file="img/madri (1).png")

#boton notas

bt_notas = Button(frame_entrada, image=blocksito, command=abrir_toplevel_notas)
bt_notas.config(bg="DodgerBlue3", fg="black", font=("Arial", 14))
bt_notas.place(x=100, y=250)

logo = PhotoImage(file="img/images.png")
lb_logo = Label(ventana_principal, image=logo, bg="white")
lb_logo.place(x=0,y=0)

Imagen = PhotoImage(file="img/Hala (1).png")
lb_Imagen = Label(frame_entrada, image=Imagen, bg="DodgerBlue3")
lb_Imagen.place(x=500,y=275)

ventana_principal.mainloop()
