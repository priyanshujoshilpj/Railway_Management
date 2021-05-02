from django.shortcuts import render,redirect
from .forms import UserForm  
from .models import User  
from django.views import View

# Create your views here.  

class Index(View):
    def get(self, request):
        return redirect('/read')

class Create(View):
    def get(self, request):
        form = UserForm()  
        return render(request,'create.html',{'form':form})  

    def post(self, request):
        form = UserForm(request.POST,request.FILES) 
        if form.is_valid():  
            form.save()  
            return redirect('/read')  
            
class Read(View):
    def get(self, request):
        user = User.objects.all()  
        return render(request,"read.html",{'user':user}) 


class Update(View):
    def get(self, request,id):
        user = User.objects.get(id=id)  
        return render(request,'update.html', {'user':user})  

    def post(self,request,id):
        user = User.objects.get(id=id)  
        for i in request.POST:
            if i == 'csrfmiddlewaretoken':
                continue
            if i == 'name':
                if user.name != request.POST['user']:
                    user.name = request.POST['user']
            if i == 'email':
                if user.email != request.POST['email']:
                    user.email = request.POST['email']
            if i == 'contact':
                if user.contact != request.POST['contact']:
                    user.contact = request.POST['contact']
            if i == 'gender':
                if user.gender != request.POST['gender']:
                    user.gender = request.POST['gender']
            if i == 'usrStatus':
                if user.usrStatus != request.POST['usrStatus'] and request.POST['usrStatus'] != '':
                    user.usrStatus = request.POST['usrStatus']
            if i == 'age':
                if user.age != request.POST['age']:
                    user.age = request.POST['age']
            if i == 'date_of_journey':
                if user.date_of_journey != request.POST['date_of_journey'] and request.POST['date_of_journey'] != '':
                    user.date_of_journey = request.POST['date_of_journey']
            if i == 'seat':
                if user.seat != request.POST['seat']:
                    user.seat = request.POST['seat']
            if i == 'birthmark':
                if user.birthmark != request.POST['birthmark']:
                    user.birthmark = request.POST['birthmark']
            if i == 'usrImg':
                if request.POST['usrImg'] != '':
                    user.usrImg = request.FILES['usrImg']
        for i in request.FILES:
            if i == 'usrImg':
                if request.FILES['usrImg'] != '':
                    user.usrImg = request.FILES['usrImg']
        user.save()
        return redirect("/read")  



class Delete(View):
    def get(self,request,id):
        user = User.objects.get(id=id)  
        user.delete()  
        return redirect("/read")      

