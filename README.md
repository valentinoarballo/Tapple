# API de Flask con Docker y MySQL

Este proyecto es una API de Flask que usa Docker y MySQL para crear y gestionar usuarios, publicaciones, temas y comentarios. La API permite hacer operaciones CRUD (crear, leer, actualizar y borrar) sobre estos recursos, usando diferentes endpoints y métodos HTTP.

La API también usa SQLAlchemy y Marshmallow para facilitar el trabajo con la base de datos y la serialización y deserialización de los datos.

<center> <h1>  Requisitos </h1>  </center>

Para ejecutar este proyecto, tenes que tener instalado Docker y docker-compose en tu máquina. 

También necesitas tener un archivo .env con las variables de entorno necesarias para la configuración de la aplicación y la base de datos. 

    Un ejemplo de este archivo es el siguiente:

`SQLALCHEMY_DATABASE_URI=mysql+pymysql://user:root@mysql:3306/db`

`MYSQL_PASSWORD=root`

`MYSQL_USER=user`

`MYSQL_DATABASE=db`


<center> <h1>  Instrucciones </h1>  </center>

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
        Espera unos segundos a que los contenedores estén listos y la base de datos se inicialice.
    </li>
    <li>
        Abri tu cliente HTTP y prueba los endpoints de la API.
        
Por ejemplo, puedes hacer una petición <strong>GET</strong> a http://0.0.0.0:5055/users para obtener la lista de usuarios.

O una petición <strong>POST</strong> a http://0.0.0.0:5055/temas para crear un nuevo tema.
    </li>
</ol>

    Para detener y eliminar los contenedores:
`docker-compose down`

<center> <h1>  Endpoints </h1>  </center>

    La API tiene los siguientes endpoints:

`/usuarios` Permite crear y obtener usuarios.

`/usuarios/<user_id>` Permite obtener, actualizar y eliminar un usuario por su id.

`/publicaciones` Permite crear y obtener publicaciones.

`/publicaciones/<publicacion_id>` Permite obtener y eliminar una publicación por su id.

`/temas` Permite crear y obtener temas.

`/temas/<tema_id>` Permite obtener y eliminar un tema por su id.

`/comentarios` Permite crear y obtener comentarios.

`/comentarios/<comentario_id>` Permite obtener y eliminar un comentario por su id.

Los métodos HTTP que se pueden usar en cada endpoint son los siguientes:

<strong>GET</strong>: Para obtener uno o más recursos.

<strong>POST</strong>: Para crear un nuevo recurso.

<strong>PUT</strong>: Para actualizar un recurso existente.

<strong>DELETE</strong>: Para eliminar un recurso existente.

Los datos que se envían y reciben en las peticiones y respuestas son de tipo JSON

# Integrantes
[Valentino Arballo](https://www.linkedin.com/in/valentino-arballo-376913252/)# Tapple
