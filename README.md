# ToDoList CLI - Gestionnaire de Tâches

Une mini API en ligne de commande (CLI) pour gérer une liste de tâches, développée en Python avec une architecture MVC et la Programmation Orientée Objet (POO).

## Structure du Projet

```
conception_backend/
├── api/
│   ├── models/
│   │   └── task.py
│   ├── controllers/
│   │   └── task_controller.py
│   ├── views/
│   │   └── cli_view.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Architecture MVC

- **Models** (`models/`): Classe `Task` avec ses propriétés et méthodes, énumération `TaskStatus`
- **Controllers** (`controllers/`): `TaskController` gère la logique métier (CRUD des tâches)
- **Views** (`views/`): `CLIView` gère l'interface utilisateur en ligne de commande

## POO - Concepts Utilisés

- **Classe Task**: Représente une tâche avec attributs et méthodes
- **Énumération TaskStatus**: États possibles (TODO, IN_PROGRESS, DONE)
- **Encapsulation**: Séparation des responsabilités entre Model, View et Controller
- **Type hints**: Pour améliorer la lisibilité du code

## Installation

```bash
cd conception_backend

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur Linux/Mac:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

```bash
cd api
python main.py
```

Au démarrage, choisir un mode :
- **1. Mode CLI** : Interface en ligne de commande
- **2. Mode Flask API** : Serveur web REST API sur http://localhost:5000

## Fonctionnalités

### Mode CLI
1. **Ajouter une tâche** - Créer une nouvelle tâche avec titre et description
2. **Afficher toutes les tâches** - Liste complète des tâches avec statut et date
3. **Supprimer une tâche** - Retirer une tâche avec confirmation
4. **Quitter** - Fermer l'application

### Mode Flask API
- `GET /api/health` - Vérifier que l'API fonctionne
- `GET /api/tasks` - Récupérer toutes les tâches
- `GET /api/tasks/<id>` - Récupérer une tâche par ID
- `POST /api/tasks` - Créer une nouvelle tâche
- `DELETE /api/tasks/<id>` - Supprimer une tâche
- `PATCH /api/tasks/<id>/status` - Modifier le statut d'une tâche

## Exemple d'utilisation

```
==================================================
      TODOLIST - GESTIONNAIRE DE TACHES
==================================================
1. Ajouter une tache
2. Afficher toutes les taches
3. Supprimer une tache
4. Quitter
==================================================

Choisissez une option (1-4): 1

Titre de la tache: Faire les courses
Description (optionnel): Acheter du pain et du lait

[OK] Tache créée avec succès! (ID: 1)

Choisissez une option (1-4): 2

--- Toutes les taches (1) ---
[ ] [1] Faire les courses - À faire
   Description: Acheter du pain et du lait
   Créée le: 2025-10-14 15:30

Choisissez une option (1-4): 3

ID de la tache a supprimer: 1
Etes-vous sur de vouloir supprimer 'Faire les courses'? (o/n): o

[OK] Tache supprimée avec succès!
```

## Bonnes Pratiques Appliquées

- Architecture MVC claire et séparée
- Programmation Orientée Objet (POO)
- Type hints pour améliorer la lisibilité
- Gestion des erreurs avec try/except
- Nommage explicite des variables et fonctions
- Code modulaire et réutilisable
- Stockage en mémoire (les tâches sont perdues à la fermeture)

## Prérequis

- Python 3.7 ou supérieur
- Flask 3.1.2 (installé via requirements.txt)

## Notes

- Les tâches sont stockées en mémoire uniquement
- Aucune persistance des données (pas de fichier JSON)
- Le même controller est partagé entre CLI et Flask API
- Projet éducatif pour apprendre MVC et POO en Python
