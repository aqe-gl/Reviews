from django.shortcuts import render

# Create your views here.
def reviews(request):
    name1 = "nick"
    email1 = "nick@gamil.com"
    review1 = "Nice View"

    name2 = request.GET.get("name")
    email2 = request.GET.get("email")
    review2 = request.GET.get("review")

    return render(request, "reviews.html", {'name1': name1, 'email1': email1, 'review1': review1, 'name2': name2, 'email2': email2, 'review2': review2})