from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm
from .models import Post
from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

def buscar_posts(request):
    query = request.GET.get('q')
    seleccion = request.GET.get('seleccion')
    resultados = Post.objects.filter(titulo__icontains=query) if query else Post.objects.all()
    if seleccion:
        resultados = resultados.filter(id=seleccion)
    return render(request, 'blog/buscar_posts.html', {'resultados': resultados, 'posts': Post.objects.all()})
