from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog_item,
        'nama': 'Amanda Christie Tarigan',
        'NPM' : '2106751322'
    }
    return render(request, "katalog.html", context)