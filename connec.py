import pymysql.cursors


def db_connect():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Toshib@123',
                                 database='flask_crud',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)


app = Flask(__name__)
db_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Toshib@123',
    database='flask_crud'
)

cursor = db_connection.cursor()

def select_all_annonce():
    request = "SELECT * FROM Annonces;"
    cursor.execute(request)
    annonces = cursor.fetchall()
    return annonces

def select_genre_annonce(genre):
    request = "SELECT * FROM Annonces WHERE genre = %s"
    cursor.execute(request, (genre,))
    annonces = cursor.fetchall()
    return annonces

def recherche_annonce(terme_recherche):
    request = "SELECT * FROM Annonces WHERE titre_annonce LIKE %s"
    cursor.execute(request, ('%'+terme_recherche+'%',))
    annonces = cursor.fetchall()

    return annonces

