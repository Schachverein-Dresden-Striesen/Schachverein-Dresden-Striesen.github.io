# API-Dokumentation für Puzzle-Dashboard

## Lichess API

### Basis-Informationen
- **Basis-URL:** `https://lichess.org/api`
- **Authentifizierung:** Nicht erforderlich für öffentliche Daten
- **Rate Limits:** 600 Requests/Minute
- **Datenformat:** JSON

### Wichtige Endpunkte

#### Benutzer-Profil
```
GET /api/user/{username}
```

**Beispiel-Response:**
```json
{
  "id": "ahtemis",
  "username": "Ahtemis",
  "createdAt": 1389040566000,
  "seenAt": 1640984651686,
  "playTime": {
    "total": 2945851,
    "tv": 0
  },
  "perfs": {
    "puzzle": {
      "games": 1250,
      "rating": 2100,
      "rd": 150,
      "prog": 25
    }
  }
}
```

#### Rating-Verlauf
```
GET /api/user/{username}/rating-history
```

**Response:** Array von Rating-Punkten über Zeit für alle Spielvarianten

## Chess.com API

### Basis-Informationen
- **Basis-URL:** `https://api.chess.com/pub`
- **Authentifizierung:** Nicht erforderlich
- **Rate Limits:** Moderat (empfohlen: 1 Request/Sekunde)
- **User-Agent:** Erforderlich

### Wichtige Endpunkte

#### Spieler-Profil
```
GET /pub/player/{username}
```

#### Spieler-Statistiken
```
GET /pub/player/{username}/stats
```

**Beispiel für Puzzle-Daten:**
```json
{
  "tactics": {
    "highest": {
      "rating": 1950,
      "date": 1640984651
    },
    "lowest": {
      "rating": 1200,
      "date": 1389040566
    }
  }
}
```

## Implementierungshinweise

### CORS-Probleme
- Lichess: CORS-Header erlauben direkte Browser-Requests
- Chess.com: Möglicherweise Proxy erforderlich

### Caching-Strategie
- Empfohlen: 1 Stunde Cache für Puzzle-Ratings
- 24 Stunden Cache für Profildaten
- Lokalspeicher für bereits abgerufene Daten

### Fehlerbehandlung
```javascript
async function safeApiCall(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('API-Fehler:', error);
    return null;
  }
}
```