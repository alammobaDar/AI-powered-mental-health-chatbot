from django.shortcuts import render, redirect


def homepage_view(request):
    return render(request, 'homepage.html')