# Projet : Optimisation

## Description

Ce projet contient l'implémentation du problème posé par le projet d'Optimisation de l'UE Optimisation
de la troisième année de licence informatique.

## Présentation du problème

Paul  a  décidé  de  partir  à  Rio  pour  assister  aux Jeux  Olympiques.  
En  plus  du billet  d’avion  et  de l’hôtel, Paul s’est fixé un budget de 1000 euros.

Le revendeur officiel propose les tarifs suivants :

* Le pack athlétisme permet de voir 9h d’athlétisme pour 450€
* Le pack basket permet de voir la finale de basket (2h) pour 700€
* Le pack cyclisme permet de voir 3h de cyclisme pour 350€
* Le pack football permet de voir 13h de football pour 500€
* Le pack judo permet de voir deux finales de judo (6h) pour 450€
* Le pack natation permet de voir 2h de natation et 3h d’handball pour 100€

Paul cherche à maximiser le nombre d’heures de sport auxquelles il peut assister sans dépasser son budget.

## Implémentation proposée

Pour répondre au problème, nous avons fourni une application Java proposant une interface indiquant :

* L’ordre initial et la solution de la relaxation 
* La solution et la valeur de l’objectifQ4.  
* Le  nombre  de  nœuds  explorés  par  l’ordre  de  B&B, le  temps  de  calcul,  la solution  optimale. 
* Puis pour chaque nœud,la valeur de la borne supérieure, et la solution relaxée. 
