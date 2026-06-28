# Microsip Stats - Application Django

Application web de statistiques d appels Microsip.
Developpee pendant la formation "Outils de Developpement Collaboratif".

## Version 1 (V1) - Ce que fait cette version

- Lit un fichier CSV d appels place dans le dossier data/
- Affiche le nombre total d appels
- Affiche le nombre d appels par heure (graphique en barres)
- Identifie l heure de pointe
- Affiche la liste complete des appels

## Installation

### 1. Creer l environnement virtuel

    python -m venv venv

    # Windows :
    venv\Scripts\activate

    # Linux/Mac :
    source venv/bin/activate

### 2. Installer les dependances

    pip install -r requirements.txt

### 3. Placer le fichier CSV

Copier votre fichier CSV dans le dossier data/ en le renommant appels.csv

Format attendu des colonnes : Date, Heure, Direction, Appelant, Appele, Duree, Statut

### 4. Lancer le serveur

    python manage.py runserver

Ouvrir le navigateur : http://127.0.0.1:8000

## Evolution prevue

- V2 : Filtre par date, filtre par direction
- V3 : Graphique par jour (30 derniers jours)
- V4 : Top 5 postes les plus actifs
- V5 : Export PDF du rapport
