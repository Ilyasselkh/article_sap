# Article SAP

Module Odoo de creation et validation des fiches articles SAP. Il couvre les donnees sales, logistique, achat, ingenierie, key user, finance, derogations et BOM.

## Objectif

Cette documentation explique le perimetre fonctionnel du module, les roles utilisateurs, le workflow, la configuration et les principaux objets techniques.

## Utilisateurs concernes

- Sales
- Logistique
- Achat
- Ingenierie
- Key user
- Finance
- Administrateur Odoo

## Workflow metier

1. Sales
2. Logistique
3. Achat 1
4. Ingenierie
5. Key user
6. Achat 2
7. Finance
8. Derogation si necessaire
9. Archive

## Fonctionnement operationnel

- Creer une fiche article.
- Completer les champs du service courant.
- Ajouter les lignes BOM si necessaire.
- Transmettre au service suivant.
- Traiter les derogations.
- Archiver la fiche terminee.

## Configuration recommandee

- Configurer les groupes par service.
- Verifier unicite de la reference.
- Adapter les templates mail.
- Verifier les droits sur fiches et lignes BOM.

## Dependances Odoo

- `base`
- `mail`

## Modeles principaux

- `article.article`
- `article.lignebom`
- `article.cat`

## Structure importante du module

- `security/ir.model.access.csv`
- `security/security.xml`
- `data/mail_template_data.xml`
- `views/article.xml`
- `views/dashboard.xml`
- `views/deleted.xml`
- `views/derogation.xml`
- `models/__init__.py`
- `models/article.py`

## Securite

Les droits sont geres par les fichiers du dossier `security`. Il faut verifier les groupes, les regles enregistrement et les acces CSV apres installation ou modification du module.

## Notifications et suivi

Les modules qui dependent de `mail` utilisent le chatter Odoo pour tracer les changements. Les templates mail presents dans le dossier `data` servent a notifier les acteurs concernes par les transitions.

## Installation

1. Copier le module dans le dossier addons Odoo.
2. Redemarrer le serveur Odoo si necessaire.
3. Mettre a jour la liste des applications.
4. Installer ou mettre a jour le module.
5. Verifier les droits utilisateurs et tester un dossier de bout en bout.

## Maintenance

- Ajouter toute nouvelle etape a la fois dans le modele Python, les vues XML, les droits et les notifications.
- Tester les workflows avec plusieurs roles utilisateurs.
- Mettre a jour les rapports et templates mail quand la procedure interne change.
- Eviter de modifier les donnees de production sans sauvegarde.
- Documenter toute evolution fonctionnelle dans ce README.
