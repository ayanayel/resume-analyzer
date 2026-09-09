import sqlite3


def connect():

    return sqlite3.connect("cv_database.db")


def create_database():

    db = connect()

    db.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER,
            matched TEXT,
            missing TEXT,
            weaknesses TEXT
        )
    """)

    db.commit()
    db.close()


def save_analysis(score, matched, missing, weaknesses):

    db = connect()

    db.execute(
        """
        INSERT INTO analyses
        (score, matched, missing, weaknesses)
        VALUES (?, ?, ?, ?)
        """,
        (
            score,
            ", ".join(matched),
            ", ".join(missing),
            ", ".join(weaknesses)
        )
    )

    db.commit()
    db.close()


def get_analyses():

    db = connect()

    data = db.execute(
        "SELECT * FROM analyses"
    ).fetchall()

    db.close()

    return data


def delete_analysis(id):

    db = connect()

    db.execute(
        "DELETE FROM analyses WHERE id = ?",
        (id,)
    )

    db.commit()
    db.close()


create_database()