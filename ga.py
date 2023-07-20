import sqlite3 as sql

conn = sql.connect("commits.db")

c = conn.cursor()

create_stmt = """
CREATE TABLE IF NOT EXISTS branches(
    repo TEXT NOT NULL,
    parent TEXT NOT NULL,
    child TEXT NOT NULL,
    PRIMARY KEY (repo, parent, child)
)
"""

create_idx = "CREATE INDEX IF NOT EXISTS repos ON branches(repo)"

c.execute(create_stmt)
c.execute(create_idx)
