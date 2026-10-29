# Consignes générales (tous les projets de Kamel)

## Communication
- Répondre en français, court et direct ; donner les liens / commandes prêts à copier.
- Ne pas poser trop de questions : choisir l'option évidente et avancer.

## Tests : aller vite
- Jamais de longue suite de tests qui part en tâche de fond (timeout) et fait attendre :
  toujours un test court et ciblé, au premier plan, terminé en quelques secondes.
- Par défaut : vérification rapide du démarrage (ex. Django `manage.py check`, build/compile rapide)
  + test ciblé du module modifié uniquement (Django : `--keepdb`, `--parallel` si plusieurs).
- Petite modif HTML / texte / URL sans logique : vérification rapide seulement.
- Suite complète uniquement sur demande ou si on touche au cœur métier (paiements, factures, droits, envois).
- Ne pas refaire de run « sur la version propre pour comparer » : les échecs déjà connus restent connus.

## Git
- Fusionner les autres branches de travail en cours (autres sessions) avant de pousser.
- Ne jamais réécrire l'historique d'une branche partagée.

## Mise en production
- Toujours une mise à jour sûre : sauvegarde (code + base) → mise à jour → vérifications → redémarrage
  → contrôle du site, avec retour arrière automatique en cas de problème
  (modèle : `scripts/maj.sh` du dépôt alrayane).
- Ne rien installer / lancer sur un serveur de production sans vérifier ce que fait le script.
