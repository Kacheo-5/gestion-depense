# Gestion de Dépenses API

Application Django REST pour la gestion des dépenses (Carburant, Huile, Réparation, etc.)

## Fonctionnalités
- CRUD complet sur les dépenses via API REST
- Filtrage, recherche, tri
- Admin Django
- Tests unitaires
- Collection Postman pour tests automatisés
- Documentation pour intégration Flutter

---

## Installation

1. **Cloner le projet**
```powershell
# Adapter le chemin si besoin
cd "c:\Users\William\Mes projets\devoirISM\exambaila\gestiondepense"
```

2. **Installer les dépendances**
```powershell
python -m pip install -r requirements.txt
```

3. **Appliquer les migrations**
```powershell
python manage.py migrate
```

4. **Créer un superutilisateur (optionnel, pour admin)**
```powershell
python manage.py createsuperuser
```

---

## Lancement du serveur
```powershell
python manage.py runserver
```
Accéder à l'API sur : [http://127.0.0.1:8000/api/depenses/](http://127.0.0.1:8000/api/depenses/)

---

## Utilisation de l'API
Voir la documentation détaillée : [API_Documentation_Flutter.md](API_Documentation_Flutter.md)

Endpoints principaux :
- `GET /api/depenses/` : liste des dépenses
- `POST /api/depenses/` : créer une dépense
- `GET /api/depenses/{id}/` : récupérer une dépense
- `PATCH /api/depenses/{id}/` : modifier une dépense
- `DELETE /api/depenses/{id}/` : supprimer une dépense

---

## Tests unitaires
```powershell
python manage.py test
```

---

## Tests automatisés avec Postman
- Importer `postman_collection.json` dans Postman
- Importer l'environnement `postman_environment.json`
- Lancer la collection pour tester le CRUD
- Voir la documentation : [postman_collection_explained.md](postman_collection_explained.md)
- Liste des tests possibles : [postman_tests_documentation.md](postman_tests_documentation.md)

---

## Intégration Flutter
- Voir la documentation : [API_Documentation_Flutter.md](API_Documentation_Flutter.md)
- Exemples de requêtes HTTP, modèles, gestion des erreurs

---

## Accès à l'admin Django
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Structure du projet
```
manage.py
requirements.txt
API_Documentation_Flutter.md
postman_collection.json
postman_environment.json
postman_collection_explained.md
postman_tests_documentation.md
/depense
    models.py
    views.py
    serializer.py
    services.py
    urls.py
    admin.py
    tests.py
/gestiondepense
    settings.py
    urls.py
    ...
```

---

## Pour aller plus loin
- Ajouter l'authentification Token (DRF)
- Ajouter pagination, filtres avancés
- Déployer sur un serveur (Heroku, OVH, etc.)

---

**Auteur : William**

Pour toute question ou amélioration, ouvre une issue ou contacte le mainteneur.
