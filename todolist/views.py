# Mengimpor modul-modul yang diperlukan
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime 
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers

# Fungsi untuk memproses registrasi user
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Menyimpan data akun ke database
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Fungsi untuk memproses aktivitas login 
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # Melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todolist")) # Membuat response
            response.set_cookie('last_login', str(datetime.now())) # Membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Fungsi untuk memproses aktivitas logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/') # Merestriksi akses halaman todolist
# Fungsi untuk menampilkan todolist user
def todolist(request):
    username = request.user.username
    user_id = request.user.id
    data_todolist = Task.objects.filter(user_id=user_id) # Menyimpan hasil query dari data pada Task dengan user_id tertentu

    context = { 
        "username": username,
        "todolist": data_todolist,
    }
    return render(request, "todolist_ajax.html", context)

@login_required(login_url='/todolist/login/') # Merestriksi akses halaman create-task
# Fungsi untuk memproses pembuatan task
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid(): # Kondisi data pada field valid
            task = Task(
                user = request.user,
                title = form.cleaned_data['judul'], 
                description = form.cleaned_data['deskripsi'],
            )
            task.save() # Menyimpan task ke database
            return HttpResponseRedirect(reverse("todolist:todolist"))
    else:
        form = TaskForm()
    
    context = {'form':form}
    return render(request, "create_task.html", context)

@login_required(login_url='/todolist/login/')
# Fungsi untuk menghapus task
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect("/todolist")

#resource: https://www.w3schools.com/django/django_delete_record.php

@login_required(login_url='/todolist/login/')
# Fungsi untuk memperbarui status task
def update_status(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.is_finished = not task.is_finished
        task.save()
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
# Fungsi untuk mengembalikan seluruh data task dalam bentuk JSON
def show_todolist_json(request):
    data = Task.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@login_required(login_url='/todolist/login/') 
# Fungsi untuk memproses pembuatan task dengan modal
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(
            user=request.user,
            title=title, 
            description=description,
            is_finished=False
        )

        context = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
            }
        }

    return JsonResponse(context)
