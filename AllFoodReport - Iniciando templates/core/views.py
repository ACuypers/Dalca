from django.shortcuts import render, redirect
from .models import UsuariosFuncoesAdm, Usuario, Empresa, RecebimentoCaixa, Mesa
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def login_user(request):
   return render(request, 'login.html')


def submit_login(request):
    if request.POST or None:
        cnpjempresa = request.POST.get('cnpj')
        username = request.POST.get('login')
        senha = request.POST.get('senha')

        #filter() estava tentando pegar o paremeto get() porem nao funcionava ele bugava na verificacao. isso aqui pode virar uma funcao

        #and Empresa.objects.filter(cnpj=cnpjempresa) and None
        if UsuariosFuncoesAdm.objects.filter(login__exact=username, senha__exact=senha):
            return render(request, 'painel.html')
        elif Usuario.objects.filter(usuario__exact=username) and Usuario.objects.filter(senha__exact=senha) and Empresa.objects.filter(cnpj=cnpjempresa):
            #Busca da ID da empresa
            for idempresauser in Usuario.objects.filter(usuario__exact=username) and Usuario.objects.filter(senha__exact=senha) and Empresa.objects.filter(cnpj=cnpjempresa):
                idempresa = idempresauser.id
            #Calcula o valor estimado na tabela RecebimentoCaixa
            for total in RecebimentoCaixa.objects.filter(idempresa_fk__exact=idempresa):
                totalestimado = total.totalrecebido + total.totalreceber

            context = {
                #Esta pegando todos as QuerySet de usuarios exemplo o 2 pega um monte assim:Usuario.objects.filter(usuario__exact=username) and Usuario.objects.filter(senha__exact=senha)
                'usuarios': Usuario.objects.filter(idempresa_fk=idempresa).get(usuario__exact=username),
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


@login_required(login_url='/login/')
def index(request):
    evento = UsuariosFuncoesAdm.objects.all()
    dados = {'evento': evento}
    return render(request, 'painel.html', dados)
