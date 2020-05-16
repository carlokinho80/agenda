from django.shortcuts import render
from core.models import Evento


# Create your views here.

def lista_eventos(resquest):
    evento = Evento.objects.all()
    response = {'eventos':evento}
    return render(resquest,'agenda.html', response)
