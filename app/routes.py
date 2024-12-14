from flask import Blueprint, render_template, request, current_app

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/results", methods=["POST"])
def results():
    query = request.form.get("query")

    # Using env variable
    ENV_EXAMPLE = current_app.config['ENV_EXAMPLE']

    # Mock results for now
    results = [
        {"title": "Mock Title 1", "snippet": "This is a snippet of result 1."},
        {"title": "Mock Title 2", "snippet": "This is a snippet of result 2."},
        {"title": ENV_EXAMPLE, "snippet": "This is a snippet of result 2."},

    ]
    return render_template("results.html", query=query, results=results)
