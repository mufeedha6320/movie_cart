from django.shortcuts import render, redirect
from . forms import Movie_form
from . models import table_movie

# Create your views here.
def index(request):
    obj = table_movie.objects.all()
    context = {
        'movie_list': obj
    }
    return render(request, 'index.html', context)

def detail(request,movie_id):
    obj_movie = table_movie.objects.get(id=movie_id)
    return render(request,'detail.html', {'key1':obj_movie})
def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        year = request.POST.get("year")
        img = request.FILES["img"]
        movie = table_movie(name=name, desc=desc, year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request, "add.html")
def update(request, id):
    old = table_movie.objects.get(id=id)
    my_form = Movie_form(request.POST or None, request.FILES, instance=old)
    if my_form.is_valid():
        my_form.save()
        return redirect('/')
    return render(request, 'edit.html', {'key_form':my_form, 'key_name':old})
def delete(request, id):
    if request.method == "POST":
        movie = table_movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')