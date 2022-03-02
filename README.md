# Brief Scraping avec Python

## Livrables :

### 3 spiders : 2 pour les Workshops et 1 pour le brief

3 dossiers de projets ont été crées :  

- 2 pour les Workshop (tutorial et WebCrawler)

- 1 pour le brief principal (brief_muzeo_scraping)

Dans le répertoire racine, 2 notebooks ont été crées pour visualier le contenu des fichiers .jsonlines générés par les spiders.
- Workshop2_display_jsonline2DF.ipynb pour le Workshop Manga
- Brief_display_jsonline2DF copy.ipynb pour le brief

### Création de la liste pour le brief
Le fichier du spider est muzeo_spider.py et le "name" permettant d'appeler le spider est "muzeo".  

Pour créer le  fichier on passe de la racine du repo dans le répertoire du projet : cd brief_muzeo_scraping  
Puis on invoque le spider : scrapy crawl muzeo -o muzeo_data.jsonlines  

### Limitations
Le prix et le délai de fabrication ne se laissent pas "scraper" malgré le soin prix pour collecter les bons xpaths.  
###
## Contexte du projet  

Vous souhaitez récuperer des données pour votre futur projet. Vous remarquez rapidement que tout ce dont vous avez besoin se trouve sur des sites internet.  
Il va vous falloir récuperer ces données de manère automatiser. Pour cela vous allez devoir, organiser votre travail et pourquoi ne pas utiliser Scrapy pour plus de facilité.  

Pour commencer il vous faudra dans la matiné commencer par maitriser Scrapy.  
A l'aide des Worshops cela ne devra pas vous poser de problème.  
L'après midi vous allez devoir mettre en pratique ce que vous avez vu le matin, en récuperant les données sur ce site :  
https://fr.muzeo.com/  

Pour cela vous disposez d'un documents avec plusieurs dizaines d'URL correpondant chacune à produit.
Vous allez devoir concevoir un code vous permetant de recuperer ces informations pour chaques produit :  
* Titre  
* Prix  
* Delai de fabrication  
* Url de l'image  

### Modalités pédagogiques  
Une journée.
Individuellement

### Critères de performance  
Le script permet de récupérer les données choisis.

### Modalités d'évaluation  
Un prototype du programme

### Livrables  
Un dépôt Git du programme, il devra inclure un readme pour les instructions de son utilisation  
