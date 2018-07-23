from django.shortcuts import render
from django.core import serializers
from .models import Users

def index(request):
    all_names = Users.objects.all()
    context = {'all_names': all_names}
    return render(request, 'life/index.html', context)