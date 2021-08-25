from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

# Opção 2 de redirecionar de '/' para '/agenda/'
# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    # evento = Evento.objects.all(usuario=usuario)
    evento = Evento.objects.all()
    dados = { 'eventos': evento }
    return render(request, 'agenda.html', dados)