# frontdepense

Flutter client for the "Gestion de dépense" REST API used for the ISM project.

This repository contains a small Flutter app (Android/iOS/web/desktop) that consumes a Django REST backend exposing `/api/depenses/` endpoints.

## What is included

- `lib/models/expense.dart` — Expense model and JSON (de)serialization.
- `lib/services/expense_service.dart` — HTTP client wrapper for CRUD operations (GET, POST, PATCH, DELETE).
- `lib/screens/*` — UI screens: list, detail, form (create & edit).
- `pubspec.yaml` — project dependencies (includes `http`).

## Quick setup (Windows)

Prerequisites:
- Flutter SDK installed and on PATH (stable channel recommended)
- Android Studio or an Android emulator available
- A running backend (Django REST API) listening on port `8000` on your host machine

1. Install dependencies

```powershell
cd "C:\Users\William\Mes projets\devoirISM\exambaila\frontdepense"
flutter pub get
```

2. Backend networking for Android emulator

If you run the Android emulator, it cannot reach `localhost` (127.0.0.1) of the host directly. The app is preconfigured to use `http://10.0.2.2:8000/api/depenses/` for the Android emulator. To allow the emulator to reach your Django server:

- Run the Django dev server on all interfaces:

```powershell
python manage.py runserver 0.0.0.0:8000
```

- Ensure `ALLOWED_HOSTS` in Django `settings.py` includes at least `['localhost', '127.0.0.1']`. For quick dev you can add `'10.0.2.2'` or `'*'` (not recommended for production).
- If you use a real device, replace the base URL in `lib/services/expense_service.dart` with your machine's LAN IP (e.g. `http://192.168.1.42:8000/api/depenses/`).

3. Run the Flutter app on the emulator

```powershell
flutter run
```

## Notes about the code

- The service uses the `http` package (`package:http/http.dart`) — dependency is declared in `pubspec.yaml`.
- The form screen (`lib/screens/expense_form_screen.dart`) displays the currency as `FrancCfa` and supports both create and update flows.
- The app surfaces backend errors (400/500) in the UI so server validation messages can be debugged quickly.

## Common issues

- "Target of URI doesn't exist: 'package:http/http.dart'" — run `flutter pub get` to fetch dependencies.
- `SocketException: OS Error: Connection refused` — means the emulator/device couldn't reach the backend. Confirm the backend is running and you used the correct host (10.0.2.2 for Android emulator).
- HTTP 400 on create — the server returns validation errors. The client now displays the server response; copy the error body and inspect expected fields/formats on the backend.

## Developer tips

- To change the backend URL for other environments, update the default `baseUrl` in `lib/services/expense_service.dart` or provide a different `ExpenseService(baseUrl: 'http://...')` when creating screens.
- Add tests: You can mock `ExpenseService` and write widget tests for the form and list screens.

## Contributing

This project is a student assignment skeleton — follow standard Git workflows. Create a branch per feature and open a PR against `main`.

## License

This repository contains educational code; adapt as needed.
