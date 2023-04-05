from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.models import Todo
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    if request.user.is_anonymous:
        return redirect('/loginUser')
    return render(request, 'index.html')


def service(request):
    if request.user.is_anonymous:
        return redirect('/loginUser')
    if request.method == 'POST':
        task = request.POST.get('task')
        date = request.POST.get('date')
        new_todo = Todo(task=task, date=date)
        new_todo.save()
    all_entries = Todo.objects.all()
    context = {'todos': all_entries}
    return render(request, 'services.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('service'))


def update(request, id):
    todo = Todo.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'todo': todo,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    if request.method == 'POST':
        task = request.POST.get('task')
        date = request.POST.get('date')
        todo = Todo.objects.get(id=id)
        todo.task = task
        todo.date = date
        todo.save()
    return HttpResponseRedirect(reverse('service'))


def contactus(request):
    if request.user.is_anonymous:
        return redirect('/loginUser')
    return render(request, 'contactus.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/loginUser')
    return render(request, 'login.html')


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/loginUser')
    return render(request, 'index.html')
