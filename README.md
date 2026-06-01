# Article SAP


> Documentation du module de cr?ation et validation des fiches articles SAP.


## Vue d?ensemble

Article SAP centralise les informations n?cessaires ? la cr?ation ou modification d?une r?f?rence SAP. Il couvre les donn?es sales, logistique, achat, ing?nierie, key user, finance, d?rogation et BOM. Chaque service compl?te sa partie et fait avancer la fiche dans le workflow.

## Utilisateurs concern?s

- Sales : cr?e la fiche et renseigne les donn?es initiales.
- Logistique : compl?te origine, NGP, r?gime, planification et emballage.
- Achat : renseigne fournisseurs, prix et donn?es achat.
- Ing?nierie : compl?te fabrication, BOM et donn?es techniques.
- Key user : contr?le coh?rence SAP.
- Finance : compl?te valorisation et prix.
- Administrateur : g?re groupes et s?curit?.

## Workflow m?tier

1. Sales
2. Logistique
3. Achat 1
4. Ing?nierie
5. Key user
6. Achat 2
7. Finance
8. D?rogation si n?cessaire
9. Archive

## Fonctionnement op?rationnel

- Cr?er une fiche article avec r?f?rence et d?signation.
- Compl?ter les champs obligatoires de chaque service.
- Ajouter les lignes BOM si n?cessaire.
- Utiliser les boutons send_* pour transmettre au service suivant.
- Traiter les d?rogations avant archivage.
- Suivre commentaires et dates par service.

## Configuration recommand?e

- Configurer les groupes sales, logistique, achat, ing?nierie, key user et finance.
- V?rifier l?unicit? de la r?f?rence.
- Adapter les templates e-mail si les notifications doivent changer.
- V?rifier les droits d?acc?s aux fiches et lignes BOM.

## D?pendances Odoo

- `base`
- `mail`

## Mod?les techniques

- `article.article` : Fiche article SAP (`models/article.py`)
- `ref` (`models/article.py`)
- `article.lignebom` : article BOM SAP (`models/article.py`)
- `article.cat` : article states (`models/article.py`)

## ?tats d?tect?s dans le code

- `models/article.py` : `sales` (Sales), `logistique` (Logistique), `achat1` (Achat), `eng` (Ingenieurie), `keyuser` (Key user), `achat2` (Achat), `finance` (Finance), `derogation` (Dérogation), `archive` (Archive)

## Actions serveur principales

- `delete` (`models/article.py`)
- `modifier` (`models/article.py`)
- `send_sales` (`models/article.py`)
- `send_logistique` (`models/article.py`)
- `send_achat1` (`models/article.py`)
- `send_eng` (`models/article.py`)
- `send_keyuser` (`models/article.py`)
- `send_achat2` (`models/article.py`)
- `send_finance` (`models/article.py`)
- `archiver` (`models/article.py`)

## Fichiers charg?s par le manifest

- `data/mail_template_data.xml`
- `security/security.xml`
- `security/ir.model.access.csv`
- `views/article.xml`
- `views/derogation.xml`
- `views/deleted.xml`

## S?curit? et droits

Le module s?appuie sur les fichiers suivants pour d?finir les groupes, r?gles d?enregistrement et droits d?acc?s :

- `security/ir.model.access.csv`
- `security/security.xml`

## Bonnes pratiques d?utilisation

- V?rifier que chaque utilisateur Odoo est li? au bon employ? lorsque le module d?pend de `hr.employee`.
- Tester le workflow avec un dossier de test avant utilisation en production.
- Contr?ler les groupes de s?curit? apr?s installation afin que seuls les bons r?les voient les boutons de validation.
- Garder les templates e-mail et rapports align?s avec les proc?dures internes.
- Sauvegarder la base avant toute modification structurelle du module.

## Maintenance

- Les ?volutions fonctionnelles doivent ?tre ajout?es dans les mod?les Python, les vues XML et les r?gles de s?curit? correspondantes.
- Apr?s modification des vues, mettre ? jour le module depuis Odoo ou red?marrer le serveur selon le type de changement.
- Apr?s modification des assets, vider le cache navigateur et recompiler les assets si n?cessaire.
- Toute nouvelle ?tape de workflow doit ?tre accompagn?e des droits, boutons, notifications et filtres correspondants.
