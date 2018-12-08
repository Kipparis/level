from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Что будет показываться когда мы перейдём на страницу с этим приложением


def index(request):    
    # if request.method == "POST":
    # name = request.POST.get('name')
        # return HttpResponse("<h1>You are welcom ;)</h1>")
    #     return render(request, 'homePage.html', dict(locals()))
    # else:
    return render(request, 'homePage.html')
