"""
helpers.py – ptites fonctions utilitaires
"""

def dictfetchall(cursor):
    """Convertit le résultat d’un cursor (DictCursor) en liste de dicts."""
    return [row for row in cursor.fetchall()]
