from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {
        "cursos":"",
        "faculdade": "Faculdade Impacta",
        "Pagina":"Homepage",
        "usuario": "Felipe",
        "logado": False,
        "idade": 17,
        "home_activate": True
    }
    return render(request, "principal/index.html",contexto)

def erro_404(request):
    return render(request, "principal/erro.html")
