from unidecode import unidecode

lists_names = ["composes_aromatiques", "epices", "groupes_aromatiques"]
raw_data = {
    "composes_aromatiques": [
        ["ACÉTONE"],
        ["2-ACÉTYL-1-PYRROLINE"],
        ["ANÉTHOL", "doux,médicinal,fenouil,réglisse,chaud,herbacé,anisé"],
        ["ANISALDÉHYDE", "doux,boisé,anisé"],
        ["ALCOOL ANISYLIQUE", "cerise,vanille,floral"],
        ["AZULÈNE", "boisé,poivré,herbacé"],
        ["CADINÈNE", "herbacé,boisé,épicé"],
        ["A-CADINOL"],
        ["CAMPHÈNE"],
        ["CAMPHRE", "piquant,médicinal,amer"],
        ["CAPSAÏCINE"],
        ["CAPSAICINOÏDES", "enragé,anesthésiant,piquant"],
        ["CARÈNE", "doux,piquant,térébenthine"],
        ["CARVACROL"],
        ["CARVÉOL"],
        ["D-CARVONE", "épicé,mentholé,réglisse"],
        ["S-CARVONE", "épicé,mentholé,réglisse"],
        ["CARYOPHYLLÈNE", "épicé,boisé,poivré,sec,amer,chaud,terreux,girofle"],
        ["CEMBRÈNE"],
        ["CINÉOL", "pénétrant,eucalyptus,frais,médicinal,herbacé"],
        ["ALDÉHYDE CINNAMIQUE", "chaud,épicé,piquant,doux,odorant"],
        ["CITRAL", "agrumes,herbacé,eucalyptus,acidulé,frais,zeste de citron"],
        ["ACIDE CITRIQUE", "citronné,acide,agrumes"],
        ["CITRONELLAL"],
        ["CITRONELLOL"],
        ["COPAÈNE", "miel,boisé,épicé"],
        ["COUMARINE", "doux,chaud,végétal,floral"],
        ["ALDÉHYDE CUMINIQUE", "amer,herbacé,terreux"],
        ["CURCUMÈNE"],
        ["CYCLOCITRAL"],
        ["CYMÈNE", "frais,boisé,agrumes,âpre"],
        ["CUBEBÈNE", "citronné,fruité,radis"],
        ["DISULFURE D'ALLYLE (DE L'ALLICINE)", "soufré,épicé,brûlant"],
        ["TRISULFURE D'ALLYLE (DE L'ALLICINE)", "soufré,épicé,brûlant"],
        ["DIMETHOXYPHÉNOL"],
        ["DIMÉTHYLPYRAZINE"],
        ["DIOXOLANE"],
        ["ÉLÉMÈNE", "agrumes,doux,aiguilles de pin"],
        ["ÉLÉMICINE"],
        ["COMBINAISONS D'ESTERS", "fruité,doux,cireux"],
        ["ESTRAGOL", "réglisse,chaud,boisé,anisé"],
        ["ACÉTATE D'ÉTHYLE", "doux,fruité"],
        ["EUDESMOL"],
        ["EUGÉNOL", "médicinal,boisé,chaud,girofle,eucalyptus"],
        ["FARNÉSÈNE"],
        ["FENCHONE", "camphré,amer,piquant,pénétrant,chaud"],
        ["ACÉTATE D'A-FENCHYLE", "doux,menthe,herbacé"],
        ["ACIDE FÉRULIQUE"],
        ["FURANMÉTHANÉTHIOL"],
        ["FURANÉOL"],
        ["FURFURAL", "doux,pain,amande"],
        ["2-FURYLMÉTHANÉTHIOL", "noisettes,café,viande rotie"],
        ["ACÉTATE DE GALANGA"],
        ["GÉRANIOL", "floral,rose,doux,persistant"],
        ["GERMACRÈNE", "bois,doux,épicé"],
        ["GINGÉROL", "chaud,piquant,épicé,brûlant"],
        ["COMBINAISONS DE GLYCOSIDES"],
        ["GLYCYRRHIZINE"],
        ["HEPTANONE"],
        ["HEXANAL", "vert,fruité,herbeux"],
        ["ACIDE HEXANOÏQUE"],
        ["HUMULÈNE", "boisé,épicé,amer"],
        ["HUMULONE", "amer,houblon,terreux"],
        ["4-HYDROXYBENZALDÉHYDE"],
        ["4-HYDROXYBENZALDÉHYDE"],
        ["ISOTHIOCYANATES", "brûlant,poivré,pénétrant"],
        ["ISOVALÉRALDÉHYDE", "chocolaté,gras,pêche,beurré"],
        ["LANIÉRONE"],
        ["LIMONÈNE", "agrumes,végétal,herbacé,térébenthine"],
        ["LINALOL", "floral,lilas,boisé,épicé,agrumes,doux,bois de rose"],
        ["ACIDE MALIQUE", "âpre"],
        ["METHOXYCOUMARINE", "doux,balsamique"],
        ["MÉTHOXYÉTHYL-CINNAMATE", "chaud,balsamique,fruité"],
        ["3-MÉTHYLBUTANAL"],
        ["CINNAMATE DE MÉTHYLE", "balsamique,cerise,canelle"],
        ["MÉTHYL-HEPTÉNONE"],
        ["SALICYLATE DE MÉTHYLE"],
        ["MYRCÈNE", "poivré,balsamique,épicé,térébenthine,boisé,piquant,céleri"],
        ["MYRISTICINE", "boisé,chaud,balsamique"],
        ["NÉROL", "fleur d'oranger,doux,frais"],
        ["NONANAL", "vert,herbeux,fruité"],
        ["OCIMÈNE", "floral,végétal,tropical"],
        ["PARADOL", "brûlant,épicé,piquant"],
        ["ACIDE PENTANOIQUE", "aigrelet,fromage suintant"],
        ["PENTANOL", "balsamique,fruité,floral"],
        ["2-PENTYLFURAN", "végétal"],
        ["PHELLANDRÈNE", "poivré,menthe,agrumes,vert,épicé,piquant"],
        ["COMBINAISONS DE PHÉNOLS"],
        ["PHENYLACETALDEHYDE"],
        ["2-PHÉNYLACÉTALDÉHYDE", "chocolat,cacao,miel"],
        ["1-PHÉNYLETHANETHIOL", "soufré,viande,floral"],
        ["PICROCROCINE", "musqué,terreux,chaud,amer"],
        ["PINÈNE", "boisé,épicé,camphré,pin,pénétrant,frais,conifère,herbacé"],
        ["PIPÉRINE", "brûlant,piquant,épicé"],
        ["PIPERONAL", "floral,subtiles notes de cerises,"],
        ["PIPERONAL", "floral,subtiles notes de cerises,"],
        ["COMBINAISONS DE PYRAZINES", "noisette,torréfié,pain,boisé,terreux,fumé,caramel"],
        ["CÉTONES DE ROSE"],
        ["ROTUNDONE"],
        ["SABINÈNE", "agrumes,poivré,boisé,camphré,épicé,orange,pin"],
        ["SAFRANAL", "miel,foin,floral"],
        ["SAFROLE", "rose,doux,chaud,anisé"],
        ["SANSHOOLS", "brûlant,anesthésiant,picotant"],
        ["SÉDANOLIDE (PHTHALIDE)", "herbacé,doux,végétal"],
        ["SÉLINÈNE"],
        ["SÉSAMOL"],
        ["SHOGAOL"],
        ["SOTOLON", "doux,sirop d'érable,caramel"],
        ["SULCATONE", "vert,pomme,humus"],
        ["COMBINAISONS DE SULFURES"],
        ["COMBINAISONS DE TANNINS"],
        ["ACIDE TARTRIQUE", "aigre,acide,âpre"],
        ["TERPINÈNE", "boisé"],
        ["TERPINÉOL", "floral,agrumes,pin"],
        ["ACÉTATE DE TERPINYLE"],
        ["THYMOL", "thym,pénétrant,refroidissant"],
        ["THYMOQUINONE"],
        ["AR-TUMÉRONE"],
        ["VANILLINE", "doux,chaud,odorant,crémeux"],
        ["VINYLAMYLCÉTONE", "terreux,crémeux,humus"],
        ["ZINGIBERÈNE", "piquant,âpre,épicé"],
        ["COMPOSÉS MINEURS RÉGLISSE", "floral,concombre,origan"]],
    "epices": [
        # [Nom humain, groupe aromatique, composé principal, [composés secondaires], image]
        ["Cannelle", "Phénols doux et chauds", "CARYOPHYLLÈNE", [], "canelle.jpg"],
        ["Casse", "Phénols doux et chauds", "$principale$", [], "casse.jpg"],
        ["Girofle", "Phénols doux et chauds", "$principale$", [], "girofle.jpg"],
        ["Quatre-épices", "Phénols doux et chauds", "$principale$", [], "allspice.jpg"],
        ["Anis", "Phénols doux et chauds", "$principale$", [], "anis-vert.jpg"],
        ["Anis étoilé", "Phénols doux et chauds", "$principale$", [], "anis-etoile.jpg"],
        ["Fenouil", "Phénols doux et chauds", "$principale$", [], "fenouil.jpg"],
        ["Réglisse", "Phénols doux et chauds", "$principale$", [], "reglisse.jpg"],
        ["Mahaleb", "Phénols doux et chauds", "$principale$", [], "mahaleb.jpg"],
        ["Vanille", "Phénols doux et chauds", "$principale$", [], "vanille.jpg"],
        ["Muscade", "Terpènes chauds", "$principale$", [], "muscade.jpg"],
        ["Macis", "Terpènes chauds", "$principale$", [], "macis.jpg"],
        ["Carvi", "Terpènes chauds", "$principale$", [], "carvi.jpg"],
        ["Aneth", "Terpènes chauds", "$principale$", [], "aneth.jpg"],
        ["Rocou", "Terpènes chauds", "$principale$", [], "rocou.jpg"],
        ["Mastic", "Terpènes odorants", "$principale$", [], "mastic.jpg"],
        ["Genièvre", "Terpènes odorants", "$principale$", [], "genievre.jpg"],
        ["Rose", "Terpènes odorants", "$principale$", [], "rose.jpg"],
        ["Coriandre", "Terpènes odorants", "$principale$", [], "coriandre.jpg"],
        ["Cumin", "Terpènes terreux", "$principale$", [], "cumin.jpg"],
        ["Nigelle", "Terpènes terreux", "$principale$", [], "nigelle.jpg"],
        ["Graines de Selim", "Terpènes pénétrants", "$principale$", [], "selim.jpg"],
        ["Cardamome noire", "Terpènes pénétrants", "$principale$", [], "cardamome-noire.jpg"],
        ["Cardamome", "Terpènes pénétrants", "$principale$", [], ".jpg"],
        ["Laurier", "Terpènes pénétrants", "$principale$", [], "cardamome.jpg"],
        ["Galanga", "Terpènes pénétrants", "$principale$", [], "galanga.jpg"],
        ["Citron noir séché", "Terpènes citronnés", "$principale$", [], "citron-noir.jpg"],
        ["Myrte citronné", "Terpènes citronnés", "$principale$", [], "myrtre-citronnee.jpg"],
        ["Citronnelle", "Terpènes citronnés", "$principale$", [], "citronelle.jpg"],
        ["Amchur", "Acides aigres-doux", "$principale$", [], "amchour.jpg"],
        ["Grenade", "Acides aigres-doux", "$principale$", [], "grenade.jpg"],
        ["Sumac", "Acides aigres-doux", "$principale$", [], "sumac.jpg"],
        ["Tamarin", "Acides aigres-doux", "$principale$", [], "tamarin.jpg"],
        ["Caroube", "Acides aigres-doux", "$principale$", [], "caroube.jpg"],
        ["Épine-vinette", "Aldéhydes fruités", "$principale$", [], "epine-vinette.jpg"],
        ["Cacao", "Aldéhydes fruités", "$principale$", [], "cacao.jpg"],
        ["Paprika", "Pyrazines grillées", "$principale$", [], "paprika.jpg"],
        ["Graines d'acacia", "Pyrazines grillées", "$principale$", [], "accacia.jpg"],
        ["Sésame", "Pyrazines grillées", "$principale$", [], "sesame.jpg"],
        ["Ail", "Composés soufrés", "$principale$", [], ".jpg", "ail.jpg"],
        ["Asafoetida", "Composés soufrés", "$principale$", [], "asafoetida.jpg"],
        ["Feuille de curry", "Composés soufrés", "$principale$", [], "curry.jpg"],
        ["Moutarde", "Composés soufrés", "$principale$", [], "moutarde.jpg"],
        ["Maniguette", "Composés piquants", "$principale$", [], "maniguette.jpg"],
        ["Poivre noir", "Composés piquants", "$principale$", [], "poivre.jpg"],
        ["Poivre du Sichuan", "Composés piquants", "$principale$", [], "sishuan.jpg"],
        ["Gingembre", "Composés piquants", "$principale$", [], "gingembre.jpg"],
        ["Piment", "Composés piquants", "$principale$", [], "piment.jpg"],
        ["Safran", "Composés uniques", "$principale$", [], "safran.jpg"],
        ["Pavot", "Composés uniques", "$principale$", [], "pavot.jpg"],
        ["Ajowan", "Composés uniques", "$principale$", [], "ajowan.jpg"],
        ["Céleri", "Composés uniques", "$principale$", [], "celeri.jpg"],
        ["Curcuma", "Composés uniques", "$principale$", [], "curcuma.jpg"],
        ["Fenugrec", "Composés uniques", "$principale$", [], "fenugrec.jpg"]],
    "groupes_aromatiques": [
        ["Phénols doux et chauds", "edb487"],
        ["Terpènes chauds", "c9b4a1"],
        ["Terpènes odorants", "d2b0ae"],
        ["Terpènes terreux", "b3aea8"],
        ["Terpènes pénétrants", "a2bfc5"],
        ["Terpènes citronnés", "a0b7a3"],
        ["Acides aigres-doux", "f1cb8a"],
        ["Aldéhydes fruités", "c09dbb"],
        ["Pyrazines grillées", "bd9ab8"],
        ["Composés soufrés", "d5ba85"],
        ["Composés piquants", "f0a38f"],
        ["Composés uniques", "a8b297"]]

}
data = {}
cleaned_data = {'composes_aromatiques': {'ACETONE': {'human_name': 'ACÉTONE', 'description': None},
                                         '2-ACETYL-1-PYRROLINE': {'human_name': '2-ACÉTYL-1-PYRROLINE',
                                                                  'description': None},
                                         'ANETHOL': {'human_name': 'ANÉTHOL',
                                                     'description': 'doux,médicinal,fenouil,réglisse,chaud,herbacé,anisé'},
                                         'ANISALDEHYDE': {'human_name': 'ANISALDÉHYDE',
                                                          'description': 'doux,boisé,anisé'},
                                         'ALCOOL_ANISYLIQUE': {'human_name': 'ALCOOL ANISYLIQUE',
                                                               'description': 'cerise,vanille,floral'},
                                         'AZULENE': {'human_name': 'AZULÈNE', 'description': 'boisé,poivré,herbacé'},
                                         'CADINENE': {'human_name': 'CADINÈNE', 'description': 'herbacé,boisé,épicé'},
                                         'A-CADINOL': {'human_name': 'A-CADINOL', 'description': None},
                                         'CAMPHENE': {'human_name': 'CAMPHÈNE', 'description': None},
                                         'CAMPHRE': {'human_name': 'CAMPHRE', 'description': 'piquant,médicinal,amer'},
                                         'CAPSAICINE': {'human_name': 'CAPSAÏCINE', 'description': None},
                                         'CAPSAICINOIDES': {'human_name': 'CAPSAICINOÏDES',
                                                            'description': 'enragé,anesthésiant,piquant'},
                                         'CARENE': {'human_name': 'CARÈNE', 'description': 'doux,piquant,térébenthine'},
                                         'CARVACROL': {'human_name': 'CARVACROL', 'description': None},
                                         'CARVEOL': {'human_name': 'CARVÉOL', 'description': None},
                                         'D-CARVONE': {'human_name': 'D-CARVONE',
                                                       'description': 'épicé,mentholé,réglisse'},
                                         'S-CARVONE': {'human_name': 'S-CARVONE',
                                                       'description': 'épicé,mentholé,réglisse'},
                                         'CARYOPHYLLENE': {'human_name': 'CARYOPHYLLÈNE',
                                                           'description': 'épicé,boisé,poivré,sec,amer,chaud,terreux,girofle'},
                                         'CEMBRENE': {'human_name': 'CEMBRÈNE', 'description': None},
                                         'CINEOL': {'human_name': 'CINÉOL',
                                                    'description': 'pénétrant,eucalyptus,frais,médicinal,herbacé'},
                                         'ALDEHYDE_CINNAMIQUE': {'human_name': 'ALDÉHYDE CINNAMIQUE',
                                                                 'description': 'chaud,épicé,piquant,doux,odorant'},
                                         'CITRAL': {'human_name': 'CITRAL',
                                                    'description': 'agrumes,herbacé,eucalyptus,acidulé,frais,zeste de citron'},
                                         'ACIDE_CITRIQUE': {'human_name': 'ACIDE CITRIQUE',
                                                            'description': 'citronné,acide,agrumes'},
                                         'CITRONELLAL': {'human_name': 'CITRONELLAL', 'description': None},
                                         'CITRONELLOL': {'human_name': 'CITRONELLOL', 'description': None},
                                         'COPAENE': {'human_name': 'COPAÈNE', 'description': 'miel,boisé,épicé'},
                                         'COUMARINE': {'human_name': 'COUMARINE',
                                                       'description': 'doux,chaud,végétal,floral'},
                                         'ALDEHYDE_CUMINIQUE': {'human_name': 'ALDÉHYDE CUMINIQUE',
                                                                'description': 'amer,herbacé,terreux'},
                                         'CURCUMENE': {'human_name': 'CURCUMÈNE', 'description': None},
                                         'CYCLOCITRAL': {'human_name': 'CYCLOCITRAL', 'description': None},
                                         'CYMENE': {'human_name': 'CYMÈNE', 'description': 'frais,boisé,agrumes,âpre'},
                                         'CUBEBENE': {'human_name': 'CUBEBÈNE', 'description': 'citronné,fruité,radis'},
                                         "DISULFURE_D'ALLYLE_(DE_L'ALLICINE)": {
                                             'human_name': "DISULFURE D'ALLYLE (DE L'ALLICINE)",
                                             'description': 'soufré,épicé,brûlant'},
                                         "TRISULFURE_D'ALLYLE_(DE_L'ALLICINE)": {
                                             'human_name': "TRISULFURE D'ALLYLE (DE L'ALLICINE)",
                                             'description': 'soufré,épicé,brûlant'},
                                         'DIMETHOXYPHENOL': {'human_name': 'DIMETHOXYPHÉNOL', 'description': None},
                                         'DIMETHYLPYRAZINE': {'human_name': 'DIMÉTHYLPYRAZINE', 'description': None},
                                         'DIOXOLANE': {'human_name': 'DIOXOLANE', 'description': None},
                                         'ELEMENE': {'human_name': 'ÉLÉMÈNE',
                                                     'description': 'agrumes,doux,aiguilles de pin'},
                                         'ELEMICINE': {'human_name': 'ÉLÉMICINE', 'description': None},
                                         "COMBINAISONS_D'ESTERS": {'human_name': "COMBINAISONS D'ESTERS",
                                                                   'description': 'fruité,doux,cireux'},
                                         'ESTRAGOL': {'human_name': 'ESTRAGOL',
                                                      'description': 'réglisse,chaud,boisé,anisé'},
                                         "ACETATE_D'ETHYLE": {'human_name': "ACÉTATE D'ÉTHYLE",
                                                              'description': 'doux,fruité'},
                                         'EUDESMOL': {'human_name': 'EUDESMOL', 'description': None},
                                         'EUGENOL': {'human_name': 'EUGÉNOL',
                                                     'description': 'médicinal,boisé,chaud,girofle,eucalyptus'},
                                         'FARNESENE': {'human_name': 'FARNÉSÈNE', 'description': None},
                                         'FENCHONE': {'human_name': 'FENCHONE',
                                                      'description': 'camphré,amer,piquant,pénétrant,chaud'},
                                         "ACETATE_D'A-FENCHYLE": {'human_name': "ACÉTATE D'A-FENCHYLE",
                                                                  'description': 'doux,menthe,herbacé'},
                                         'ACIDE_FERULIQUE': {'human_name': 'ACIDE FÉRULIQUE', 'description': None},
                                         'FURANMETHANETHIOL': {'human_name': 'FURANMÉTHANÉTHIOL', 'description': None},
                                         'FURANEOL': {'human_name': 'FURANÉOL', 'description': None},
                                         'FURFURAL': {'human_name': 'FURFURAL', 'description': 'doux,pain,amande'},
                                         '2-FURYLMETHANETHIOL': {'human_name': '2-FURYLMÉTHANÉTHIOL',
                                                                 'description': 'noisettes,café,viande rotie'},
                                         'ACETATE_DE_GALANGA': {'human_name': 'ACÉTATE DE GALANGA',
                                                                'description': None},
                                         'GERANIOL': {'human_name': 'GÉRANIOL',
                                                      'description': 'floral,rose,doux,persistant'},
                                         'GERMACRENE': {'human_name': 'GERMACRÈNE', 'description': 'bois,doux,épicé'},
                                         'GINGEROL': {'human_name': 'GINGÉROL',
                                                      'description': 'chaud,piquant,épicé,brûlant'},
                                         'COMBINAISONS_DE_GLYCOSIDES': {'human_name': 'COMBINAISONS DE GLYCOSIDES',
                                                                        'description': None},
                                         'GLYCYRRHIZINE': {'human_name': 'GLYCYRRHIZINE', 'description': None},
                                         'HEPTANONE': {'human_name': 'HEPTANONE', 'description': None},
                                         'HEXANAL': {'human_name': 'HEXANAL', 'description': 'vert,fruité,herbeux'},
                                         'ACIDE_HEXANOIQUE': {'human_name': 'ACIDE HEXANOÏQUE', 'description': None},
                                         'HUMULENE': {'human_name': 'HUMULÈNE', 'description': 'boisé,épicé,amer'},
                                         'HUMULONE': {'human_name': 'HUMULONE', 'description': 'amer,houblon,terreux'},
                                         '4-HYDROXYBENZALDEHYDE': {'human_name': '4-HYDROXYBENZALDÉHYDE',
                                                                   'description': None},
                                         'ISOTHIOCYANATES': {'human_name': 'ISOTHIOCYANATES',
                                                             'description': 'brûlant,poivré,pénétrant'},
                                         'ISOVALERALDEHYDE': {'human_name': 'ISOVALÉRALDÉHYDE',
                                                              'description': 'chocolaté,gras,pêche,beurré'},
                                         'LANIERONE': {'human_name': 'LANIÉRONE', 'description': None},
                                         'LIMONENE': {'human_name': 'LIMONÈNE',
                                                      'description': 'agrumes,végétal,herbacé,térébenthine'},
                                         'LINALOL': {'human_name': 'LINALOL',
                                                     'description': 'floral,lilas,boisé,épicé,agrumes,doux,bois de rose'},
                                         'ACIDE_MALIQUE': {'human_name': 'ACIDE MALIQUE', 'description': 'âpre'},
                                         'METHOXYCOUMARINE': {'human_name': 'METHOXYCOUMARINE',
                                                              'description': 'doux,balsamique'},
                                         'METHOXYETHYL-CINNAMATE': {'human_name': 'MÉTHOXYÉTHYL-CINNAMATE',
                                                                    'description': 'chaud,balsamique,fruité'},
                                         '3-METHYLBUTANAL': {'human_name': '3-MÉTHYLBUTANAL', 'description': None},
                                         'CINNAMATE_DE_METHYLE': {'human_name': 'CINNAMATE DE MÉTHYLE',
                                                                  'description': 'balsamique,cerise,canelle'},
                                         'METHYL-HEPTENONE': {'human_name': 'MÉTHYL-HEPTÉNONE', 'description': None},
                                         'SALICYLATE_DE_METHYLE': {'human_name': 'SALICYLATE DE MÉTHYLE',
                                                                   'description': None},
                                         'MYRCENE': {'human_name': 'MYRCÈNE',
                                                     'description': 'poivré,balsamique,épicé,térébenthine,boisé,piquant,céleri'},
                                         'MYRISTICINE': {'human_name': 'MYRISTICINE',
                                                         'description': 'boisé,chaud,balsamique'},
                                         'NEROL': {'human_name': 'NÉROL', 'description': "fleur d'oranger,doux,frais"},
                                         'NONANAL': {'human_name': 'NONANAL', 'description': 'vert,herbeux,fruité'},
                                         'OCIMENE': {'human_name': 'OCIMÈNE', 'description': 'floral,végétal,tropical'},
                                         'PARADOL': {'human_name': 'PARADOL', 'description': 'brûlant,épicé,piquant'},
                                         'ACIDE_PENTANOIQUE': {'human_name': 'ACIDE PENTANOIQUE',
                                                               'description': 'aigrelet,fromage suintant'},
                                         'PENTANOL': {'human_name': 'PENTANOL',
                                                      'description': 'balsamique,fruité,floral'},
                                         '2-PENTYLFURAN': {'human_name': '2-PENTYLFURAN', 'description': 'végétal'},
                                         'PHELLANDRENE': {'human_name': 'PHELLANDRÈNE',
                                                          'description': 'poivré,menthe,agrumes,vert,épicé,piquant'},
                                         'COMBINAISONS_DE_PHENOLS': {'human_name': 'COMBINAISONS DE PHÉNOLS',
                                                                     'description': None},
                                         'PHENYLACETALDEHYDE': {'human_name': 'PHENYLACETALDEHYDE',
                                                                'description': None},
                                         '2-PHENYLACETALDEHYDE': {'human_name': '2-PHÉNYLACÉTALDÉHYDE',
                                                                  'description': 'chocolat,cacao,miel'},
                                         '1-PHENYLETHANETHIOL': {'human_name': '1-PHÉNYLETHANETHIOL',
                                                                 'description': 'soufré,viande,floral'},
                                         'PICROCROCINE': {'human_name': 'PICROCROCINE',
                                                          'description': 'musqué,terreux,chaud,amer'},
                                         'PINENE': {'human_name': 'PINÈNE',
                                                    'description': 'boisé,épicé,camphré,pin,pénétrant,frais,conifère,herbacé'},
                                         'PIPERINE': {'human_name': 'PIPÉRINE', 'description': 'brûlant,piquant,épicé'},
                                         'PIPERONAL': {'human_name': 'PIPERONAL',
                                                       'description': 'floral,subtiles notes de cerises,'},
                                         'COMBINAISONS_DE_PYRAZINES': {'human_name': 'COMBINAISONS DE PYRAZINES',
                                                                       'description': 'noisette,torréfié,pain,boisé,terreux,fumé,caramel'},
                                         'CETONES_DE_ROSE': {'human_name': 'CÉTONES DE ROSE', 'description': None},
                                         'ROTUNDONE': {'human_name': 'ROTUNDONE', 'description': None},
                                         'SABINENE': {'human_name': 'SABINÈNE',
                                                      'description': 'agrumes,poivré,boisé,camphré,épicé,orange,pin'},
                                         'SAFRANAL': {'human_name': 'SAFRANAL', 'description': 'miel,foin,floral'},
                                         'SAFROLE': {'human_name': 'SAFROLE', 'description': 'rose,doux,chaud,anisé'},
                                         'SANSHOOLS': {'human_name': 'SANSHOOLS',
                                                       'description': 'brûlant,anesthésiant,picotant'},
                                         'SEDANOLIDE_(PHTHALIDE)': {'human_name': 'SÉDANOLIDE (PHTHALIDE)',
                                                                    'description': 'herbacé,doux,végétal'},
                                         'SELINENE': {'human_name': 'SÉLINÈNE', 'description': None},
                                         'SESAMOL': {'human_name': 'SÉSAMOL', 'description': None},
                                         'SHOGAOL': {'human_name': 'SHOGAOL', 'description': None},
                                         'SOTOLON': {'human_name': 'SOTOLON',
                                                     'description': "doux,sirop d'érable,caramel"},
                                         'SULCATONE': {'human_name': 'SULCATONE', 'description': 'vert,pomme,humus'},
                                         'COMBINAISONS_DE_SULFURES': {'human_name': 'COMBINAISONS DE SULFURES',
                                                                      'description': None},
                                         'COMBINAISONS_DE_TANNINS': {'human_name': 'COMBINAISONS DE TANNINS',
                                                                     'description': None},
                                         'ACIDE_TARTRIQUE': {'human_name': 'ACIDE TARTRIQUE',
                                                             'description': 'aigre,acide,âpre'},
                                         'TERPINENE': {'human_name': 'TERPINÈNE', 'description': 'boisé'},
                                         'TERPINEOL': {'human_name': 'TERPINÉOL', 'description': 'floral,agrumes,pin'},
                                         'ACETATE_DE_TERPINYLE': {'human_name': 'ACÉTATE DE TERPINYLE',
                                                                  'description': None},
                                         'THYMOL': {'human_name': 'THYMOL',
                                                    'description': 'thym,pénétrant,refroidissant'},
                                         'THYMOQUINONE': {'human_name': 'THYMOQUINONE', 'description': None},
                                         'AR-TUMERONE': {'human_name': 'AR-TUMÉRONE', 'description': None},
                                         'VANILLINE': {'human_name': 'VANILLINE',
                                                       'description': 'doux,chaud,odorant,crémeux'},
                                         'VINYLAMYLCETONE': {'human_name': 'VINYLAMYLCÉTONE',
                                                             'description': 'terreux,crémeux,humus'},
                                         'ZINGIBERENE': {'human_name': 'ZINGIBERÈNE',
                                                         'description': 'piquant,âpre,épicé'},
                                         'COMPOSES_MINEURS_REGLISSE': {'human_name': 'COMPOSÉS MINEURS RÉGLISSE',
                                                                       'description': 'floral,concombre,origan'}},
                'epices': {'Cannelle': 'Cannelle', 'Casse': 'Casse', 'Girofle': 'Girofle',
                           'Quatre-epices': 'Quatre-épices', 'Anis': 'Anis', 'Anis_etoile': 'Anis étoilé',
                           'Fenouil': 'Fenouil', 'Reglisse': 'Réglisse', 'Mahaleb': 'Mahaleb', 'Vanille': 'Vanille',
                           'Muscade': 'Muscade', 'Macis': 'Macis', 'Carvi': 'Carvi', 'Aneth': 'Aneth', 'Rocou': 'Rocou',
                           'Mastic': 'Mastic', 'Genievre': 'Genièvre', 'Rose': 'Rose', 'Coriandre': 'Coriandre',
                           'Cumin': 'Cumin', 'Nigelle': 'Nigelle', 'Graines_de_Selim': 'Graines de Selim',
                           'Cardamome_noire': 'Cardamome noire', 'Cardamome': 'Cardamome', 'Laurier': 'Laurier',
                           'Galanga': 'Galanga', 'Citron_noir_seche': 'Citron noir séché',
                           'Myrte_citronne': 'Myrte citronné', 'Citronnelle': 'Citronnelle', 'Amchur': 'Amchur',
                           'Grenade': 'Grenade', 'Sumac': 'Sumac', 'Tamarin': 'Tamarin', 'Caroube': 'Caroube',
                           'Epine-vinette': 'Épine-vinette', 'Cacao': 'Cacao', 'Paprika': 'Paprika',
                           "Graines_d'acacia": "Graines d'acacia", 'Sesame': 'Sésame', 'Ail': 'Ail',
                           'Asafoetida': 'Asafoetida', 'Feuille_de_curry': 'Feuille de curry', 'Moutarde': 'Moutarde',
                           'Maniguette': 'Maniguette', 'Poivre_noir': 'Poivre noir',
                           'Poivre_du_Sichuan': 'Poivre du Sichuan', 'Gingembre': 'Gingembre', 'Piment': 'Piment',
                           'Safran': 'Safran', 'Pavot': 'Pavot', 'Ajowan': 'Ajowan', 'Celeri': 'Céleri',
                           'Curcuma': 'Curcuma', 'Fenugrec': 'Fenugrec'},
                'groupes_aromatiques': {'Phenols_doux_et_chauds': 'Phénols doux et chauds',
                                        'Terpenes_chauds': 'Terpènes chauds', 'Terpenes_odorants': 'Terpènes odorants',
                                        'Terpenes_terreux': 'Terpènes terreux',
                                        'Terpenes_penetrants': 'Terpènes pénétrants',
                                        'Terpenes_citronnes': 'Terpènes citronnés',
                                        'Acides_aigres-doux': 'Acides aigres-doux',
                                        'Aldehydes_fruites': 'Aldéhydes fruités',
                                        'Pyrazines_grillees': 'Pyrazines grillées',
                                        'Composes_soufres': 'Composés soufrés',
                                        'Composes_piquants': 'Composés piquants',
                                        'Composes_uniques': 'Composés uniques'}}


def convert_raw_data_to_dict():
    """
    Convertis les listes en dictionnaire {"nom humain": "nom_machine", ...}
    :return: affiche à l'écran le dictionnnaire.
    """
    for list_name in lists_names:
        data[list_name] = {}
        for item in raw_data[list_name]:
            if list_name == "composes_aromatiques":
                if len(item) > 1:
                    data[list_name][unidecode(item[0]).replace(" ", "_")] = {"human_name": item[0],
                                                                             "description": item[1]}
                else:
                    data[list_name][unidecode(item[0]).replace(" ", "_")] = {"human_name": item[0],
                                                                             "description": None}
            elif list_name =="epices":
                # Ajouter l'image, le groupe aromatique, les composés aromatiques principaux et secondaires
                pass
            else:
                data[list_name][unidecode(item).replace(" ", "_")] = item
    print(data)


if __name__ == "__main__":
    # Cette fonction me sert à créer le dictionnaire "cleaned_data" (son contenu est la sortie print de la fonction
    # convert_raw_data_to_dict().
    convert_raw_data_to_dict()