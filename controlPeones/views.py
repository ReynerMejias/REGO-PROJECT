from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from . import forms
from django.utils import timezone

# Create your views here.

def InicioSesion(request):
    if request.user.is_authenticated:
        return redirect('Peones')
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('Peones')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, "controlPeones/inicio.html") 

def logoutUser(request):
    logout(request)
    return redirect('Peones')

@login_required(login_url='Inicio')
def Peones(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    peones = models.Peon.objects.filter(nombre__icontains=q)
    context = {"peones": peones}
    return render(request, "controlPeones/peones.html", context=context)

@login_required
def Peon(request, pk):
    peon = models.Peon.objects.get(id=pk)
    contrato = peon.contrato
    retiros = contrato.retiro_set.order_by('-fecha_retiro')
    
    context = {"peon": peon, "retiros": retiros, 'contrato': contrato}
    return render(request, "controlPeones/peon.html", context=context)

@login_required
def CrearPeon(request):
    formPeon = forms.PeonForm()
    formContrato = forms.ContratoForm()
    context = {"formPeon": formPeon, "formContrato": formContrato}
    if request.method == 'POST':
        formPeon = forms.PeonForm(request.POST)
        formContrato = forms.ContratoForm(request.POST)

        if formPeon.is_valid():
            peon = formPeon.save(commit=False)
            
            formContrato.instance.peon = peon

            if formContrato.is_valid():
                peon.save()
                formContrato.save()
                return redirect('Peones')
            else:
                print("Errores en FormContrato:", formContrato.errors)
        else:
            n_cedula_errors = formPeon.errors.get('n_cedula')
            if n_cedula_errors:
                messages.error(request, ' '.join(n_cedula_errors))
    return render(request, "controlPeones/CrearPeon.html", context=context)

@login_required
def CrearRetiro(request, pk):
    peon = models.Peon.objects.get(id=pk)
    contrato = peon.contrato
    retiros = contrato.retiro_set.order_by('-fecha_retiro')
    form = forms.RetiroForm()

    if request.method == 'POST':
        form = forms.RetiroForm(request.POST)
        
        if form.is_valid():
            retiro = form.save(commit=False)
            retiro.contrato = contrato
            retiro.save()
            contrato.fecha_inicio = request.POST.get('fecha_retiro')
            contrato.save()
            return redirect('Peon', pk=pk)
        else:
            messages.error(request, ' '.join(form.errors.get('__all__')))

    context = {"peon": peon, "retiros": retiros, 'form': form, 'contrato': contrato}
    
    return render(request, "controlPeones/CrearRetiro.html", context=context)


@login_required
def CambiarActivo(request, pk):
    peon = models.Peon.objects.get(id=pk)
    contrato = peon.contrato
    if request.method == 'POST':
        if peon.activo:
            peon.activo = False
        else:
            peon.activo = True
            contrato.fecha_inicio = timezone.now()
            contrato.save()
        peon.save()
        return redirect('Peon', pk=pk)
    if peon.activo:
        estado = "desactivar"
    else:
        estado = "activar"
    return render(request, "controlPeones/cambiarActivo.html", context={"peon": peon, "estado": estado})

