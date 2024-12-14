from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/results", methods=["POST"])
def results():
    query = request.form.get("query")
    # Mock results for now
    results = [
        {"title": "Mock Title 1", "snippet": "This is a snippet of result 1."},
        {"title": "Mock Title 2", "snippet": "This is a snippet of result 2."},
    ]
    return render_template("results.html", query=query, results=results)
