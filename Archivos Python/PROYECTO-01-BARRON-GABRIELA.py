"""
Este archivo es el que despliega la GUI, el usuario para ingresar es usuario y la contraseña es contraseña
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
#importamos  del archivo lifestore_consignas las variables que usaremos
from lifestore_consignas import lista_top_ventas, lista_top_busqueda,lista_top_reseña, lista_top_categoria, lista_categorias, lista_años, ventas_año

#definimos la funcion de login
def login():
    #tomamos los valores que se ingresaron de usuario y contraseña
    uname=username.get()
    pwd=password.get()
    #validaciones 
    if uname=='' or pwd=='': #si no se llenaron los espacios mandamos mensaje
        message.set("Llena el espacio vacío")
    else: 
      if uname=="usuario" and pwd=="contraseña": #si el usuario y contraseña son los correctos
        reporte()
      else: #si no, mandamos mensaje 
       message.set("Usuario y/o contraseña incorrectos")
       
#funcion ventana de login
def Loginform():
    global login_screen #definimos variable global para una ventana
    login_screen = tk.Tk()
    #Titulo o nombre de la ventana
    login_screen.title("Inicio Sesión")
    #Definimos el tamaño de la ventana
    login_screen.geometry("300x250")
    #declaramos las varaibles a usar
    global  message;
    global username
    global password
    username = StringVar() #definimos entradas 
    password = StringVar()
    message=StringVar()
    #Diseño de la ventana
    tk.Label(login_screen,width="300", text="Ingrese su usuario y contraseña").pack()
    tk.Label(login_screen, text="Usuario * ").place(x=20,y=40)#Etiqueta de usuario, def posicion
    tk.Entry(login_screen, textvariable=username).place(x=90,y=42) #Caja de texto donde se escribe el usuario
    tk.Label(login_screen, text="Contraseña * ").place(x=20,y=80) #Etiqueta de contraseña, def posicion
    tk.Entry(login_screen, textvariable=password ,show="*").place(x=90,y=82) #Caja de texto donde se escribe la contraseña
    tk.Label(login_screen, text="",textvariable=message).place(x=95,y=100) #Etiqueta, despliega la validacion de los datos ingresados 
    tk.Button(login_screen, text="Aceptar", width=10, height=1,command=login).place(x=105,y=130) #Boton para validar login, def posicion
    login_screen.mainloop()
    
    

#funcion ventana reporte
def reporte():
    #Funciones que desplegaran las tablas a visualizar
    def top_ventas(): #funcion top ventas
        lista_top_ventas.sort(key = lambda x: x[2], reverse= True) #ordenamos nuestra lista en orden descendente conforme al atributo total ventas
        tk.Label(ventana, text="   PRODUCTOS MÁS VENDIDOS    ", font=("Arial",15)).grid(row=0, columnspan=3) #Etiqueta, def posicion
        cols = (['',40], ['Id',40],['Nombre',600], ['Total ventas',100]) #Definimos el tamaño que tendra cada columna 
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20)  #Definimos la tabla que se desplegara, def tamaño 
        for i, (id_, name, score) in enumerate(lista_top_ventas, start=1):  #Llenado de tabla
              listBox.insert("", "end", values=(i, id_, name, score))
              if i == 10: #condicion de paro
                break
        for col in cols:  #Imprime tabla
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)   

    def top_busquedas(): #funcion top busquedas
        lista_top_busqueda.sort(key = lambda x: x[2], reverse= True) #ordenamos nuestra lista en orden descendente conforme al atributo total busquedas
        tk.Label(ventana, text="   PRODUCTOS MÁS BUSCADOS    ", font=("Arial",15)).grid(row=0, columnspan=3) #Etiqueta, def posicion
        cols = (['',40], ['Id',40],['Nombre',500], ['Total busquedas',200]) #Definimos el tamaño que tendra cada columna 
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) #Definimos la tabla que se desplegara, def tamaño
        for i, (id_, name, score) in enumerate(lista_top_busqueda, start=1): #Llenado de tabla
            listBox.insert("", "end", values=(i, id_, name, score))
            if i == 10: #condicion de paro
              break
        for col in cols:  #Imprime tabla
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)
     
    def top_reseña(): #funcion top reseña (mayor)
        #ordenamos nuestra lista de forma descendente, tomando como primer parametro el promedio de score, despues por el numero de ventas
        lista_top_reseña.sort(key = lambda x: (x[2],x[3]), reverse= True) #Etiqueta, def posicion
        tk.Label(ventana, text="PRODUCTOS CON MEJOR RESEÑA", font=("Arial",15)).grid(row=0, columnspan=3) #Etiqueta, def posicion
        cols = (['',30], ['Id',30],['Nombre',500], ['Score',60],['Ventas',60],['Devoluciones',100]) #Definimos el tamaño que tendra cada columna
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20) #Definimos la tabla que se desplegara, def tamaño
        for i, (id_, name, score,ventas, devoluciones) in enumerate(lista_top_reseña, start=1): #Llenado de tabla
            listBox.insert("", "end", values=(i,id_, name, score,ventas, devoluciones))
            if i == 20: #condicion de paro
              break
        for col in cols: #Imprime tabla
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)

    def top_reseña2(): #funcion top reseña (menor)
        #ordenamos nuestra lista de forma ascendente, tomando como primer parametro el promedio de score, despues por el numero de ventas
        lista_top_reseña.sort(key = lambda x: (x[2],x[3]), reverse= False)  
        tk.Label(ventana, text="PRODUCTOS CON PEOR RESEÑA", font=("Arial",15)).grid(row=0, columnspan=3) #Etiqueta, def posicion
        cols = (['',30], ['Id',30],['Nombre',500], ['Score',60],['Ventas',60],['Devoluciones',100]) #Definimos el tamaño que tendra cada columna
        listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20)  #Definimos la tabla que se desplegara, def tamaño
        for i, (id_, name, score,ventas, devoluciones) in enumerate(lista_top_reseña, start=1):  #Llenado de tabla
            listBox.insert("", "end", values=(i,id_, name, score,ventas, devoluciones))
            if i == 20: #condicion de paro
              break
        for col in cols: #Imprime tabla
            listBox.heading(col[0], text=col[0])  
            listBox.column(col[0], width=col[1])   
        listBox.grid(row=1, column=0, columnspan=2)
    """
    Esta funcion es un tanto particular, ya que vamos a llamarla conforme a la eleccion que se ingrese de un menu
    tipo cascada para desplegar la tabla correspondiente a la categoria elegida.
    """
    def top_categoria(): #funcion top por categoría
      indice = 0 #variable para guardar el indice de la opcion que se escogio 
      categoria = categoria_sel.get() #asignamos a la variable la opcion que se escogio
      for cat in lista_top_categoria: #bucle, para buscar el indice exacto en donde esta la opcion que se escogio 
        if cat[0] == categoria: #condicion, si categoria en cat = a categoria que se ingreso
          indice = lista_top_categoria.index(cat) #asignamos el indice exacto en el que se encuentra
        else: #si no se cumple pasamos a la siguiente iteracion
          continue
      tk.Label(ventana, text="                     "+categoria+"                    ", font=("Arial",15)).grid(row=0, columnspan=3) #Etiqueta, def posicion
      cols = (['',30], ['Id',30],['Nombre',510], ['Ventas',70],['Busquedas',70],['Stock',70]) #Definimos el tamaño que tendra cada columna
      listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20)#Definimos la tabla que se desplegara, def tamaño
      for i, (id_, name, ventas, busquedas, stock) in enumerate(lista_top_categoria[indice][1], start=1): #Llenado de tabla
          listBox.insert("", "end", values=(i, id_, name,ventas, busquedas, stock))
          
      for col in cols: #Imprime tabla
          listBox.heading(col[0], text=col[0])  
          listBox.column(col[0], width=col[1])   
      listBox.grid(row=1, column=0, columnspan=2)

    """
    Esta funcion aplica la misma logica que la anterior, primero haremos una eleccion del menu tipo cascada, para posteriormente
    llamar a la funcion y desplegar la tabla correspondiende conforme al indice de la opcion que se eligio.
    """
    def ingreso_anual(): #funcion ingresos mensuales
      indice = 0 #variable para guardar el indice de la opcion que se escogio 
      año = año_sel.get() #asignamos a la variable la opcion que se escogio
      for year in ventas_año: #bucle, para buscar el indice exacto en donde esta la opcion que se escogio 
        if str(year[0]) == str(año): #condicion, si año en year = a año elegido por el usuario
          indice = ventas_año.index(year) #asignamos el indice exacto en el que se encuentra
        else: #si no se cumple pasamos a la siguiente iteracion
          continue
    #definimos una lista para dar mejor visibilidad a los meses
      meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
      tk.Label(ventana, text="  INGRESO MENSUAL AÑO:  "+ año , font=("Arial",15)).grid(row=0, columnspan=3) #Etiqueta, def posicion
      cols = (['Mes',390], ['Ingreso mensual',390]) #Definimos el tamaño que tendra cada columna
      listBox = ttk.Treeview(ventana, columns=[x[0] for x in cols], show='headings', heigh = 20)  #Definimos la tabla que se desplegara, def tamaño
      for i, (mes, ingresos) in enumerate(ventas_año[indice][2], start=1): #Llenado de tabla
          listBox.insert("", "end", values=(meses[i-1], ingresos))
          
      for col in cols: #Imprime tabla
          listBox.heading(col[0], text=col[0])  
          listBox.column(col[0], width=col[1])   
      listBox.grid(row=1, column=0, columnspan=2)
      #tk.Label(ventana, text="Total anual: "+ str(ventas_año[indice][1]), font=("Arial",15)).grid(row=22, columnspan=3)

    #desplegando ventana con menu de opciones para desplegar tablas
    global ventana
    login_screen.state(newstate = "withdraw") #una vez que el login es exitoso, suspendemos la ventana login y mostramos la ventana de reporte
    ventana = tk.Tk() #asignamos la variable ventana 
    ventana.title("Reporte Lifestore") #Asignamos titulo a ventana
    ventana.geometry("800x500") #tamaño de ventana


    categoria_sel = tk.StringVar(ventana) #definimos una variable para la seleccion de categorias 
    categoria_sel.set(lista_categorias[0]) #le damos un valor default

    reseña_sel = tk.StringVar(ventana) #definimos una variable para la seleccion de categorias 
    reseña_sel.set(lista_categorias[0]) #le damos un valor default

    año_sel = tk.StringVar(ventana) #definimos una variable para la seleccion de categorias 
    año_sel.set(lista_años[0]) #le damos un valor default

    menu_lifestore = tk.Menu(ventana) #asignamos a una variable al menu de opciones
    categoria_menu = tk.Menu(menu_lifestore, tearoff = 0) #menu tipo cascada o submenu para la lista de categorias 
    for categoria in lista_categorias: #asignamos las etiquetas al submenu de categorias
      categoria_menu.add_radiobutton(label = categoria, value = categoria, variable = categoria_sel, command = top_categoria )

    menu_reseña = tk.Menu(menu_lifestore, tearoff = 0) #menu tipo cascada o submenu para las opciones top reseña
    #asignamos las etiquedas al submenu de reseña
    menu_reseña.add_radiobutton(label = 'Mejor reseña', value = 'Mejor reseña', variable = reseña_sel, command = top_reseña)
    menu_reseña.add_radiobutton(label = 'Peor reseña', value = 'Peor reseña', variable = reseña_sel, command = top_reseña2)

    año_menu = tk.Menu(menu_lifestore, tearoff = 0) #menu tipo cascada o submenu para los años
    for año in lista_años: #asignamos las etiquedas al submenu de año
      año_menu.add_radiobutton(label = año, value = año, variable = año_sel, command = ingreso_anual )

    ventana.config(menu = menu_lifestore) #condiguramos la ventana y le asignamos el menu 

    #comandos que realiza cada pestaña del menu, aqui se llama a las funciones que definimos arriba 
    menu_lifestore.add_command(label = 'Top Ventas', command=top_ventas )
    menu_lifestore.add_command(label = 'Top Busquedas', command=top_busquedas)
    menu_lifestore.add_cascade(label = 'Top por Categoria', menu = categoria_menu)
    menu_lifestore.add_cascade(label = 'Top por Reseña', menu = menu_reseña)
    menu_lifestore.add_cascade(label = 'Ingresos anuales', menu = año_menu)
    menu_lifestore.add_command(label = 'Salir', command = exit)
    
    
    ventana.mainloop()
    
#llamamos a la funcion loginform()
Loginform()
