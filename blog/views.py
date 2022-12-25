from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel,Kategori
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def is_creator(user):
    if user.groups.filter(name='Creator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
        request.session['is_creator'] = 'creator'
    
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    print(artikel)
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)


@login_required
@user_passes_test(is_creator)
def users(request):
    template_name = "back/table_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)
      
        #simpan produk karena ada relasi ke tabel kategori 
        Artikel.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            kategori = kat,
        )
        return redirect (artikel)
    context = {
        'title':'Tambah Artikel',
        'kategori':kategori,

    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request ,id ):
    template_name = 'back/edit_artikel.html'
    kategori = Kategori.objects.all()
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        
        kategori = request.POST.get('kategori')
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kat = Kategori.objects.get(nama=kategori)

        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.judul = judul
        a.body = body
        a.kategori = kat
        a.save() 
        return redirect(artikel)
    context = {
        'title':'Edit Artikel',
        'kategori':kategori,
        'artikel' : artikel,

    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

# def sinkron_berita(request):
# 	url = "https://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=cf90c64250eb4cb2b85dcae943394920"
# 	data = requests.get(url).json()
# 	for d in data['articles']:
# 		cek_resep = Resep.objects.filter(nama=d['author'])
# 		if cek_resep:
# 			print('data sudah ada')
# 			c = cek_resep.first()
# 			c.nama=d['author']
# 			c.save()
# 		else: 
#       		#jika belum ada maka tulis baru kedatabase
# 			b = Resep.objects.create(
# 				idMeal = d['idMeal'],
#                 strMeal = d['strMeal'],
#                 strDrinkAlternate = d['strDrinkAlternate'],
#                 strCategory = d['strCategory'],
#                 strArea = d['strArea'],
#                 strInstructions = d['strInstructions'],
#                 strTags = d['strTags'],
#                 strYoutube = d['strYoutube'],
#                 strIngredient1 = d['strIngredient1'],
#                 strIngredient2 = d['strIngredient2'],
#                 strIngredient3 = d['strIngredient3'],
#                 strIngredient4 = d['strIngredient4'],
#                 strIngredient5 = d['strIngredient5'],
#                 strIngredient6 = d['strIngredient6'],
#                 strIngredient7 = d['strIngredient7'],
#                 strIngredient8 = d['strIngredient8'],
#                 strIngredient9 = d['strIngredient9'],
#                 strIngredient10 = d['strIngredient10'],
#                 strIngredient11 = d['strIngredient11'],
#                 strIngredient12 = d['strIngredient12'],
#                 strIngredient13 = d['strIngredient13'],
#                 strMeasure1 = d['strMeasure1'],
#                 strMeasure2 = d['strMeasure2'],
#                 strMeasure3 = d['strMeasure3'],
#                 strMeasure4 = d['strMeasure4'],
#                 strMeasure5 = d['strMeasure5'],
#                 strMeasure6 = d['strMeasure6'],
#                 strMeasure7 = d['strMeasure7'],
#                 strMeasure8 = d['strMeasure8'],
#                 strMeasure9 = d['strMeasure9'],
#                 strMeasure10 = d['strMeasure10'],
#                 strMeasure11 = d['strMeasure11'],
#                 strMeasure12 = d['strMeasure12'],
#                 strMeasure13 = d['strMeasure13'],
#                 strSource = d['strSource'],
#                 strImageSource = d['strImageSource'],
#                 strCreativeCommonsConfirmed = d['strCreativeCommonsConfirmed'],
#                 dateModified = d['dateModified'],
#                 strMealThumb = d['strMealThumb'],
#             )
# 	return redirect(resep)
# def hapus_berita(request,id):
#     Resep.objects.get(id=id).delete()
#     return redirect(resep)