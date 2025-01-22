# Book Recommender System

A web application that recommends books based on user preferences using popularity-based and collaborative filtering methods.

## Description

This project is a book recommender system built with Flask, Pandas, and Scikit-learn. It provides two types of recommendations:
- **Popularity-Based Recommendations**: Recommends books that are popular among all users.
- **Collaborative Filtering Recommendations**: Recommends books based on the similarity of user preferences.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Book-Recommender-System.git
    cd Book-Recommender-System
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the dataset and place it in the  directory.

5. Run the Jupyter notebook to preprocess the data and generate the model files:
    ```sh
    jupyter notebook book_recommender_system.ipynb
    ```

6. Start the Flask application:
    ```sh
    python app.py
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Use the search form to get book recommendations based on a book title.
3. Browse the top 50 books recommended by the system.



## Acknowledgements

- [Pandas](https://pandas.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
