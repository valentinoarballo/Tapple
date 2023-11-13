# Imports que son nativos del Framework y Librerias
from app import app

from flask import (
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
    flash,
)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/endpoints")
def endpoints():
    return render_template("endpoints.html")


@app.route("/models")
def models():
    return render_template("models.html")


@app.route("/tapple")
def tapple():
    return render_template("tapple.html")


@app.route("/manual")
def manual():
    return render_template("manual.html")

class Producto:
    def __init__(self, nombre, foto):
        self.nombre = nombre
        self.foto = foto


@app.route('/celulares')
def celulares():
    productos_laptops = [
        Producto(nombre="Iphone 15 Pro", foto="../static/store/compare_iphone_15_pro.png"),
        Producto(nombre="Iphone 15", foto="../static/store/compare_iphone_15.png"),
        Producto(nombre="Iphone 14", foto="../static/store/compare_iphone_14.png"),
        Producto(nombre="Iphone se", foto="../static/store/compare_iphone_se.png"),
    ]

    producto_laptop_hero = Producto(nombre="Iphone 15 Pro", foto="../static/store/hero_iphone15.jpg")

    return render_template('layoutProductos.html', productos=productos_laptops, producto_hero=producto_laptop_hero)

@app.route('/relojes')
def relojes():
    productos_relojes = [
        Producto(nombre="Apple Watch Ultra 2", foto="../static/store/compare_ultra2.jpg"),
        Producto(nombre="Apple Watch S9", foto="../static/store/compare_s9.jpg"),
        Producto(nombre="Apple Watch se", foto="../static/store/compare_se.jpg"),
    ]

    producto_reloj_hero = Producto(nombre="Apple Watch Ultra 2", foto="../static/store/watch_hero.jpg")

    return render_template('layoutProductos.html', productos=productos_relojes, producto_hero=producto_reloj_hero)

@app.route('/laptops')
def laptps():
    productos_laptops = [
        Producto(nombre="MacBook Air M2", foto="../static/store/compare_macbook_air_m2.jpg"),
        Producto(nombre="MacBook Pro M2", foto="../static/store/compare_macbook_pro.jpg"),
        Producto(nombre="MacBook Pro M1", foto="../static/store/compare_macbook_pro.jpg"),
    ]

    producto_laptop_hero = Producto(nombre="New MacBook Pro M3", foto="../static/store/Apple-MacBook-Pro.jpg")

    return render_template('layoutProductos.html', productos=productos_laptops, producto_hero=producto_laptop_hero)