from django.shortcuts import render


# Create your views here.
def main(request):
    username = "Anton"
    return render(request, "main_page.html", {"name": username})
