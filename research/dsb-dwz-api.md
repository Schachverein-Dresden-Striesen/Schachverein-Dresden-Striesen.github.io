# Research: Official DSB / Liga.nu API for club DWZ data (SV Dresden-Striesen, F2810)

**Ticket:** [#195 — Research the DSB API for current club DWZ data](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues/195)
(follow-up to [#106 — Neue DWZ Api](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues/106))
**Date of research:** 2026-10-31
**Scope:** Can the official DSB ("Deutscher Schachbund") / Liga.nu Wertungsportal API serve current, public DWZ data for SV Dresden-Striesen e.V. (Vereinskennziffer/VKZ `F2810`) for the existing `pages/dwz-liste.md` page, and if so, how, safely, on a static GitHub Pages site?

All findings below were obtained by directly fetching the cited DSB/schachbund.de and liga.nu URLs on 2026-10-31 (primary sources only). Live test calls against the REST API were made read-only, with no write/upload attempted.

---

## Summary

- The DSB's rating backend ("Wertungsportal", operated by the Austrian company *nu Datenautomaten GmbH* on the `liga.nu` platform) exposes **three distinct interfaces**, documented at schachbund.de:
  1. **JSON-Schnittstelle der DWZ-Abfrage** (`wertungsportal-api.html`) — the interface **intended for clubs** to show their own current member/DWZ list on their own website. Requires a per-club **access token** obtained by email registration (VKZ + name + email + homepage).
  2. **REST-Schnittstelle des Wertungsportals** (`rest-schnittstelle-des-wertungsportals.html`), backed by `schachde-apps.liga.nu/dsbwertungsportal/rs/...` — a general-purpose, richer REST API ("DWZListeREST" for players/clubs/federations, and separately "DSBTournamentREST" for **tournament evaluation** data). Per the DSB's own documentation this was only *publicly* open "bis 14. Oktober 2026"; afterwards it is meant to require **OAuth2**, restricted to approved "Umsysteme" (partner systems), **not** for individual clubs — the DSB explicitly tells clubs to use the JSON interface (1) instead.
  3. **XML-Schnittstelle des Wertungsportals** (`DSB_DWZ_TournamentReport`, XSD-validated) — this is for **submitting/uploading tournament results for DWZ evaluation**, i.e. the opposite data-flow direction (write, not read), and is unrelated to displaying a club's current list.
- As of the test date (2026-10-31, i.e. *after* the documented Oct‑14‑2026 public-access cutoff), the `DWZListeREST` `clubs` and `persons` read endpoints on `schachde-apps.liga.nu` **still answered without any authentication**, returning live, correct data for VKZ `F2810`. This is undocumented/unsupported behavior from the DSB's own stated policy and **could be revoked or gated by OAuth2 at any time** — it must not be relied upon for a production site.
- Neither the JSON club endpoint nor the REST endpoint send CORS (`Access-Control-Allow-Origin`) headers permitting cross-origin browser JavaScript calls from a GitHub Pages origin; calls were confirmed to omit any `access-control-*` response header.
- The JSON interface explicitly states the token **must not** be placed in client-side JavaScript or other publicly readable source — which rules out any pure-static/client-side embedding on GitHub Pages, token-security concerns aside from the CORS issue.
- The bulk CSV/DOS downloads (`download-dwz-daten.html`), which also contain the same per-club DWZ rows, carry an explicit **republication restriction**: "Eine Veröffentlichung dieser Daten ist nur nach vorheriger Absprache mit dem zuständigen DWZ-Referenten erlaubt!" ("Publication of this data requires prior agreement with the responsible DWZ representative"). The per-club JSON interface does not carry that same blanket restriction — it is explicitly designed and offered for clubs to publish their own member list on their own site, which fits our use case far better.
- `robots.txt` on schachbund.de disallows crawling of `/dwz-vereine/`, `/dwz-spieler/`, `/dwz-turniere/`, `/dwz-verbaende/` (the public HTML DWZ pages) — consistent with the DSB not wanting those pages scraped, and reinforcing that the supported path for a club website is the documented API, not HTML scraping.
- **Recommendation:** Register for the JSON club-list token (one-time, via the form on `wertungsportal-api.html`, with VKZ `F2810`), store the token only as a **GitHub Actions secret**, and fetch/refresh the data via a **scheduled GitHub Actions workflow** (server-side, at most once per day per the DSB's own guidance) that writes a generated, token-free data file (e.g. a Jekyll `_data/dwz.yml`/JSON file) into the repo for the static build to render — never calling the API from client-side JS and never committing the token.

---

## 1. DWZ-list endpoint(s) vs. tournament-evaluation endpoint(s)

The DSB's "Wertungsportal" documentation page (`dwz.html`) lists, under "Wertungsportal", three sub-pages: *XML-Schnittstelle des Wertungsportals*, *REST-Schnittstelle des Wertungsportals*, *JSON-Schnittstelle der DWZ-Abfrage* — <https://www.schachbund.de/dwz.html>.

### 1.1 DWZ-list / current-rating resources (read-only, what we need)

| Interface | Base | Purpose |
|---|---|---|
| **JSON club list** | `https://www.schachbund.de/wertungsportal-api/vereinsliste?token=…&vkz=…` | Per-club current member/DWZ list as JSON, for embedding on the club's own website. Documented at <https://www.schachbund.de/wertungsportal-api.html>. |
| **REST `DWZListeREST`** | `https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/dwzliste/{persons\|clubs\|federations\|download}` | General player/club/federation current-rating lookup and bulk download, documented at <https://www.schachbund.de/rest-schnittstelle-des-wertungsportals.html> and the live API doc <https://schachde-apps.liga.nu/dsbwertungsportal/apidocs/resource_DWZListeREST.html>. Per the DSB page, public only "bis 14. Oktober 2026", then OAuth2/partner-only. |
| **Bulk CSV/DOS download** | `https://www.schachbund.de/download-dwz-daten.html` (files under `files/wertungsportal/downloads/export/{csv,dos}/LV-{code}-{csv,dos}.zip`) | Daily (04:15) full-database export per Landesverband (`LV-F` = Sachsen, which includes `F2810`), refreshed from "der Schnittstelle des Wertungsportals" (i.e. the same backend). Carries a republication-permission restriction (see §5). |

### 1.2 Tournament-evaluation resources (different purpose — not needed here)

| Interface | Base | Purpose |
|---|---|---|
| **XML `DSB_DWZ_TournamentReport`** | XSD-validated XML file upload, schema at `https://www.schachbund.de/files/wertungsportal/XMLSchema/2026/DSB_DWZ_Tounament_2_5.xsd` | **Submission** of tournament results for DWZ calculation by a tournament organizer ("Einreichung von Turnierdaten"). Documented at <https://www.schachbund.de/xml-schnittstelle-des-wertungsportals.html>. This is a write/ingest interface, not a read interface for a club's current list. |
| **REST `DSBTournamentREST`** | `https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/tournaments`, `/tournaments/{uuid}`, `/tournaments/{uuid}/evaluation`, `/tournaments/{uuid}/matches`, `/tournaments/{uuid}/players/{playerUuid}/scoresheet` | Retrieves **tournament performance/evaluation data** (old/new rating, K-factor, expected wins, performance per tournament) for a specific tournament, not a club's current rating list. Live API doc: <https://schachde-apps.liga.nu/dsbwertungsportal/apidocs/resource_DSBTournamentREST.html> (and the `DSBTournamentEvaluationDTO` schema referenced from issue #106). |

**Distinction confirmed:** `DWZListeREST` (`/dwz/dwzliste/...`) returns a **person's/club's current DWZ and membership snapshot**; `DSBTournamentREST` (`/dwz/tournaments/...`) returns **per-tournament evaluation/calculation detail** (old rating → new rating, K-factor, performance). For "show our club's current DWZ list" we only need the former; the XML upload and `DSBTournamentREST` are out of scope.

## 2. Supported endpoints and fields

### 2.1 JSON club endpoint (recommended path)
- URL: `https://www.schachbund.de/wertungsportal-api/vereinsliste?token=SCHLÜSSEL&vkz=VKZ` — documented verbatim at <https://www.schachbund.de/wertungsportal-api.html> ("Die Schnittstelle liefert die Mitgliederliste als JSON").
- Returns the member list of the one club tied to the token (VKZ `F2810` for us).
- The DSB page does not publish a field-level schema for this specific endpoint's JSON shape, but the exact same underlying rating data is visible in: (a) the bulk CSV export's `spieler.csv`/`README.txt` (<https://www.schachbund.de/download-dwz-daten.html>, fetched live 2026-10-31), and (b) the structurally equivalent `DWZListeREST` `persons` JSON response (verified live below) — both backed by the same Wertungsportal/liga.nu data store, per the `dwz.html` statement "Die DWZ-Abfragen beim Deutschen Schachbund greifen seitdem auf deren Schnittstelle zu."

  CSV field list (`README.txt` inside `LV-F-csv.zip`, downloaded 2026-10-31):
  `ID, ZPS (VKZ), Mitgliedsnummer, Status (A=Aktiv/P=Passiv), Name/Vorname, Geschlecht, Spielberechtigung, Geburtsjahr, Woche der letzten Turnierauswertung (JJJJWW), DWZ, Index, FIDE-Elozahl, FIDE-Titel, FIDE-ID, FIDE-Land, Vorname, Nachname, FIDE-Frauentitel, FIDE-Elozahl-Schnellschach, FIDE-Elozahl-Blitz`.

  Sample row for our club, `F2810` (from `LV-F-csv.zip/spieler.csv`, downloaded 2026-10-31, 04:15 snapshot):
  ```
  NU4241593,F2810,1220,A,"Pascual,Diego",M,,1987,202629,2121,17,2088,,110876,ARG,...
  ```

### 2.2 REST `DWZListeREST` (for comparison / field verification only — see §6 on why not to rely on it)
- `GET https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/dwzliste/clubs?vkz=F2810` — live call on 2026-10-31 returned:
  ```json
  {"data":[{"clubVkz":"F2810","clubName":"SV Dresden-Striesen e.V.","federation":"F","parentFederation":"F28","state":"DELETE_STATE_FALSE"}], ...}
  ```
- `GET https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/dwzliste/persons?vkz=F2810&limit=5` — live call on 2026-10-31 returned entries such as:
  ```json
  {"uuid":"f5a3063d-4ff8-11ee-a699-0050561f324c","nuLigaPersonId":"NU4241593","firstname":"Diego","lastname":"Pascual","birthyear":1987,"gender":"MALE","fideId":110876,"rating":2121,"index":17,
   "memberships":[{"vkz":"F2810","memberNo":"1220","clubName":"SV Dresden-Striesen e.V.","licenceState":"ACTIVE","regionName":"Dresden","federationName":"Schachverband Sachsen e.V."}],
   "weekOfLastTournamentEvaluation":"202629","fideRatingStandard":2088,"fideRatingRapid":2088,"fideRatingBlitz":2080,"fideCountry":"ARG"}
  ```
- Per the live API docs (<https://schachde-apps.liga.nu/dsbwertungsportal/apidocs/resource_DWZListeREST.html>, fetched 2026-10-31), the `persons` resource supports query filters `firstname, lastname, clubName, vkz, memberNo, regionName, federationName, minRating, maxRating, fideId, gender, minAge, maxAge, limit, offset`, and a person is included if a **current** membership matches; `clubs` supports `vkz, clubName, federationName, regionName, limit, offset, includeArchived`; there is also `GET /dwz/dwzliste/download/{fileName}` for the bulk export files, and `GET /dwz/dwzliste/persons/{nuLigaId}` for one person.
- `DSBTournamentREST` (not needed for our use case) supports `GET /dwz/tournaments` with filters `label, vkz, fromDate, toDate, referentFirstname, …` and per-tournament `evaluation`/`matches`/`scoresheet` sub-resources (<https://schachde-apps.liga.nu/dsbwertungsportal/apidocs/resource_DSBTournamentREST.html>).

## 3. Authentication / API-key requirements

- **JSON club endpoint:** requires a **per-club access token**, requested via a form on <https://www.schachbund.de/wertungsportal-api.html> that asks for VKZ (e.g. `F2810`), first/last name, email, and homepage; "Der Schlüssel gilt für genau einen Verein und wird Ihnen per E-Mail zugeschickt" (the key is valid for exactly one club and is emailed to the requester). The token is then passed as a query parameter (`?token=...&vkz=...`). The page explicitly warns: *"Behandeln Sie den Schlüssel wie ein Kennwort: Er gehört nicht in Javascript oder in anderen öffentlich lesbaren Quelltext."* ("Treat the key like a password: it does not belong in JavaScript or other publicly readable source code.")
- **REST `DWZListeREST`/`DSBTournamentREST`:** per <https://www.schachbund.de/rest-schnittstelle-des-wertungsportals.html>, this was public for players/clubs/federations only *"bis 14. Oktober 2026"*; afterward "ist nur noch ein Zugang mit OAuth2-Authentifizierung möglich. Zugriff haben dann nur noch die sogenannten Umsysteme" (access then limited to OAuth2-authenticated partner systems ("Umsysteme")), and credentials for that are only granted on request to `wp@schachbund.de` after review of the intended use. The same page tells clubs directly: *"Um nur eine DWZ-Liste für Ihren Verein abzurufen, benötigen Sie keinen Zugriff auf diese Schnittstelle. Füllen Sie stattdessen einfach nur dieses Formular aus"* — i.e., clubs should use the JSON endpoint (§2.1), not this REST interface.
- **Bulk CSV download:** no authentication, anonymous HTTP GET from `download-dwz-daten.html`'s linked ZIP files — but see the republication restriction in §5.

## 4. Rate limits / CORS / server-side constraints

- **Rate limit:** the JSON endpoint's own documentation states: *"Bitte rufen Sie die Liste höchstens einmal am Tag ab — die Daten ändern sich seltener, und die Schnittstelle liefert ohnehin einen zwischengespeicherten Stand."* (Please fetch the list at most once a day — data changes less often, and the interface serves a cached snapshot anyway.) This matches the bulk-CSV refresh cadence of once daily at 04:15 (`download-dwz-daten.html`).
- **CORS:** live requests to the REST endpoint with an `Origin: https://schachverein-dresden-striesen.github.io` header returned **no `Access-Control-Allow-Origin` (or any other `access-control-*`) response header** (verified 2026-10-31 against `https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/dwzliste/persons?vkz=F2810`). No CORS documentation for either interface was found on schachbund.de. **Conclusion: a browser running client-side JS on a GitHub Pages origin cannot read either endpoint's response** (the request may be sent, but the browser will block script access to the response body without a permissive CORS header) — a server-side/build-time fetch is required regardless of the token-secrecy requirement in §3.
- **robots.txt:** `https://www.schachbund.de/robots.txt` (fetched 2026-10-31) disallows crawling `/dwz-vereine/`, `/dwz-spieler/`, `/dwz-verbaende/`, `/dwz-turniere/` (and their `.html` equivalents) with `Crawl-delay: 5`. The API paths (`wertungsportal-api/...`) and the liga.nu domain are not covered by this `robots.txt` (different host), but the directive signals the DSB does not want the public HTML DWZ pages scraped — reinforcing that the documented API (not HTML scraping of `dwz-vereine/F2810.html`) is the sanctioned path.
- **Server-side constraints:** the public club HTML page itself (`dwz-vereine/F2810.html`) is gated by a JS/cookie interstitial ("Einen Moment – die Seite wird geladen …", setting a `dwzc=1` cookie and reloading) before Contao serves the real content — this is a bot-mitigation measure, further discouraging scraping that page directly as a data source.

## 5. Terms of use

- The bulk CSV/DOS export (`download-dwz-daten.html`) ships a `README.txt` **inside each ZIP** stating, verbatim (fetched 2026-10-31, `LV-F-csv.zip/README.txt`):
  > "Eine Veröffentlichung dieser Daten ist nur nach vorheriger Absprache mit dem zuständigen DWZ-Referenten erlaubt!"
  (Publishing this data is only permitted after prior arrangement with the responsible DWZ representative.) This applies to the **full Landesverband export** (all 127 Saxon clubs, 3,895 players) — a much broader dataset than just our one club.
- By contrast, the **JSON club endpoint is explicitly designed and offered by the DSB for a club to publish its own member list on its own website** ("können Sie die Mitgliederliste Ihres Vereins als JSON abrufen und auf Ihrer eigenen Website ausgeben" — <https://www.schachbund.de/wertungsportal-api.html>). This is the clearest first-party authorization for our exact use case (publishing *only our own club's* current DWZ list), and it does not carry the blanket "ask the Wertungsreferent first" restriction that the full-export README imposes.
- No separate general "Nutzungsbedingungen"/terms-of-service page specific to the Wertungsportal API was found; the per-page statements above are the closest primary-source terms. A generic site-wide Datenschutz/Impressum exists (linked from every page footer) but was not reviewed in depth as out of scope for data-reuse terms.

## 6. Refresh / automation options for a static GitHub Pages site

GitHub Pages serves pre-built static files only; there is no server-side runtime available at request time (aside from the optional GitHub Actions build pipeline). Given §3 (token secrecy) and §4 (no CORS), the options are:

1. **✅ Recommended: scheduled GitHub Actions workflow, server-side fetch, commit generated data.**
   - Register once for the JSON club token (VKZ `F2810`) via the form on <https://www.schachbund.de/wertungsportal-api.html>.
   - Store the token as a **GitHub Actions encrypted secret** (as already suggested in issue #106 by `VaeterchenFrost`, referencing GitHub's own secrets documentation).
   - Add a scheduled workflow (e.g. `on: schedule`, no more than once per day, matching the DSB's own stated cadence/cache policy) that runs `curl` (or similar) **inside the Action runner** — i.e. server-side, not in a browser — against `https://www.schachbund.de/wertungsportal-api/vereinsliste?token=$SECRET&vkz=F2810`, transforms the JSON into a Jekyll-consumable data file (e.g. `_data/dwz.json`/`.yml`, containing no token), and commits only that generated file to the repository/triggers a Pages rebuild.
   - This never exposes the token in client-side JS, in the public repo's source, or in any file served to visitors — satisfying the "treat it like a password" requirement — and respects the "once a day" rate-limit guidance.
2. **❌ Not viable: pure client-side JS fetch at page-load time.** Blocked by both the explicit "don't put the token in JS" warning (§3) and the absence of CORS headers (§4) — even a public, token-free endpoint would still need CORS support that is not present.
3. **❌ Not viable (unsupported/fragile): calling the `DWZListeREST` REST API directly** (even though it currently answers unauthenticated for `clubs`/`persons`). The DSB's own documentation says public access to this surface was only intended **until 14 Oct 2026** (already past at the time of this research) and is meant to move to OAuth2/partner-only access; it could be cut off or start requiring credentials with no notice, and the DSB explicitly directs clubs toward the JSON endpoint instead. Building the production page around it would be building on a surface the operator has already announced as deprecated for this purpose.
4. **➖ Fallback / zero-effort status quo:** keep the current `pages/dwz-liste.md` behavior of linking out to the official schachbund.de pages (no local data, no token to manage) if the team decides the token-registration/Action-maintenance overhead isn't justified yet.

## 7. Remaining uncertainties / gaps

- **Exact JSON response schema of `wertungsportal-api/vereinsliste`** was not directly observed, because obtaining it requires registering for a token (an action with side effects — email registration — that this read-only research deliberately did not perform, per the parent ticket's instruction not to implement or store credentials). The field set was inferred by cross-referencing the CSV export schema and the structurally-equivalent `DWZListeREST persons` JSON (§2), both confirmed to draw on the same backend ("Die DWZ-Abfragen beim Deutschen Schachbund greifen seitdem auf deren Schnittstelle zu" — <https://www.schachbund.de/dwz.html>), but the exact key names/shape for the club endpoint specifically should be verified once a token is obtained.
- **Whether/when the `DWZListeREST` public read access will actually be shut off** is unclear: the documented cutoff (14 Oct 2026) has already passed as of this research (31 Oct 2026), yet unauthenticated calls still succeeded live. This could mean the cutoff slipped, applies only to some operations, or enforcement is pending — the DSB page gives no update, so this should be treated as **unreliable and temporary**, not as evidence the REST API is safe to depend on.
- **Formal legal Terms of Service for API reuse** (beyond the two primary-source statements quoted in §5) could not be located; only the page-level statements on `wertungsportal-api.html` and the ZIP `README.txt` were found. A generic Impressum/Datenschutz page exists but was not analyzed for data-reuse clauses.
- **Turnaround time for token issuance** (how quickly the DSB emails back the access key after the form submission) is not stated on the page and was not tested.
- **Whether GitHub Actions' outbound IP ranges are blocked or rate-limited** by schachbund.de/liga.nu infrastructure was not tested (would require making the actual scheduled calls in production); the once-daily cadence requested by the DSB should make this unlikely to be an issue in practice.

## Sources (all fetched directly on 2026-10-31)

- <https://www.schachbund.de/dwz.html> — Wertungsportal overview, links to all three Schnittstellen pages, "Die DWZ-Abfragen ... greifen seitdem auf deren Schnittstelle zu."
- <https://www.schachbund.de/wertungsportal-api.html> — JSON club-list endpoint, registration form, token-secrecy and once-daily guidance.
- <https://www.schachbund.de/rest-schnittstelle-des-wertungsportals.html> — REST interface, public-until-14-Oct-2026 / OAuth2-afterwards policy, "Umsysteme" restriction, redirect to JSON endpoint for simple club-list use, and the live/demo API doc links.
- <https://www.schachbund.de/xml-schnittstelle-des-wertungsportals.html> — `DSB_DWZ_TournamentReport` XML tournament-submission schema documentation.
- <https://www.schachbund.de/download-dwz-daten.html> — bulk CSV/DOS daily export, file layout.
- `LV-F-csv.zip` → `README.txt`, `spieler.csv`, `vereine.csv` (downloaded from the above page) — field schema and republication-permission restriction; confirms `F2810` = "SV Dresden-Striesen e.V." in Landesverband `F` (Sachsen).
- <https://www.schachbund.de/robots.txt> — Disallow rules for `/dwz-vereine/` etc., `Crawl-delay: 5`.
- <https://www.schachbund.de/dwz-vereine/F2810.html> — the existing public club DWZ page (JS/cookie interstitial gate, Contao-rendered table, no client-visible AJAX/JSON API).
- <https://schachde-apps.liga.nu/dsbwertungsportal/apidocs/resource_DWZListeREST.html> — live API documentation for `clubs`, `federations`, `persons`, `download`, `persons/{id}` resources and their query parameters.
- <https://schachde-apps.liga.nu/dsbwertungsportal/apidocs/resource_DSBTournamentREST.html> — live API documentation for `tournaments`, `tournaments/{uuid}`, `.../evaluation`, `.../matches`, `.../players/{id}/scoresheet` (tournament-evaluation resource, distinct from the DWZ list).
- Live read-only test calls (2026-10-31, no auth):
  `https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/dwzliste/clubs?vkz=F2810`
  `https://schachde-apps.liga.nu/dsbwertungsportal/rs/dwz/dwzliste/persons?vkz=F2810&limit=5` (and with an `Origin` header to check CORS).
- [Issue #106 — "Neue DWZ Api"](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues/106) — prior internal discussion linking the JSON endpoint, the `DWZListeREST` docs, and the `DSBTournamentREST`/`DSBTournamentEvaluationDTO` tournament-evaluation schema, used here to confirm the two API families were already identified and to scope this research against them.
- [Issue #195 — "Research the DSB API for current club DWZ data"](https://github.com/Schachverein-Dresden-Striesen/Schachverein-Dresden-Striesen.github.io/issues/195) — this ticket.
- `pages/dwz-liste.md` (this repository, branch `origin/website`) — current page behavior (links out to schachbund.de, no embedded data) that this research is meant to inform.
