from django.http import HttpResponse

def home(request):
      return HttpResponse("<h1>HOME Page</h1>")

def index(request):
      return HttpResponse("<h1>Index Page </h1>")

def about(request):
      return HttpResponse("<h1>About Page</h1>")