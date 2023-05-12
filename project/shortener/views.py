from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import ShortForm
from .models import URL


# Create your views here.
@require_http_methods(["GET", "POST"])
def shortener(req: HttpRequest) -> HttpResponse:
    match req.method:
        case "GET":
            return render(req, "shortener/index.html", {"form": ShortForm()})
        case "POST":
            form = ShortForm(req.POST)
            print("START")

            if form.is_valid():
                url = URL(url=form.cleaned_data["url"])
                url.save()

                return render(
                    req, "shortener/index.html", {"form": ShortForm(), "id": url.id}
                )

    return HttpResponse("ERROR")


@require_GET
def resolve(request: HttpRequest, id: int) -> HttpResponse:
    url = get_object_or_404(URL, id=id)

    if url.url:
        return redirect(url.url)

    return redirect("index")
