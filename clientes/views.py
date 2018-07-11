from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm,AdressForm


# Create your views here.

@login_required()
def list_clientes(request):

    clientes = lista_clientes()

    return render(request, 'clientes/lista-de-clientes.html', {'clientes': clientes})


@login_required()
def new_cliente(request):

    lista = lista_clientes()

    form = ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    return render(request, 'clientes/cliente-form.html', {'formu': form, 'lista':lista})

@login_required()
def update_cliente(request, id):

    lista = lista_clientes()
    print(lista)


    if id==0:
        lista_none = lista_clientes()
        cliente = Cliente()
        cliente.adress = None
        cliente.first_name = ''
        cliente.last_name = ''
        cliente.age = ''
        form_none = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
        return render(request, 'clientes/cliente-form.html', {'formu': form_none, 'lista': lista_none})

    if id != 0:
        cliente = get_object_or_404(Cliente, pk=id)
        print(cliente)
        form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)
        lista = lista_clientes()
        print(lista)

        if form.is_valid():
            form.save()

        return render(request, 'clientes/cliente-form.html', {'formu': form , 'lista': lista},)

@login_required()
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, request.FILES or None, instance=cliente)

    if request.method == 'POST':
        cliente.delete()

    return render(request, 'clientes/cliente-delete-confirm.html', {'cliente': form})


@login_required()
def new_adress(request):
    adress_form = AdressForm(request.POST or None, request.FILES or None)
    if adress_form.is_valid():
        adress_form.save()

    return render(request, 'clientes/endereco-form.html', {'adress_form':adress_form})



def lista_clientes():
    clientes = Cliente.objects.all()
    return clientes






