from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Solicitacao,Solicitante
from .forms import TeleconsultorForm,SolicitanteForm,SolicitacaoForm
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def solicitacao_list(request):
    posts = Solicitacao.objects.all().order_by('DataSolicitacao')
    return render(request, 'TS/solicitacao_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Solicitacao, pk=pk)
    return render(request, 'TS/post_detail.html', {'post': post})


def teleconsultor_new(request):
    if request.method == "POST":
        form = TeleconsultorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('TS/views.solicitacao_list.html')
    else:
        form = TeleconsultorForm()
    return render(request, 'TS/teleconsultor_new.html', {'form': form})



def solicitante_new(request):
    if request.method == "POST":
        cpf = request.POST.get("CPF")
        checkIfExists = Solicitante.objects.filter(CPF =cpf).count()
        if checkIfExists > 0:
            return render(request,'TS/errorsolicitante.html')
        else :
            form = SolicitanteForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('TS/views.solicitacao_list.html')
    else:
        form = SolicitanteForm()
    return render(request, 'TS/solicitante_new.html', {'form': form})


def solicitacao_new(request):
    if request.method == "POST":
        idSolicitante = request.POST.get("solicitante")
        checkSolicitanteToday = Solicitacao.objects.filter(solicitante_id = idSolicitante)
        countItens = checkSolicitanteToday.filter(solicitante__solicitacao__DataSolicitacao__gt=timezone.now().date()).count()
        if countItens > 0 :
            messages.error(request, 'usuario possui ja uma solicitação no dia de hoje')
            return render(request, 'TS/solicitacao_new.html')
        else:
            form = SolicitacaoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, 'Solicitação salva')
                return redirect('TS/views.solicitacao_list.html')
    else:
        form = SolicitacaoForm()
    return render(request, 'TS/solicitacao_new.html', {'form': form})

