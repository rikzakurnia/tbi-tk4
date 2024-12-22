import numpy as np

def cosine_similarity(vec1, vec2):
    """Calculates cosine similarity between two vectors."""
    vec1, vec2 = np.ravel(vec1), np.ravel(vec2)
    norm_vec1, norm_vec2 = np.linalg.norm(vec1), np.linalg.norm(vec2)
    if norm_vec1 <= 0 or norm_vec2 <= 0:
        return 0
    return np.dot(vec1, vec2.T) / (norm_vec1 * norm_vec2)

def tfidf_similarity(doc, query, tfidf_vectorizer):
    """Calculates similarity using TF-IDF vectors."""
    doc_vector = tfidf_vectorizer.transform([doc]).toarray()
    query_vector = tfidf_vectorizer.transform([query]).toarray()
    return cosine_similarity(doc_vector, query_vector)

def lsa_similarity(doc, query, tfidf_vectorizer, lsa_model):
    """Calculates similarity using LSA."""
    doc_vector = tfidf_vectorizer.transform([doc])
    query_vector = tfidf_vectorizer.transform([query])
    return cosine_similarity(lsa_model.transform(doc_vector), lsa_model.transform(query_vector))

def doc2vec_similarity(doc, query, doc2vec_model):
    """Calculates similarity using Doc2Vec."""
    doc_vector = doc2vec_model.infer_vector(doc.split())
    query_vector = doc2vec_model.infer_vector(query.split())
    return cosine_similarity([doc_vector], [query_vector])

def generate_features(doc, query, tfidf_vectorizer, lsa_model, doc2vec_model):
    """Generates a feature vector for a document-query pair."""
    return np.array([
        tfidf_similarity(doc, query, tfidf_vectorizer),
        lsa_similarity(doc, query, tfidf_vectorizer, lsa_model),
        doc2vec_similarity(doc, query, doc2vec_model),
    ])
