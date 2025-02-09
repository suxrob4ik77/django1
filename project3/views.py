from django.http import HttpResponse

def sen(request):
    return HttpResponse("salom salom salom")

def sen1(request):
    return HttpResponse("salom salom ")


def sen2(request):
    return HttpResponse("salom")



