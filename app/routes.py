from flask import Blueprint, render_template, request, current_app
from .retrieval.retrieve import retrieve_documents

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
        results = documents_retrieved

    return render_template("results.html", query=query, results=results)

@main.route('/view-document', methods=['POST'])
def view_document():
    doc_title = request.form['doc_title']
    doc_fulltext = request.form['doc_fulltext']
    print(doc_title)
    return render_template('view_document.html', title=doc_title, fulltext=doc_fulltext)