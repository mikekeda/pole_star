from django.shortcuts import render


def homepage_view(request):
    """ Homepage page. """
    return render(request, "index.html")
