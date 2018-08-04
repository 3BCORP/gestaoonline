from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm,AdressForm


# Create your views here.
@login_required()
def new_cliente(request):

    lista = lista_clientes()

    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    return render(request, 'clientes/cliente-form.html', {'formu': form, 'lista': lista})

@login_required()
def update_cliente(request, id):


    if id==0:
        form_none = white_client()
        lista_none = lista_clientes()
        return render(request, 'clientes/cliente-form.html', {'formu': form_none, 'lista': lista_none})

    if id != 0:
        cliente = get_object_or_404(Cliente, pk=id)
        print(cliente)
        form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
        lista = lista_clientes()

        if form.is_valid():
            form.save()

        return render(request, 'clientes/cliente-form.html', {'formu': form, 'lista': lista})

@login_required()
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('update', 0)

    return render(request, 'clientes/cliente-delete-confirm.html', {'cliente': form})

# TODO: ao salvar o endereço retornar para a view com o form preenchido com os dados que foram digitados e o usuario cliica em novo endereço
@login_required()
def new_adress(request):
    print(request.POST)
    adress_form = AdressForm(request.POST or None)
    if adress_form.is_valid():
        adress_form.save()
        return redirect('new')

    return render(request, 'clientes/endereco-form.html', {'adress_form': adress_form})


# TODO:implementar comparação do valor de request.POST  com lista de clientes e retornar o objeto cliente correspondente para o form na url update
@login_required()
def search_cliente(request):


    pesquisa = request.POST['search_input']
    return redirect('update',0)


def lista_clientes():
    clientes = Cliente.objects.all()
    return clientes


def white_client():
    cliente = Cliente()
    cliente.adress = None
    cliente.first_name = ''
    cliente.last_name = ''
    cliente.age = ''
    form_none = ClienteForm(instance=cliente)

    return form_none






