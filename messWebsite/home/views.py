from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import About, Update, Carousel, Photos, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact, Rebate, File, Allocation, Student
from .forms import RebateForm
import pandas as pd
import datetime
from django.views.generic import TemplateView
import io
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_date


kanaka_limit=900
ajay_limit=900
gauri_limit=500

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

def rebate(request):
    text=""
    if request.method =='POST' and request.user.is_authenticated:
        # form = RebateForm(request.POST)
        # if form.is_valid():
            # form.save()
            # rebate = Rebate.objects.latest("id")
            start_date = parse_date(request.POST['start_date'])
            end_date = parse_date(request.POST['end_date'])
            diff = ((end_date-start_date).days)+1
            diff2 = (start_date-datetime.date.today()).days
            # print(diff)
            # print(diff2)
            if((diff)<=7 and diff>=2 and diff2>=2):
                approved = True
                text="You have successfully submitted the form. Thank you"
            else:
                approved = False
                text="Your rebate application has been rejected due to non-compliance of the short term rebate rules"
            try:
                a1 = Allocation.objects.get(student_id = request.POST['allocation_id'])
                try:
                    a2=Allocation.objects.get(roll_no__email = str(request.user.email))
                    if(a1==a2):
                        r = Rebate(
                            email=request.user.email,
                            allocation_id = a1,
                            start_date = request.POST['start_date'],
                            end_date = request.POST['end_date'],
                            approved=approved
                        )
                        r.save()
                    else: text="Email ID does not match with the allocation ID"
                except Allocation.DoesNotExist:
                    text ="The asked Email ID does not have an Allocation ID"
            except Allocation.DoesNotExist:
                text=" The asked allocation ID does not exist. Please enter the correct ID."
            # rebate.save(update_fields=["approved"])      
    context = {'text': text}
    return render(request,"rebateForm.html",context)



class allocation(TemplateView):
    # if request.method == 'POST':
    #     file = request.FILES['file']
    #     obj = File.objects.create(file = file)
    #     create_db(obj.file)
    # return render(request,"allocation.html")

    template_name = 'allocation.html'
    def post(self, request):
        context = {
            'messages':[],
        }
        if request.user.is_authenticated and request.user.is_staff :
            csv = request.FILES['csv']
            csv_data = pd.read_csv(
                io.StringIO(
                    csv.read().decode("utf-8")
                )
            )
            print(csv_data.head())

            for record in csv_data.to_dict(orient="records"):
                try:
                    global kanaka_limit, gauri_limit, ajay_limit
                    # student_id = record["student_id"]
                    # caterer_name = record["caterer_name"]
                    first_pref = record["first_pref"]
                    second_pref = record["second_pref"]
                    third_pref = record["third_pref"]
                    r = Student.objects.get(roll_no = record["roll_no"])    
                    print(r)
                    print("hi1")
                    for pref in [first_pref,second_pref,third_pref]:
                        if(pref == "kanaka" and kanaka_limit>0):
                            student_id="K"+str(kanaka_limit)
                            caterer_name = "Kanaka"
                            kanaka_limit-=1
                            break 
                        elif(pref == "ajay" and ajay_limit>0):
                            student_id="A"+str(ajay_limit)
                            caterer_name = "Ajay"
                            ajay_limit-=1
                            break
                        elif(pref == "gauri" and gauri_limit>0):
                            student_id="G"+str(gauri_limit)
                            caterer_name = "Gauri"
                            gauri_limit-=1
                            break
                    print(student_id)
                    a = Allocation(
                        roll_no = r,
                        student_id = student_id,
                        month = record["month"],
                        caterer_name = caterer_name,
                        high_tea = record["high_tea"],
                        first_pref = first_pref,
                        second_pref = second_pref,
                        third_pref = third_pref
                    )
                    a.save()
                except Exception as e:
                    context['exceptions_raised'] = e
                    print(e)  
            messages="Form submitted. Please check the admin page."              
        return render(request, self.template_name, context)
