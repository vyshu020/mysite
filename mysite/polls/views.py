
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def about_us(request):
    return HttpResponse("I have created this site. My name is Vyshnavi.")