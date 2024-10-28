from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load pickled data once at startup to avoid redundant loads
with open('models/popular.pkl', 'rb') as f:
    popular_df = pickle.load(f)
with open('models/books.pkl', 'rb') as f:
    books = pickle.load(f)
with open('models/pt.pkl', 'rb') as f:
    pt = pickle.load(f)
with open('models/similarity_scores.pkl', 'rb') as f:
    similarity_scores = pickle.load(f)

# Homepage route for Top 50 Books
@app.route('/')
def index():
    return render_template('index.html', books=popular_df)

# Recommendation route for searching similar books
@app.route('/recommend', methods=['POST'])
def recommend():
    book_name = request.form.get('book_name')

    if not book_name:
        return render_template('recommend.html', books=[], error="Please enter a book name.")
    
    try:
        # Check if book is in pivot table index
        if book_name not in pt.index:
            raise ValueError("Book not found")

        # Get book recommendations
        index = pt.index.get_loc(book_name)
        similar_items = sorted(enumerate(similarity_scores[index]), key=lambda x: x[1], reverse=True)[1:11]
        
        # Collect book details for recommended books
        recommended_books = [
            {
                'title': pt.index[i[0]],
                'author': books.loc[books['Book-Title'] == pt.index[i[0]], 'Book-Author'].values[0],
                'image': books.loc[books['Book-Title'] == pt.index[i[0]], 'Image-URL-M'].values[0],
                'published': books.loc[books['Book-Title'] == pt.index[i[0]], 'Year-Of-Publication'].values[0]
            }
            for i in similar_items
        ]

        return render_template('recommend.html', books=recommended_books, search_term=book_name)

    except (IndexError, ValueError):
        return render_template('recommend.html', books=[], search_term=book_name, error="Book not found")

if __name__ == '__main__':
    app.run(debug=True)
