"""
URL configuration for pos_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import login_view, logout_view
from categories.views import category_list, category_add, category_edit, category_delete
from products.views import product_list, product_add, product_delete, product_edit
from orders.views import order_list, order_add, order_edit, order_delete, dashboard_view, order_detail
from customers.views import customer_list, customer_add, customer_edit, customer_delete
from suppliers.views import supplier_list, supplier_add, supplier_edit, supplier_delete
from reports.views import sales_report, download_sales_report

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Ensure this line exists
    path('dashboard/', dashboard_view, name='dashboard'),

    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Category URLs
    path("categories/", category_list, name="category_list"),
    path("categories/add/", category_add, name="category_add"),
    path("categories/edit/<int:category_id>/",
         category_edit, name="category_edit"),
    path("categories/delete/<int:category_id>/",
         category_delete, name="category_delete"),

    # Product URLs
    path("products/", product_list, name="product_list"),
    path("products/add/", product_add, name="product_add"),
    path("products/edit/<int:product_id>/",
         product_edit, name="product_edit"),
    path("products/delete/<int:product_id>/",
         product_delete, name="product_delete"),

    # Order URLs
    path("orders/", order_list, name="order_list"),
    path("orders/<int:order_id>/", order_detail, name="order_detail"),
    path("orders/add/", order_add, name="order_add"),
    path("orders/edit/<int:order_id>/", order_edit, name="order_edit"),
    path("orders/delete/<int:order_id>/", order_delete, name="order_delete"),

    # Customer URLs
    path("customers/", customer_list, name="customer_list"),
    path("customers/add/", customer_add, name="customer_add"),
    path("customers/edit/<int:customer_id>/",
         customer_edit, name="customer_edit"),
    path("customers/delete/<int:customer_id>/",
         customer_delete, name="customer_delete"),

    # Supplier URLs
    path("suppliers/", supplier_list, name="supplier_list"),
    path("suppliers/add/", supplier_add, name="supplier_add"),
    path("suppliers/edit/<int:supplier_id>/",
         supplier_edit, name="supplier_edit"),
    path("suppliers/delete/<int:supplier_id>/",
         supplier_delete, name="supplier_delete"),

    # Reports
    path("reports/sales/", sales_report, name="sales_report"),
    path("reports/download/", download_sales_report,
         name="download_sales_report"),
]
