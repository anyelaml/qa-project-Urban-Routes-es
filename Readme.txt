   Proyecto Urban Routes

El proyecto busca hacer las pruebas para el proceso completo de hacer una reserva de 
taxi en la web, desde introducir la ruta del trayecto, en Desde y Hasta, elegir una
tarifa, que en este caso es la tarifa comfort, ingresar un numero de telefono y de 
tarjeta de credito para hacer el pago respectivo, agregar un mensaje al conductor y
por ultimo adicionar requisitos de pedido, como son agregar manta y pañuelos y agregar
cubeta de 2 helados. para al final reservar el vehiculo.
para realizar las pruebas se necesita
PREVIAMENTE A LAS PRUEBAS
descargar los archivos a la carpeta del proyecto
verificar la instalacion de python en la terminal, con el comando python --version
haber instalado selenium y el controlador web driver para chrome.

CREACION DE ARCHIVOS

- Para una mejor organizacion en las pruebas, los localizadores necesarios y las
funciones que interactuan con estos se encuentran en la carpeta Locator dentro de
la clase UrbanRoutesPage, se hizo uso de diferentes
tipos de localizadores, entre ellos, ID, CSS SELECTOR, CLASSNAME Y XPATH
en el archivo Locator se importan la clase By del paquete selenium
el archivo data
archivo codigo
la clase web driver wait para las esperas que se utilizaran y la clase expected conditions.
- se necesita crear el archivo data.py donde se encuentran el enlace al servidor 
de urban routes, las direcciones para ingresar en los campos Desde y Hasta, el numero
de telefono, el numero de la tarjeta de credito y el codigo de la misma y el mensaje para
el conductor.
- crear el archivo main.py en donde se van a importa:
el archivo data
elwebdriver
importamos el archivo Locator donde estan los localizadores en la clase Urban Routes Page

- en el archivo Locator, en la clase Urban Routes Page se van a realizar todas
 las interacciones con los localizadores, como buscar el elemento, dar click, llenar campos,
 las esperas implicitas y otras funciones combinadas.
- en el archivo main archivo tenemos la clase TestUrbanRoutes donde se especifican todas
las pruebas del proceso de reserva de un taxi.

CREACION DE FUNCIONES

definimos la clase Urban Routes page la cual engloba la pagina principal de urban routes y 
contiene las diferentes funciones comenzando con la funcion init que contiene el driver
para las pruebas.

seguidamente, se tienen las funciones que interactuan con los diferentes elementos de la pagina
a traves de los localizadores ingresando en todas como parametro obligatorio, self.
Se crean funciones para ingresar texto, usando send_keys,  hacer click en botones, usando click y
esperas para que algunos elementos se visualicen.

tambien se definen funciones que agrupan acciones que se pueden repetir, como son el ingresar
la ruta del viaje, con set route, donde ingresamos las direcciones que se encuentran en data.
añadir un numero de telefono en add new phone number y en esta funcion 
llamamos a retrieve phone code del archivo codigo para que pueda generarnos el codigo de confirmacion 
y poder confirmar el nuevo numero de telefono.
añadir una tarjeta de credito con la funcion new credit card haciendo uso de los datos que se encuentran
en data
por ultimo, en main se tiene la clase test Urban Routes la cual contiene todas las pruebas a realizar
en el proceso de pedir un taxi.
se define para comenzar la funcion de driver para chrome

PRUEBAS A REALIZAR

- def test set route, abre la pagina de urban, e ingresa la direccion desde y hasta y confirma los valores 
ingresados.
- def test tariff picker, hace click en el boton de reserva de taxi y espera a que aparezca el recuadro 
de tarifas y selecciona la tarifa comfort para tambien confirmar que se eligio la tarifa correcta.
- def test select phone, selecciona el campo añadir telefono, e ingresa el numero que proviene del 
archivo data, hace click en siguiente para poder ingresar el codigo  de confirmacion y presiona en confirmar.
- def test new credit card, presiona en el campo añadir tarjeta, hace click en ingresar tarjeta, e 
ingresa el numero y codigo de esta que se encuentran en el archivo data. tambien presiona
en un espacio vacío de la ventana, que se encuentra al costado del CVV para poder activar el boton agregar tarjeta
y hacer click en el. para despues presionar en el boton de cerrar la ventana de agregar tarjeta.
- def test send message, busca el campo enviar mensaje al conductor e ingresa el mensaje que se
encuentra en data
- def test blanket, activa el boton de manta y pañuelos para luego comprobar que se haya
desplazado el botón.
- def test add ice cream, hace click dos veces en el contador de añadir helado
- def test click reserve taxi, encuentra el boton para reservar taxi y lo presiona para comprobarlo espera a que aparezca
la ventana de detalles de reserva.
- def test driver info, esta funcion espera a que aparezca la ventana de detalles de reserva, donde aparece el temporizador.
finalmente tenemos la funcion def teardown class, la que cierra la pantalla y finaliza las pruebas.

Posterior a escribir las pruebas, las podemos correr a traves de current file colocandonos en el archivo main.py,
tambien podemos ubicarnos en main.py y presionar el boton verde que se encuentra junto a class TestUrbanRoutes
y seleccionar Run.