from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer_list.html", {"customers": customers})


def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully!")
            return redirect("customer_list")
    else:
        form = CustomerForm()
    return render(request, "customer_add.html", {"form": form})


def customer_edit(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully!")
            return redirect("customer_list")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "customer_add.html", {"form": form})


def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    messages.success(request, "Customer deleted successfully!")
    return redirect("customer_list")
