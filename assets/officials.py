import mysql.connector

DATABASE_HOST = 'localhost'
DATABASE_USER = 'root'
DATABASE_NAME = 'jailguardian'
DATABASE_PASSWORD = 'root'


def reset_back_to_start() -> None:
    """
    Reset the database to the initial state.

    This function drops the existing 'officials' table and recreates it.

    Note:
        This action requires admin privilege.

    Returns:
        None
    """
    conn = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    c = conn.cursor()

    print("[WARNING!] You need admin privilege to clear and reset the data! Are you sure? (y/n/yes/no)")
    a = input()
    c.execute("DROP TABLE IF EXISTS officials")
    if a in ("y", "yes"):
        c.execute('''CREATE TABLE IF NOT EXISTS officials
                    (uid INT PRIMARY KEY,
                     name VARCHAR(255) NOT NULL,
                     password VARCHAR(255) NOT NULL
                     )''')

    conn.commit()
    conn.close()


def update_user(uid, name=None, password=None) -> None:
    """
    Update user information in the database.

    Args:
        uid: User ID of the user to update.
        name: New name (optional).
        password: New password (optional).

    Returns:
        None
    """
    conn = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    c = conn.cursor()
    update_fields = []

    if name is not None:
        update_fields.append(("name", name))
    if password is not None:
        update_fields.append(("password", password))

    if len(update_fields) > 0:
        update_query = "UPDATE officials SET "
        update_query += ", ".join(f"{field} = %s" for field, _ in update_fields)
        update_query += " WHERE uid = %s"
        values = [value for _, value in update_fields]
        values.append(uid)
        c.execute(update_query, values)

    conn.commit()
    conn.close()


def insert_user(uid, name, password) -> None:
    """
    Insert a new user into the database.

    Args:
        uid: User ID.
        name: name.
        password: Password.

    Returns:
        None
    """
    conn = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    c = conn.cursor()

    c.execute("INSERT INTO officials (uid, name, password) VALUES (%s, %s, %s)",
              (uid, name, password))

    conn.commit()
    conn.close()


def read_user(uid=-1) -> list:
    """
    Read user details from the database.

    Args:
        uid: User ID to retrieve. If -1, retrieve all officials.

    Returns:
        list: User details as a list of tuples.
    """
    conn = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    c = conn.cursor()

    if uid != -1:
        c.execute("SELECT * FROM officials WHERE uid = %s", (uid,))
        result = c.fetchone()
    else:
        c.execute("SELECT * FROM officials")
        result = c.fetchall()

    conn.close()

    return result
