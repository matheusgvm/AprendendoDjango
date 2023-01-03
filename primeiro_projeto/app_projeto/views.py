from django.shortcuts import render
from django.views import View
from django import forms
from datetime import date
from django.urls.base import reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Pessoa

# Create your views here.
class ListarPessoas(View):
  def get(self,request):
    # Retornando apenas o id e o nome -> Boa prática! Busca somente o necessário
    # Requisição assincrona
    lst_pessoas = list(Pessoa.objects.all().values("id","nome"))
    return JsonResponse({"pessoas":lst_pessoas})

class SalvarPessoa(View):
    def get(self,request,id=None): #Requisitou a exibição do formulário
        pessoa = Pessoa.objects.get(id=id) if id != None else None
        return render(request,"salvar_pessoa.html",{"pessoa":PessoaForm(instance=pessoa)})

    def post(self,request,id=None):#via post, salva a pessoa
        pessoa = Pessoa.objects.get(id=id) if id != None else None
        form = PessoaForm(request.POST,request.FILES, instance=pessoa)

        if form.is_valid():
            form.save()
            #se estiver ok, salva e lista as pessoas
            return HttpResponseRedirect(reverse('listar_pessoas') )
        else:
            #caso nao esteja valido, volte a exibir o formulario
            return render(request,"salvar_pessoa.html",{"pessoa":form})

class PessoaForm(forms.ModelForm):
    class Meta:
      # Especifica a classe do DB
        model = Pessoa
        # Mostra quais atributos da classe serão utilizados
        fields = ['nome', 'data_nascimento']
        # Mostra como cada campo será exbido no form
        labels = {"data_nascimento": "Data de Nascimento"}

class Home(View):
    def get(self, request):
        lista_itens = [{"titulo":"De onde eles vêm",
                        "texto":"Lorem ipsum dolor sit amet, consectetur"},
                        {"titulo":"O que eles querem",
                        "texto":"osakdpokasdokaspok"},
                      ]
        itens = {'lista_itens':lista_itens }
        return render(request,"home.html",itens)

class Contato(View):
    def get(self, request):
      return render(request,
                          "contato.html",
                          {"contato":PessoaForm(initial={"data_nascimento":date.today()})})
    def post(self,request):
      form = PessoaForm(request.POST)
      if form.is_valid():
        # processa o formulario (usando form.cleaned_data)
        return HttpResponseRedirect(reverse('sucesso') )

      return render(request, "contato.html", {'contato': form})

class Ola(View):
   def get(self, request, nome,cidade):
       return render(request,
                       "ola.html",
                       {'nome_pessoa': nome,'cidade':cidade})