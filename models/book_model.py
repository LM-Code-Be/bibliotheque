
from datetime import date, timedelta
from utils.helpers import dictfetchall

class BookModel:
    def __init__(self, mysql):
        self.db = mysql

    # --------------- CRUD --------------- #
    def get_all_books(self):
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM books ORDER BY id DESC")
        books = dictfetchall(cur)
        cur.close()
        return books

    def get_filtered_books(self, status: str | None, author: str | None):
        cur = self.db.connection.cursor()
        sql = "SELECT * FROM books WHERE 1=1"
        params = []
        if status:
            sql += " AND status = %s"
            params.append(status)
        if author:
            sql += " AND author LIKE %s"
            params.append(f"%{author}%")
        sql += " ORDER BY id DESC"
        cur.execute(sql, tuple(params))
        res = dictfetchall(cur)
        cur.close()
        return res

    def get_by_id(self, book_id: int):
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM books WHERE id=%s", (book_id,))
        row = cur.fetchone()
        cur.close()
        return row

    def insert_book(self, data: dict):
        cur = self.db.connection.cursor()
        cur.execute("""
            INSERT INTO books (title, author, summary, read_date, note, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data.get("title"),
            data.get("author"),
            data.get("summary"),
            data.get("read_date") or None,
            data.get("note") or None,
            data.get("status"),
        ))
        self.db.connection.commit()
        cur.close()

    def update_book(self, book_id: int, data: dict):
        cur = self.db.connection.cursor()
        cur.execute("""
            UPDATE books SET
                title=%s, author=%s, summary=%s,
                read_date=%s, note=%s, status=%s
            WHERE id=%s
        """, (
            data.get("title"),
            data.get("author"),
            data.get("summary"),
            data.get("read_date") or None,
            data.get("note") or None,
            data.get("status"),
            book_id,
        ))
        self.db.connection.commit()
        cur.close()

    def delete_book(self, book_id: int):
        cur = self.db.connection.cursor()
        cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
        self.db.connection.commit()
        cur.close()

    # --------------- Stats --------------- #
    def stats_status(self):
        """Retourne nb de livres par statut."""
        cur = self.db.connection.cursor()
        cur.execute("SELECT status, COUNT(*) AS nb FROM books GROUP BY status")
        rows = dictfetchall(cur)
        cur.close()

        # remet en forme pour Chart.js
        labels, values = [], []
        for r in rows:
            labels.append(r["status"])
            values.append(r["nb"])
        return {"labels": labels, "values": values}

    def stats_notes(self):
        """Retourne la note moyenne."""
        cur = self.db.connection.cursor()
        cur.execute("SELECT AVG(note) AS mean_note FROM books WHERE note IS NOT NULL")
        mean = cur.fetchone()["mean_note"]
        cur.close()
        return {"mean": round(mean or 0, 2)}
    
    # ---------- Résumé global ----------
    def stats_summary(self):
        cur = self.db.connection.cursor()
        cur.execute("""
            SELECT
              COUNT(*)                               AS total,
              SUM(status='à lire')                   AS to_read,
              SUM(status='en cours')                 AS reading,
              SUM(status='lu')                       AS finished,
              ROUND(AVG(note),2)                     AS avg_note
            FROM books
        """)
        row = cur.fetchone()
        cur.close()
        return row

    # ---------- Livres finis / mois (12 derniers) ----------
    def stats_monthly(self):
        cur = self.db.connection.cursor()
        cur.execute("""
            SELECT DATE_FORMAT(read_date,'%Y-%m') AS ym, COUNT(*) AS nb
            FROM books
            WHERE status='lu' AND read_date IS NOT NULL
              AND read_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
            GROUP BY ym ORDER BY ym
        """)
        rows = dictfetchall(cur)
        cur.close()

        # remet sous forme liste complète (même si mois = 0)
        labels, values = [], []
        today = date.today().replace(day=1)
        for i in range(11,-1,-1):
            d = today - timedelta(days=i*30)   # ~1 mois
            label = d.strftime("%Y-%m")
            labels.append(label)
            found = next((r["nb"] for r in rows if r["ym"]==label), 0)
            values.append(found)
        return {"labels": labels, "values": values}
