import mysql.connector
import random


DATABASE_HOST = 'localhost'
DATABASE_USER = 'root'
DATABASE_NAME = 'jailguardian'
DATABASE_PASSWORD = 'root'


def reset_back_to_start() -> None:
    """
    Reset the database to the initial state.

    This function drops the existing 'inmates' table and recreates it.

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
    c.execute("DROP TABLE IF EXISTS inmates")
    if a in ("y", "yes"):
        c.execute('''CREATE TABLE IF NOT EXISTS inmates
                    (uid VARCHAR(255) PRIMARY KEY,
                     name VARCHAR(255) NOT NULL,
                     dob DATE NOT NULL,
                     adhar VARCHAR(255) NOT NULL,
                     nationality VARCHAR(255) NOT NULL,
                     state VARCHAR(255) NOT NULL,
                     address VARCHAR(255) NOT NULL,
                     ipc_section VARCHAR(255) NOT NULL,
                     jail_type VARCHAR(255) NOT NULL,
                     jail_location VARCHAR(255) NOT NULL,
                     times_in_jail VARCHAR(255) NOT NULL
                     )''')

    conn.commit()
    conn.close()


def update_inmate(uid, name=None, dob=None, adhar=None, nationality=None, state=None,
                  address=None, ipc_section=None, jail_type=None, jail_location=None,
                  times_in_jail=None) -> None:
    """
    Update inmate information in the database.

    Args:
        uid: User ID of the inmate to update.
        name: New name (optional).
        dob: New date of birth (optional).
        adhar: New Aadhaar number (optional).
        nationality: New nationality (optional).
        state: New state (optional).
        address: New address (optional).
        ipc_section: New IPC section (optional).
        jail_type: New jail type (optional).
        jail_location: New jail location (optional).
        times_in_jail: New number of times in jail (optional).

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
    if dob is not None:
        update_fields.append(("dob", dob))
    if adhar is not None:
        update_fields.append(("adhar", adhar))
    if nationality is not None:
        update_fields.append(("nationality", nationality))
    if state is not None:
        update_fields.append(("state", state))
    if address is not None:
        update_fields.append(("address", address))
    if ipc_section is not None:
        update_fields.append(("ipc_section", ipc_section))
    if jail_type is not None:
        update_fields.append(("jail_type", jail_type))
    if jail_location is not None:
        update_fields.append(("jail_location", jail_location))
    if times_in_jail is not None:
        update_fields.append(("times_in_jail", times_in_jail))

    if len(update_fields) > 0:
        update_query = "UPDATE inmates SET "
        update_query += ", ".join(f"{field} = %s" for field, _ in update_fields)
        update_query += " WHERE uid = %s"
        values = [value for _, value in update_fields]
        values.append(uid)
        c.execute(update_query, values)

    conn.commit()
    conn.close()


def generate_uid() -> int:
    """
    Generate a random 6-digit UID.

    Returns:
        int: Randomly generated UID.
    """
    return random.randint(100000, 999999)

def insert_inmate(name, dob, adhar, nationality, state, address, ipc_section,
                  jail_type, jail_location, times_in_jail) -> None:
    """
    Insert a new inmate into the database.

    Args:
        name: Name.
        dob: Date of birth.
        adhar: Aadhaar number.
        nationality: Nationality.
        state: State.
        address: Address.
        ipc_section: IPC section.
        jail_type: Jail type.
        jail_location: Jail location.
        times_in_jail: Number of times in jail.

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

    uid = generate_uid()

    c.execute("INSERT INTO inmates (uid, name, dob, adhar, nationality, state, address, ipc_section, "
              "jail_type, jail_location, times_in_jail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
              (uid, name, dob, adhar, nationality, state, address, ipc_section, jail_type,
               jail_location, times_in_jail))

    conn.commit()
    conn.close()



def read_inmate(uid=-1) -> list:
    """
    Read inmate details from the database.

    Args:
        uid: User ID to retrieve. If -1, retrieve all inmates.

    Returns:
        list: Inmate details as a list of dictionaries.
    """
    conn = mysql.connector.connect(
        host=DATABASE_HOST,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        database=DATABASE_NAME
    )
    c = conn.cursor()

    if uid != -1:
        c.execute("SELECT * FROM inmates WHERE uid = %s", (uid,))
        result = c.fetchone()
        inmate_dict = {
            "uid": result[0],
            "name": result[1],
            "dob": str(result[2]),
            "adhar": result[3],
            "nationality": result[4],
            "state": result[5],
            "address": result[6],
            "ipc_section": result[7],
            "jail_type": result[8],
            "jail_location": result[9],
            "times_in_jail": result[10]
        }
        return inmate_dict

    else:
        c.execute("SELECT * FROM inmates")
        result = c.fetchall()

    inmate_list = []
    for row in result:
        inmate_dict = {
            "uid": row[0],
            "name": row[1],
            "dob": row[2],
            "adhar": row[3],
            "nationality": row[4],
            "state": row[5],
            "address": row[6],
            "ipc_section": row[7],
            "jail_type": row[8],
            "jail_location": row[9],
            "times_in_jail": row[10]
        }
        inmate_list.append(inmate_dict)

    conn.close()

    return inmate_list
