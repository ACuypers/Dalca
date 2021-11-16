from django.shortcuts import render, redirect
from .models import UsuariosFuncoesAdm, Usuario, Empresa, RecebimentoCaixa, Mesa
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_user(request):
   return render(request, 'login.html')


def submit_login(request):
    if request.POST or None:
        username = request.POST.get('login')
        senha = request.POST.get('senha')

        #filter() estava tentando pegar o paremeto get() porem nao funcionava ele bugava na verificacao. isso aqui pode virar uma funcao

        if UsuariosFuncoesAdm.objects.filter(login=username, senha=senha):
            return render(request, 'painel.html')
        elif Usuario.objects.filter(usuario__exact=username) and Usuario.objects.filter(senha__exact=senha):
            #Busca da ID da empresa
            for idempresauser in Usuario.objects.filter(usuario__exact=username) and Usuario.objects.filter(senha__exact=senha):
                idempresa = idempresauser.idempresa_fk
            #Calcula o valor estimado na tabela RecebimentoCaixa
            for total in RecebimentoCaixa.objects.filter(idempresa_fk__exact=idempresa):
                totalestimado = total.totalrecebido + total.totalreceber

            context = {
                'usuarios': Usuario.objects.filter(usuario__exact=username) and Usuario.objects.filter(senha__exact=senha),
                'idempresa': idempresa,
                'empresa': Empresa.objects.filter(id=idempresa),
                'recebimento': RecebimentoCaixa.objects.filter(idempresa_fk__exact=idempresa),
                'totalestimado': totalestimado,

                'mesa': Mesa.objects.filter(idempresa_fk__exact=idempresa),
            }
            return render(request, 'dashboard.html', context)
        elif UsuariosFuncoesAdm.DoesNotExist or Usuario.DoesNotExist:
            messages.error(request, 'Usuario ou senha invalido')
        else:
            return render(request, 'login.html')
    return redirect('/')
'''
        user = authenticate(request, username=username, senha=senha)
        if user is not None:
            login(request, user)
           return render(request, 'login.html')
        else:
            return render(request, 'dashboard.html')
'''


@login_required(login_url='/login/')
def painellogin(request):
    evento = UsuariosFuncoesAdm.objects.all()
    dados = {'evento': evento}
    return render(request, 'painel.html', dados)
