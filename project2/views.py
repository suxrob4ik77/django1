from django.http import HttpResponse

def exe(request):
    return HttpResponse("salom ")

def exe1(request):
    return HttpResponse("salom salom")

def exe2(request):
    return HttpResponse("salom salom salom")

