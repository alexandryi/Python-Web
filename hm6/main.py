import sqlite3

def run_query(cursor, file_name):
    try:
        with open(file_name, "r") as f:
            sql = f.read()
            cursor.execute(sql)
            
            if sql.strip().lower().startswith("select"):
                rows = cursor.fetchall()
                print(f"\nРезультат {file_name}:")
                for row in rows:
                    print(row)
            else:
                conn.commit()
                print(f"Виконано {file_name}")
                
    except Exception as e:
        print(f"Помилка у {file_name}: {e}")

if __name__ == "__main__":
    conn = sqlite3.connect("university.db")
    cursor = conn.cursor()

    for i in range(1, 11):
        file_name = f"query{i}.sql"
        run_query(cursor, file_name)

    conn.close()
    print("Усі запити оброблені.")
