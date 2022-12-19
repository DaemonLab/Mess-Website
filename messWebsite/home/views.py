from django.shortcuts import render
from django.http import HttpResponse
from home.models import About, Update, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact

# Create your views here.
def home(request):
    """ aboutInfo=about.objects.first()
    update=update.objects.all()
    context={'about': aboutInfo, 'updates': update} """
    return HttpResponse("This is my webpage")



def rules(request):
    return render(request,'rules.html')

def kanaka(request):
    """ info=kanaka.objects.all()
    context={'info': info} """
    return HttpResponse("This is my webpage")

def ajay(request):
    """ info=ajay.objects.all()
    context={'info': info} """
    return HttpResponse("This is my webpage")

def links(request):
    """ allLinks=link.objects.all()
    context={'allLinks': allLinks} """
    return HttpResponse("This is my webpage")

def cafeteria(request):
    """ allCafe=cafeteria.objects.all()
    context={'allCafe': allCafe} """
    return HttpResponse("This is my webpage")

def contact(request):
    """ allContacts=contact.objects.all()
    context={'allContacts': allContacts} """
    return HttpResponse("This is my webpage")