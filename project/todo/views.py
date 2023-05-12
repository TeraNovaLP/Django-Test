from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_POST

from .forms import NewItemForm, UpdateItemForm
from .models import ToDo


@require_GET
def index(request: HttpRequest) -> HttpResponse:
    forms = []

    for item in ToDo.objects.all():
        forms.append({"id": item.id, "form": UpdateItemForm(instance=item)})

    return render(
        request, "todo/index.html", {"new_form": NewItemForm(), "item_forms": forms}
    )


@require_POST
def new(request: HttpRequest) -> HttpResponse:
    form = NewItemForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect("index")


@require_POST
def update(request: HttpRequest, id: int) -> HttpResponse:
    item = get_object_or_404(ToDo, id=id)
    form = UpdateItemForm(request.POST, instance=item)

    if form.is_valid():
        form.save()

    return redirect("index")
