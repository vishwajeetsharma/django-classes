from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, World!!</h1><br>Hello front page")

def testCricket(request):
    return HttpResponse("hello welcome to the test cricket")