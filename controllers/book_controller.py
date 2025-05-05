"""
book_controller.py – routes & logique web
Les flash / redirect / etc sont gérés ici
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash

book_bp = Blueprint("book_bp", __name__)
model = None   # sera injecté depuis app.py

# -------------------- LISTE + FILTRE -------------------- #
@book_bp.route("/")
def index():
    status = request.args.get("status")
    author = request.args.get("author")
    books = model.get_filtered_books(status, author) if (status or author) else model.get_all_books()
    return render_template("index.html", books=books)

# -------------------- AJOUT -------------------- #
@book_bp.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        model.insert_book(request.form)
        flash("Livre ajouté !")
        return redirect(url_for("book_bp.index"))
    return render_template("add_book.html")

# -------------------- MODIF -------------------- #
@book_bp.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = model.get_by_id(book_id)
    if not book:
        flash("Livre introuvable…", "warning")
        return redirect(url_for("book_bp.index"))

    if request.method == "POST":
        model.update_book(book_id, request.form)
        flash("Livre mis à jour ✔")
        return redirect(url_for("book_bp.index"))

    return render_template("edit_book.html", book=book)

# -------------------- SUPPR -------------------- #
@book_bp.route("/delete/<int:book_id>")
def delete_book(book_id):
    model.delete_book(book_id)
    flash("Livre supprimé 🗑️")
    return redirect(url_for("book_bp.index"))

# -------------------- STATS -------------------- #

@book_bp.route("/stats")
def stats():
    summary = model.stats_summary()
    summary_cards = [
        {"label":"Total",        "value": summary["total"]},
        {"label":"À lire",       "value": summary["to_read"]},
        {"label":"En cours",     "value": summary["reading"]},
        {"label":"Terminés",     "value": summary["finished"]},
        {"label":"Note moy.",    "value": summary["avg_note"] or "–"},
    ]

    return render_template("stats.html",
                           summary_cards=summary_cards,
                           stats_status = model.stats_status(),
                           stats_monthly= model.stats_monthly())
