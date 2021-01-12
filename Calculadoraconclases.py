"""
Calculadora :
-Dos campos de texto
-4 botones para las operaciones
-mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox

# Se crea una clase calculadora donde iran todos los metodos
# que tengan que ver con la calculadora
class Calculadora:

    # las variables que se utilizaran seran 2 numeros
    # y se creara una tercera variable llamada resultado
    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    # Se deben crear las funciones que usara la calculadora
    # Todas las funciones llamaran a mostrarResultado desde
    # sumar, restar, multiplicar y dividir

    # Se crea  la funcion cFloat para capturar los errores
    # al momento de ingresar los numeros en la ventana
    # se usa self para acceder a la clase en cada caso
    def cFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos")
        return result

    # funcion SUMAR
    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    # funcion RESTAR
    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    # funcion MULTIPLICAR
    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    # funcion DIVIDIR
    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    # funcion que mostrara el resultado en una alerta
    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operacion es: {self.resultado.get()}")
        # se les da un valor vacio a las variables
        # para que al mostrar el resultado se borren
        # los numeros
        self.numero1.set("")
        self.numero2.set("")

# la ventana es Tk
ventana = Tk()

# titulo de la ventana
ventana.title("Calculadora con tkinter")

# Ajustar el tamaño de la ventana
ventana.geometry("400x400")

# darle margen a la ventana para que no se vea comprimido
ventana.config(bd=25)

# se crea el objeto de la caclculadora
calculadora = Calculadora(messagebox)

# Para que todo este bien ordenado dentro de la ventana
# se crea un Frame que llamaremos marco
marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
# Esto evitara que el marco se desordene
marco.pack_propagate(False)

# CREAR CAMPOS DE TEXTO Y LOS 4 BOTONES

# Label crea el texto en la ventana que indicara el primer numero
# .pack() acomoda los elementos dentro del marco
Label(marco, text="Ingrese el primer numero: ").pack()

# entry indica donde se ingresaran los datos
# debe guardar los datos dentro de una variable,
# por ello se usa textvariable
# se usa un justify center para que el texto salga de el medio
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

# Se crea una label y una entrada para los datos del segundo numero
Label(marco, text="Ingrese el segundo numero: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

# Se le agrega un label para generar un espacio
# entre las casillas blancas y los botones
Label(marco, text="").pack()

# Se crean los botones
# agregar pack(side="left")
# es para que los botones se agrupen hacia el lado
# ademas se les agrega fiil=x y expand=YES para que
# los botones ocupen el mismo espacio
# con command vinculamos los botones con las funciones
Button(marco, text="Sumar(+)", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar(-)", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar(x)", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir(/)", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()