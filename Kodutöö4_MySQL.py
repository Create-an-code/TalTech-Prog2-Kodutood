import mysql.connector
import hashlib
import secrets

# Loome ühenduse andmebaasiga
connection = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",  # Andmebaasi host
    user="sql11702778",  # Andmebaasi kasutajanimi
    password="TH7Nc7Fx2r",  # Andmebaasi parool
    database="sql11702778"  # Andmebaasi nimi
)
cursor = connection.cursor()

def registreeri_kasutaja():
    # Küsime kasutajalt kasutajanime ja parooli
    kasutajanimi = input("Sisestage oma Kasutajanimi: ")
    parool = input("Sisestage oma Parool: ")

    # Soolamine
    # Genereerime juhusliku soola
    sool = secrets.token_hex(16)
    parool_soolatud = parool + sool

    # Räsime parooli
    parool_rasitud = hashlib.sha256(parool_soolatud.encode()).hexdigest()
    print(parool_rasitud)
    print(sool)

    # Lisame kasutaja andmed andmebaasi
    lisamise_kask = "INSERT INTO Tabel (Kasutajanimi, Parool, Sool) VALUES (%s, %s, %s)"
    kasutaja_andmed = (kasutajanimi, parool_rasitud, sool)
    cursor.execute(lisamise_kask, kasutaja_andmed)

    # Salvestame muudatused andmebaasi
    connection.commit()

    print("Kasutaja registreeritud!")

def logi_sisse():
    global cursor
    
    connection = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",  # Andmebaasi host
    user="sql11702778",  # Andmebaasi kasutajanimi
    password="TH7Nc7Fx2r",  # Andmebaasi parool
    database="sql11702778"  # Andmebaasi nimi
    )
    # Küsime kasutajalt kasutajanime ja parooli
    kasutajanimi = input("Sisestage oma Kasutajanimi: ")
    parool = input("Sisestage oma Parool: ")

     # Hangime soola andmebaasist
    cursor.execute("SELECT Sool FROM Tabel WHERE Kasutajanimi = %s", (kasutajanimi,))
    sool_andmebaasist = cursor.fetchone()
    
    cursor.execute("SELECT Parool FROM Tabel WHERE Kasutajanimi = %s", (kasutajanimi,))
    parool_andmebaasist = cursor.fetchone()
    
    if sool_andmebaasist:
        # Sulgeme eelneva päringu tulemuse

        # Räsime sisestatud parooli ning kasutame soola andmebaasist, mida registreerimisel kasutati
        parool_rasitud = hashlib.sha256((parool + sool_andmebaasist[0]).encode()).hexdigest()
        print(parool_rasitud)
        print(sool_andmebaasist[0])
        print(parool_andmebaasist[0]==parool_rasitud)
        print(parool_andmebaasist[0], parool_rasitud)
        print(f'pikkused: {len(parool_andmebaasist[0])}, {len(parool_rasitud)}')

        
    # Kontrollime, kas kasutaja on andmebaasis olemas ja kas sisestatud parooli räsi vastab andmebaasis olevale räsile
     #võrdleme räsitud paroole
        cursor.execute("SELECT * FROM Tabel WHERE Kasutajanimi = %s AND Parool = %s", (kasutajanimi, parool_rasitud))
        kasutaja = cursor.fetchone()

        if kasutaja:
            print("Sisselogimine õnnestus!")
        else:
            print("Vale kasutajanimi või parool!")
    else:
        print("Sellist kasutajanime ei eksisteeri!")

# Registreerime uue kasutaja
registreeri_kasutaja()

# Sisselogimine
logi_sisse()

# Sulgeme ühenduse andmebaasiga
connection.close()
