from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>გაუმარჯოს, გაუმარჯოს, დედამიწას გაუმარჯოს!</h1>')
