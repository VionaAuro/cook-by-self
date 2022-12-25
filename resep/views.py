from blog.models import Artikel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.db import  transaction
from django.contrib.auth.hashers import make_password 

from blog.models import Artikel
from blog.views import artikel
from user.models import Biodata
import requests

def home(request):
    template_name = 'front/home.html'
    context = {
        'title':'my home',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)

def blog_post(request):
    template_name = 'front/hidangan-mahal.html'
    context = {
        'title':'about me',
        'welcome':'ini page about',
    }
    return render(request, template_name, context)
def blog_page(request):
    template_name = 'front/blog-page.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'Blog me',
        'welcome':'ini page about',
        'artikel' : artikel
    }
    return render(request, template_name, context)

def hidangan_mahal(request):
    template_name = 'front/hidangan_mahal.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'Hidangan Mahal',
        'artikel':artikel
    }
    return render(request, template_name, context)

def blog_page(request):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?f=a"


    data = requests.get(url).json()

    a = data['meals']
    idMeal = []
    strMeal = []
    strDrinkAlternate = []
    strCategory = []
    strArea =[]
    strInstructions = []
    strTags = []
    strYoutube = []
    strIngredient1 = []
    strIngredient2 = []
    strIngredient3 = []
    strIngredient4 = []
    strIngredient5 = []
    strIngredient6 = []
    strIngredient7 = []
    strIngredient8 = []
    strIngredient9 = []
    strIngredient10 = []
    strIngredient11= []
    strIngredient12= []
    strIngredient13= []
    strMeasure1 = []
    strMeasure2 = []
    strMeasure3 = []
    strMeasure4 = []
    strMeasure5 = []
    strMeasure6 = []
    strMeasure7 = []
    strMeasure8 = []
    strMeasure9 = []
    strMeasure10 = []
    strMeasure11 = []
    strMeasure12 = []
    strMeasure13 = []
    strSource = []
    strImageSource = []
    strCreativeCommonsConfirmed = []
    dateModified = []
    strMealThumb = []

    for i in range(len(a)):
        f = a[i]

        idMeal.append(f['idMeal'])
        strMeal.append(f['strMeal'])
        strDrinkAlternate.append(f['strDrinkAlternate'])
        strCategory.append(f['strCategory'])
        strArea.append(f['strArea'])
        strInstructions.append(f['strInstructions'])
        strTags.append(f['strTags'])
        strYoutube.append(f['strYoutube'])
        strIngredient1.append(f['strIngredient1'])
        strIngredient2.append(f['strIngredient2'])
        strIngredient3.append(f['strIngredient3'])
        strIngredient4.append(f['strIngredient4'])
        strIngredient5.append(f['strIngredient5'])
        strIngredient6.append(f['strIngredient6'])
        strIngredient7.append(f['strIngredient7'])
        strIngredient8.append(f['strIngredient8'])
        strIngredient9.append(f['strIngredient9'])
        strIngredient10.append(f['strIngredient10'])
        strIngredient11.append(f['strIngredient11'])
        strIngredient12.append(f['strIngredient12'])
        strIngredient13.append(f['strIngredient13'])
        strMeasure1.append(f['strMeasure1'])
        strMeasure2.append(f['strMeasure2'])
        strMeasure3.append(f['strMeasure3'])
        strMeasure4.append(f['strMeasure4'])
        strMeasure5.append(f['strMeasure5'])
        strMeasure6.append(f['strMeasure6'])
        strMeasure7.append(f['strMeasure7'])
        strMeasure8.append(f['strMeasure8'])
        strMeasure9.append(f['strMeasure9'])
        strMeasure10.append(f['strMeasure10'])
        strMeasure11.append(f['strMeasure11'])
        strMeasure12.append(f['strMeasure12'])
        strMeasure13.append(f['strMeasure13'])
        strSource.append(f['strSource'])
        strImageSource.append(f['strImageSource'])
        strCreativeCommonsConfirmed.append(f['strCreativeCommonsConfirmed'])
        dateModified.append(f['dateModified'])
        strMealThumb.append(f['strMealThumb'])

    mylist = zip(idMeal, strMeal, strDrinkAlternate, strCategory, strArea, strInstructions,  strTags, strYoutube, strIngredient1, strIngredient2, strIngredient3, strIngredient4, strIngredient5, strIngredient6, strIngredient7, strIngredient8, strIngredient9, strIngredient10, strIngredient11, strIngredient12, strIngredient13, strMeasure1, strMeasure2, strMeasure3, strMeasure4, strMeasure5, strMeasure6, strMeasure7, strMeasure8, strMeasure9, strMeasure10, strMeasure11, strMeasure12, strMeasure13, strSource, strImageSource, strCreativeCommonsConfirmed, dateModified,strMealThumb)
    context ={'mylist':mylist}

    return render(request, 'front/blog-page.html', context)

def base(request):
    template_name = 'front/base.html'
    context = {
        'title':'Tabel',
    }
    return render(request, template_name, context)

def about_us(request):
    template_name = 'front/about-us.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def contact_us(request):
    template_name = 'front/contact-us.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def isi(request):
    template_name = 'front/isi.html'
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('home')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(home)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)


