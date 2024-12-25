from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from .forms import ClienteForm
from django.contrib import messages

def lista_cliente(request):
    clientes = Clientes.objects.all()
    return render(request, 'lista_cliente.html', {'clientes':clientes})

def detalhes(request, cliente_id):
    cliente = get_object_or_404(Clientes ,id=cliente_id)
    return render(request, 'detalhes.html', {'cliente':cliente})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente adicionado com sucesso')
            return redirect('lista_cliente')
    
    else:
        form = ClienteForm()

    return render(request, 'adicionar_cliente.html', {'form': form})

def edit_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente')
        
    else:
        form = ClienteForm()

    return render(request, 'edit_cliente.html', {'cliente':cliente, 'form': form} )

def delete_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)
    cliente.delete()
    return redirect('lista_cliente')