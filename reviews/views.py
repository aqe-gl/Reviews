from django.shortcuts import render, redirect

from reviews.forms import ReviewForm


# Create your views here.
def reviews(request):
    name1 = "nick"
    email1 = "nick@gamil.com"
    review1 = "Nice View"

    if request.method == "GET":
        form = ReviewForm()
        return render(request, "reviews.html",
                      {'form': form, 'name1': name1, 'email1': email1, 'review1': review1})
    elif request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return redirect("reviews")
        else:
            form = ReviewForm()
            return render(request, "reviews.html",
                          {'form': form, 'name1': name1, 'email1': email1, 'review1': review1})
    else:
        form = ReviewForm()
        return render(request, "reviews.html",
                      {'form': form, 'name1': name1, 'email1': email1, 'review1': review1})


