

from django.shortcuts import render
from .models import Year,Business,Month,Incomes

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "finapp/index.html")

def year(request):
    year = Year.objects.order_by('year')
    content = {"year": year}
    return render(request, 'finapp/year.html', content)

def years(request, year_id):
    years = Year.objects.get(id=year_id)
    month = years.entry_set.order_by('month')
    context = {"year":years, "month": month}
    return render(request, 'finapp/year.html', context)

def month(request):
    month = Month.objects.order_by('month')
    content = {"month": month}
    return render(request, 'finapp/month.html', content)

def months(request, month_id):
    months = Month.objects.get(id=month_id)
    business = months.entry_set.order_by('month')
    context = {"months":months, "business":business}
    return render(request, 'finapp/month.html', context)

def business(request):
    business= Business.objects.order_by('business')
    content = {"business": business}
    return render(request, 'finapp/business.html', content)

def businesss(request, business_id):
    businesss = Business.objects.get(id=business_id)
    income = businesss.entry_set.order_by('business')
    context = {"business":businesss, "income":income}
    return render(request, 'finapp/business.html', context)

