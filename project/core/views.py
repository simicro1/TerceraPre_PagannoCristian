from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import CustomAuthenticationForm, CustomUserCreationForm

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def error404(request):
    return render(request, "core/error404.html")
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html", {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})