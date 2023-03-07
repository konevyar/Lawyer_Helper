from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Case

# Create your views here.

def index(request):
    latest_cases_list = Case.objects.order_by('case_id')
    context = {
        'latest_cases_list': latest_cases_list,
        }
    return render(request, 'index.html', context)


def detail(request, case_id):
    case = get_object_or_404(Case, id=case_id)
    context = {'case': case,}
    return render(request, 'detail.html', context)
    
"""
    try:
        case = Case.objects.get(pk=case_id)
        context = {'case': case,}
    except Case.DoesNotExist:
        raise Http404("Дело не существует.")
    return render(request, 'LawHelp/detail.html', context)
"""
