from django.shortcuts import render

from .models import Tag

def home(request):
    tags = Tag.objects.all()
    return render(request, "index.html", {"tags": tags})
