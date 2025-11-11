from django.shortcuts import render, redirect

from reviews.forms import ReviewForm


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
            with open('data.csv', 'a') as file:
                file.write(f"{name}|{email}|{review}|{rating}\n")
            return redirect("reviews")

    with open('data.csv') as file:
        reviews = file.readlines()
        if len(reviews) > 0:
            reviews_data = reviews[0]
            name = reviews_data.split('|')[0]
            email = reviews_data.split('|')[1]
            review = reviews_data.split('|')[2]
            rating = reviews_data.split('|')[3]
            form = ReviewForm()
            return render(request, "reviews.html", {'form': form, 'name1': name, 'email1': email, 'review1': review, 'rating1': rating},)
        else:
            form = ReviewForm()
            return render(request, "reviews.html", {'form': form})

