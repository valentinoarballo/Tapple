# Tapple Store 

Este es un proyecto para la asignatura de programacion II de la tecnicatura desarrollo de software, institucion tecnologica de rio cuarto .

La Web esta diseñada con Tailwind CSS bajo el framework de Flask, en python.

<center> <h2>  Requisitos </h2>  </center>

Para ejecutar este proyecto, tiene que tener instalado Docker y docker-compose en su máquina, solo eso. Docker se va a encargar de encapsular todo el proyecto, junto a el framework, librerias y dependencias para que no sea requisito instalarlas una por una, ademas nos libra de archivos residuales a la hora de detener el proyecto. 

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
        Ejecuta el comando <code>docker-compose up -d</code> para construir y levantar los contenedores de Flask y MySQL.
    </li>
    <li>
        Espera unos segundos a que el contenedor esté listo.
    </li>
    <li>
        Abri tu navegador y dirigite a la ruta http://0.0.0.0:5055/
    </li>
</ol>

Para detener y eliminar los contenedores:
    
    docker-compose down

# Como se ve el proyecto

### pagina principal

Tiene una seccion principal con el producto estrella del sitio y luego una grilla de cuatro
elementos destacados del sitio web

![alt text](/app/static/appfotos/foto1.png)
![alt text](/app/static/appfotos/foto2.png)

### Secciones por productos

Cada  tipo de producto tiene su propia seccion en el sitio web, todas las secciones cumplen con los mismos patrones de diseño y estructura general, mostrando todos los productos disponibles en el encabezado, seguido del producto estrella dentro de la categoria seleccionada, finalizando con una grilla de otros cuatro productos vendidos en la pagina.

![alt text](/app/static/appfotos/foto3.png)
![alt text](/app/static/appfotos/foto4.png)

Un ejemplo de otra categoria, en este caso la categoria de relojes.

![alt text](/app/static/appfotos/foto5.png)

### Seccion de soporte humano

Desntro de la categoria soporte se encuentra un acordion con las preguntas mas frecuentes hechas por los usuarios y facilita un chat con un operador de Tapple, junto con un link que nos lleva al formulario de contacto de google forms.

![alt text](/app/static/appfotos/foto6.png)

### Seccion de descarga de Tapple IA

Esta es una seccion simple pero tiene sus detalles, un claro y intuitivo boton de descarga para la app y una imagen de un iphone con la app descargada.

![alt text](/app/static/appfotos/foto7.png)

### Carrito de compra

El carrito consta de 4 partes, esta es una de ellas, tenemos una barra de progreso que va avanzando a medida que completamos nuestro pedido, un boton para avanzar de color azul a la derecha y uno para volver mas discreto a la izquierda, todas las secciones de la pasarela de pago cumplen con esta organizacion basica y muestran informacion pertinente y sobre todo clara de lo que el usuario esta haciendo con cada clic.

![alt text](/app/static/appfotos/foto8.png)

## Integrantes
<ul>
    <li>
        <a href="">Valentino Arballo</a>
    </li>
    <li>
        <a href="">Nazareno Bucciarelli</a>
    </li>
    <li>
        <a href="">Facundo Lemo</a>
    </li>
    <li>
        <a href="">"El Teclas"</a>
    </li>
</ul>
