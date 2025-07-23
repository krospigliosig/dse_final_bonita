from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Posteo
# Create your views here.

@csrf_exempt
def index(request):
    mensaje = ''
    if request.method == 'GET':
        mensaje = request.GET.get('mensaje', '')
        if mensaje:
            Posteo.objects.create(contenido=mensaje) 

    # Obtener los mensajes existentes ordenados por fecha
    mensajes = Posteo.objects.order_by('-fecha')

    # Armar HTML con todos los mensajes
    lista_html = "<ul>"
    for m in mensajes:
        lista_html += f"<li>{m.fecha.strftime('%Y-%m-%d %H:%M:%S')} - {m.contenido}</li>"
    lista_html += "</ul>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mensajes acumulados</title>
    </head>
    <body>
        <h1>Mensajes recibidos</h1>
        {lista_html}
    </body>
    </html>
    """
    return HttpResponse(html)