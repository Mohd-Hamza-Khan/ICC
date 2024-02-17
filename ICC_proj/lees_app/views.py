from django.shortcuts import render, HttpResponse, redirect
from .models import Student

# Create your views here.


def all_entries(request):
    studs = Student.objects.all()
    context = {
        'studs': studs
    }
    return render(request, "index.html", context)



def add_entry(request):
    if request.method == "POST":
       enrollment_no = eval(request.POST['enrollment_no'])
       dept = (request.POST['dept'])
       year = eval(request.POST['year'])
       purpose = (request.POST['purpose'])
       new_stud = Student(enrollment_no=enrollment_no,dept=dept,year=year,purpose=purpose)
       new_stud.save()
    #    return HttpResponse("Entry Added Successfully")
       return all_entries(request)
    elif request.method == "GET":
        return all_entries(request)
    else:
        return HttpResponse("An Error Occured! Entry was not Added")
        
def delet(request,id):
    dele = Student.objects.get(id=id)
    il = dele.delete()
    return redirect(all_entries)

def filter(request):
   #create a filter function using youtube video

   if request.method == "POST":
       enrollment_no = eval(request.POST['enrollment_no'])
       dept = (request.POST['dept'])
       year = eval(request.POST['year'])
       purpose = (request.POST['purpose'])
       studs = Student.objects.all()
       if enrollment_no:
           studs = studs.filter(enrollment_no=enrollment_no)
       if dept:
           studs = studs.filter(dept=dept)
       if year:
           studs = studs.filter(year=year)
       if purpose:
           studs = studs.filter(purpose=purpose)
       context = {
        'studs': studs
       }
       return render(request, "select.html", context)
   elif request.method == "GET":
      return render(request,'select.html')
   else:
      return HttpResponse("An Error Occured! Entry is not Valid")
