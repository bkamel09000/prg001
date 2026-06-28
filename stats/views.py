import csv
import os
from collections import defaultdict
from django.shortcuts import render
from django.conf import settings

CSV_PATH = os.path.join(settings.BASE_DIR, "data", "appels.csv")

def lire_csv(chemin):
    """Lit le fichier CSV et retourne la liste des appels."""
    appels = []
    if not os.path.exists(chemin):
        return appels
    with open(chemin, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            appels.append(ligne)
    return appels

def calculer_stats(appels):
    """Calcule les statistiques a partir de la liste des appels."""
    if not appels:
        return {}

    total = len(appels)

    # Nombre d appels par heure
    par_heure = defaultdict(int)
    for appel in appels:
        heure = appel.get("Heure", "00:00:00")[:2] + "h"
        par_heure[heure] += 1

    # Trier les heures
    heures_triees = sorted(par_heure.items(), key=lambda x: int(x[0].replace("h", "")))

    # Heure de pointe (heure avec le plus d appels)
    heure_max = max(par_heure, key=par_heure.get) if par_heure else "-"
    nb_max = par_heure[heure_max] if heure_max != "-" else 0

    return {
        "total": total,
        "par_heure": heures_triees,
        "heure_max": heure_max,
        "nb_max": nb_max,
    }

def tableau_de_bord(request):
    """Vue principale : affiche le tableau de bord."""
    appels = lire_csv(CSV_PATH)
    stats = calculer_stats(appels)

    contexte = {
        "appels": appels,
        "stats": stats,
        "titre_page": "Tableau de bord - Appels Microsip",
    }
    return render(request, "stats/tableau_de_bord.html", contexte)
