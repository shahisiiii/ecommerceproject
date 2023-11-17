from typing import Any
from django.shortcuts import render
from django.views.generic import CreateView,FormView,TemplateView,DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from ecommapp.forms import SignUpForm,SignInForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ecommapp.models import Products

# Create your views here.

class SignUpView(CreateView):
    template_name="register.html"
    form_class=SignUpForm
    model=User
    success_url=reverse_lazy("login")

class SignIn(FormView):
    template_name="login.html"
    form_class=SignInForm
    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get("username")
            pass_word=form.cleaned_data.get("password")
            user=authenticate(request,username=user_name,password=pass_word)
            if user:
                login(request,user)
                msg="Login successful"
                messages.success(request,msg)
                return render(request,"signin.html")
            else:
                msg="invalid credentials"
                messages.error(request,msg)
                return render (request,"signin.html")
            
class HomeView(TemplateView):
    template_name="homehtml"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Products.objects.all()
        context['products']=all_products
        return context
        
        

class ProductDetilView(DetailView):
    model =Products
    template_name="productdetail.html"
    pk_url_kwarg="id"
    context_object_name="product"