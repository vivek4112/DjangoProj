import requests
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import books, Review
from django.contrib.auth.models import User
from .import forms


# Create your views here.
def index(request):
    return render(request, "readbooks/index.html")

def book(request):
        
        name = request.POST["name"] # getting the ISBN/Title of the book to be searched
        search_key = request.POST["search_key"] # getting the type(ISBN/Title) of the search

        # Defining an error message
        err_msg = {
           "message" : 'Book not Found!'
        }

        # Keys to make API calls to fetch book details, cover and critical reviews

        key = "5JCTgW3KWZrZ302j2ouhQ"  
        key2 = "9082ca37e18f3da7ce630243313c9c14b06e6b91"

        if search_key == "isbn":  #searching based on isbn
            if books.objects.filter(isbn=name).count() == 0:
                return render(request, "readbooks/error.html",err_msg)
            else:
                book = books.objects.get(isbn__exact=name)
                res_rev = requests.get("https://idreambooks.com/api/books/reviews.json",params={"q": name, "key": key2})
                rev_data = res_rev.json()
                

                if rev_data["total_results"] == 1:
                    rev_data = rev_data["book"]["critic_reviews"]
                else:
                    rev_data = [{"snippet":"danmsg"}]   

                book_review =Review.objects.filter(bookid=book.id)
                res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": key, "isbns": book.isbn})
                if res.status_code != 200:
                    return render(request, "readbooks/error.html",{"message" : 'ERROR: API request unsuccessful.Book not found on goodreads!'})
                data = res.json()
                data = data["books"]
                avg_rat = data[0]['average_rating']
                if res.status_code != 200: 
                   return render(request, "readbooks/error.html",err_msg)
        elif search_key == "title": #searching based on title
            if books.objects.filter(title=name).count() == 0:
                return render(request, "readbooks/error.html",err_msg)
            else:
                book = books.objects.get(title__exact=name)

                res_rev = requests.get("https://idreambooks.com/api/books/reviews.json",params={"q": book.isbn, "key": key2})
                rev_data = res_rev.json()
                

                if rev_data["total_results"] == 1:
                    rev_data = rev_data["book"]["critic_reviews"]
                else:
                    rev_data = [{"snippet":"danmsg"}]   

                book_review =Review.objects.filter(bookid=book.id)
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
        # Creating the context for rendering
        context = {
            "book": book,
            "avg_rat": avg_rat,
            "user": user,
            "form": form,
            "rev_data": rev_data,
            "book_review":book_review
        }
    
        return render(request, "readbooks/book.html",context)

# method to create and submit the Reviews by Customers
def Create_Review(request):
    if request.method == 'POST':
        user_id = request.user.id    # getting the user id of the logged-in/Authenticated user
        if User.objects.filter(id=user_id).count() != 0: 
            form = forms.CreateReview(request.POST) # creating review form using Create review class defined in forms.py
            if form.is_valid():
                instance = form.save(commit=False)
                instance.userid=request.user
                b_id = request.POST["Bookid"]
                book = books.objects.get(id__exact=b_id)
                if Review.objects.filter(bookid=b_id, userid=request.user.id).count() != 0:
                    return render(request, "readbooks/error.html",{"message" : 'You have submited the review for this book already!'}) 
                instance.bookid=book
                instance.save()    # Saving the review instance to database.
                return redirect('/')
        else:
            return render(request, "readbooks/error.html",{"message" : 'Please login or Register to submit a review!'})        
           
           
def about(request):
    return redirect('/readbooks/about')