from lifestore_file import lifestore_searches
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_products
from datetime import datetime


"""
Lista de productos mas vendidos
-------------------------------
Se crearon dos bubles for, uno para recorrer cada producto y el segundo anidado 
al antes mencionado para contar cuantas veces se repite cada producto en la lista de ventas, y asi, tener el total de ventas para cada producto.
"""
lista_top_ventas = [] #Definimos una nueva lista que contendra el total de ventas por producto 
for producto in lifestore_products:  #Vamos a recorrer la lista de productos tomando en cada iteracion el atributo id_product
    veces = 0 #inicilizamos el contador de ventas
    for venta in lifestore_sales:#Recorremos la lista de busquedas para ver cuantas veces se repite cada id_product
        if producto[0] == venta[1]: #condicion, si id_product en producto es igual al id_product de venta
            veces += 1  #si se cumple actualizamos nuestro contador
    lista_top_ventas.append([producto[0],producto[1][0:producto[1].index(',')],veces]) #agregamos valores a la lista -> lista_top_ventas = [id_product, name, total ventas]
       

"""
Lista de productos mas buscados
-------------------------------
Se crearon dos bucles for, uno para recorrer cada producto y el segundo anidado 
al antes mencionado para contar cuantas veces se repite cada producto en la lista de busquedas, y asi, tener el total de busquedas para cada producto.
"""
lista_top_busqueda = [] #Definimos una nueva lista que contendrá el total de busquedas por producto
for producto in lifestore_products: #Vamos a recorrer la lista de productos tomando en cada iteracion el atributo id_product
    veces = 0 #inicilizamos el contador de busquedas
    for busqueda in lifestore_searches: #Recorremos la lista de busquedas para ver cuantas veces se repite cada id_product
        if producto[0] == busqueda[1]: #condicion, si id_product en producto es igual al id_product de busqueda 
            veces += 1 #si se cumple actualizamos nuestro contador
    lista_top_busqueda.append([producto[0], producto[1][0:producto[1].index(',')], veces]) #agregamos valores a la lista -> lista_top_busqueda = [id_product, name, total busquedas]


"""
Top de ventas y busquedas de productos por categoria
----------------------------------------
Antes de separar los productos por categoria, haremos una lista que guarde el id_producto, name, total ventas y total busquedas para despues poder clasificar por categoria.
Para encontrar el total de ventas y busquedas por categoria, es necesario saber que categorias hay por lo que primero ordenamos la lista de productos tomando como atributo "category".
Una vez que tenemos la lista ordenada, recorreremos dicha lista tomando la frecuencia con la que se repite la palabra en el atributo "category" como auxiliar para saber cuantos indices
debemos saltar para pasar a la siguiente categoria.
Mientras recorremos la lista por categoria, iremos contabilizando el numero de ventas por producto y el total por categoria.
"""
           
lista_ord_top_ventas = sorted(lista_top_ventas, key = lambda x: x[0]) #ordenamos la lista que obtuvimos en "Lista de productos mas vendidos" tomando id_product como parametro de ordenamiento 
lista_ord_top_busqueda = sorted(lista_top_busqueda, key = lambda x: x[0]) #ordenamos la lista que obtuvimos en "Lista de productos mas buscados" tomando id_product como parametro de ordenamiento 
lista_ventas_busqueda = [] #Definimos una lista en la que guardaremos las ventas y busquedas totales de cada producto. 
for producto in lista_ord_top_ventas: #Usaremos la lista que sacamos en los productos mas vendidos para generar esta nueva lista.
    #agregamos datos a la lista -> lista_ventas_busqueda = [id_product, name, total ventas, total busquedas]
    lista_ventas_busqueda.append([producto[0],producto[1], producto[2], lista_ord_top_busqueda[producto[0]-1][2]]) 
    
#vamos a iniciar el proceso para ordenar por categoria.
j = 0 #contador, nos ayudara a recorrer la lista de productos para posicionarnos en las diferentes categorias que hay
lista_categorias = []  
lista_ord_prod = sorted(lifestore_products, key = lambda x: x[3]) #creamos una nueva lista, la cual contiene la lista lifestore_products ordenada conforme al atributo category
lista_top_categoria = [] #Definimos una lista que contendra el total de busquedas por categoria y las busquedas por producto
while j <= len(lista_ord_prod)-1: #Bucle while que nos ayudara a recorrer la lista ya ordenada de productos 
    lista_prod_in_cat = [] #Definimos una lista que contendra los productos que hay en cada categoria
    busqueda_categoria = 0 #Inicializamos un contador para las busquedas totales por categoria 
    ventas_categoria = 0 #Inicializamos un contador para las ventas totales por categoria 
    frecuencia = sum(x.count(lista_ord_prod[j][3]) for x in lista_ord_prod) #Para saber cuantas veces se repite la categoria hacemos un conteo con ayuda de la funcion count(), asi sabemos cuantos indices debemos saltar para pasar a la siguiente categoria
    for i in range(frecuencia): #Bucle for que recorrera cada producto que esta en la categoria actual.
        #agregamos valores a la lista -> lista_prod_in_cat=[id_product, name,total ventas, total busquedas, stock]
        lista_prod_in_cat.append([lifestore_products[lista_ord_prod[j][0]-1][0], lista_ventas_busqueda[lista_ord_prod[j][0]-1][1], lista_ventas_busqueda[lista_ord_prod[j][0]-1][2],lista_ventas_busqueda[lista_ord_prod[j][0]-1][3],lifestore_products[lista_ord_prod[j][0]-1][4] ])
        busqueda_categoria += lista_ventas_busqueda[lista_ord_prod[j][0]-1][3] #Actualizamos el contador de busquedas totales por categoria
        ventas_categoria += lista_ventas_busqueda[lista_ord_prod[j][0]-1][2] #Actualizamos el contador de ventas totales por categoria
        j += 1 #Actualizamos nuestro contador que recorre la lista
        lista_prod_in_cat.sort(key = lambda x: (x[2],x[3]), reverse = False) #Una vez terminamos de recorrer la lista por la categoria actual, ordenamos la lista de productos por categoria en forma ascendente tomando como parametro el total de busquedas
    lista_categorias.append(lista_ord_prod[j-1][3]) #agregamos categoria a la lista
    #agregamos valores a la lista -> lista_busqueda_categoria =[categoria, lista_prod_in_cat,total ventas por categoria,total busquedas por categoria] 
    lista_top_categoria.append([lista_ord_prod[j-1][3], lista_prod_in_cat, ventas_categoria, busqueda_categoria]) 
"""
Lista de productos mejor/peor rankeados
----------------------------------
Para tener la lista de productos por reseña, se tomo el promedio de la suma total del 'score' de cada producto, para poder obtener ese promedio
hicimos uso de dos bubles for, uno para recorrer la lista lifestore_products, dentro recorreremos la lista lifestore_sales, para asi ir contabilizando
cuantas veces se vendio el producto (y asi poder obtener el promedio) y que score se le dio. Como dato adicional vamos a tomar en cuenta el total de devoluciones
para el analisis posterior.
"""

lista_top_reseña = [] #Definimos la lista donde guardaremos el promedio de score
for producto in lifestore_products: #Vamos a recorrer la lista lifestore_products producto a producto
    veces = 0 #Inicializamos nuestro contador de ventas 
    suma = 0 #Inicializamos nuestro contador del score
    devoluciones = 0 #Inicializamos nuestro contador para las devoluciones 
    for reseña in lifestore_sales: #Recorreremos la lista lifestore_sales para tomar los datos de scrore y refund
        if producto[0] == reseña[1]: #Condicion, si el id_product de lifestore_products es el mismo al de lifestore_sales
            veces += 1 #En caso de que se cumpla la condicion, actualizamos nuestro contador de ventas
            suma += reseña[2] #Actualizamos nuestro contador de score
            devoluciones += reseña[4] #Actualizamos el contador de devoluciones
    if veces == 0: #Una vez que terminamos de recorrer la lista lifestore_sales para el id_producto actual hacemos una condicion ya que no tiene sentido rankear por score productos que no tienen ventas
        continue
    else: #En otro caso hacamos la operacion para sacar el promedio
        promedio = round(suma/veces,2) 
#agregamos valores a la lista -> lista_top_reseña = [id_product, name, promedio score, total ventas, total devoluciones]  
    lista_top_reseña.append([producto[0],producto[1][0:producto[1].index(',')], promedio, veces, devoluciones])
    
"""
Total ingresos anual y mensual.
-------------------------------
Para encontrar el total de ingresos mensual y anual lo primero que se hizo fue acomodar una lista por año de menor a mayor, despues se fue recorriendo
la lista por año con un ciclo while, dentro del bucle hay un ciclo for en el que se recorre mes por mes para poder ir tomando el conteo mensual de ingresos, una vez que se sale de ese bucle
se toma el conteo anual.

"""   
lista_año = sorted(lifestore_sales,key=lambda date: datetime.strptime(date[3], '%d/%m/%Y')) #creamos una lista con las fechas ordenadas de forma ascendente
año = int(lista_año[0][3][6:10]) #Definimos año que ira recorriendo la lista, en este caso sera año que esta en el primer elemento de la lista
año_fin = int(lista_año[len(lista_año)-1][3][6:10]) #Definimos el año en el que termina la lista
ventas_año = [] #Definimos la lista que tendra las ventas anuales y mensuales
lista_años = [] #Definimos una lista para guardar los años
total_ingresos = 0 #Definimos la variable que tendra el total de ingresos
while año <= año_fin: #El primer bucle sera por año
    ventas_mes = [] #Definimos la lista para las ventas mensuales de cada año
    sum_año_venta = 0 #Inicializamos nuestro contador para la suma de ventas anuales
    for mes in range(1,13): #Segundo bucle que recorrera mes por mes
        sum_mes_venta = 0 #Inicializamos nuestro contador para la suma de ventas mensual
        fecha = str(mes) + '/' + str(año) #Definimos la cadena de fecha a buscar en la lista lifestore_sales
        for producto in lifestore_sales: #Con la fecha definida, recorremos la lista de ventas para encontrar las ventas mensuales y anuales.
            if fecha in producto[3] and producto[4] == 0: #Condicion, si el valor de fecha esta en el indice de la lista y no hay devolucion
                sum_mes_venta += lifestore_products[producto[1]-1][2] #Actualizacion nuestro contador de ventas mensual
        ventas_mes.append([mes, sum_mes_venta]) #Agregamos valores a la lista -> ventas_mes = [mes, ingreso mensual]
        sum_año_venta += sum_mes_venta #actualizamos la suma de ventas anuales
    
    lista_años.append(año) #Agregamos el año actual a la lista de años.
    ventas_año.append([año, sum_año_venta, ventas_mes]) #Agregamos valores a la lista -> ventas_año = [año, ingreso anual, ventas_mes]
    año += 1 #actualizamos nuestro indice para el año
    total_ingresos += sum_año_venta #Actualizamos el total de ingresos
    
