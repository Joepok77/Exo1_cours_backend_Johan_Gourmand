# ToDoList - Gestionnaire de Tâches

Application simple pour gérer une liste de tâches, développée en Python avec une architecture MVC.

## Structure du Projet

```
conception_backend/
├── models/
│   └── task.py
├── controllers/
│   └── task_controller.py
├── views/
│   └── cli_view.py
├── main.py          # Mode CLI
├── app.py           # Mode Flask API
├── README.md
├── .gitignore
└── requirements.txt
```

## Architecture MVC

- **Models** (`models/`): Classe `Task` représentant une tâche
- **Controllers** (`controllers/`): `TaskController` gère la logique métier
- **Views** (`views/`): `CLIView` gère l'interface utilisateur

## Installation

```bash
git clone https://github.com/Joepok77/Exo1_cours_backend_Johan_Gourmand.git

cd Exo1_cours_backend_Johan_Gourmand

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

### Mode CLI (Terminal)
```bash
python main.py
```

### Mode Flask API (Serveur web)
```bash
python app.py
```
L'API sera disponible sur http://localhost:5000

## Fonctionnalités

### Mode CLI
1. **Ajouter une tâche** - Créer une nouvelle tâche
2. **Afficher toutes les tâches** - Voir la liste des tâches
3. **Supprimer une tâche** - Retirer une tâche
4. **Quitter** - Fermer l'application

### Mode Flask API
- `GET /api/tasks` - Voir toutes les tâches
- `POST /api/tasks` - Ajouter une tâche
- `DELETE /api/tasks/<id>` - Supprimer une tâche

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
[1] Faire les courses
   Description: Acheter du pain et du lait
   Créée le: 2025-10-14 15:30

Choisissez une option (1-4): 3

ID de la tache a supprimer: 1
Etes-vous sur de vouloir supprimer 'Faire les courses'? (o/n): o

[OK] Tache supprimée avec succès!
```

## Notes

- Les tâches sont stockées en mémoire uniquement
- Pas de base de données
- Architecture MVC simple
