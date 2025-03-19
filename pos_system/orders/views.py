from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderForm
from products.models import Product
from customers.models import Customer


def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    paginator = Paginator(orders, 15)  # Display 15 orders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "order_list.html", {"orders": page_obj})


def order_add(request):
    products = Product.objects.filter(status=True)
    customers = Customer.objects.all()

    if request.method == "POST":
        print("✅ Form submission received.")  # Debugging print
        print("📌 POST Data:", request.POST)  # Print all received data

        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            print("✅ Order saved:", order)  # Debugging print

            # Process order items
            product_ids = request.POST.getlist("product[]")
            quantities = request.POST.getlist("quantity[]")

            if not product_ids or not any(map(str.isdigit, quantities)):
                messages.error(
                    request, "⚠️ You must add at least one product with a valid quantity.")
                return render(request, "order_add.html", {"form": form, "products": products, "customers": customers})

            for i in range(len(product_ids)):
                try:
                    product = Product.objects.get(id=product_ids[i])
                    quantity = int(quantities[i])

                    # Debugging print
                    print(f"✅ Adding item: {product.name} (Qty: {quantity})")

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price
                    )

                    # Reduce stock
                    product.stock -= quantity
                    product.save()
                except Exception as e:
                    print("❌ Error adding product:", e)  # Print the error

            # Update total
            order.update_total()
            print("✅ Order total updated.")  # Debugging print
            messages.success(request, "✅ Order added successfully!")
            return redirect("order_list")

        else:
            print("❌ Form is invalid!")  # Debugging print
            print("📌 Errors:", form.errors)  # Show form errors in console
            messages.error(
                request, "⚠️ Form is invalid. Please check the fields.")

    else:
        form = OrderForm()

    return render(request, "order_add.html", {"form": form, "products": products, "customers": customers})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.filter(
        order=order)  # Ensure this fetches related items
    return render(request, "order_detail.html", {"order": order, "order_items": order_items})


def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    products = Product.objects.filter(status=True)
    customers = Customer.objects.all()
    order_items = OrderItem.objects.filter(order=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            OrderItem.objects.filter(order=order).delete()

            # Process updated order items
            product_ids = request.POST.getlist("product[]")
            quantities = request.POST.getlist("quantity[]")

            if not product_ids or not any(map(str.isdigit, quantities)):
                messages.error(
                    request, "⚠️ You must add at least one product with a valid quantity.")
                return render(request, "order_edit.html", {
                    "form": form, "order": order, "products": products, "customers": customers, "order_items": order_items
                })

            for i in range(len(product_ids)):
                try:
                    product = Product.objects.get(id=product_ids[i])
                    quantity = int(quantities[i])

                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price
                    )

                    # Reduce stock
                    product.stock -= quantity
                    product.save()
                except Exception as e:
                    print("❌ Error updating product in order:", e)

            # Update total
            order.update_total()
            messages.success(request, "Order updated successfully!")
            return redirect("order_list")

    else:
        form = OrderForm(instance=order)

    return render(request, "order_edit.html", {
        "form": form, "order": order, "products": products, "customers": customers, "order_items": order_items
    })


def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        order.delete()
        messages.success(request, "Order deleted successfully!")
        return redirect("order_list")
    return render(request, "order_delete.html", {"order": order})


def dashboard_view(request):
    # Ensure this file exists in templates/
    return render(request, "dashboard.html")
