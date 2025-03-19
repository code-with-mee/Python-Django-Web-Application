from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
import csv
from .models import SalesReport


def sales_report(request):
    sales_reports = SalesReport.objects.all()
    paginator = Paginator(sales_reports, 15)  # Display 15 reports per page
    page_number = request.GET.get('page')
    sales_reports = paginator.get_page(page_number)
    return render(request, "sales_report.html", {"sales_reports": sales_reports})


def download_sales_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Total Sales', 'Total Orders', 'Total Revenue'])

    for report in SalesReport.objects.all():
        writer.writerow([report.date, report.total_sales,
                        report.total_orders, report.total_revenue])

    return response
