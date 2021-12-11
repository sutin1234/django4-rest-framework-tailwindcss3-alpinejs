from django.shortcuts import render


# Create your views here.
def index_home(request):
    ctx = {
        'text_hello': ' Hello Django4'
    }
    return render(request, "blog/index.html", ctx)
