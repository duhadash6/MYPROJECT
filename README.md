# TP Mi-Guidé Django — Installation et Architecture de Base

> **Université Abdelmalek Essaadi — FST Tanger**  
> Licence | Développement Web Avancé — Back End (Python) | 2025/2026  
> Prof. Sara AHSAIN

---

## Description

Ce projet est réalisé dans le cadre d'un TP mi-guidé sur **Django**, un framework web open-source écrit en Python. Il couvre l'installation, la configuration et les fonctionnalités de base de Django, notamment :

- La création d'un projet et d'une application Django
- L'architecture MVT (Modèle-Vue-Template)
- La gestion des formulaires
- Les modèles de données et migrations
- L'interface d'administration
- L'authentification des utilisateurs

---

## Technologies utilisées

- **Python** 3.11+
- **Django** 6.0.3
- **SQLite** (base de données par défaut)
- **Bootstrap** (pour le style)
- **HTML / CSS**

---

## Installation et lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/duhadash6/MYPROJECT.git
cd MYPROJECT
```

### 2. Créer et activer l'environnement virtuel

```bash
# Créer l'environnement virtuel
python -m venv monenv

# Activer (Windows)
monenv\Scripts\activate

# Activer (macOS/Linux)
source monenv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install django
```

### 4. Appliquer les migrations

```bash
cd myproject
python manage.py migrate
```

### 5. Créer un super-utilisateur (pour l'admin)

```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

### 7. Ouvrir dans le navigateur

- **Site principal** : http://127.0.0.1:8000
- **Interface admin** : http://127.0.0.1:8000/admin

---

## Structure du projet

```
myproject/
├── manage.py               <- Commandes Django
├── db.sqlite3              <- Base de données SQLite
├── templates/
│   ├── index.html          <- Page d'accueil avec formulaire
│   ├── counter.html        <- Résultat du compteur de mots
│   ├── register.html       <- Page d'inscription
│   └── login.html          <- Page de connexion
├── static/                 <- Fichiers CSS, JS, images
├── myapp/
│   ├── models.py           <- Modèle Feature
│   ├── views.py            <- Vues (index, counter, register, login, logout)
│   ├── urls.py             <- Routes de l'application
│   ├── admin.py            <- Enregistrement des modèles dans l'admin
│   └── migrations/         <- Migrations de la base de données
└── myproject/
    ├── settings.py         <- Configuration globale
    ├── urls.py             <- Routeur principal
    ├── wsgi.py
    └── asgi.py
```

---

## Fonctionnalités

### Compteur de mots
Saisissez un texte dans le formulaire de la page d'accueil et obtenez le nombre de mots en un clic.

### Authentification
- **Inscription** : `/register`
- **Connexion** : `/login`
- **Déconnexion** : `/logout`

### Administration
Accédez à l'interface d'administration Django sur `/admin/` pour gérer les objets **Feature** (nom + détails).

---

## Commandes utiles

| Commande | Description |
|----------|-------------|
| `python manage.py runserver` | Lancer le serveur local |
| `python manage.py makemigrations` | Générer les migrations |
| `python manage.py migrate` | Appliquer les migrations |
| `python manage.py createsuperuser` | Créer un administrateur |
| `python manage.py startapp nom` | Créer une nouvelle application |

---

## Auteure

**Doha ZIOUANI**  
Etudiante en Licence Développement Web Avancé  
Université Abdelmalek Essaadi — FST Tanger
