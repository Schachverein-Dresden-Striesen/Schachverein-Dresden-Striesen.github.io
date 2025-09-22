---
layout: single
title: "Tags Übersicht"
permalink: /tags/
sidebar:
  nav: "main"
---

Diese Seite zeigt alle verwendeten Tags und die dazugehörigen Artikel.

{% comment %}
Collect all tags from pages and posts
{% endcomment %}
{% assign all_tags = '' | split: '' %}
{% for page in site.pages %}
  {% if page.tags %}
    {% for tag in page.tags %}
      {% unless all_tags contains tag %}
        {% assign all_tags = all_tags | push: tag %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% for post in site.posts %}
  {% if post.tags %}
    {% for tag in post.tags %}
      {% unless all_tags contains tag %}
        {% assign all_tags = all_tags | push: tag %}
      {% endunless %}
    {% endfor %}
  {% endif %}
{% endfor %}

{% assign sorted_tags = all_tags | sort %}

{% for tag_name in sorted_tags %}
## {{ tag_name }}

{% comment %}Find pages with this tag{% endcomment %}
{% for page in site.pages %}
  {% if page.tags contains tag_name %}
- [{{ page.title }}]({{ page.url | relative_url }})
  {% endif %}
{% endfor %}

{% comment %}Find posts with this tag{% endcomment %}
{% for post in site.posts %}
  {% if post.tags contains tag_name %}
- [{{ post.title }}]({{ post.url | relative_url }}) ({{ post.date | date: "%d.%m.%Y" }})
  {% endif %}
{% endfor %}

{% endfor %}

---

[← Zurück zur Startseite]({{ site.baseurl }}/)