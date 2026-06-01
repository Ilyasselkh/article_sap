# Article SAP

Module Odoo de création et validation des fiches articles SAP.

## Objectif

Ce module centralise les informations nécessaires à la création d'un article SAP : données commerciales, logistiques, achats, ingénierie, key user, finance, dérogations et BOM.

## Dépendances

- `base`
- `mail`

## Modèles principaux

- `article.article` : fiche article SAP.
- `article.lignebom` : lignes de BOM rattachées à la fiche article.
- `article.cat` : catégories/compteurs par statut.

## Workflow

La fiche passe par les étapes suivantes :

1. `sales` : saisie commerciale initiale.
2. `logistique` : données logistiques.
3. `achat1` : première validation achat.
4. `eng` : ingénierie.
5. `keyuser` : contrôle key user.
6. `achat2` : complément achat.
7. `finance` : données finance.
8. `derogation` : traitement des dérogations si nécessaire.
9. `archive` : fiche terminée ou archivée.

## Fonctionnement

- La référence article est unique.
- Les champs couvrent les données SAP principales : référence, désignation, statut, type, MOQ, NGP, régime douanier, pays d'origine, MRP, emballage, prix, classe de valorisation, fabrication et données finance.
- Des indicateurs de dérogation permettent de signaler les champs exceptionnels.
- Les lignes BOM permettent d'associer des composants et de suivre leur statut.
- Les actions `send_*` font avancer la fiche selon le rôle métier.
- Les commentaires et dates par service sont conservés.
- Le chatter trace les modifications.

## Sécurité

Les groupes et droits sont définis dans :

- `security/security.xml`
- `security/ir.model.access.csv`

## Notifications

Le module charge un template e-mail pour notifier les acteurs concernés lors des transitions clés.

