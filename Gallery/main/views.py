from django.shortcuts import render


def error404(request, exception):
    return render(request, 'main/404.html')
