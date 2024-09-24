import psycopg2
from psycopg2 import sql

# Paramètres de connexion
host = "localhost"  # Adresse du serveur PostgreSQL
port = "5432"       # Port par défaut de PostgreSQL
dbname = "nom_de_la_base"  # Nom de la base de données
user = "votre_utilisateur"  # Utilisateur PostgreSQL
password = "votre_mot_de_passe"  # Mot de passe associé

try:
    # Établir la connexion
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    
    # Créer un curseur
    cursor = connection.cursor()

    # Vérifier la connexion
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connecté à la base de données PostgreSQL version : {db_version}")
    
    # Fermer le curseur et la connexion
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Erreur lors de la connexion à la base de données PostgreSQL : {e}")
