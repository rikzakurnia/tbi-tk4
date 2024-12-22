import pickle
import tempfile
from gensim.models import Doc2Vec
import xgboost as xgb
import pyterrier as pt
import zipfile
import os

temp_dir = tempfile.mkdtemp()
os.environ["PYTERRIER_HOME"] = temp_dir

if not pt.started():
    pt.init(version="snapshot")

TFIDF_MODEL_PATH = os.path.abspath("./app/model/tfidf_vectorizer.pkl")
LSA_MODEL_PATH = os.path.abspath("./app/model/lsa_model.pkl")
DOC2VEC_MODEL_PATH = os.path.abspath("./app/model/doc2vec_model.model")
LMART_MODEL_PATH = os.path.abspath( "./app/model/lmart_model.json")
INDEX_PATH = os.path.abspath('./app/model/index.zip')

INDEX_FOLDER_PATH = os.path.abspath("./index")

with zipfile.ZipFile(INDEX_PATH, 'r') as zipf:
    zipf.extractall('./index')

index = pt.IndexFactory.of(INDEX_FOLDER_PATH)
bm25 = pt.terrier.Retriever(index, wmodel="BM25")

def load_models():
    """Loads and returns all required models."""
    with open(TFIDF_MODEL_PATH, "rb") as file:
        tfidf_vectorizer = pickle.load(file)

    with open(LSA_MODEL_PATH, "rb") as file:
        lsa_model = pickle.load(file)

    doc2vec_model = Doc2Vec.load(DOC2VEC_MODEL_PATH)

    lmart_model = xgb.XGBRanker()
    lmart_model.load_model(LMART_MODEL_PATH)

    return tfidf_vectorizer, lsa_model, doc2vec_model, lmart_model
