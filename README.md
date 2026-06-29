# Article SAP

Module Odoo de creation, enrichissement et validation des fiches articles SAP.

Le module centralise les donnees Sales, Logistique, Achat, Ingenierie, Key User et Finance, gere les lignes BOM, les derogations et l'archivage de la fiche article.

## Objectif fonctionnel

Structurer la creation ou modification d'une reference article avant creation dans SAP.

Le module permet de :

- creer une fiche article ;
- garantir l'unicite de la reference ;
- renseigner les donnees generales ;
- suivre les informations logistiques ;
- renseigner les donnees achat ;
- renseigner les donnees ingenierie ;
- renseigner les donnees key user ;
- renseigner les donnees finance ;
- ajouter des lignes BOM ;
- gerer les derogations champ par champ ;
- notifier les groupes a chaque transition ;
- archiver la fiche terminee.

## Roles fonctionnels

### Sales

Sales initie la fiche article.

Il renseigne notamment :

- reference ;
- designation ;
- statut de reference ;
- type de reference ;
- Sales Traffic Light ;
- commentaires sales.

### Logistique

Logistique complete les informations de flux et stockage.

Elle renseigne notamment :

- NGP ;
- regime douanier ;
- pays et region d'origine ;
- temps de reception ;
- type de planification ;
- gestionnaire MRP ;
- taille de lot ;
- stock de securite.

### Achat

Achat intervient sur deux etapes du workflow.

Il renseigne notamment :

- fournisseur ;
- MOQ ;
- delai previsionnel de livraison ;
- prix ;
- devise ;
- fiche information achat ;
- validations liees aux achats.

### Ingenierie

Ingenierie renseigne les informations techniques.

Elle intervient notamment sur :

- type de fabrication ;
- type d'emballage ;
- poste de travail ;
- temps de cycle ;
- nombre d'empreintes ;
- tonnage presse ;
- moule ;
- donnees de BOM.

### Key User

Le Key User controle les donnees metier et peut intervenir sur plusieurs etapes selon les droits.

### Finance

Finance renseigne les donnees de valorisation.

Elle intervient notamment sur :

- classes de valorisation ;
- code prix ;
- prix moyen pondere ;
- base de prix ;
- donnees internal et external.

## Etats du workflow

Les etats principaux sont :

- `Sales`
- `Logistique`
- `Achat`
- `Ingenierie`
- `Key user`
- `Achat`
- `Finance`
- `Derogation`
- `Archive`

## Flux standard

1. `Sales`
2. `Logistique`
3. `Achat 1`
4. `Ingenierie`
5. `Key user`
6. `Achat 2`
7. `Finance`
8. `Archive`

Une etape `Derogation` peut etre utilisee lorsque certaines donnees necessitent une validation ou une exception.

## Donnees article

La fiche article contient notamment :

- reference ;
- designation ;
- statut ;
- type de reference ;
- donnees logistiques ;
- donnees achat ;
- donnees techniques ;
- donnees finance ;
- commentaires par service ;
- dates de passage par service ;
- indicateurs de creation SAP, BOM et gamme.

## BOM

Les lignes BOM sont gerees dans le modele :

- `article.lignebom`

Elles permettent de rattacher les composants, quantites et unites a la fiche article.

## Derogations

Le module contient plusieurs champs de derogation permettant de signaler une exception sur :

- type d'emballage ;
- temps de cycle ;
- nombre d'empreintes ;
- tonnage presse ;
- poste de travail ;
- moule ;
- MOQ ;
- unite d'emballage ;
- BOM ;
- volume annuel ;
- donnees logistiques.

## Notifications

Les templates email couvrent :

- creation article ;
- modification article ;
- derogation ;
- archivage.

Fichier principal :

- `data/mail_template_data.xml`

## Securite et droits

Les droits sont organises par groupes :

- Sales ;
- Logistique ;
- Achat ;
- Ingenierie ;
- Key User ;
- Finance.

Le module active l'edition selon l'etat courant et le groupe de l'utilisateur.

## Modeles principaux

- `article.article`
- `article.lignebom`
- `article.cat`

## Structure du module

- `security/security.xml`
- `security/ir.model.access.csv`
- `data/mail_template_data.xml`
- `views/article.xml`
- `views/derogation.xml`
- `views/deleted.xml`
- `models/article.py`

## Installation

1. Copier le module dans le dossier addons Odoo.
2. Redemarrer le serveur Odoo si necessaire.
3. Mettre a jour la liste des applications.
4. Installer le module.
5. Affecter les utilisateurs aux groupes par service.
6. Tester une fiche article de bout en bout.
7. Tester un cas de derogation.

## Maintenance fonctionnelle

Lorsqu'une donnee SAP change, verifier aussi :

- les selections Python ;
- les champs de la vue formulaire ;
- les groupes de securite ;
- les templates email ;
- les controles de derogation ;
- ce README.
