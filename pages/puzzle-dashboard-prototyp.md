---
layout: single
title: "Puzzle-Dashboard Prototyp"
sidebar:
  nav: "main"
---

# Puzzle-Dashboard Prototyp

Dieser Prototyp demonstriert die technische Machbarkeit des geplanten Puzzle-Dashboards.

<div id="dashboard-container">
  <h2>Vereinsmitglieder Puzzle-Statistiken</h2>
  <div id="loading">Lade Daten...</div>
  <div id="error-message" style="display: none; color: red;"></div>
  
  <!-- Member Stats Cards -->
  <div id="member-stats" style="display: none;">
    <div class="stats-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0;">
      <!-- Cards will be inserted here -->
    </div>
  </div>
  
  <!-- Charts Container -->
  <div id="charts-container" style="display: none;">
    <h3>Rating-Entwicklung</h3>
    <canvas id="ratingChart" width="400" height="200"></canvas>
    
    <h3 style="margin-top: 40px;">Aktivitätsvergleich</h3>
    <canvas id="activityChart" width="400" height="200"></canvas>
  </div>
</div>

<style>
.member-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.member-card h4 {
  margin: 0 0 10px 0;
  color: var(--chess-black, #2c3e50);
}

.stat-row {
  display: flex;
  justify-content: space-between;
  margin: 8px 0;
  padding: 5px 0;
  border-bottom: 1px solid #eee;
}

.stat-label {
  font-weight: bold;
}

.rating-high {
  color: #27ae60;
  font-weight: bold;
}

.rating-medium {
  color: #f39c12;
  font-weight: bold;
}

.rating-low {
  color: #e74c3c;
  font-weight: bold;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Anonymisierte Mapping-Tabelle (in Produktion würde dies server-seitig geschehen)
const memberMapping = {
  'ahtemis': 'Max Mustermann',
  'testuser1': 'Anna Schmidt', 
  'testuser2': 'Klaus Weber'
};

// Mock-Daten für Demonstration (würde in Realität von APIs kommen)
const mockData = {
  'ahtemis': {
    rating: 2100,
    games: 1250,
    progress: 25,
    accuracy: 78,
    lastActivity: '2024-01-15'
  },
  'testuser1': {
    rating: 1850,
    games: 890,
    progress: -5,
    accuracy: 72,
    lastActivity: '2024-01-14'
  },
  'testuser2': {
    rating: 1950,
    games: 1100,
    progress: 15,
    accuracy: 75,
    lastActivity: '2024-01-16'
  }
};

// Rating-Verlaufsdaten für Charts
const ratingHistory = {
  'Max Mustermann': [1950, 1975, 2000, 2050, 2100],
  'Anna Schmidt': [1800, 1820, 1840, 1850, 1850],
  'Klaus Weber': [1900, 1920, 1940, 1960, 1950]
};

async function loadDashboard() {
  try {
    // Simuliere API-Aufruf Delay
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    const statsContainer = document.getElementById('member-stats');
    const chartsContainer = document.getElementById('charts-container');
    const loadingElement = document.getElementById('loading');
    
    // Erstelle Member Cards
    let statsHTML = '';
    
    Object.entries(mockData).forEach(([lichessId, stats]) => {
      const memberName = memberMapping[lichessId];
      const ratingClass = stats.rating >= 2000 ? 'rating-high' : 
                         stats.rating >= 1800 ? 'rating-medium' : 'rating-low';
      
      statsHTML += `
        <div class="member-card">
          <h4>${memberName}</h4>
          <div class="stat-row">
            <span class="stat-label">Puzzle-Rating:</span>
            <span class="${ratingClass}">${stats.rating}</span>
          </div>
          <div class="stat-row">
            <span class="stat-label">Gelöste Puzzles:</span>
            <span>${stats.games.toLocaleString()}</span>
          </div>
          <div class="stat-row">
            <span class="stat-label">Fortschritt (30 Tage):</span>
            <span style="color: ${stats.progress >= 0 ? '#27ae60' : '#e74c3c'}">
              ${stats.progress >= 0 ? '+' : ''}${stats.progress}
            </span>
          </div>
          <div class="stat-row">
            <span class="stat-label">Genauigkeit:</span>
            <span>${stats.accuracy}%</span>
          </div>
          <div class="stat-row">
            <span class="stat-label">Letzte Aktivität:</span>
            <span>${new Date(stats.lastActivity).toLocaleDateString('de-DE')}</span>
          </div>
        </div>
      `;
    });
    
    document.querySelector('.stats-grid').innerHTML = statsHTML;
    
    // Zeige Inhalte, verstecke Loading
    loadingElement.style.display = 'none';
    statsContainer.style.display = 'block';
    chartsContainer.style.display = 'block';
    
    // Erstelle Charts
    createRatingChart();
    createActivityChart();
    
  } catch (error) {
    document.getElementById('loading').style.display = 'none';
    const errorElement = document.getElementById('error-message');
    errorElement.textContent = 'Fehler beim Laden der Daten: ' + error.message;
    errorElement.style.display = 'block';
  }
}

function createRatingChart() {
  const ctx = document.getElementById('ratingChart').getContext('2d');
  
  const datasets = Object.entries(ratingHistory).map((([name, data]), index) => ({
    label: name,
    data: data,
    borderColor: ['#3498db', '#e74c3c', '#2ecc71'][index],
    backgroundColor: ['#3498db', '#e74c3c', '#2ecc71'][index] + '20',
    tension: 0.1,
    fill: false
  }));
  
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mär', 'Apr', 'Mai'],
      datasets: datasets
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Puzzle-Rating Entwicklung (letzten 5 Monate)'
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          title: {
            display: true,
            text: 'Rating'
          }
        }
      }
    }
  });
}

function createActivityChart() {
  const ctx = document.getElementById('activityChart').getContext('2d');
  
  const memberNames = Object.values(memberMapping);
  const activityData = Object.values(mockData).map(stats => stats.games);
  
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: memberNames,
      datasets: [{
        label: 'Gelöste Puzzles',
        data: activityData,
        backgroundColor: [
          'rgba(52, 152, 219, 0.8)',
          'rgba(231, 76, 60, 0.8)', 
          'rgba(46, 204, 113, 0.8)'
        ],
        borderColor: [
          'rgba(52, 152, 219, 1)',
          'rgba(231, 76, 60, 1)',
          'rgba(46, 204, 113, 1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Gesamtanzahl gelöster Puzzles'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Anzahl Puzzles'
          }
        }
      }
    }
  });
}

// Lade Dashboard beim Seitenaufruf
document.addEventListener('DOMContentLoaded', loadDashboard);
</script>

## Technische Details

### API-Integration (Produktion)

```javascript
// Echter Lichess API-Aufruf (für Referenz)
async function fetchLichessStats(username) {
  try {
    const response = await fetch(`https://lichess.org/api/user/${username}`);
    if (!response.ok) throw new Error('API-Fehler');
    
    const data = await response.json();
    return {
      rating: data.perfs?.puzzle?.rating || 'N/A',
      games: data.perfs?.puzzle?.games || 0,
      progress: data.perfs?.puzzle?.prog || 0
    };
  } catch (error) {
    console.error('Fehler beim Laden der Lichess-Daten:', error);
    return null;
  }
}
```

### Datenschutz-Implementierung

- **Anonymisierung:** Lichess-Benutzernamen werden durch Vereinsnamen ersetzt
- **Keine Direktlinks:** Keine Verweise auf tatsächliche Profile
- **Minimale Datenerhebung:** Nur Puzzle-relevante Statistiken
- **Client-seitige Verarbeitung:** Keine Speicherung sensibler Daten

### Nächste Entwicklungsschritte

1. **Echte API-Integration** mit Lichess/Chess.com
2. **Server-seitige Anonymisierung** für bessere Sicherheit  
3. **Erweiterte Visualisierungen** (Heatmaps, Radar-Charts)
4. **Mobile Optimierung** für bessere Nutzererfahrung
5. **Automatische Updates** der Statistiken

---

**Hinweis:** Dies ist ein Prototyp mit Mock-Daten. In der finalen Version würden echte API-Aufrufe und eine sichere Anonymisierung implementiert.

[← Zurück zur Startseite]({{ site.baseurl }}/)