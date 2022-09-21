from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()

    watched = MyWatchList.objects.filter(watched=True).count()
    not_watched = MyWatchList.objects.filter(watched=False).count()
    
    message = ""

    # Showing message.
    if watched >= not_watched:
        message = "Selamat, kamu sudah banyak menonton!🥳"
    else:
        message = "Wah, kamu masih sedikit menonton!🤔"
    
    context = {
    'mywatchlist': data_mywatchlist,
    'message': message,
    'name': 'Amanda Christie Tarigan',
    'student_id': '2106751322'
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_mywatchlist_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")