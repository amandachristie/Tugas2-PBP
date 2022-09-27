# Mengimpor modul-modul yang diperlukan
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from todolist.models import Task

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
            response.set_cookie('last_login', str(datetime.datetime.now())) # Membuat cookie last_login dan menambahkannya ke dalam response
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
        "todolist": data_todolist
    }
    return render(request, "todolist.html", context)

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
	deleted_task = Task.objects.get(id=id) # Mengambil data task yang ingin dihapus sesuai id
	deleted_task.delete() # Menghapus task 

	return HttpResponseRedirect("/todolist")

#resource: https://www.w3schools.com/django/django_delete_record.php

@login_required(login_url='/todolist/login/')
# Fungsi untuk memperbarui status task
def update_status(request, id):
    updated_task = Task.objects.get(id=id)

    if updated_task.is_finished:
        updated_task.is_finished = False
    else:
        updated_task.is_finished = True
    
    updated_task.save() # Menyimpan pembaruan ke database
    return HttpResponseRedirect("/todolist")