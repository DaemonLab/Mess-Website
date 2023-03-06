from django.shortcuts import render
from django.http import HttpResponse
from home.models import About, Update, Carousel, Photos, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact, Rebate

# Create your views here.
def home(request):
    aboutInfo=About.objects.all()
    update=Update.objects.all()
    caterer=Caterer.objects.all()
    carousel=Carousel.objects.all()
    photos=Photos.objects.all()
    context={'about': aboutInfo, 'updates': update,'caterer':caterer,'carousel':carousel,'photos':photos}
    return render(request,'home.html',context)



def rules(request):
    rules=Rule.objects.all()
    shortRebates=ShortRebate.objects.all()
    LongRebates=LongRebate.objects.all()
    form=Form.objects.all()
    caterer=Caterer.objects.all()
    params={'rule':rules,'shortRebate':shortRebates,'longRebate': LongRebates,'form':form,'caterer':caterer}
   
    return render(request,'rules.html',params)

def kanaka(request):
    caterer=Caterer.objects.all()
    context={'caterer':caterer}
    return render(request,'caterer2.html',context)

def ajay(request):
    caterer=Caterer.objects.all()
    context={'caterer':caterer}
    return render(request,'caterer1.html',context)

def links(request):
    """ allLinks=link.objects.all()
    context={'allLinks': allLinks} """
    caterer=Caterer.objects.all()
    form=Form.objects.all()
    context={'caterer':caterer,'form':form}
    return render(request,'links.html',context)

def cafeteria(request):
    caterer=Caterer.objects.all()
    cafeteria=Cafeteria.objects.all()
    context={'caterer':caterer,'cafeteria':cafeteria}
    return render(request,'cafeteria.html',context)

def contact(request):
    """ allContacts=contact.objects.all()
    context={'allContacts': allContacts} """
    caterer=Caterer.objects.all()
    contact=Contact.objects.all()
    context={'caterer':caterer,'contact':contact}
    return render(request,'contact.html',context)

def approveRebate():
    rebate