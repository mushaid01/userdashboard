from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,TemplateView

from .import forms
from .serializers import userserializer
# Create your views here.
def base(request):
    return render(request,'base.html')


class SignUp(CreateView):
    form_class=forms.UserCreateForm
    serializer_class=userserializer
    success_url=reverse_lazy('login')
    template_name='user/signup.html'



class dashboard(TemplateView):
    template_name='user/dashboard.html'






