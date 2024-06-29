from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Cadastra um novo usuário"""
    if request.method != 'POST':
        # exibe um formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # processa o formulário preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # faz o login do usuário e o redireciona para a pág inicial
            login(request, new_user)
            return redirect('learning_logs:index')

    # exibe um formulário em branco ou invalido
    context = {'form': form}
    return render(request, 'registration/register.html', context)
