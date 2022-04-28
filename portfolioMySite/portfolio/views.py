from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Linguagem
from .models import Projeto

# Create your views here.


def home(request):
    linguagem = Linguagem.objects.all()
    ultimos_projetos = Projeto.objects.all()[:12]
    linguagens = Linguagem.objects.all()

    return render(request, 'home.html', {'linguagem': linguagem,
                                         'projetos': ultimos_projetos,
                                         'linguagens': linguagens})


def linguagem(request, linguagem_id):
    linguagem = get_object_or_404(Linguagem, id=linguagem_id)
    linguagens = Linguagem.objects.all()
    projetos = Projeto.objects.filter(linguagem=linguagem)

    return render(request, 'home.html', {'linguagens': linguagens,
                                         'projetos': projetos,
                                         'linguagem': linguagem})


def projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    linguagens = Linguagem.objects.all()

    return render(request, 'projeto.html', {'linguagens': linguagens,
                                            'projeto': projeto})
