from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import SalesReport


def sales_report(request):
    sales_reports = SalesReport.objects.all().order_by('-date')
    return render(request, "sales_report.html", {"sales_reports": sales_reports})


def download_sales_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Total Sales', 'Total Orders', 'Total Revenue'])

    for report in SalesReport.objects.all().order_by('-date'):
        writer.writerow([report.date, report.total_sales,
                        report.total_orders, report.total_revenue])

    return response
