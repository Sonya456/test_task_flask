# Aplikacja Kalendarza Wydarzeń

## Uruchomienie aplikacji

1. Skopiuj repozytorium na swój komputer.
2. Zainstaluj Docker.
3. Uruchom polecenie:
   ```bash
   docker build -t event_calendar .
   docker run -p 8000:8000 event_calendar
4. Otwórz przeglądarkę i przejdź do http://localhost:8000