from tkinter import *
from tkinter import ttk
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
    frame_madri.config(bg="DodgerBlue3", width=450    , height=450)
    frame_madri.place(x=0, y=0)
    
    
    
    #todo lo utilizado
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Procedimental 30%:")
    lineas_texto_toplevel .config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_texto_toplevel .place(x=45, y=65)
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Cognitivo 30%:")
    lineas_texto_toplevel.config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=105)
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Bimestral 20%:")
    lineas_texto_toplevel.config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=145)

    lineas_texto_toplevel = Label(toplevel_notas, text = "Autoevaluacion 10%:")
    lineas_texto_toplevel.config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=185)

    lineas_texto_toplevel = Label(toplevel_notas, text = "Actitudinal 10%:")
    lineas_texto_toplevel.config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_texto_toplevel.place(x=45, y=225)

    proce_informacion_toplevel = Entry(toplevel_notas)
    proce_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=17)
    proce_informacion_toplevel.focus_set()
    proce_informacion_toplevel.place(x=250,y=65)
    
    cog_informacion_toplevel = Entry(toplevel_notas)
    cog_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=17)
    cog_informacion_toplevel.focus_set()
    cog_informacion_toplevel.place(x=250,y=105)

    bi_informacion_toplevel = Entry(toplevel_notas)
    bi_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=17)
    bi_informacion_toplevel.focus_set()
    bi_informacion_toplevel.place(x=250,y=145)

    ac_informacion_toplevel = Entry(toplevel_notas)
    ac_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=17)
    ac_informacion_toplevel.focus_set()
    ac_informacion_toplevel.place(x=250,y=185)

    aut_informacion_toplevel = Entry(toplevel_notas)
    aut_informacion_toplevel.config(bg="white", fg="Black", font=("Times New Roman", 15), width=17)
    aut_informacion_toplevel.focus_set()
    aut_informacion_toplevel.place(x=250,y=225)

    #lista desplegable
    lista= ttk.Combobox(toplevel_notas,state="reandoly")
    lista.place(x=250, y=25)
    lista["values"]=("Quimica", "Fisica", "Sistemas", "Trigonometria", "Ingles")
    lista.current(0)
    
    lineas_texto_toplevel = Label(toplevel_notas, text = "Seleccione la materia:")
    lineas_texto_toplevel .config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_texto_toplevel .place(x=45, y=25)
  


    #procedimiento
    def Convertir():
        messagebox.showinfo("Nota Difinitiva", "Operacion realizada")
        proce_informacion_def = float(proce_informacion_toplevel.get())
        cog_informacion_def = float(cog_informacion_toplevel.get())
        aut_informacion_def = float(bi_informacion_toplevel.get())
        ac_informacion_def = float(ac_informacion_toplevel.get())
        bi_informacion_def = float(aut_informacion_toplevel.get())

        entry_not_final = (0.3*proce_informacion_def) + (0.3*cog_informacion_def) + (0.1*ac_informacion_def) + (0.1*aut_informacion_def) + (0.2*bi_informacion_def)

        if entry_not_final < 30:
            messagebox.showinfo("Resultado", "El alumno a aprobado la asignatura :) "+str(entry_not_final))
        else:
            messagebox.showinfo("Resultado", "El alumno a reprobado la asignatura ;() "+str(entry_not_final))

    #   boton para sumar
    lineas_hola = Button(toplevel_notas,text = "Convertir", command= Convertir)
    lineas_hola.config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_hola.place(x=200, y=300)

#   boton para sumar
    lineas_hola = Button(frame_madri,command= Convertir)
    lineas_hola.config(bg ="DodgerBlue3", fg="white", font=("Arial", 14))
    lineas_hola.place(x=200, y=300)
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
