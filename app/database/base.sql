CREATE TABLE users(
    id INTEGER PRIMARY KEY autoincrement,
    username VARCHAR(20) UNIQUE,
    password VARCHAR(80)
)