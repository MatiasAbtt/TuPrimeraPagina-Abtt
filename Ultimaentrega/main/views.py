from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

from django.views.generic import ListView
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'main/page_list.html'
    context_object_name = 'pages'


from django.views.generic import DetailView

class PageDetailView(DetailView):
    model = Page
    template_name = 'main/page_detail.html'
    context_object_name = 'page'

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'main/page_form.html'
    success_url = reverse_lazy('page_list')

from django.views.generic.edit import UpdateView

class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'main/page_form.html'
    success_url = reverse_lazy('page_list')

from django.views.generic.edit import DeleteView

class PageDeleteView(DeleteView):
    model = Page
    template_name = 'main/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('login')  # Redirige al inicio de sesión después del registro
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})