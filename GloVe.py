import numpy as np
from numpy.linalg import norm

# Function to load GloVe embeddings
def load_glove_embeddings(file_path):
    embeddings_index = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
    return embeddings_index

# Function to calculate cosine similarity
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# Function to calculate Euclidean distance
def euclidean_distance(vec1, vec2):
    return norm(vec1 - vec2)

# Load GloVe embeddings (example path)
glove_file = 'path/to/glove.6B.100d.txt'
embeddings_index = load_glove_embeddings(glove_file)

# Get embeddings for two words
word1 = 'king'
word2 = 'queen'
vec1 = embeddings_index.get(word1)
vec2 = embeddings_index.get(word2)

if vec1 is not None and vec2 is not None:
    # Calculate cosine similarity
    cos_sim = cosine_similarity(vec1, vec2)
    print(f'Cosine similarity between "{word1}" and "{word2}": {cos_sim}')
    
    # Calculate Euclidean distance
    eucl_dist = euclidean_distance(vec1, vec2)
    print(f'Euclidean distance between "{word1}" and "{word2}": {eucl_dist}')
else:
    print(f'One of the words "{word1}" or "{word2}" not found in GloVe embeddings')
