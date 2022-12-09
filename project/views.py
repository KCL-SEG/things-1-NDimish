from django.shortcuts import render

# Create your views here.


def page(request, Logged_ID):

    return render(request, 'page.html')