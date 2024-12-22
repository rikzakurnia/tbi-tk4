from flask import Blueprint, render_template, request, current_app
from .retrieval.retrieve import retrieve_documents
from .utils import format_retrieved_data

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/results", methods=["POST"])
def results():
    query = request.form.get("query")

    documents_retrieved = retrieve_documents(query)

    results = []

    if documents_retrieved is not None:
        results = format_retrieved_data(documents_retrieved)

    return render_template("results.html", query=query, results=results)
