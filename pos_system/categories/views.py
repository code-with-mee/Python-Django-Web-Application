from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Category
from .forms import CategoryForm


def category_list(request):
    category_list = Category.objects.all()
    paginator = Paginator(category_list, 15)  # Display 15 categories per page
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
    return render(request, "category_list.html", {"categories": categories})


def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully!")
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "category_add.html", {"form": form})


def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully!")
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "category_edit.html", {"form": form, "category": category})


def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Category deleted successfully!")
        return redirect("category_list")
    return render(request, "category_delete.html", {"category": category})
