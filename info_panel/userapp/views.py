from django.shortcuts import render
from .count import get_count
from .progress import get_cumulative_user_count_per_date
import json

def info_panel(request):
    return render(request, 'panel.html', {"userCountPerCompany": get_count(), "cumulativeUserCountPerDate": json.dumps(get_cumulative_user_count_per_date())})
