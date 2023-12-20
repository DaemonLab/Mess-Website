from ..models import *
from django.contrib.admin.views.decorators import staff_member_required
import pandas as pd
import io
from django.shortcuts import redirect
from django.shortcuts import render

@staff_member_required(redirect_field_name="/", login_url="/")
def allocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    *Template:*

    :template:`home/allocation.html`

    Gets the data from the allocation csv,
    parses each row and allocates each student an allocation ID and caterer for that month.
    Which can be then exported in the admin page.
    CSV should be imported from /allocation/ url only
    This form can only be accessed by the Institute's admin
    """
    messages = ""
    if (
        request.method == "POST"
        and request.user.is_authenticated
        and request.user.is_staff
    ):
        try:
            file = request.FILES["csv"]
            file_extension = file.name.split('.')[-1].lower()
            if file_extension == 'csv':
                csv_data = pd.read_csv(io.StringIO(file.read().decode('utf-8')))
            elif file_extension == 'xlsx':
                csv_data = pd.read_excel(file, engine='openpyxl')
            print(csv_data.head())

            for record in csv_data.to_dict(orient="records"):
                try:
                    if 'First Preference' in csv_data.columns:
                        first_pref = str(record["First Preference"]).capitalize()
                        caterer1 = Caterer.objects.get(name=first_pref)
                    else:
                        first_pref =None
                    if 'Second Preference' in csv_data.columns:
                        second_pref = str(record["Second Preference"]).capitalize()
                        caterer2 = Caterer.objects.get(name=second_pref)
                    else:
                        second_pref=None
                    if 'Third Preference' in csv_data.columns:
                        third_pref = str(record["Third Preference"]).capitalize()
                        caterer3 = Caterer.objects.get(name=third_pref)
                    else:
                        third_pref=None

                    #  getting period object
                    # if 'Period' in csv_data.columns and 'Semester' in csv_data.columns:
                    #     period = str(record["Period"]).capitalize()
                    #     semester = str(record["Semester"]).capitalize()
                    #     period_obj = Period.objects.get(Sno=period, semester=Semester.objects.get(name=semester))
                    # else:
                    #     period_obj = Period.objects.filter().last()
                    period_obj = Period.objects.filter().last()

                    # getting high tea
                    high_tea = record["High Tea"]
                    jain = record["Jain"]
                    print(high_tea)
                    if(high_tea=="Yes" or high_tea==True or high_tea=="TRUE"):
                        high_tea=True
                    else:
                        high_tea=False
                    
                    student = Student.objects.filter(name=record["Name"], hostel=record["Hostel"]).first()
                    if(student==None):
                        messages+=str(record["Email"])
                    print(student)

                    if caterer1.student_limit>0:
                        caterer1.student_limit-=1
                        caterer1.save(update_fields=["student_limit"])
                        caterer=caterer1
                    elif caterer2 and caterer2.student_limit>0:
                        caterer2.student_limit-=1
                        caterer2.save(update_fields=["student_limit"])
                        caterer=caterer2
                    elif caterer3 and caterer3.student_limit>0:
                        caterer3.student_limit-=1
                        caterer3.save(update_fields=["student_limit"])
                        caterer=caterer3
                    student_id = str(caterer.name[0])
                    if high_tea == True:
                        student_id += "H"
                    else:
                        student_id+="NH"
                    student_id += str(caterer.student_limit)
                    allocation = Allocation(
                        email=student,
                        student_id=student_id,
                        period=period_obj,
                        caterer=caterer,
                        high_tea=high_tea,
                        jain=jain,
                        first_pref=first_pref,
                        second_pref=second_pref,
                        third_pref=third_pref,
                    )
                    allocation.save()
                    student_bill = StudentBills.objects.get_or_create(email=student, semester=period_obj.semester)
                    UnregisteredStudent.objects.filter(email__iexact=student.email).delete()
                except Exception as e:
                    print(e)
            messages += "Form submitted. Please check the admin page."
        except Exception as e:
            print(e)
            messages = "Invalid CSV file"
        request.session["messages"] = messages
        return redirect(request.path)
    messages = request.session.get("messages", "")
    if(messages!=""): 
        del request.session["messages"]
    period_obj = Period.objects.filter().last()
    caterer_list = []
    for caterer in Caterer.objects.filter(visible=True).all():
        caterer_high_tea = Allocation.objects.filter(caterer=caterer, high_tea=True,period=period_obj).count()
        caterer_total = Allocation.objects.filter(caterer=caterer,period=period_obj).count()
        caterer_left = caterer.student_limit
        caterer_list.append([caterer.name,caterer_high_tea,caterer_total,caterer_left])
    context = {"messages": messages,"list": caterer_list}
    return render(request, "admin/allocation.html", context)