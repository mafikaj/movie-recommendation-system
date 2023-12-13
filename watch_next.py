import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_md')


def read_movies_from_file(file_path):
    """
    Read movie descriptions from a file and return a dictionary.
    Each line in the file is treated as a separate movie description.
    The dictionary keys are movie titles (A, B, C, etc.).
    """
    movies = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            movies[chr(ord('A') + i)] = line.strip()
    return movies


def find_similar_movie(description, movies):
    """
    Find the most similar movie based on the input description.
    """
    similarity_scores = {}

    # Compare similarity between the input description and each movie description
    for key, movie_description in movies.items():
        similarity_scores[key] = nlp(
            movie_description).similarity(nlp(description))

    # Return the title of the most similar movie
    most_similar_movie = max(similarity_scores, key=similarity_scores.get)
    return f"Watch next: Movie {most_similar_movie}"


if __name__ == "__main__":
    # Read movie descriptions from the file
    movie_file_path = 'movies.txt'
    movies = read_movies_from_file(movie_file_path)

    # Example usage
    user_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    recommendation = find_similar_movie(user_description, movies)
    print(recommendation)
