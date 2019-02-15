from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from .models import Producto

from .forms import Add_form

def home(request):
    model = Producto
    if request.method == "POST":
        form = Add_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home',)
    else:
        form = Add_form()

    
    print(model.objects.all())

    return render(request, 'home.html',{'form': form,'productos': model.objects.all()})

def prod_edit(request, pk):
    model = Producto
    post = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = Add_form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home',)
    else:
        form = Add_form(instance=post)
    return render(request, 'edit.html',{'form': form,})

def prod_delete(request, pk):
    model = Producto
    post = Producto.objects.filter(pk=pk)
    if post.exists():
        post.delete()
        return redirect('home',)
    
    return render(request, 'home.html',{})