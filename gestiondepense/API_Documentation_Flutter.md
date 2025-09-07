# Documentation détaillée de l'API Expense pour intégration Flutter

## Base URL
```
http://127.0.0.1:8000/api/depenses/
```

---

## Authentification
- Par défaut, l'API est publique. Si l'authentification est activée, il faut ajouter le header :
```
Authorization: Token <votre_token>
```

---

## Endpoints disponibles

### 1. Lister les dépenses
- **Méthode** : GET
- **URL** : `/api/depenses/`
- **Paramètres query (optionnels)** :
  - `search` : filtre par type de dépense (ex: `?search=Carburant`)
  - `ordering` : tri (ex: `?ordering=-date`)
  - `page`, `page_size` : pagination (si activée)
- **Réponse** :
```json
[
  {
    "id": 1,
    "expense_type": "Carburant",
    "date": "2025-09-07",
    "quantity": "10.00",
    "amount": "5000.00",
    "created_at": "2025-09-07T12:00:00Z"
  },
  ...
]
```
- **Code succès** : 200

---

### 2. Créer une dépense
- **Méthode** : POST
- **URL** : `/api/depenses/`
- **Body (JSON)** :
```json
{
  "expense_type": "Carburant",
  "date": "2025-09-07",
  "quantity": "10.00",
  "amount": "5000.00"
}
```
- **Réponse** :
```json
{
  "id": 2,
  "expense_type": "Carburant",
  "date": "2025-09-07",
  "quantity": "10.00",
  "amount": "5000.00",
  "created_at": "2025-09-07T12:01:00Z"
}
```
- **Code succès** : 201
- **Erreurs** : 400 (validation)

---

### 3. Récupérer une dépense
- **Méthode** : GET
- **URL** : `/api/depenses/{id}/`
- **Réponse** :
```json
{
  "id": 2,
  "expense_type": "Carburant",
  "date": "2025-09-07",
  "quantity": "10.00",
  "amount": "5000.00",
  "created_at": "2025-09-07T12:01:00Z"
}
```
- **Code succès** : 200
- **Erreurs** : 404 (non trouvé)

---

### 4. Modifier une dépense (partiel)
- **Méthode** : PATCH
- **URL** : `/api/depenses/{id}/`
- **Body (JSON)** :
```json
{
  "amount": "70000.00"
}
```
- **Réponse** :
```json
{
  "id": 2,
  "expense_type": "Carburant",
  "date": "2025-09-07",
  "quantity": "10.00",
  "amount": "70000.00",
  "created_at": "2025-09-07T12:01:00Z"
}
```
- **Code succès** : 200
- **Erreurs** : 400 (validation), 404 (non trouvé)

---

### 5. Supprimer une dépense
- **Méthode** : DELETE
- **URL** : `/api/depenses/{id}/`
- **Réponse** : vide
- **Code succès** : 204
- **Erreurs** : 404 (non trouvé)

---

## Format des champs
- `id` : entier (auto-généré)
- `expense_type` : string (ex: "Carburant", "Huile", ...)
- `date` : string (format `YYYY-MM-DD`)
- `quantity` : string ou nombre décimal (optionnel)
- `amount` : string ou nombre décimal
- `created_at` : string (format ISO 8601, UTC)

---

## Codes d'erreur principaux
- **400** : Données invalides (ex: champ manquant, format incorrect)
- **404** : Ressource non trouvée
- **401/403** : Non authentifié ou non autorisé (si l'authentification est activée)

---

## Exemples Flutter (pseudo-code)

### GET (liste)
```dart
final response = await http.get(Uri.parse('http://127.0.0.1:8000/api/depenses/'));
if (response.statusCode == 200) {
  final List expenses = jsonDecode(response.body);
}
```

### POST (création)
```dart
final response = await http.post(
  Uri.parse('http://127.0.0.1:8000/api/depenses/'),
  headers: {'Content-Type': 'application/json'},
  body: jsonEncode({
    'expense_type': 'Carburant',
    'date': '2025-09-07',
    'quantity': '10.00',
    'amount': '5000.00',
  }),
);
if (response.statusCode == 201) {
  final expense = jsonDecode(response.body);
}
```

### PATCH (modification partielle)
```dart
final response = await http.patch(
  Uri.parse('http://127.0.0.1:8000/api/depenses/2/'),
  headers: {'Content-Type': 'application/json'},
  body: jsonEncode({'amount': '70000.00'}),
);
```

### DELETE
```dart
final response = await http.delete(
  Uri.parse('http://127.0.0.1:8000/api/depenses/2/'),
);
```

---

## Conseils pour Flutter
- Utiliser le package `http` ou `dio` pour les requêtes.
- Gérer les erreurs HTTP (statusCode != 200/201/204).
- Utiliser les modèles Dart pour sérialiser/désérialiser les objets Expense.
- Pour l'authentification, stocker le token et l'ajouter dans le header `Authorization`.

---

**N'hésite pas à demander si tu veux des exemples de modèles Dart ou des helpers pour Flutter !**
