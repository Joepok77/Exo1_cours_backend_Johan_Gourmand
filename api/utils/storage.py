"""
Gestionnaire de persistance des données
"""
import json
import os
from typing import List, Dict
from pathlib import Path


class StorageManager:
    """Gère la sauvegarde et le chargement des tâches dans un fichier JSON"""

    def __init__(self, filename: str = "tasks.json"):
        """
        Initialise le gestionnaire de stockage

        Args:
            filename: Nom du fichier JSON pour stocker les tâches
        """
        # Créer le dossier data s'il n'existe pas
        self.data_dir = Path(__file__).parent.parent / "data"
        self.data_dir.mkdir(exist_ok=True)

        self.filepath = self.data_dir / filename

    def save_tasks(self, tasks: List) -> bool:
        """
        Sauvegarde les tâches dans le fichier JSON

        Args:
            tasks: Liste des tâches à sauvegarder

        Returns:
            True si la sauvegarde a réussi, False sinon
        """
        try:
            tasks_data = [task.to_dict() for task in tasks]

            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(tasks_data, f, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
            return False

    def load_tasks(self) -> List[Dict]:
        """
        Charge les tâches depuis le fichier JSON

        Returns:
            Liste des tâches sous forme de dictionnaires
        """
        if not self.filepath.exists():
            return []

        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
            return tasks_data
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return []

    def file_exists(self) -> bool:
        """Vérifie si le fichier de données existe"""
        return self.filepath.exists()

    def get_filepath(self) -> str:
        """Retourne le chemin complet du fichier"""
        return str(self.filepath)
