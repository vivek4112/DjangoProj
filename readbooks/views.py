import requests
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import books
from django.contrib.auth.models import User
from .import forms


# Create your views here.
def index(request):
    return render(request, "readbooks/index.html")

def book(request):
    
        name = request.POST["name"]
        search_key = request.POST["search_key"]
        err_msg = {
           "message" : 'Book not Found!'
        }

        key = "5JCTgW3KWZrZ302j2ouhQ"

        
        
        
        
        if search_key == "isbn":
            if books.objects.filter(isbn=name).count() == 0:
                return render(request, "readbooks/error.html",err_msg)
            else:
                book = books.objects.get(isbn__exact=name)
                res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": key, "isbns": book.isbn})
                if res.status_code != 200:
                    return render(request, "readbooks/error.html",{"message" : 'ERROR: API request unsuccessful.Book not found on goodreads!'})
                data = res.json()
                data = data["books"]
                avg_rat = data[0]['average_rating']
                if res.status_code != 200: 
                   return render(request, "readbooks/error.html",err_msg)
        elif search_key == "title":
            if books.objects.filter(title=name).count() == 0:
                return render(request, "readbooks/error.html",err_msg)
            else:
                book = books.objects.get(title__exact=name)
                res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": key, "isbns": book.isbn})
                if res.status_code != 200:
                    return render(request, "readbooks/error.html",{"message" : 'ERROR: API request unsuccessful.Book not found on goodreads!'})
                data = res.json()
                data = data["books"]
                avg_rat = data[0]['average_rating']
                if res.status_code != 200: 
                   return render(request, "readbooks/error.html",err_msg)
        else:
            return render(request, "readbooks/error.html",err_msg)             
                      
        
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
        user_id = request.user.id
        if User.objects.filter(id=user_id).count() != 0:
            form = forms.CreateReview(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.userid=request.user
                b_id = request.POST["Bookid"]
                book = books.objects.get(id__exact=b_id)
                instance.bookid=book
                instance.save()
                return redirect('/readbooks/index')
        else:
            return render(request, "readbooks/error.html",{"message" : 'Please login or Register to submit a review!'})        
           
           
    