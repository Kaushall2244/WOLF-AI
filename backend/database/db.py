import sqlite3
from pathlib import Path
from datetime import datetime

DB_DIR = Path(__file__).parent


class DatabaseManager:
    def __init__(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)
        self.profile_db = DB_DIR / "profile.db"
        self.memory_db = DB_DIR / "memory.db"
        self.history_db = DB_DIR / "history.db"
        self.chat_db = DB_DIR / "chat.db"
        self._init_tables()

    def _get_connection(self, db_path):
        conn = sqlite3.connect(str(db_path))
        conn.row_factory = sqlite3.Row
        return conn

    def _init_tables(self):
        # Profile DB
        with self._get_connection(self.profile_db) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS profile (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

        # Long-Term Memory DB
        with self._get_connection(self.memory_db) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    key TEXT NOT NULL,
                    value TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

        # Command History DB
        with self._get_connection(self.history_db) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    command TEXT NOT NULL,
                    intent TEXT,
                    response TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

        # Chat DB
        with self._get_connection(self.chat_db) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS chat (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender TEXT NOT NULL,
                    message TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            conn.commit()

    # --- Profile Methods ---
    def set_profile(self, key: str, value: str):
        with self._get_connection(self.profile_db) as conn:
            conn.execute(
                """
                INSERT INTO profile (key, value, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
                """,
                (key, value, datetime.now())
            )
            conn.commit()

    def get_profile(self, key: str, default=None):
        with self._get_connection(self.profile_db) as conn:
            cur = conn.execute("SELECT value FROM profile WHERE key = ?", (key,))
            row = cur.fetchone()
            return row["value"] if row else default

    # --- Memory Methods ---
    def remember(self, category: str, key: str, value: str):
        with self._get_connection(self.memory_db) as conn:
            conn.execute(
                """
                INSERT INTO memory (category, key, value, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (category, key, value, datetime.now())
            )
            conn.commit()

    def recall(self, category: str = None, key: str = None):
        with self._get_connection(self.memory_db) as conn:
            if category and key:
                cur = conn.execute(
                    "SELECT value FROM memory WHERE category = ? AND key = ? ORDER BY id DESC LIMIT 1",
                    (category, key)
                )
                row = cur.fetchone()
                return row["value"] if row else None
            elif category:
                cur = conn.execute(
                    "SELECT key, value FROM memory WHERE category = ? ORDER BY id DESC",
                    (category,)
                )
                return [dict(r) for r in cur.fetchall()]
            else:
                cur = conn.execute("SELECT category, key, value FROM memory ORDER BY id DESC")
                return [dict(r) for r in cur.fetchall()]

    # --- History Methods ---
    def log_history(self, command: str, intent: str = None, response: str = None):
        with self._get_connection(self.history_db) as conn:
            conn.execute(
                """
                INSERT INTO history (command, intent, response, timestamp)
                VALUES (?, ?, ?, ?)
                """,
                (command, intent, response, datetime.now())
            )
            conn.commit()

    def get_last_history(self):
        with self._get_connection(self.history_db) as conn:
            cur = conn.execute("SELECT command, intent, response FROM history ORDER BY id DESC LIMIT 1")
            row = cur.fetchone()
            return dict(row) if row else None


db = DatabaseManager()
