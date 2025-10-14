"""
Script de test simple pour l'API ToDoList
"""
import requests
import json

API_URL = "http://localhost:5000/api"


def test_api():
    """Test basique de l'API"""
    print("🧪 Test de l'API ToDoList\n")

    # 1. Health check
    print("1. Test Health Check...")
    response = requests.get(f"{API_URL}/health")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}\n")

    # 2. Créer une tâche
    print("2. Créer une nouvelle tâche...")
    new_task = {
        "title": "Test Task",
        "description": "Ceci est une tâche de test"
    }
    response = requests.post(f"{API_URL}/tasks", json=new_task)
    print(f"   Status: {response.status_code}")
    task = response.json()
    print(f"   Task créée: {task['task']}\n")
    task_id = task['task']['id']

    # 3. Récupérer toutes les tâches
    print("3. Récupérer toutes les tâches...")
    response = requests.get(f"{API_URL}/tasks")
    print(f"   Status: {response.status_code}")
    data = response.json()
    print(f"   Nombre de tâches: {data['count']}\n")

    # 4. Récupérer une tâche par ID
    print(f"4. Récupérer la tâche ID={task_id}...")
    response = requests.get(f"{API_URL}/tasks/{task_id}")
    print(f"   Status: {response.status_code}")
    print(f"   Task: {response.json()['task']}\n")

    # 5. Modifier le statut
    print(f"5. Changer le statut en 'IN_PROGRESS'...")
    response = requests.patch(
        f"{API_URL}/tasks/{task_id}/status",
        json={"status": "IN_PROGRESS"}
    )
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json()['message']}\n")

    # 6. Statistiques
    print("6. Obtenir les statistiques...")
    response = requests.get(f"{API_URL}/stats")
    print(f"   Status: {response.status_code}")
    print(f"   Stats: {response.json()['stats']}\n")

    # 7. Supprimer la tâche
    print(f"7. Supprimer la tâche ID={task_id}...")
    response = requests.delete(f"{API_URL}/tasks/{task_id}")
    print(f"   Status: {response.status_code}")
    print(f"   Message: {response.json()['message']}\n")

    print("✅ Tous les tests sont passés!")


if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Erreur: L'API n'est pas accessible.")
        print("   Assurez-vous que le serveur Flask est démarré:")
        print("   cd api && python app.py")
    except Exception as e:
        print(f"❌ Erreur: {e}")
