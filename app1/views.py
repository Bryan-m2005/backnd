from django.shortcuts import render
from django.http import HttpResponse

def pagina(requests):
    html= """
    <h1> hola mundo </h1>
    <h2>bievenido a la tienda online<h2/>
    <a href=pagina2>ir a informacion<a/>
    <p>
    <a href=pagina1/>ir a tienda<a/>
    """
    return HttpResponse(html)
def info(requests):
    html = """
    <h1>Quienes somos</h1>
    <p>Contacto: +56912345678</p>
    <p>Nombres: Bryan Martinez, Hans Vidal"""
    return HttpResponse(html)