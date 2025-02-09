from django.urls import path,include
from project2.views import *

urlpatterns = [
    path('exe/', exe),
    path('exe1/', exe1),
    path('exe2/', exe2)


]