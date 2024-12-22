import pyterrier as pt
from .models import index, bm25, load_models
from .features import generate_features

tfidf_vectorizer, lsa_model, doc2vec_model, lmart_model = load_models()

def generate_pipeline():
    """Generates a retrieval pipeline with BM25 and LambdaMART."""
    features = pt.apply.doc_features(lambda row: generate_features(
        row["text"], row["query"], tfidf_vectorizer, lsa_model, doc2vec_model))
    CUT_OFF = 30
    pipeline = (bm25 % CUT_OFF) >> pt.text.get_text(index, "text") >> (features ** bm25)
    return pipeline >> pt.ltr.apply_learned_model(lmart_model, form="ltr")
