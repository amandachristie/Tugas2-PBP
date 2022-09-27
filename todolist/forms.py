from django import forms

class TaskForm(forms.Form):
    judul = forms.CharField()
    deskripsi = forms.CharField(widget=forms.Textarea)
