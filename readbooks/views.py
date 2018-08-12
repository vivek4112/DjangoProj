import requests
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import books
from .import forms


# Create your views here.
def index(request):
    return render(request, "readbooks/index.html")

def book(request):
    
        name = request.POST["name"]
        search_key = request.POST["search_key"]

        key = "5JCTgW3KWZrZ302j2ouhQ"

        res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": key, "isbns": name})
        if res.status_code != 200:
           raise Exception("ERROR: API request unsuccessful.")
        data = res.json()
        data = data["books"]
        avg_rat = data[0]['average_rating']  
        book = books.objects.get(isbn__exact=name)
        user = request.user.id
        form = forms.CreateReview()
        context = {
            "book": book,
            "avg_rat": avg_rat,
            "user": user,
            "form": form
        }
    
        return render(request, "readbooks/book.html",context)

def Create_Review(request):
    if request.method == 'POST':
        form = forms.CreateReview(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userid=request.user
            b_id = request.POST["Bookid"]
            book = books.objects.get(id__exact=b_id)
            instance.bookid=book
            instance.save()
            return redirect("/readbooks/index")
           
    