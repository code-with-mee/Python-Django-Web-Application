from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Order, OrderItem
from .forms import OrderForm


def order_list(request):
    order_list = Order.objects.all()
    paginator = Paginator(order_list, 15)  # Display 15 orders per page
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    return render(request, "orders/order_list.html", {"orders": orders})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, "orders/order_detail.html", {"order": order, "order_items": order_items})


def order_add(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order added successfully!")
            return redirect("order_list")
    else:
        form = OrderForm()
    return render(request, "orders/order_add.html", {"form": form})


def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order updated successfully!")
            return redirect("order_list")
    else:
        form = OrderForm(instance=order)
    return render(request, "orders/order_add.html", {"form": form})


def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    messages.success(request, "Order deleted successfully!")
    return redirect("order_list")


def dashboard_view(request):
    # Ensure this file exists in templates/
    return render(request, "dashboard.html")
