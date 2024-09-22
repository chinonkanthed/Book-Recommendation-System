from django.shortcuts import render, get_object_or_404
from .models import Book
from urllib.parse import unquote
import pickle
import numpy as np

# Load your data
popular_df = pickle.load(open('recommend/data/popular.pkl', 'rb'))
pt = pickle.load(open('recommend/data/pt.pkl', 'rb'))
books = pickle.load(open('recommend/data/books.pkl', 'rb'))
similarity_scores = pickle.load(open('recommend/data/similarity_scores.pkl', 'rb'))

def index(request):
    books_data = []
    for i in range(len(popular_df)):
        book = {
            'name': popular_df['Book-Title'].values[i],
            'author': popular_df['Book-Author'].values[i],
            'image': popular_df['Image-URL-M'].values[i],
            'votes': popular_df['num_ratings'].values[i],
            'rating': popular_df['avg_rating'].values[i]
        }
        books_data.append(book)

    context = {
        'books_data': books_data
    }
    return render(request, 'recommend/index.html', context)

def recommend_ui(request):
    return render(request, 'recommend/recommend.html')

def recommend(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        context = {'data': data}
        return render(request, 'recommend/recommend.html', context)
    return render(request, 'recommend/recommend.html')

def book_detail(request, book_title):
    # Decode the URL-encoded book title
    book_title = unquote(book_title)
    # Fetch the book with the given title
    book = get_object_or_404(Book, title=book_title)
    return render(request, 'recommend/book_detail.html', {'book': book})

def recommendation_page(request):
    recommended_books = Book.objects.all()  # Or your specific query to get recommended books
    return render(request, 'recommend/recommendations.html', {'recommended_books': recommended_books})