from django.shortcuts import render, redirect

from reviews.forms import ReviewForm
from reviews.models import Review


# Create your views here.
def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            Review.objects.create(name=name, email=email, review=review, rating=rating)
            return redirect("reviews")

    form = ReviewForm()
    all_reviews = Review.objects.all()
    return render(request, "reviews.html", {'form': form, 'reviews': all_reviews})

