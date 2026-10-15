# ADR 0002: GitHub-Pages-Veröffentlichung aus dem Branch

**Status:** Accepted
**Date:** 2026-10-15

GitHub Pages baut und veröffentlicht die Website aus dem Branch `website`; GitHub Actions prüft Pull Requests mit einem Produktionsbuild und html-proofer, veröffentlicht aber kein Build-Artefakt. Damit bleibt der Branch die Quelle der veröffentlichten Website, während CI Änderungen vor dem Merge validiert.
