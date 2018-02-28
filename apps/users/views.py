from django.shortcuts import render

# Create your views here.

def get_blank(request):
    return render(request, "blank.html")