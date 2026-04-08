# Web App

## Présentation

Cette page documente la partie **web** du projet `Pipeline-CI-CD`.
L’objectif est de lancer l’interface, comprendre sa structure, et préparer la suite de la documentation MkDocs.

## Prérequis

- Python 3.10+
- Un environnement virtuel actif (`venv` recommandé)
- Les dépendances installées depuis `requirements.txt`

## Installation

Depuis la racine du projet :

```bash
/Users/asmataberkokt/Pipeline-CI-CD/venv/bin/python -m pip install -r requirements.txt
```

## Lancer l’application web

Le frontend est situé dans `frontend/app.py`.

```bash
cd frontend
/Users/asmataberkokt/Pipeline-CI-CD/venv/bin/python app.py
```

## Structure utile

- `frontend/app.py` : point d’entrée de l’interface web
- `backend/app/` : logique backend et services
- `dataset/load.py` : chargement des données (ex. Iris)
- `requirements.txt` : dépendances Python du projet

## Intégration MkDocs (prochaine étape)

Quand tu voudras, on pourra ajouter :

1. Un `mkdocs.yml` à la racine
2. Une navigation entre les pages (`index.md`, `web.md`, `backend.md`)
3. Une section “Guide de déploiement” (Docker + CI/CD)

## Notes

Ce document est une base initiale. On peut ensuite détailler :

- variables d’environnement
- endpoints backend utilisés par le frontend
- procédures de test et debugging
