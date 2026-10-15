# ADR 0003: Öffentliche URLs der Website

**Status:** Accepted
**Date:** 2026-10-15

Die Website wird unter `https://www.sv-dresden-striesen.de` mit leerem `baseurl` veröffentlicht; die Permalinks werden je Inhaltstyp in `_config.yml` festgelegt. Diese veröffentlichten URLs gelten als stabil: Änderungen an Permalinks müssen bestehende Verweise berücksichtigen und bei Bedarf Weiterleitungen vorsehen. Eine einheitliche Slash-Regel wird nicht festgelegt, da die bestehenden Inhaltstypen unterschiedliche Permalink-Muster verwenden.
