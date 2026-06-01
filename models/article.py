from odoo import models, fields, api
from odoo import exceptions
import datetime

class article(models.Model):
    _name = 'article.article'
    _description = 'Fiche article SAP'
    _inherit = [ 'mail.thread', 'mail.activity.mixin']
    _rec_name = "ref"
    _sql_constraints = [('ref_unique', 'unique(ref)', 'reference existe déja')]


    ref = fields.Char(string='Référence',tracking=True)
    designation = fields.Char(string='Désignation',tracking=True)   
    refstatut = fields.Selection([('prototype', 'Prototype'),('serie', 'Série'),('fin', 'Fin de vie'),('supprime', 'Supprimé')], string= 'Statut de la référence',tracking=True)
    reftype = fields.Selection([('matiere', 'Matière première'),('negoce', 'Produit Fini Négoce'),('interne', 'Produit Fini Manufacturing'),('semifini', 'Semi fini Manufacturing'),('composant', 'Composant'),('consommable', 'Consommables (Emballage; Palettes...)')] , string='Type de référence',tracking=True)
    moq = fields.Integer(string='MOQ',tracking=True)
    ngp = fields.Char(string='NGP',tracking=True)
    regime = fields.Char(string='Régime douanier',tracking=True)
    pays = fields.Char(string="Pays d'origine",tracking=True)
    region = fields.Char(string="Région d'origine",tracking=True)
    tempsreception = fields.Integer(string='Temps de réception',tracking=True)
    typeplanif = fields.Char(string='Type planification',tracking=True)
    MRPgest = fields.Selection([('101', '101 Injection 420_500'),('102','102 Injection 160_210'), ('100', 'OLD-103 Injection 80_100'),('103', '103 Injection 80_100'), ('200','200 Assembly'), ('300','300 MAT 1ere PLASTIQUE'),('400','400 COMPOSANT'),('500','500 Négoce')],string='Gestionnaire MRP',tracking=True)
    taillelotmin = fields.Integer(string= 'Taille de lot minimale',tracking=True)
    arrondie = fields.Integer(string='Valeur arrondi',tracking=True)
    delailiv = fields.Integer(string='Délai prévisionnel de livraison',tracking=True)
    Stocksec = fields.Integer(string='Stock de sécurité',tracking=True)
    fournisseur = fields.Char(string="Fournisseur", tracking=True)
    moule = fields.Char(string='Moule', tracking=True)
    poids = fields.Float(string='Poids', tracking= True)
    unitepoids = fields.Char(string='Unité de poids', tracking=True)
      

    classeval = fields.Selection([('z001', 'Z001'),('z002', 'Z002'),('z030', 'Z030'),('z031', 'Z031'),('z040', 'Z040')],string="Classe de valorisation ENTETE",tracking=True)
    codeprix = fields.Selection([('s', 'S'),('v','V')], string ='Code prix ENTETE',tracking=True)
    
    prixpond = fields.Float(string='Prix moyen pondéré ENTETE',tracking=True)
    classevalint = fields.Selection([('z001', 'Z001'),('z002', 'Z002'),('z030', 'Z030'),('z031', 'Z031'),('z040', 'Z040')],string="Classe de valorisation INTERNAL",tracking=True)
    codeprixint = fields.Selection([('s', 'S'),('v','V')], string ='Code prix INTERNAL',tracking=True)
    baseprixint = fields.Integer(string='Base de prix INTERNAL',tracking=True)
    prixpondint = fields.Float(string='Prix moyen pondéré INTERNAL',tracking=True)
    classevalext = fields.Selection([('z001', 'Z001'),('z002', 'Z002'),('z030', 'Z030'),('z031', 'Z031'),('z040', 'Z040')],string="Classe de valorisation EXTERNAL",tracking=True)
    codeprixext = fields.Selection([('s', 'S'),('v','V')], string ='Code prix EXTERNAL',tracking=True)
    baseprixext = fields.Integer(string='Base de prix EXTERNAL',tracking=True)
    prixpondext = fields.Float(string='Prix moyen pondéré EXTERNAL',tracking=True)
    pasccr = fields.Selection([('oui', 'OUI'),('non','NON')], string="Cocher 'pas de CCR'",tracking=True)
    structureq = fields.Selection([('oui', 'OUI'),('non','NON')], string="Cocher 'Avec structure de quantité'",tracking=True)
    origine = fields.Selection([('oui', 'OUI'),('non','NON')], string="Cocher 'Origine article'",tracking=True)
    fraisgen = fields.Selection([('assembly', 'ASSEMBLY'), ('brokered', 'BROKERED')], string="Groupe de frais généraux",tracking=True)
    typefab = fields.Selection([('injection', 'Injection'), ('assemblage', 'Assemblage')], string="Type de fabrication", tracking=True)
    typeemb = fields.Selection([('700100996','A5'),('700100997','A9'),('700100009','A10'),('700100010','A11'),('700100995','A12'),('700100012','A15'),('700100013','A16'),('700100014','B12'),('700100015','B14'),('700100676','C9'),('700100011','C13'),('700100041','MN7'),('700200640','RC2 BAC VERT 40L GEFBOX 6422'),('700200641','RC3 BAC IVOIRE 20 L GEFBOX 4322'),('700200642','SC4 BAC ORANGE 10L GEFBOX 4312'),('autre','Autre')], string="Type d'emballage",tracking=True) #TODO : SELECTION et autre ( ajouter un champs  commentaire obligatoire )
    uniteemb = fields.Integer(string="Unité d'emballage",tracking=True)
    postetrav = fields.Char(string="Poste de travaille",tracking=True) #TODO : SELECTION
    tempscyc = fields.Integer(string="Temps de cycle",tracking=True)
    nbrempr = fields.Integer(string="Nombre d'empreintes",tracking=True)
    tonpresse = fields.Integer(string="Tonnage presse",tracking=True)
    isfab = fields.Boolean(string="isfab", compute="compute_isfab", store=True, tracking=True)
    volumeannuel = fields.Integer(string='Volume annuel',tracking=True)
    isderogation = fields.Boolean(string ="Dérogation",tracking=True)
    modif = fields.Char(string="Date de modification")
    prix = fields.Float(string="Prix", tracking=True)
    currency = fields.Selection([('mad','MAD'),('eur','EUR')], tracking=True)
    baseprix = fields.Integer(string='Base de prix', tracking=True)
    baseunite = fields.Selection([('pce','PCE'),('l','L'),('kg','KG'),('g','G')],string="Unité", tracking=True)
    fichefour = fields.Boolean(string="Fiche Info achat créée",tracking=True)
    fichedumy = fields.Boolean(string="Fiche DUMY créée",tracking=True)
    ccr = fields.Boolean(string="CCR lancé",tracking=True)
    budget = fields.Boolean(string="Prix budgeté 1 renseigné", tracking=True)
    validation = fields.Boolean(string="Validation", tracking=True)
    #
    dertypeemb = fields.Char(string="Entrer type d'emballage",tracking=True)
    dertempscyc = fields.Boolean(string="Dérogation",tracking=True)
    dernbrempr = fields.Boolean(string="Dérogation",tracking=True)
    dertonpresse = fields.Boolean(string="Dérogation",tracking=True)
    derpostetrav = fields.Boolean(string="Dérogation",tracking=True)
    dermoule = fields.Boolean(string="Dérogation",tracking=True)
    dermoq = fields.Boolean(string="Dérogation",tracking=True)
    deruniteemb = fields.Boolean(string="Dérogation",tracking=True)
    derbom = fields.Boolean(string="Dérogation BOM",tracking=True)
    dervolumeannuel = fields.Boolean(string="Dérogation",tracking=True)
    
    derngp = fields.Boolean(string='Dérogation',tracking=True)
    derregime = fields.Boolean(string='Dérogation',tracking=True)
    dertempsreception = fields.Boolean(string='Dérogation',tracking=True)
    dertypeplanif = fields.Boolean(string='Dérogation',tracking=True)
    derMRPgest = fields.Boolean(string='Dérogation',tracking=True)
    dertaillelotmin = fields.Boolean(string= 'Dérogation',tracking=True)
    derdelailiv = fields.Boolean(string='Dérogation',tracking=True)

    creationar = fields.Boolean(string="Article créé sur SAP",tracking=True)
    creationbom = fields.Boolean(string="BOM créé sur SAP",tracking=True)
    creationgam = fields.Boolean(string="Gamme créé sur SAP",tracking=True)
    
    comsal = fields.Char(string="Commentaire sales")
    comfin = fields.Char(string="Commentaire finance")
    comach = fields.Char(string="Commentaire achat")
    comlog = fields.Char(string="Commentaire logistique")
    comkey = fields.Char(string="Commentaire key user")
    comeng = fields.Char(string="Commentaire ingenieurie")

    datelog = fields.Char(string='Date logistique')
    dateach1 = fields.Char(string='Date achat 1')
    dateeng = fields.Char(string='Date Ingenieurie')
    datekey = fields.Char(string='Date Key user')
    dateach2 = fields.Char(string='Date achat 2')
    datefin = fields.Char(string='Date finance')
    dateder = fields.Char(string='Date derogation')
    datearc = fields.Char(string='Date archive')

    
    state = fields.Selection([('sales', 'Sales'),('logistique', 'Logistique'),('achat1', 'Achat'), ('eng', 'Ingenieurie'), ('keyuser', 'Key user'),('achat2', 'Achat'),('finance', 'Finance'),('derogation', 'Dérogation'), ('archive', 'Archive')], default ='sales' ,string="Statut",tracking=True)
    deleted = fields.Boolean(default=False,tracking=True)

    id_lignes_bom = fields.One2many('article.lignebom', 'id_fiche_article', string='lignes de BOM',tracking=True)

    email_to_notify_success = 'issam.eddabbar@araymond.com'
    
    
    #le field STL
    stl = fields.Selection([('T0', 'T0--n/a'),('T1', 'T1--Prefered'),('T2', 'T2--Preferred with legal carry-over limitat.'),('T3', 'T3--Check prior offering'),('T4', 'T4--Vehicule specific'),('T5', 'T5--Customer specific'),('T6', 'T6--Phasing-out'),('T7', 'T7--Obsolete'),('T8', 'T8--Non assessed')], default='T8' ,string='Sales Traffic Light', tracking=True)

    #TODO : ajouter les fichiers attachés 
    # 
    #TODO : > 0 pour les chemps obligatoires
    #TODO : ajouter la zone des commentaires
    #TODO : dans la section BOM afficher les status des composants pour verifier si la reference est déja crée => DONE


    created = fields.Boolean(default=False)
    edit = fields.Boolean(string="edit", default=False, compute='get_user_grp')

    

    #edittext= fields.Char(string="text")

        

    @api.depends('state')
    @api.depends_context('uid')
    def get_user_grp(self):
        for rec in self:
            rec.edit = False
            user = rec.env.user
            if rec.state == 'sales' and (
                user.has_group('article_sap.group_sales') or user.has_group('article_sap.group_keyuser')
            ):
                rec.edit = True
            
            elif user.has_group('article_sap.group_achat') and rec.state == 'achat1':
                rec.edit = True
            elif user.has_group('article_sap.group_achat') and rec.state == 'achat2':
                rec.edit = True

            elif user.has_group('article_sap.group_logistique') and rec.state == 'logistique':
                rec.edit = True
                
            elif user.has_group('article_sap.group_finance') and rec.state == 'finance':
                rec.edit = True
                
            elif user.has_group('article_sap.group_keyuser') and rec.state == 'keyuser':
                rec.edit = True
            
            elif user.has_group('article_sap.group_eng') and rec.state == 'eng':
                rec.edit = True

            #rec.edittext = "grp: "+ str(res_user.has_group('article_sap.group_logistique')) + "state : " + str(rec.state) + "edit : "+ str(rec.edit)


    @api.model
    def create(self, vals):
        return super(article, self).create(vals)

    def _group_email_string(self, group_xmlid):
        users = self.env['res.users'].sudo().search([])
        group_users = users.filtered(lambda user: user.has_group(group_xmlid))
        return ', '.join(email for email in group_users.mapped('partner_id.email') if email)

    @api.depends('ref')

    def delete(self):
        for rec in self:
            rec.deleted = True
            rec.state = 'archive'

    def modifier(self):
        for rec in self:
            
            if rec.dertempscyc == True or rec.dernbrempr == True or rec.dertonpresse == True or rec.derpostetrav == True or rec.dermoq == True or rec.deruniteemb == True or rec.derbom == True or rec.dervolumeannuel == True or rec.derngp == True or rec.derregime == True or rec.dertempsreception == True or rec.dertypeplanif == True or rec.derMRPgest == True  or rec.dertaillelotmin == True or rec.derdelailiv == True :
                rec.isderogation = True
            if rec.dertempscyc == False and rec.dernbrempr == False and rec.dertonpresse == False and rec.derpostetrav == False and rec.dermoq == False and rec.deruniteemb == False and rec.derbom == False and rec.dervolumeannuel == False and rec.derngp == False and rec.derregime == False  and rec.dertempsreception == False and rec.dertypeplanif == False and rec.derMRPgest == False  and rec.dertaillelotmin == False and rec.derdelailiv == False :
                rec.isderogation = False
            
            if rec.env.user.has_group ('article_sap.group_sales'):
                
                if rec.state == 'archive':
                    raise exceptions.AccessDenied("Impossible de modifier, article archivé.")
                else :     
                    rec.state = 'sales'
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                
            elif rec.env.user.has_group ('article_sap.group_logistique'):
                
                if rec.state == 'archive':
                    raise exceptions.AccessDenied("Impossible de modifier, article archivé.")

                elif rec.state in {'finance','keyuser','derogation','achat1','achat2','eng'}:
                    rec.state = 'logistique'
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            elif rec.env.user.has_group ('article_sap.group_eng'):
                
                if rec.state == 'archive':
                    raise exceptions.AccessDenied("Impossible de modifier, article archivé.")

                elif rec.state in {'finance','keyuser','derogation','achat2'}:
                    rec.state = 'eng'
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
   
            elif rec.env.user.has_group ('article_sap.group_achat'):
                
                if rec.state == 'archive':
                    raise exceptions.AccessDenied("Impossible de modifier, article archivé.")

                elif rec.state in {'keyuser','achat2','eng'}:
                    rec.state = 'achat1'
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                elif rec.state in {'finance','derogation'}:
                    rec.state = 'achat2'
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            elif rec.env.user.has_group ('article_sap.group_finance'):
                
                if rec.state == 'archive':
                    raise exceptions.AccessDenied("Impossible de modifier, article archivé.")

                elif rec.state in {'derogation'}:
                    rec.state = 'finance'
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

            elif rec.env.user.has_group('article_sap.group_keyuser'):
                rec.state = 'keyuser'
                rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    

    def send_sales(self):
        for rec in self:
            if rec.dertempscyc == True or rec.dernbrempr == True or rec.dertonpresse == True or rec.derpostetrav == True or rec.dermoq == True or rec.deruniteemb == True or rec.derbom == True or rec.dervolumeannuel == True or rec.derngp == True or rec.derregime == True  or rec.dertempsreception == True or rec.dertypeplanif == True or rec.derMRPgest == True  or rec.dertaillelotmin == True or rec.derdelailiv == True :
                rec.isderogation = True
            if rec.dertempscyc == False and rec.dernbrempr == False and rec.dertonpresse == False and rec.derpostetrav == False and rec.dermoq == False and rec.deruniteemb == False and rec.derbom == False and rec.dervolumeannuel == False and rec.derngp == False and rec.derregime == False  and rec.dertempsreception == False and rec.dertypeplanif == False and rec.derMRPgest == False  and rec.dertaillelotmin == False and rec.derdelailiv == False :
                rec.isderogation = False   
            if rec.isfab == True: 
                if len(rec.id_lignes_bom) <1:
                    raise exceptions.MissingError('Merci de remplir la partie BOM')
                if  rec.tempscyc < 1 :
                        raise exceptions.MissingError('Merci de renseigner le champ: \r\n\r\nTemps de cycle')                  
                if rec.typefab == "injection":
                    if rec.nbrempr <1 : 
                        raise exceptions.MissingError("Merci de renseigner tous les champs obligatoires:\r\n\r\nNombre d'empreintes")
                    if rec.tonpresse <1:
                        raise exceptions.MissingError("Merci de renseigner tous les champs obligatoires:\r\n\r\nTonnage presse")
            if rec.uniteemb <1 :
                raise exceptions.MissingError("Merci de renseigner tous les champs obligatoires:\r\n\r\nUnité d'emballage")
            if rec.volumeannuel <1:
                raise exceptions.MissingError("Merci de renseigner tous les champs obligatoires:\r\n\r\nVolume annuel")
            if rec.reftype in ('interne','semifini','negoce') and rec.moq <1:
                raise exceptions.MissingError("Merci de renseigner le MOQ")
            else :            
                rec.state = 'logistique'
                rec.datelog = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                if rec.modif is False :
                    mail_template = self.env.ref('article_sap.article_creation')
                    email_string = self._group_email_string("article_sap.group_all")
                    mail_template.email_to = email_string
                    mail_template.send_mail(rec.id, force_send=True)
                elif rec.modif is not None:
                    mail_template = self.env.ref('article_sap.article_modification')
                    email_string = self._group_email_string("article_sap.group_all")
                    mail_template.email_to = email_string
                    mail_template.send_mail(rec.id, force_send=True)
                return {
                        'res_model' : 'article.article',
                        'type': 'ir.actions.act_window',
                        "views": [[False, "list"], [False, "form"]],
                        'target' : 'main',
                        'domain':[('state','!=',"archive")],
                        }

    def send_logistique(self):
        for rec in self:
            if rec.dertempscyc == True or rec.dernbrempr == True or rec.dertonpresse == True or rec.derpostetrav == True or rec.dermoq == True or rec.deruniteemb == True or rec.derbom == True or rec.dervolumeannuel == True or rec.derngp == True or rec.derregime == True or rec.dertempsreception == True or rec.derMRPgest == True or rec.dertaillelotmin == True or rec.derdelailiv == True :
                rec.isderogation = True
            if rec.dertempscyc == False and rec.dernbrempr == False and rec.dertonpresse == False and rec.derpostetrav == False and rec.dermoq == False and rec.deruniteemb == False and rec.derbom == False and rec.dervolumeannuel == False and rec.derngp == False and rec.derregime == False and rec.dertempsreception == False and rec.derMRPgest == False  and rec.dertaillelotmin == False and rec.derdelailiv == False :
                rec.isderogation = False
            if rec.taillelotmin <1 and rec.reftype in ('interne', 'semifini'):
                raise exceptions.MissingError("Merci de renseigner le champs:\r\n\r\n*Taille de lot minimale")           
            if rec.tempsreception <1 and rec.reftype == "negoce" :
                raise exceptions.MissingError("Merci de renseigner le champs:\r\n\r\n*Temps de réception") 
            if rec.delailiv <1 and rec.reftype == "negoce" :
                raise exceptions.MissingError("Merci de renseigner le champs:\r\n\r\n*Délai prévisionnel de livraison")
            else:
                if rec.created == True:
                    rec.state = 'keyuser'
                    mail_template = self.env.ref('article_sap.article_modification')
                    email_string = self._group_email_string("article_sap.group_keyuser")
                    mail_template.email_to = email_string
                    mail_template.send_mail(rec.id, force_send=True)
                    rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }                            
                else:
                    if rec.reftype in ('interne','semifini'):
                        rec.state = 'eng'
                        rec.dateeng = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                        mail_template = self.env.ref('article_sap.article_creation')
                        email_string = self._group_email_string("article_sap.group_eng")
                        mail_template.email_to = email_string
                        mail_template.send_mail(rec.id, force_send=True)
                        return {
                                    'res_model' : 'article.article',
                                    'type': 'ir.actions.act_window',
                                    "views": [[False, "list"], [False, "form"]],
                                    'target' : 'main',
                                    'domain':[('state','!=',"archive")],
                                    }
                    else:    
                        rec.state = 'achat1'
                        rec.dateach1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                        mail_template = self.env.ref('article_sap.article_creation')
                        email_string = self._group_email_string("article_sap.group_achat")
                        mail_template.email_to = email_string
                        mail_template.send_mail(rec.id, force_send=True)
                        return {
                                    'res_model' : 'article.article',
                                    'type': 'ir.actions.act_window',
                                    "views": [[False, "list"], [False, "form"]],
                                    'target' : 'main',
                                    'domain':[('state','!=',"archive")],
                                    }

    def send_achat1(self):
        for rec in self:            
            if rec.prix <1 or rec.baseprix <1:
                raise exceptions.MissingError("Merci de renseigner les champs:\r\n\r\nPrix.\r\nBase de prix.")
            else:
                
                if rec.reftype not in {'consomable','negoce','composant'}:
                    rec.state = 'eng'
                    rec.dateeng = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    mail_template = self.env.ref('article_sap.article_creation')
                    email_string = self._group_email_string("article_sap.group_eng")
                    mail_template.email_to = email_string
                    mail_template.send_mail(rec.id, force_send=True)
                    return {
                                'res_model' : 'article.article',
                                'type': 'ir.actions.act_window',
                                "views": [[False, "list"], [False, "form"]],
                                'target' : 'main',
                                'domain':[('state','!=',"archive")],
                                }
                else:
                    rec.state = 'keyuser'
                    rec.datekey = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    mail_template = self.env.ref('article_sap.article_creation')
                    email_string = self._group_email_string("article_sap.group_keyuser")
                    mail_template.email_to = email_string
                    mail_template.send_mail(rec.id, force_send=True)
                    return {
                                'res_model' : 'article.article',
                                'type': 'ir.actions.act_window',
                                "views": [[False, "list"], [False, "form"]],
                                'target' : 'main',
                                'domain':[('state','!=',"archive")],
                                }

    def send_eng(self):
        for rec in self:
            rec.state = 'keyuser'
            rec.datekey = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            mail_template = self.env.ref('article_sap.article_creation')
            email_string = self._group_email_string("article_sap.group_keyuser")
            mail_template.email_to = email_string
            mail_template.send_mail(rec.id, force_send=True)
            return {
                        'res_model' : 'article.article',
                        'type': 'ir.actions.act_window',
                        "views": [[False, "list"], [False, "form"]],
                        'target' : 'main',
                        'domain':[('state','!=',"archive")],
                        }

    def send_keyuser(self):
        for rec in self:
            if rec.reftype in ('interne','semifini'):
                rec.state = 'finance'
                rec.datefin = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                mail_template = self.env.ref('article_sap.article_creation')
                email_string = self._group_email_string("article_sap.group_finance")
                mail_template.email_to = email_string
                mail_template.send_mail(rec.id, force_send=True)
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }
            else:
                rec.state = 'achat2'
                rec.dateach2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                mail_template = self.env.ref('article_sap.article_creation')
                email_string = self._group_email_string("article_sap.group_achat")
                mail_template.email_to = email_string
                mail_template.send_mail(rec.id, force_send=True)
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }

    def send_achat2(self):
        for rec in self:            
            if rec.created == True:
                rec.state = 'finance'
                mail_template = self.env.ref('article_sap.article_modification')
                email_string = self._group_email_string("article_sap.group_finance")
                mail_template.email_to = email_string
                mail_template.send_mail(rec.id, force_send=True)
                rec.modif = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                return {
                        'res_model' : 'article.article',
                        'type': 'ir.actions.act_window',
                        "views": [[False, "list"], [False, "form"]],
                        'target' : 'main',
                        'domain':[('state','!=',"archive")],
                        }                            
            else:
                rec.state = 'finance'
                rec.datefin = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                mail_template = self.env.ref('article_sap.article_creation')
                email_string = self._group_email_string("article_sap.group_finance")
                mail_template.email_to = email_string
                mail_template.send_mail(rec.id, force_send=True)
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }

    def send_finance(self):
        for rec in self:
            if rec.isderogation == True :
                rec.state = 'derogation'
                rec.dateder = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                rec.created = True
                mail_template = self.env.ref('article_sap.article_derogation')
                email_string = self._group_email_string("article_sap.group_all")
                mail_template.email_to = email_string
                mail_template.send_mail(rec.id, force_send=True)
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }
            if rec.isderogation == False :
                rec.state = 'archive'
                rec.created = True
                mail_template = self.env.ref('article_sap.article_archive')
                email_string = self._group_email_string("article_sap.group_all")
                mail_template.email_to = email_string
                mail_template.send_mail(rec.id, force_send=True)
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }

    def archiver(self):
        for rec in self:
            if rec.isderogation == True :
                rec.state = 'derogation'
                rec.created = True
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }
            if rec.isderogation == False :
                rec.state = 'archive'
                rec.datearc = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                rec.created = True
                return {
                            'res_model' : 'article.article',
                            'type': 'ir.actions.act_window',
                            "views": [[False, "list"], [False, "form"]],
                            'target' : 'main',
                            'domain':[('state','!=',"archive")],
                            }

    @api.depends('reftype')
    def compute_isfab(self):
        for rec in self:
            if rec.reftype in ['matiere','negoce','consommable']:
                rec.isfab = False
            elif rec.reftype in ['interne','semifini']:
                rec.isfab = True 
            else:
                rec.isfab = False

    @api.onchange('reftype')
    def _onchange_reftype(self):
        for rec in self:
            if rec.reftype in ['matiere', 'negoce', 'consommable']:
                rec.typefab = False



class articlebom(models.Model):
    _name = 'article.lignebom'
    _description = 'article BOM SAP'
    _inherit = [ 'mail.thread', 'mail.activity.mixin']


    id_ref = fields.Many2one('article.article', string="Référence", required=True)
    
    id_fiche_article = fields.Many2one('article.article', string="fiche article")
    designation_article = fields.Char(string="Désignation", compute="get_designation_article", store=True)
    state_fiche_article = fields.Char(string="Statut", compute="get_state_fiche_article", store=True)
    type_fab_article = fields.Char(string="Type composant", compute="get_type_fab_article", store=True)
   

    @api.depends('id_ref')
    def get_designation_article(self):
        for rec in self:
             rec.designation_article = rec.id_ref.designation

    @api.depends('id_ref')
    def get_state_fiche_article(self):
        for rec in self:
             rec.state_fiche_article = rec.id_ref.state

    @api.depends('id_ref')
    def get_type_fab_article(self):
        for rec in self:
             rec.type_fab_article = rec.id_ref.reftype
             

    @api.depends('id_ref')
    def get_taux_article(self):
        for rec in self:
             rec.Taux_scrap = rec.id_ref.reftype    
    
    qtysap = fields.Float(string="Qunatité SAP(par 1000)", required=True)
    unitecomp = fields.Selection([('pce','PCE'),('l','L'),('kg','KG'),('g','G'),('zu','ZU')], string="Unité", required=True)  #TODO : SELECTION (PC,L,KG,ZU) => DONE
    Taux_scrap = fields.Float(string="Taux scrap",  required=True)
    
    combom = fields.Char(string="Commentaire")


class articlecat(models.Model):
    _name = 'article.cat'
    _description = 'article states'


    title = fields.Char()

    statename = fields.Selection([('sales', 'Sales'),('logistique', 'Logistique'),('achat1', 'Achat'), ('eng', 'Ingenieurie'), ('keyuser', 'Key user'),('achat2', 'Achat'),('finance', 'Finance'),('derogation', 'Dérogation'), ('archive', 'Archive')])
    
    color = fields.Char()
    countsales = fields.Integer(compute='_get_count_rec',default=0)
    countlogistique = fields.Integer(compute='_get_count_rec',default=0)
    countachat = fields.Integer(compute='_get_count_rec',default=0)
    counteng = fields.Integer(compute='_get_count_rec',default=0)
    countkeyuser = fields.Integer(compute='_get_count_rec',default=0)
    countfinance = fields.Integer(compute='_get_count_rec',default=0)
    countderogation = fields.Integer(compute='_get_count_rec',default=0)
    countarchive = fields.Integer(compute='_get_count_rec',default=0)

    def get_stock_picking_action_picking_type(self):
        return self._get_action('article.action_kanban')

    def _get_count_rec(self):
        for rec in self:
            rec.countsales = self.env['article.article'].search_count([('state','=','sales')])
            rec.countlogistique = self.env['article.article'].search_count([('state','=','logistique')])
            rec.countachat = self.env['article.article'].search_count([('state','in',('achat1','achat2'))])
            rec.counteng = self.env['article.article'].search_count([('state','=','eng')])
            rec.countkeyuser = self.env['article.article'].search_count([('state','=','keyuser')])
            rec.countfinance = self.env['article.article'].search_count([('state','=','finance')])
            rec.countderogation = self.env['article.article'].search_count([('state','=','derogation')])
            rec.countarchive = self.env['article.article'].search_count([('state','=','archive')])







