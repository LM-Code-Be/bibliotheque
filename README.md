# 📚 Bibliothèque personnelle – Application Flask + MySQL

Développée par [LM-Code](https://lm-code.be)  
🔗 GitHub : [github.com/LM-Code-Be](https://github.com/LM-Code-Be)

---

## ✨ Description

Cette application web permet de gérer une **bibliothèque personnelle** en ligne. Tu peux :

- Ajouter des livres avec résumé, statut, date, note
- Filtrer par statut ou auteur
- Visualiser des statistiques sous forme de **dashboard graphique**
- Gérer tes lectures à lire / en cours / terminées
- Explorer une vraie architecture Flask MVC propre et claire

---

## 🔧 Technologies utilisées

- [Python 3.10+](https://www.python.org/)
- [Flask 3.x](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/) + PyMySQL
- [Bootstrap 5](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/) pour les graphiques
- HTML, CSS, JavaScript

---

## 🗂️ Structure du projet

bibliotheque/
├── app.py
├── config.py
├── requirements.txt
├── run.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── chart.js
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── add_book.html
│   ├── edit_book.html
│   ├── stats.html
├── models/
│   └── book_model.py
├── controllers/
│   └── book_controller.py
├── db/
│   └── init_db.sql
└── utils/
    └── helpers.py



---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/LM-Code-Be/bibliotheque.git
cd bibliotheque

2. Créer un environnement virtuel
python -m venv venv
source venv/Scripts/activate   # Windows
# ou
source venv/bin/activate       # macOS/Linux

3. Installer les dépendances
pip install -r requirements.txt

4. Configurer la base de données

Créer une base bibliotheque dans MySQL puis exécuter :

mysql -u root -p < db/init_db.sql

5. Créer un fichier .env

SECRET_KEY=change_moi
MYSQL_USER=lm-code (tu peux changer et mettre le tien)
MYSQL_PASSWORD=lm-code (tu peux changer et mettre le tien)
MYSQL_DB=bibliotheque

▶️ Lancer l’application

python run.py

Puis ouvrir ton navigateur à http://127.0.0.1:5000
📈 Fonctionnalités principales

    Interface responsive avec Bootstrap

    Ajout / modification / suppression de livres

    Filtrage dynamique

    Statistiques : total, note moyenne, statut, évolution mensuelle

    100 % Python, 0 dépendance front‑end complexe

🔐 Prochaines améliorations (à venir)

    Authentification multi-utilisateur

    Upload de couvertures de livres

    Export PDF / CSV

    API REST pour app mobile


🧑‍💻 Auteurs

Développé par LM-Code
Site : https://lm-code.be
GitHub : https://github.com/LM-Code-Be
📄 Licence

Ce projet est distribué sous licence MIT. Utilisation libre à des fins pédagogiques ou personnelles.
