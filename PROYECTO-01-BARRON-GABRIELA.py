from tkinter import *
import tkinter as tk
from tkinter import ttk
from lifestore_consignas import lista_top_ventas, lista_top_busqueda,lista_top_reseña, lista_top_categoria, lista_categorias, lista_años, ventas_año

#defining login function
def login():
    #getting form data
    uname=username.get()
    pwd=password.get()
    #applying empty validation
    if uname=='' or pwd=='':
        message.set("Llena el espacio vacío")
    else:
      if uname=="usuario" and pwd=="contraseña":
        reporte()
      else:
       message.set("Usuario y/o contraseña incorrectos")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = tk.Tk()
    #Setting title of screen
    login_screen.title("Inicio Sesión")
    #setting height and width of screen
    login_screen.geometry("300x250")
    #declaring variable
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Creating layout of login form
    tk.Label(login_screen,width="300", text="Ingrese su usuario y contraseña").pack()
    #Username Label
    tk.Label(login_screen, text="Usuario * ").place(x=20,y=40)
    #Username textbox
    tk.Entry(login_screen, textvariable=username).place(x=90,y=42)
    #Password Label
    tk.Label(login_screen, text="Contraseña * ").place(x=20,y=80)
    #Password textbox
    tk.Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82)
    #Label for displaying login status[success/failed]
    tk.Label(login_screen, text="",textvariable=message).place(x=95,y=100)
    #Login button
    tk.Button(login_screen, text="Aceptar", width=10, height=1,command=login).place(x=105,y=130)
    login_screen.mainloop()
    
    


def reporte():
    def top_ventas():
        lista_top_ventas.sort(key = lambda x: x[2], reverse= True) #ordenamos nuestra lista en orden descendente conforme al atributo total ventas
        tk.Label(ventana, text="   PRODUCTOS MÁS VENDIDOS    ", font=("Arial",15)).grid(row=0, columnspan=3)
        cols = (['',40], ['Id',40],['Nombre',600], ['Total ventas',100])
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) 
        for i, (id_, name, score) in enumerate(lista_top_ventas, start=1):
              listBox.insert("", "end", values=(i, id_, name, score))
              if i == 20:
                break
        for col in cols:
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)   

    def top_busquedas():
        lista_top_busqueda.sort(key = lambda x: x[2], reverse= True) #ordenamos nuestra lista en orden descendente conforme al atributo total busquedas
        tk.Label(ventana, text="   PRODUCTOS MÁS BUSCADOS    ", font=("Arial",15)).grid(row=0, columnspan=3)
        cols = (['',40], ['Id',40],['Nombre',500], ['Total busquedas',200])
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) 
        for i, (id_, name, score) in enumerate(lista_top_busqueda, start=1):
            listBox.insert("", "end", values=(i, id_, name, score))
            if i == 20:
              break
        for col in cols:
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)
     
    def top_reseña():
        #ordenamos nuestra lista de forma descendente, tomando como primer parametro el promedio de score, despues por el numero de ventas
        lista_top_reseña.sort(key = lambda x: (x[2],x[3]), reverse= True) 
        tk.Label(ventana, text="PRODUCTOS CON MEJOR RESEÑA", font=("Arial",15)).grid(row=0, columnspan=3)
        cols = (['',30], ['Id',30],['Nombre',500], ['Score',60],['Ventas',60],['Devoluciones',100])
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) 
        for i, (id_, name, score,ventas, devoluciones) in enumerate(lista_top_reseña, start=1):
            listBox.insert("", "end", values=(i,id_, name, score,ventas, devoluciones))
            if i == 20:
              break
        for col in cols:
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)

    def top_reseña2():
        #ordenamos nuestra lista de forma descendente, tomando como primer parametro el promedio de score, despues por el numero de ventas
        lista_top_reseña.sort(key = lambda x: (x[2],x[3]), reverse= False) 
        tk.Label(ventana, text="PRODUCTOS CON PEOR RESEÑA", font=("Arial",15)).grid(row=0, columnspan=3)
        cols = (['',30], ['Id',30],['Nombre',500], ['Score',60],['Ventas',60],['Devoluciones',100])
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) 
        for i, (id_, name, score,ventas, devoluciones) in enumerate(lista_top_reseña, start=1):
            listBox.insert("", "end", values=(i,id_, name, score,ventas, devoluciones))
            if i == 20:
              break
        for col in cols:
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)

    def top_categoria():
      indice = 0
      categoria = categoria_sel.get()
      for cat in lista_top_categoria:
        if cat[0] == categoria:
          indice = lista_top_categoria.index(cat)
        else: 
          continue
      tk.Label(ventana, text="                     "+categoria+"                    ", font=("Arial",15)).grid(row=0, columnspan=3)
      cols = (['',30], ['Id',30],['Nombre',510], ['Ventas',70],['Busquedas',70],['Stock',70])
      listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) 
      for i, (id_, name, ventas, busquedas, stock) in enumerate(lista_top_categoria[indice][1], start=1):
          listBox.insert("", "end", values=(i, id_, name,ventas, busquedas, stock))
          
      for col in cols:
          listBox.heading(col[0], text=col[0])  
          listBox.column(col[0], width=col[1])   
      listBox.grid(row=1, column=0, columnspan=2)

    def ingreso_anual():
      indice = 0
      año = año_sel.get()
      for year in ventas_año: 
        if str(year[0]) == str(año):
          indice = ventas_año.index(year)
        else: 
          continue
      meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
      tk.Label(ventana, text="  INGRESO MENSUAL AÑO:  "+ año , font=("Arial",15)).grid(row=0, columnspan=3)
      cols = (['Mes',390], ['Ingreso mensual',390])
      listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) 
      for i, (mes, ingresos) in enumerate(ventas_año[indice][2], start=1):
          listBox.insert("", "end", values=(meses[i-1], ingresos))
          
      for col in cols:
          listBox.heading(col[0], text=col[0])  
          listBox.column(col[0], width=col[1])   
      listBox.grid(row=1, column=0, columnspan=2)
      #tk.Label(ventana, text="Total anual: "+ str(ventas_año[indice][1]), font=("Arial",15)).grid(row=22, columnspan=3)

    
    global ventana
    login_screen.state(newstate = "withdraw")
    ventana = tk.Tk()
    ventana.title("Reporte Lifestore")
    ventana.geometry("800x500") 


    categoria_sel = tk.StringVar(ventana)
    categoria_sel.set(lista_categorias[0])

    reseña_sel = tk.StringVar(ventana)
    reseña_sel.set(lista_categorias[0])

    año_sel = tk.StringVar(ventana)
    año_sel.set(lista_años[0])

    menu_lifestore = tk.Menu(ventana)
    categoria_menu = tk.Menu(menu_lifestore, tearoff = 0)
    for categoria in lista_categorias:
      categoria_menu.add_radiobutton(label = categoria, value = categoria, variable = categoria_sel, command = top_categoria )

    menu_reseña = tk.Menu(menu_lifestore, tearoff = 0)
    menu_reseña.add_radiobutton(label = 'Mejor reseña', value = 'Mejor reseña', variable = reseña_sel, command = top_reseña)
    menu_reseña.add_radiobutton(label = 'Peor reseña', value = 'Peor reseña', variable = reseña_sel, command = top_reseña2)

    año_menu = tk.Menu(menu_lifestore, tearoff = 0)
    for año in lista_años:
      año_menu.add_radiobutton(label = año, value = año, variable = año_sel, command = ingreso_anual )

    ventana.config(menu = menu_lifestore)
    
    menu_lifestore.add_command(label = 'Top Ventas', command=top_ventas )
    menu_lifestore.add_command(label = 'Top Busquedas', command=top_busquedas)
    menu_lifestore.add_cascade(label = 'Top por Categoria', menu = categoria_menu)
    menu_lifestore.add_cascade(label = 'Top por Reseña', menu = menu_reseña)
    menu_lifestore.add_cascade(label = 'Ingresos anuales', menu = año_menu)
    menu_lifestore.add_command(label = 'Salir', command = exit)
    
    
    ventana.mainloop()
    
#calling function Loginform
Loginform()
