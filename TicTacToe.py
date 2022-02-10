from tkinter import *
from tkinter import ttk, messagebox
from tkinter.constants import END
import time
from random import randrange
from constantes import LOGO_ICON, PORTADA_PNG


class UsersError (Exception):
    def __init__(self, Name, mensaje):
        Exception.__init__(self, mensaje)
        self.Name = Name

class Tic_Tac:
    lista=[['1','2','3'],['4','5','6'],['7','8','9']]
    Num_veces=0
    Nombre_jugadores = ()
    finaliza = False
    # ('./img/*.ico', 'img'), ('./img/*.png', 'img')

    def __init__ (self, key):
        self.window=key
        self.window.iconbitmap (LOGO_ICON)
        self.window.title ('Tic Tac Toe')
        self.window.resizable (False, False)

        # ---------- imagen de fondo --------------
        self.img_portada = PhotoImage (file=PORTADA_PNG)
        Label (self.window, image=self.img_portada).grid (row=0, column=0)
        
        # ---------- Contenedor principal ----------------
        self.contenedor = Frame (self.window, background="#b5b5b5")
        self.contenedor.place (x=120, y=80)

        Label (self.contenedor, text='Bienvenido a TIC TAC TOE', fg='#004D40', font=('Arial 15 bold'), bg='#b5b5b5', width=27).grid (row=0, column=0, columnspan=3, padx=10, pady=20)

        Label (self.contenedor, text="Nombre", bg="#b5b5b5", fg="black", font=("Cambria 12 bold")).grid (row=1, column=1, padx=10, pady=10, sticky=W)
        self.jugador_solo=Entry (self.contenedor, font=("Cambria 12 bold"), borderwidth=0, background="#b5b5b5")
        self.jugador_solo.grid (row=2, column=1, sticky=W+E, padx=10)
        ttk.Separator (self.contenedor, orient="horizontal").grid (row=3, column=1, padx=10, pady=2, sticky=W+E)
        
        # ------------ Contenedor (tipo de juego) ------------
        self.contenedor_jugador=LabelFrame (self.contenedor, text='N° de Usuarios', font=('Cambria 12 bold'), bd=5, bg='#b5b5b5', foreground='green', width=30)
        self.contenedor_jugador.grid (row=4, column=1, padx=10, pady=20, ipady=10, sticky=W+E)        

        self.jugadores=IntVar ()
        self.ds_jugador=Radiobutton (self.contenedor_jugador, variable=self.jugadores, value=1, text='2 Jugadores', font=('Arial 12 bold'), bg="#b5b5b5", fg='blue', command=lambda: self.insert_users ())
        self.ds_jugador.grid (row=1,column=1, ipadx=6, padx=20, pady=8, sticky='W')
        
        self.un_jugador=Radiobutton (self.contenedor_jugador, text='1 Jugador    ', variable=self.jugadores, value=2, font=('Arial 12 bold'), bg='#b5b5b5', fg='blue', bd=0, command=lambda: self.solo ())
        self.un_jugador.grid (row=2,column=1,ipadx=6, padx=20, pady=8, sticky='W')
        
        # --------------- Boton de salir -----------------
        self.next=Button (self.contenedor, text='Salir', foreground='black', background='#9032bb', borderwidth=3, width=15, relief='raised', font=('Cambria 10 bold'), command=lambda: self.window.destroy ())
        self.next.grid (row=5, column=1, padx=15, pady=6)
    
    # Ingresar nombre de jugadores...........
    def  insert_users (self):
        time.sleep(1)
        self.window2=Toplevel ()
        self.window2.iconbitmap (LOGO_ICON)
        self.window2.title ('Nombre jugador')
        self.window2.geometry ('360x410')
        self.window2.resizable (False, False)
        self.window2.config (bg='black')

        """"
            #004D40 : Turquesa oscuro
            #9032bb : Violeta
            #B2DFD8 : Turquesa opaco
        """
         
        # --------------- titulo del juego ----------------
        Label (self.window2, text='!Listo para divertirte!', foreground="white", font=('Cambria 14 bold'), bg='black', width=28).grid (row=0, column=0, columnspan=2, sticky=W+E, padx=20, pady=20)
        
        # -------------- Contenedor donde se ingresa los nombres de los jugadores ------------------
        self.Contendor_jugador=LabelFrame (self.window2, text='Nombre de usuario', fg='blue', font=('Cambria 12 bold'), bg='black', bd=3)
        self.Contendor_jugador.grid (row=1, column=0, columnspan=2, sticky=W+E, padx=20, pady=10, ipadx=8, ipady=5)
         
        # ****** Nombre del jugador uno ********
        Label(self.Contendor_jugador, text='Jugador 1 *', font=('Cambria 12 bold'), fg='green', bg='black').grid (row=0, column=0, pady=8, sticky=W, padx=15)
        
        self.jugador1=Entry (self.Contendor_jugador, font=('Cambria 12 bold'), foreground="white", background="black", borderwidth=0, width=30, justify=CENTER)
        self.jugador1.grid (row=1, column=0, pady=3, padx=15, sticky=W+E)
        ttk.Separator (self.Contendor_jugador, orient="horizontal").grid (row=2, column=0, sticky=W+E, padx=13)
        
        # ****** Nombre del jugador dos **********
        Label(self.Contendor_jugador, text='Jugador 2 *', font=('Cambria 12 bold'), fg='green', bg='black').grid (row=3, column=0,  pady=8, sticky=W, padx=15)
        
        self.jugador2=Entry (self.Contendor_jugador, font=('Cambria 12 bold'), foreground="white", background="black", borderwidth=0, width=30, justify=CENTER)
        self.jugador2.grid (row=4, column=0, pady=3, padx=15, sticky=W+E)
        ttk.Separator (self.Contendor_jugador, orient="horizontal").grid (row=5, column=0, sticky=W+E, padx=13)

        # -------------- Mensaje en pantalla -------------
        self.mensaje=Label (self.window2, font=("Cambria 11"), foreground="red", background="black")
        self.mensaje.grid (row=2, column=0, columnspan=2, sticky=W+E, padx=5, pady=5)
         
        # ------------- Botones de "atras" y "jugar" -------------
        Button (self.window2, text='Atras', relief='raised', bd=2, background="#1DE9B6", fg='red', font=('Cambria 12 bold'), width=12, command=lambda:self.window2.destroy ()).grid (row=3, column=0, padx=10, pady=2)
        
        Button (self.window2, text='Jugar', relief='raised', bd=2, background="#1DE9B6", fg='red', font=('Cambria 12 bold'), width=12, command=lambda: self.jugar ()).grid (row=3, column=1, padx=10, pady=2)

          
     # Tablero.............................................
    def  tablero (self):
        self.window1=Toplevel ()
        self.window1.iconbitmap (LOGO_ICON)
        self.window1.title('Tablero')
        self.window1.config(bg='black')
        self.window1.geometry ('341x420')
        self.window1.resizable (False, False)

        """"
            #004D40 : Turquesa oscuro
            #9032bb : Violeta
            #B2DFD8 : Turquesa opaco
        """

        # ----------- Título del juego ------------
        Label (self.window1, text='Tic Tac Toe', fg='#1DE9B6', font=('Cambria 16 bold'), bg="black", bd=3). place (x=120, y=30)

        # ----------- Seleccion de la ficha de cada jugador -------------
        self.tipo_ficha=LabelFrame (self.window1, text="Fichas", foreground="red", font=("Cambria 11 bold"), background="black")
        self.tipo_ficha.place (x=20, y=100)

        Label (self.tipo_ficha, text="Jugador 1", foreground="white", font=("Cambria 11 bold"), background="black").grid (row=0, column=0, padx=7, pady=4)
        self.ficha1=Entry (self.tipo_ficha, width=4, justify="center", foreground="red", font=("Cambria 11 bold"), bd="4", relief=RAISED)
        self.ficha1.grid (row=1, column=0)

        Label (self.tipo_ficha, text="Jugador 2", foreground="white", font=("Cambria 11 bold"), background="black").grid (row=2, column=0, padx=7, pady=3)
        self.ficha2=Entry (self.tipo_ficha, width=4, justify="center", foreground="blue", font=("Cambria 11 bold"), bd=4, relief=RAISED)
        self.ficha2.grid (row=3, column=0, pady=2)

        # ----------- Botones de limpiar y atras -----------
        self.panel=Frame (self.window1, background="black")
        self.panel.place (x=20, y=245)

        Button (self.panel, text="Limpiar", background="blue", relief="ridge", borderwidth=1, font=("Cambria 11 bold"), fg="white", command=lambda: self.Limpiar ()).grid (row=1, column=1, sticky="WE", padx=8, pady=10)

        Button (self.panel, text="Atrás", background="blue", relief="ridge", borderwidth=1, font=("Cambria 11 bold"), fg="white", command=lambda: self.window1.destroy ()).grid (row=2, column=1, sticky="WE", padx=8, pady=10)
        
        # ----------- Contenedor del tablero ----------------
        self.content_table=Frame (self.window1, bg='black', bd=5)
        self.content_table.place (x=130, y=90)
        
        self.boton1= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (1, self.boton1, 1, self.window1))
        self.boton1.grid(row=1, column=1, padx=2, pady=2)
        
        self.boton2= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (2, self.boton2, 1, self.window1))
        self.boton2.grid(row=1, column=2, padx=2, pady=2)
        
        self.boton3= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (3, self.boton3, 1, self.window1))
        self.boton3.grid(row=1, column=3, padx=2, pady=2)
        
        self.boton4= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (4, self.boton4, 1, self.window1))
        self.boton4.grid(row=2, column=1, padx=2, pady=2)
        
        self.boton5= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (5, self.boton5, 1, self.window1))
        self.boton5.grid(row=2, column=2, padx=2, pady=2)
        
        self.boton6= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (6, self.boton6, 1, self.window1))
        self.boton6.grid(row=2, column=3, padx=2, pady=2)
        
        self.boton7= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (7, self.boton7, 1, self.window1))
        self.boton7.grid(row=3, column=1, padx=2, pady=2)
        
        self.boton8= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (8, self.boton8, 1, self.window1))
        self.boton8.grid(row=3, column=2, padx=2, pady=2)
        
        self.boton9= Button (self.content_table, text='', bg='grey', bd=5, relief='raised', width='2', font=('Arial 26 bold'), command=lambda: self.Partida (9, self.boton9, 1, self.window1))
        self.boton9.grid(row=3, column=3, padx=2, pady=2)

        self.botones=[[self.boton1, self.boton2, self.boton3], [self.boton4, self.boton5, self.boton6], [self.boton7, self.boton8, self.boton9]]

        self.mensaje_tablero = Label (self.window1, font=("Cambria 12"), background="black", width=31)
        self.mensaje_tablero.place (x=10, y=360)


    # funciones................

    def jugar (self):
        if (len(self.jugador1.get()) == 0 or len(self.jugador2.get ()) == 0):
            self.mensaje.config (text="Error: Verifique si haya ingresado los \nnombres de los jugadores \nVerifique si los nombres ingresados no \nson iguales!")

        elif self.jugador1.get () == self.jugador2.get ():
            self.mensaje.config (text="Error: Verifique si haya ingresado los \nnombres de los jugadores \nVerifique si los nombres ingresados no \nson iguales!")

        else:
            self.mensaje.configure (text="")
            self.Nombre_jugadores = (self.jugador1.get (), self.jugador2.get ())
            self.window2.destroy ()
            self.tablero ()

    def solo (self):
        if self.jugador_solo.get ():
            self.tablero ()

        else:
            messagebox.showinfo (title="Información", message="Esta jugando modo 1 jugador porfavor ingrese\n su nombre en la parte superior")

    # funciones limpiar juego........

    def Limpiar (self):
        self.finaliza = False
        self.lista=[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        self.Num_veces=0
        self.new_lista=[]
        self.ficha1.delete (0, END)
        self.ficha2.delete (0, END)
        for k in self.botones:
            for l in k:
                l.configure (text="")
        
        self.mensaje_tablero.config (text="")

    # Funciones de juego

    def Validar_space (self):
        self.new_lista=[]
        for fila in range(3):
            for columna in range (3):
                if self.lista[fila][columna] == "x" or self.lista[fila][columna] == "o":
                    continue

                else:
                    self.new_lista.append (([fila],[columna]))

    def __Fichas_validar (self):
        if self.jugadores.get () == 2:
            if self.ficha1.get ().upper() not in ['X', 'O']:
                self.mensaje_tablero.config (text="Ficha no disponible fichas permitidas\n ('X' u 'O')", foreground="red")
                return False
            else:
                return True
        
        elif self.jugadores.get () == 1:
            if self.ficha1.get ().upper() not in ['X', 'O'] or self.ficha2.get ().upper () not in ['X', 'O']:
                self.mensaje_tablero.config (text="Ficha no disponible fichas permitidas\n ('X' u 'O')", foreground="red")
                return False
            else:
                return True


    def movimiento_jugador1 (self, number, boton):
        while True:
            if not self.__Fichas_validar ():
                break
            if str(number) not in self.lista[0] and str(number) not in self.lista[1] and str(number) not in self.lista[2]:
                messagebox.askretrycancel (title="Reintentar", message="Espacio no disponible \n¿Intentar denuevo?")
                break
            
            for fila in range(3):
                for columna in range(3):
                    if self.lista[fila][columna] == str (number):
                        self.lista[fila][columna]=self.ficha1.get ()
                        #boton['text']=self.ficha1.get ()
                        boton.configure (text=self.ficha1.get ())

                        break

            break

    def movimiento_jugador2 (self, number, boton):
        while True:
            if not self.__Fichas_validar ():
                break
            if str(number) not in self.lista[0] and str(number) not in self.lista[1] and str(number) not in self.lista[2]:
                messagebox.askretrycancel (title="Reintentar", message="Espacio no disponible \n¿Intentar denuevo?")
                break

            for fila in range(3):
                for columna in range(3):
                    if self.lista[fila][columna] == str (number):
                        self.lista[fila][columna]=self.ficha2.get ()
                        boton.configure (text=self.ficha2.get ())
                    
                        break
            break

    def movimiento_compu (self, boton):
        time.sleep (.4)
        while True:
            fila=randrange(3)
            columna=randrange(3)
            if ([fila],[columna]) not in self.new_lista:
                continue

            else:
                if self.ficha1.get () == "x": compu="o"
                else: compu="x"
                self.lista[fila][columna]=compu
                self.botones[fila][columna].configure (text=compu)
                # boton.configure (text='o')

                break

    def victoria (self):
        if self.lista[0][0]==self.lista[0][1]==self.lista[0][2] or self.lista[1][0]==self.lista[1][1]==self.lista[1][2] or self.lista[2][0]==self.lista[2][1]==self.lista[2][2] or \
        self.lista[0][0]==self.lista[1][0]==self.lista[2][0] or self.lista[0][1]==self.lista[1][1]==self.lista[2][1] or self.lista[0][2]==self.lista[1][2]==self.lista[2][2] or \
        self.lista[0][0]==self.lista[1][1]==self.lista[2][2] or self.lista[0][2]==self.lista[1][1]==self.lista[2][0]:
            return True

        else:
            return False


    def Partida (self, number, boton, n, window1):
        if self.finaliza:
            return

        elif self.jugadores.get () == 2 and self.__Fichas_validar ():
            self.ficha2.configure (state="disable")

            self.movimiento_jugador1 (number, boton)
            self.Num_veces+=n
            if self.victoria ():
                self.mensaje_tablero.config (text=f"Gana {self.jugador_solo.get ()}", foreground="blue")
                self.finaliza = True
                return
                
            elif self.Num_veces == 9 and self.victoria () is False:
                self.mensaje_tablero.config (text="Juego empatado", foreground="green")
                self.finaliza = True

            else:
                self.Validar_space ()
                    
            # Movimiento de la computadora..........
            self.movimiento_compu (boton)
            self.Num_veces+=1
            if self.victoria ():
                self.mensaje_tablero.config (text="Gana Computadora", foreground="blue")
                self.finaliza = True

            else:
                self.Validar_space ()


        # Modo dos jugadores.............
        elif self.jugadores.get () == 1: 
            if self.Num_veces % 2 == 0:
                self.movimiento_jugador1 (number, boton) 
                self.Num_veces+=n

                if self.victoria ():
                    self.mensaje_tablero.config (text=f"Gana {self.Nombre_jugadores[0]}", foreground="blue") 
                    self.finaliza = True
                    
                elif self.Num_veces == 9 and self.victoria () is False:
                    self.mensaje_tablero.config (text="Juego empatado", foreground="green")
                    self.finaliza = True

                else:
                    self.Validar_space ()
                    
                return
            
            else:
                self.movimiento_jugador2 (number, boton)
                self.Num_veces+=n

                if self.victoria ():
                    self.mensaje_tablero.config (text=f"Gana {self.Nombre_jugadores[1]}", foreground="blue")
                    self.finaliza = True
                            
                elif self.Num_veces == 9 and self.victoria () is False:
                    self.mensaje_tablero.config (text="Juego empatado", foreground="green")
                    self.finaliza = True

                else:
                    self.Validar_space ()



if __name__ == '__main__':
    window= Tk()
    ventana=Tic_Tac (window)
    
    window.mainloop()
  
 