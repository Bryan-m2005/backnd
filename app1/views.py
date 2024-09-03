from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pagina1(requests):
    html = """
    <h1>Bienvenido, seleccione sus productos<h1/>
    <a href=pescados>atun<a/>
    """
    return HttpResponse(html)
def pescados(requests):
    html = """
    <h2>soy un jurel<h2/>
    <h1><°))))><<h1/>
    <h2>precio = 1500 el kilo<h2/>
    <h2>info nutricional por cada 100g<h2/>
    <h3>carbohidratos = 0g<h3/>
    <h2>proteinas = 25g<h2/>
    <h3>calorias = 250<h3/>
    """
    return HttpResponse(html)