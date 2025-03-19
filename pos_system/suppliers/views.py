from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Supplier
from .forms import SupplierForm


def supplier_list(request):
    supplier_list = Supplier.objects.all()
    paginator = Paginator(supplier_list, 15)  # Display 15 suppliers per page
    page_number = request.GET.get('page')
    suppliers = paginator.get_page(page_number)
    return render(request, "supplier_list.html", {"suppliers": suppliers})


def supplier_add(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier added successfully!")
            return redirect("supplier_list")
    else:
        form = SupplierForm()
    return render(request, "supplier_add.html", {"form": form})


def supplier_edit(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier updated successfully!")
            return redirect("supplier_list")
    else:
        form = SupplierForm(instance=supplier)
    return render(request, "supplier_edit.html", {"form": form, "supplier": supplier})


def supplier_delete(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == "POST":
        supplier.delete()
        messages.success(request, "Supplier deleted successfully!")
        return redirect("supplier_list")
    return render(request, "supplier_delete.html", {"supplier": supplier})
