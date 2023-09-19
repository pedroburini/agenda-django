from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from contact.models import Contact

def create(request):
    context = {

    }
    return render(
        request,
        'contact/create.html',
        context
    )
