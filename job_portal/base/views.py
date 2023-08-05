from django.shortcuts import render
from .models import Job, Employee_Details
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Create your views here.

class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user =True

    def get_success_url(self):
        return reverse_lazy('home')

def home(request):
    data = Job.objects.all()
    context = {'data': data}
    return render(request, 'base/main.html', context)

def emp(request):
    emp_data = Employee_Details.objects.all()
    items, created =  Employee_Details.objects.get_or_create(name="name", email_id="email_id", highest_education="highest_education", interview_date="interview_date")
    context ={'emp_data': emp_data, 'items': items}
    return render(request, 'base/emp.html', context)

