from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from categories.models import Category  # Ensure correct import


def product_list(request):
    products = Product.objects.all().order_by('-id')
    paginator = Paginator(products, 15)  # Show 15 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "product_list.html", {"products": page_obj})


def product_add(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)

            # Ensure the selected category is valid
            selected_category_id = request.POST.get("category")
            if not selected_category_id or not Category.objects.filter(id=selected_category_id).exists():
                messages.error(request, "Invalid category selected.")
                return redirect("product_add")

            product.category = Category.objects.get(id=selected_category_id)
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect("product_list")

    else:
        form = ProductForm()

    return render(request, "product_add.html", {"form": form, "categories": categories})


def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "product_edit.html", {"form": form, "product": product, "categories": categories})


def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("product_list")
    return render(request, "product_delete.html", {"product": product})
