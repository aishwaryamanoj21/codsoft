
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: User ratings for movies
user_ratings = {
    'Aishu': {'angry bird': 5, 'Titanic': 3, 'Avatar': 4},
    'tara': {'angry bird': 4, 'Titanic': 5, 'Avatar': 5},
    'sara': {'angry bird': 5, 'Titanic': 4},
    'kiara': {'Titanic': 5, 'Avatar': 4},
    'sallu': {'angry bird': 3, 'Avatar': 4},
}

def get_user_similarity(user_ratings):
    users = list(user_ratings.keys())
    ratings_matrix = []

    for user in users:
        ratings = []
        for movie in all_movies:
            ratings.append(user_ratings[user].get(movie, 0))
        ratings_matrix.append(ratings)

    ratings_matrix = np.array(ratings_matrix)
    similarity_matrix = cosine_similarity(ratings_matrix)

    return users, similarity_matrix

all_movies = set(movie for ratings in user_ratings.values() for movie in ratings)
users, similarity_matrix = get_user_similarity(user_ratings)
print("User Similarity Matrix:")
print(similarity_matrix)

def recommend_movies(target_user, user_ratings, users, similarity_matrix, n_recommendations=3):
    target_index = users.index(target_user)
    similarity_scores = similarity_matrix[target_index]
    target_user_movies = set(user_ratings[target_user].keys())
    movie_scores = {}
    for i, user in enumerate(users):
        if user == target_user:
            continue
        weight = similarity_scores[i]
        for movie, rating in user_ratings[user].items():
            if movie not in target_user_movies:
                if movie not in movie_scores:
                    movie_scores[movie] = 0
                movie_scores[movie] += rating * weight
    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

    return [movie for movie, score in recommended_movies[:n_recommendations]]
recommendations = recommend_movies('Aishu', user_ratings, users, similarity_matrix)
print("Recommended Movies for Aishu:", recommendations)

