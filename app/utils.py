def format_retrieved_data(retrieved_data):
    """Formats retrieved data into a dictionary with title and snippet."""
    formatted_results = []
    for idx, (docno, text) in enumerate(retrieved_data, start=1):
        formatted_results.append({
            "title": f"Document {docno}", 
            "snippet": f"{text[:200]}...",  
        })
    return formatted_results