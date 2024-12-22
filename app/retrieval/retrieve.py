import re
import contractions
import pandas as pd
from .pipeline import generate_pipeline

def preprocess_query(query):
    """Preprocesses a query by normalizing, expanding, and cleaning."""
    query = contractions.fix(query.lower())
    query = re.sub('[\\W_]+', ' ', query)
    return pd.DataFrame([{"qid": "Qsearch", "query": query}])

PIPELINE = generate_pipeline()

def retrieve_documents(query):
    """Retrieves ranked documents for a given query."""
    preprocessed_query = preprocess_query(query)
    try:
        result_df = PIPELINE.transform(preprocessed_query).sort_values(by='score', ascending=False)
        filtered_result = result_df[["docno", "text"]]
        return [tuple(x) for x in filtered_result.to_records(index=False)]
    except Exception:
        return []