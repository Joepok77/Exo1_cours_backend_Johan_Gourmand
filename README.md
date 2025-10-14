# ToDoList CLI - Gestionnaire de Tâches

Une application en ligne de commande (CLI) pour gérer une liste de tâches, développée en Python avec une architecture MVC et la Programmation Orientée Objet (POO).

## Structure du Projet

```
conception_backend/
├── api/
│   ├── models/           # Modèles (Task, TaskStatus)
│   │   ├── __init__.py
│   │   └── task.py
│   ├── controllers/      # Logique métier
│   │   ├── __init__.py
│   │   └── task_controller.py
│   ├── views/           # Interface utilisateur CLI
│   │   ├── __init__.py
│   │   └── cli_view.py
│   └── main.py          # Point d'entrée
├── .env.exemple         # Exemple de configuration
├── .gitignore
└── requirements.txt
```

## Architecture MVC

- **Models** (`models/`): Contient la classe `Task` avec ses propriétés et méthodes, et l'énumération `TaskStatus`
- **Controllers** (`controllers/`): Gère la logique métier avec `TaskController` (CRUD des tâches)
- **Views** (`views/`): Interface utilisateur en ligne de commande avec `CLIView`

## POO - Concepts Utilisés

- **Classe Task**: Représente une tâche avec attributs et méthodes
- **Énumération TaskStatus**: États possibles d'une tâche (TODO, IN_PROGRESS, DONE)
- **Encapsulation**: Séparation des responsabilités entre Model, View et Controller
- **Méthodes**: `__init__`, `__str__`, `__repr__`, `to_dict()`, etc.

## Installation

```bash
# Cloner le repository
git clone <url-du-repo>
cd conception_backend

# Aucune dépendance externe requise (Python 3.7+)
```

## Utilisation

Lancer l'application:

```bash
cd api
python main.py
```

## Fonctionnalités

1. **Ajouter une tâche** - Créer une nouvelle tâche avec titre et description
2. **Afficher toutes les tâches** - Liste complète des tâches
3. **Afficher par statut** - Filtrer les tâches (À faire, En cours, Terminé)
4. **Modifier une tâche** - Éditer le titre et/ou la description
5. **Changer le statut** - Mettre à jour l'état d'une tâche
6. **Supprimer une tâche** - Retirer une tâche de la liste
7. **Quitter** - Fermer l'application

## Exemple d'utilisation

```
📝 TODOLIST - GESTIONNAIRE DE TÂCHES
1. Ajouter une tâche
2. Afficher toutes les tâches
...

Choisissez une option (1-7): 1
Titre de la tâche: Faire les courses
Description (optionnel): Acheter du pain et du lait

✅ Tâche créée avec succès! (ID: 1)
```

## Bonnes Pratiques Appliquées

- Architecture MVC claire et séparée
- Programmation Orientée Objet (POO)
- Docstrings pour toutes les classes et méthodes
- Type hints pour améliorer la lisibilité
- Gestion des erreurs avec try/except
- Nommage explicite des variables et fonctions
- Code modulaire et réutilisable

## Prérequis

- Python 3.7 ou supérieur
- Aucune bibliothèque externe nécessaire

## Auteur

[Votre Nom]

## Licence

Projet éducatif
