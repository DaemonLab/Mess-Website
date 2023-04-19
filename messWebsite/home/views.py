from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import About, Update, Carousel, Photos, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact, Rebate, File, Allocation, Student
import pandas as pd
import datetime
from django.views.generic import TemplateView
import io
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_date
from django.core.exceptions import MultipleObjectsReturned
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


def caterer(request,name):
    caterer = Caterer.objects.get(name=name)
    context={'caterer':caterer}
    return render(request,'caterer.html',context)

# def kanaka(request):
#     caterer=Caterer.objects.all()
#     context={'caterer':caterer}
#     return render(request,'caterer2.html',context)

# def ajay(request):
#     caterer=Caterer.objects.all()
#     context={'caterer':caterer}
#     return render(request,'caterer1.html',context)

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
    caterer=Caterer.objects.all()
    contact=Contact.objects.all()
    context={'caterer':caterer,'contact':contact}
    return render(request,'contact.html',context)

def days(s,list):
    total_days = 0
    try:
        count = Rebate.objects.filter(allocation_id = s).count()
        for i in range(count):
            rebate = Rebate.objects.filter(allocation_id = s)[i]
            start_date = rebate.start_date
            end_date = rebate.end_date
            list.append([(start_date),(end_date)])
            total_days += ((end_date-start_date).days)+1
        return total_days
    except Exception as e:
        print(e)
        return total_days

def rebate(request):
    text=""
    list=[]
    try:
        allocation_id = Allocation.objects.get(roll_no__email = str(request.user.email))
        key = str(allocation_id.student_id)
    except Allocation.DoesNotExist:
        key = "Signed IN account does not does not have any allocation ID"
    except Allocation.MultipleObjectsReturned:
        allocation_id = Allocation.objects.filter(roll_no__email = str(request.user.email)).first()
        key = str(allocation_id.student_id)
    if request.method =='POST' and request.user.is_authenticated:
            try:
                start_date = parse_date(request.POST['start_date'])
                end_date = parse_date(request.POST['end_date'])
                diff = ((end_date-start_date).days)+1
                diff2 = (start_date-datetime.date.today()).days
                if((diff)<=7 and diff>=2 and diff2>=2):
                    # approved = True
                    text="You have successfully submitted the form. Thank you"
                    try:
                        Allocation.objects.get(student_id = request.POST['allocation_id'])
                        try:
                            a=Allocation.objects.get(roll_no__email = str(request.user.email), student_id = request.POST['allocation_id'])
                            total_days = days(a,list)+diff
                            print(total_days)
                            print(list)
                            if(total_days>8): 
                                text="You can only apply for max 8 days in a month"
                            else:
                                r = Rebate(
                                    email=request.user.email,
                                    allocation_id = a,
                                    start_date = request.POST['start_date'],
                                    end_date = request.POST['end_date'],
                                    approved=False
                                )
                                r.save()
                            # else: text="Email ID does not match with the allocation ID"
                        except Allocation.DoesNotExist:
                            text ="Email ID does not match with the allocation ID"
                    except Allocation.DoesNotExist:
                        text=" The asked allocation ID does not exist. Please enter the correct ID."
                else:
                    # approved = False
                    text="Your rebate application has been rejected due to non-compliance of the short term rebate rules"
                # rebate.save(update_fields=["approved"])    
            except Exception as e:
                print(e)
                text="Invalid Dates filled"  
    context = {'text': text, "key":key, "list": list}
    return render(request,"rebateForm.html",context)



class allocation(TemplateView):
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
                    first_pref = str(record["first_pref"]).capitalize()
                    second_pref = str(record["second_pref"]).capitalize()
                    third_pref = str(record["third_pref"]).capitalize()
                    high_tea = record["high_tea"]
                    r = Student.objects.get(roll_no = record["roll_no"])    
                    print(r)
                    print("hi1")
                    for pref in [first_pref,second_pref,third_pref]:
                        kanaka = Caterer.objects.get(name = "Kanaka")
                        ajay = Caterer.objects.get(name = "Ajay")
                        gauri = Caterer.objects.get(name = "Gauri")
                        if(pref == kanaka.name and kanaka.student_limit>0):
                            student_id=str(kanaka.name[0])
                            if(high_tea==True): student_id+="H"
                            student_id+=str(kanaka.student_limit) 
                            caterer_name = kanaka.name
                            kanaka.student_limit-=1
                            kanaka.save(update_fields=["student_limit"])
                            break 
                        elif(pref == ajay.name and ajay.student_limit>0):
                            student_id=str(ajay.name[0])
                            if(high_tea==True): student_id+="H"
                            student_id+=str(ajay.student_limit) 
                            caterer_name = ajay.name
                            ajay.student_limit-=1
                            ajay.save(update_fields=["student_limit"])
                            break
                        elif(pref == gauri.name and gauri.student_limit>0):
                            student_id=str(gauri.name[0])
                            if(high_tea==True): student_id+="H"
                            student_id+=str(gauri.student_limit) 
                            caterer_name = gauri.name
                            gauri.student_limit-=1
                            gauri.save(update_fields=["student_limit"])
                            break
                    a = Allocation(
                        roll_no = r,
                        student_id = student_id,
                        month = record["month"],
                        caterer_name = caterer_name,
                        high_tea = high_tea,
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
