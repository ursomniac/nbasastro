---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
# PRIORITY 0: BUILD EXCLUSIONS
_build:
  list: never     # Prevents appearing in Recent Articles or Series lists
  render: always  # Must render so members can see it via direct link
  publishResources: false
# PRIORITY 1: SEARCH & SEO
sitemap:
  disable: true   # Removes from sitemap.xml
layout: "members" # Uses a dedicated layout with no-index meta tags
---

## Internal Documentation
> [!CAUTION] 
> INTERNAL ONLY. Do not link to this page from public articles.
