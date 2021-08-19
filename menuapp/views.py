from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Menu
from .forms import MenuForm

# Create your views here.
def menu_list(request) :
    menus = Menu.objects.order_by('id')
    return render(request, 'menu_list.html', { 'menus' : menus })

def menu_add(request) :
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'menu_edit.html', { 'form': form })

def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk = pk)
    return render(request, 'menu_detail.html', {'menu': menu})

def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk = pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu_edit.html', { 'form': form })

def menu_delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        menu.delete()
        return redirect('menu_list')

    return render(request, 'menu_delete.html', {})       