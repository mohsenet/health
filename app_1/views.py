from django.http import HttpResponse
from django.shortcuts import render

from app_1.models import Health


def index(request):
    context = {
        "mohsen": "moghim"
    }
    return render(request, "app_1/index.html", {})


def report(request):
    all_data = Health.objects.all()
    date = request.POST.get("date")
    toothbrush = request.POST.get("toothbrush")
    sport = request.POST.get("sport")
    contex = {
        "date": date,
        "toothbrush": toothbrush,
        "sport": sport,
        "all_data": all_data,
    }
    obj = Health(date=date, toothbrush=toothbrush, sport=sport)
    obj.save()

    return render(request, 'app_1/report.html', contex)
