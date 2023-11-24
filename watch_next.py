import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_md')

# Movie descriptions
movies = {
    'A': "When Hiccup discovers Toothless isn't the only Night Fury, he must seek 'The Hidden World', a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
    'B': "After the death of Superman, several new people present themselves as possible successors.",
    'C': "A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.",
    'D': "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
    'E': "A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
    'F': "In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.",
    'G': "The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
    'H': "A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
    'I': "Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
    'J': "Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."
}


def find_similar_movie(description):
    similarity_scores = {}

    # Compare similarity between the input description and each movie description
    for key, movie_description in movies.items():
        similarity_scores[key] = nlp(
            movie_description).similarity(nlp(description))

    # Return the title of the most similar movie
    most_similar_movie = max(similarity_scores, key=similarity_scores.get)
    return f"Watch next: Movie {most_similar_movie}"


if __name__ == "__main__":
    # Example usage
    user_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    recommendation = find_similar_movie(user_description)
    print(recommendation)
