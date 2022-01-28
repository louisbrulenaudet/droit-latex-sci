# Droit des contrats et technique informatique : conception d’un algorithme de composition de documents avec Python 3.10 et LaTeX
[![Documentation](https://img.shields.io/badge/Template-LaTeX-blue.svg)](https://github.com/latex3/)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.10.html)

LaTeX en tant que code source est hautement disponible pour la manipulation, il peut en fait l’être avec n’importe quel langage supportant la lecture et l’écriture de fichiers .txt. C’est d’ailleurs la raison pour laquelle il reste une solution appliquée au sein d’entreprises publiques et privées de tous horizons dans la publication de rapports d’analyses statistiques internes relatifs à l’utilisation de leurs services. Dans notre travail, nous privilégierons le Python, en version 3.10, pour de multiples raisons : d’abord, le langage à été élu pour la cinquième année consécutive top programming language par l’Institute of Electrical and Electronics Engineers (IEEE) grâce notamment, à son importante communauté comprenant quelques unes des plus grandes entreprises au monde (Netflix, IBM, la NASA, Google et même Disney), mais également du fait de son caractère open source, de sa flexibilité et de la présence de nombreuses bibliothèques et packages rendant le développement plus aisé pour les débutants en informatique.

## Exigences minimales et configuration classique pour la composition de contrats

Afin de débuter dans la programmation orientée automatisation en Python avec LaTeX, on s’assurera d’être en possession d’une distribution récente des deux langages, chacune disponible en ligne sur les sites internet respectifs des deux systèmes. On notera que de nombreux éditeurs spécialisés pour la rédaction en LaTeX sont disponibles sur les différents systèmes d’exploitation destinés au grand public, et offriront un plus grand confort pour la production de modèles destinés à être manipulés algorithmiquement. Ainsi, un exemple de fichier `.tex` minimal pour la production d’actes juridiques satisfaisants devrait comprendre les éléments suivants :

```
\documentclass[french, 12pt]{report}
\usepackage[utf8]{inputenc}
\usepackage{setspace}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[french]{babel}
\title{Titre du document}
\author{Louis Brulé Naudet}
\date{\today}

\begin{document}
  ...
\end{document}
```

Nous l’avons évoqué, **le langage est évolutif et cette qualité se matérialise dans la diversité d’affichages qu’il propose**, ainsi, il sera possible au juriste de définir ses propres modèles grâce aux librairies disponibles sur le Comprehensive TEX Archive Network, et on restreindra notre exemple aux simples usages de `Babel` pour l’adoption des conventions habituelles de la typographie française. Intégré dans toutes les distributions LaTeX, ce dernier se présentera comme une nécessité pour l’écriture en langue française, notamment grâce à sa prise en charge des guillemets françaises, des alinéas rentrants, mais également, lorsqu’il est utilisé de concert avec le package `inputenc`, des caractères accentués et de la ponctuation française. La constitution d’un modèle destiné à une substitution de variables pourra prendre diverses formes, nous ne présenterons que sa manifestation au sein du corps du texte :

```
Lorem ipsum dolor sit amet,  adipiscing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna \{{###}\}. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi
ut aliquip ex ea commodo \{{###}\}.

Duis aute irure dolor in reprehenderit in voluptate \{{###}\}
esse cillum \{{###}\} eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, \{{###}\} in culpa qui officia
deserunt mollit anim id est laborum.
```

**Il deviendra alors fondamental de conserver au sein du raisonnement la mise en place d’une nomenclature spécifique pour servir différents encrages à l’algorithme**, ici, nous avons opté pour un système clair permettant une visibilité des variables au sein même du rendu simultané sur les éditeurs LaTeX. Cette nomenclature doit posséder naturellement un caractère global et être partagée au sein de tous les fichiers que le programme Python devra manipuler : sans cette rigueur, nous serions en présence d’une situation ne pouvant résoudre avec une suffisante précision la problématique de substitution et l’intérêt de l’instauration d’un tel processus en serait réduit. **Aussi, la définition de cette norme contraignante devra prendre en compte la syntaxe native de LaTeX afin de ne pas entrer en contradiction avec les règles connues par le compilateur**. Dès lors que cet effort de rédaction est satisfait avec rigueur et que le corps du document est conforme aux pratiques juridiques en vigueur, son appréhension par un algorithme de composition devient réalisable.

## Application en Python 3.10 et introduction à la manipulation de données

L’intérêt de la solution repose sur son caractère itératif, permettant la **généralisation à haut niveau et l’applicabilité à un grand nombre de documents**. Il n’y a pas besoin de connaitre tous les aspects de la programmation en Python 3.10 pour réaliser un algorithme performant pour la substitution de variables au sein d’un document textuel, seule une connaissance minimale de l’élaboration des structures de contrôle (boucles, opérations conditionnelles, exceptions...) se présentera suffisante. Le principe d’un processeur de modèles reste simple de compréhension : l’algorithme parcourt un contenu textuel à la recherche de structures normalisées renseignées au sein de son code source, puis, à chaque occurence d’un marqueur spécifique, adressera une requête au sein d’une base de données afin de récupérer les éléments d’indice correspondant et procéder à une substitution. Pour l’intelligibilité de notre modèle, nous insérerons ces données directement dans le code source en Python sous la forme de dictionnaires, prenant l’apparence d’associations clé-valeur, plébiscités pour leur efficacité de développement.

```python
data = {
"prénom": "Louis",
"nom": "Brulé Naudet",
"date de naissance": "6 septembre 2000", " ville de naissance": "Longjumeau",
}
```

Cette structure pourra prendre diverses formes, notamment en se fondant sur un système de gestion de bases de données, option pertinente au sein d’organisations moyennes à grandes, mais nécessitant un bagage technique plus important. **La construction de l’algorithme reposera ensuite sur la mise en place d’un procédé itératif permettant de prendre en compte la multiplicité des actes documentaires à composer**, et un code source minimal pourrait prendre la forme suivante :

```python
with open(filename + ".tex", "r") as file : 
  textcontent = file .read()
  for key, value in data.items():
    textcontent = textcontent.replace("\{{"+ key + "}\}", value)
    
  with open(filename_bis + ".tex", "w") as output: 
    output.write(textcontent)
```

**La fonction primitive est facilement observable**, l’algorithme assigne à une variable texcontent la valeur du contenu récupéré au sein du fichier .tex, puis l’analysera afin de réaliser une version dupliquée avec substitution des variables identifiées selon la nomenclature renseignée à la fonction `replace()`. Finalement, un second fichier `.tex` sera enregistré dans le répertoire local, afin d’être directement manipulable par le programme. À ce stade, la solution n’est cependant que partiellement satisfaisante car le fichier nouvellement créé n’a pas subi de processus de compilation et reste sous la forme d’un contenu textuel enrichi. Afin d’accroitre sa portabilité et de pouvoir l’échanger sous l’extension `.pdf`, sera nécessaire une étape de compilation par un logiciel de mise en page. Dans notre cas, nous utiliserons XeTeX, pour plusieurs raisons, de manière non limitative : le système gère nativement Unicode, et permet d’utiliser une diversité de fontes sans obligation de dépendre des paquets de polices, génère directement un fichier .pdf hautement disponible, ect. Nous exécuterons la commande permettant son application grâce au module Python os, offrant la possibilité d’interagir avec le système d’exploitation par l’intermédiaire du terminal servant à l’exécution.


[Louis Brulé Naudet](https://louisbrulenaudet.com)
