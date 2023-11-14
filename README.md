
# Tapple Store 

Este es un proyecto para la asignatura de programación II de la tecnicatura desarrollo de software, Institución Tecnologica de Río Cuarto.

La Web está diseñada con Tailwind CSS bajo el framework de Flask, en python.

<center> <h2>  Requisitos </h2>  </center>

Para ejecutar este proyecto, tiene que tener instalado Docker y docker-compose en su máquina. Docker se va a encargar de encapsular todo el proyecto, junto a el framework, librerías y dependencias para que no sea requisito instalarlas una por una. Además nos libra de archivos residuales a la hora de cerrar el proyecto. 

<center> <h2>  Instrucciones </h2>  </center>

Para ejecutar este proyecto, sigue estos pasos:


<ol>
    <li>
        Clona este repositorio en tu máquina.
    </li>
    <li>
        Abre una terminal y navega hasta la carpeta del proyecto.
    </li>
    <li>
        Ejecuta el comando <code>docker-compose up -d</code> para construir y levantar el contenedores de Flask.
    </li>
    <li>
        Espera unos segundos a que el contenedor esté listo.
    </li>
    <li>
        Abre tu navegador y dirigite a la ruta http://0.0.0.0:5055/
    </li>
</ol>

Para detener y eliminar los contenedores:
    
    docker-compose down

# Como se ve el proyecto

### Página principal

Tiene una sección principal con el producto estrella del sitio y luego una grilla de cuatro
elementos destacados del sitio web

![alt text](/app/static/appfotos/foto1.png)
![alt text](/app/static/appfotos/foto2.png)

### Secciones por productos

Cada  tipo de producto tiene su propia sección en el sitio web, todas las secciones cumplen con los mismos patrones de diseño y estructura general, mostrando todos los productos disponibles en el encabezado, seguido del producto estrella dentro de la categoría seleccionada, finalizando con una grilla de otros cuatro productos vendidos en la página.

![alt text](/app/static/appfotos/foto3.png)
![alt text](/app/static/appfotos/foto4.png)

Un ejemplo de otra categoría, en este caso la categoría de relojes.

![alt text](/app/static/appfotos/foto5.png)

### Sección de soporte humano

Dentro de la categoría soporte se encuentra un acordeón con las preguntas más frecuentes hechas por los usuarios y facilita un chat con un operador de Tapple, junto con un link que nos lleva al formulario de contacto de google forms.

![alt text](/app/static/appfotos/foto6.png)

### Sección de descarga de Tapple IA

Esta es una sección simple pero tiene sus detalles, un claro y intuitivo botón de descarga para la app y una imagen de un iphone con la app descargada.

![alt text](/app/static/appfotos/foto7.png)

### Carrito de compra

El carrito consta de 4 partes, en la foto se describe uno de los pasos. Tenemos una barra de progreso que va avanzando a medida que completamos nuestro pedido, un botón para avanzar de color azul a la derecha y uno para volver mas discreto a la izquierda. Todas las secciones de la pasarela de pago cumplen con esta organización básica y muestran información pertinente y, sobre todo, clara de lo que el usuario está haciendo con cada clic.

![alt text](/app/static/appfotos/foto8.png)


## Integrantes
<ul>
    <li>
        <a href="https://github.com/valentinoarballo">Valentino Arballo</a>
    </li>
    <li>
        <a href="https://github.com/nazabucciarelli">Nazareno Bucciarelli</a>
    </li>
    <li>
        <a href="https://github.com/FacuLemo">Facundo Lemo</a>
    </li>
    <li>
        <a href="https://github.com/LucaPetrocchi">"El Teclas"</a>
    </li>
</ul>
