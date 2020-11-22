from unidecode import unidecode
import pprint
from json import dumps
from os import path

lists_names = ["flavors", "spices", "compounds"]
raw_data = {
    "flavors": [
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
        ["PHENYLACÉTALDÉHYDE"],
        ["2-PHÉNYLACÉTALDÉHYDE", "chocolat,cacao,miel"],
        ["1-PHÉNYLETHANETHIOL", "soufré,viande,floral"],
        ["PICROCROCINE", "musqué,terreux,chaud,amer"],
        ["PINÈNE", "boisé,épicé,camphré,pin,pénétrant,frais,conifère,herbacé"],
        ["PIPÉRINE", "brûlant,piquant,épicé"],
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
    "spices": [
        # [Nom humain, groupe aromatique, [composés principaux], [composés secondaires], image]
        ["Cannelle", "Phénols doux et chauds", ["ALDÉHYDE CINNAMIQUE"],
         ["CARYOPHYLLÈNE", "EUGÉNOL", "LINALOL", "MYRCÈNE"], "canelle.jpg"],
        ["Casse", "Phénols doux et chauds", ["ALDÉHYDE CINNAMIQUE"],
         ["CAMPHRE", "CINÉOL", "COUMARINE", "HEPTANONE", "COMBINAISONS DE TANNINS"], "casse.jpg"],
        ["Girofle", "Phénols doux et chauds", ["EUGÉNOL"],
         ["CARYOPHYLLÈNE", "LINALOL", "SALICYLATE DE MÉTHYLE", "TERPINÉOL"], "girofle.jpg"],
        ["Quatre-épices", "Phénols doux et chauds", ["EUGÉNOL"],
         ["CINÉOL", "LINALOL", "MYRCÈNE", "PHELLANDRÈNE", "PINÈNE"], "allspice.jpg"],
        ["Anis", "Phénols doux et chauds", ["ANÉTHOL", "ALCOOL ANISYLIQUE"],
         ["ANISALDÉHYDE", "ESTRAGOL", "LIMONÈNE", "MYRCÈNE", "PINÈNE"], "anis-vert.jpg"],
        ["Anis étoilé", "Phénols doux et chauds", ["ANÉTHOL"], ["CINÉOL", "LINALOL", "PHELLANDRÈNE", "SAFROLE"],
         "anis-etoile.jpg"],
        ["Fenouil", "Phénols doux et chauds", ["ANÉTHOL"], ["ESTRAGOL", "FENCHONE", "LIMONÈNE", "PINÈNE"],
         "fenouil.jpg"],
        ["Réglisse", "Phénols doux et chauds", ["GLYCYRRHIZINE"],
         ["ANÉTHOL", "CINÉOL", "ESTRAGOL", "EUGÉNOL", "LINALOL", "COMBINAISONS DE PHÉNOLS"], "reglisse.jpg"],
        ["Mahaleb", "Phénols doux et chauds", ["COUMARINE"],
         ["AZULÈNE", "DIOXOLANE", "MÉTHOXYÉTHYL-CINNAMATE", "PENTANOL"], "mahaleb.jpg"],
        ["Vanille", "Phénols doux et chauds", ["VANILLINE"], ["ANISALDÉHYDE", "4-HYDROXYBENZALDÉHYDE", "PIPERONAL"],
         "vanille.jpg"],
        ["Muscade", "Terpènes chauds", ["MYRISTICINE"],
         ["CINÉOL", "EUGÉNOL", "GÉRANIOL", "PINÈNE", "SABINÈNE", "SAFROLE"], "muscade.jpg"],
        ["Macis", "Terpènes chauds", ["MYRISTICINE"],
         ["ÉLÉMICINE", "EUGÉNOL", "PINÈNE", "SABINÈNE", "SAFROLE", "TERPINÈNE", "TERPINÉOL"], "macis.jpg"],
        ["Carvi", "Terpènes chauds", ["S-CARVONE"], ["CARVÉOL", "LIMONÈNE", "PINÈNE", "SABINÈNE"], "carvi.jpg"],
        ["Aneth", "Terpènes chauds", ["D-CARVONE"], ["CARVÉOL", "FENCHONE", "LIMONÈNE", "PHELLANDRÈNE", "TERPINÈNE"],
         "aneth.jpg"],
        ["Rocou", "Terpènes chauds", ["GERMACRÈNE"], ["CARYOPHYLLÈNE", "COPAÈNE", "ÉLÉMÈNE"], "rocou.jpg"],
        ["Mastic", "Terpènes odorants", ["PINÈNE"], ["CAMPHÈNE", "CARYOPHYLLÈNE", "LINALOL", "MYRCÈNE"],
         "mastic.jpg"],
        ["Genièvre", "Terpènes odorants", ["PINÈNE"], ["GÉRANIOL", "LIMONÈNE", "MYRCÈNE", "TERPINÉOL"],
         "genievre.jpg"],
        ["Rose", "Terpènes odorants", ["GÉRANIOL"],
         ["CITRONELLOL", "EUGÉNOL", "LINALOL", "NÉROL", "CÉTONES DE ROSE"], "rose.jpg"],
        ["Coriandre", "Terpènes odorants", ["LINALOL"], ["CYMÈNE", "LIMONÈNE", "PINÈNE", "TERPINÈNE"],
         "coriandre.jpg"],
        ["Cumin", "Terpènes terreux", ["ALDÉHYDE CUMINIQUE"], ["CYMÈNE", "MYRCÈNE", "PINÈNE", "TERPINÈNE"],
         "cumin.jpg"],
        ["Nigelle", "Terpènes terreux", [],
         ["CARVACROL", "D-CARVONE", "CYMÈNE", "LIMONÈNE", "PINÈNE", "THYMOQUINONE"], "nigelle.jpg"],
        ["Graines de Selim", "Terpènes pénétrants", ["FENCHONE"],
         ["CINÉOL", "GÉRANIOL", "GERMACRÈNE", "LINALOL", "PINÈNE", "VANILLINE"], "selim.jpg"],
        ["Cardamome noire", "Terpènes pénétrants", ["CINÉOL"],
         ["DIMETHOXYPHÉNOL", "EUGÉNOL", "LIMONÈNE", "COMBINAISONS DE PHÉNOLS", "PINÈNE", "SABINÈNE",
          "ACÉTATE DE TERPINYLE"], "cardamome-noire.jpg"],
        ["Cardamome", "Terpènes pénétrants", ["CINÉOL"], ["ACÉTATE D'A-FENCHYLE", "LIMONÈNE", "LINALOL"],
         "cardamome.jpg"],
        ["Laurier", "Terpènes pénétrants", ["CINÉOL"],
         ["EUGÉNOL", "GÉRANIOL", "LINALOL", "PHELLANDRÈNE", "PINÈNE", "TERPINÉOL"], "laurier.jpg"],
        ["Galanga", "Terpènes pénétrants", ["CINÉOL"],
         ["CAMPHRE", "ACÉTATE D'A-FENCHYLE", "ACÉTATE DE GALANGA", "CINNAMATE DE MÉTHYLE"], "galanga.jpg"],
        ["Citron noir séché", "Terpènes citronnés", ["CITRAL"],
         ["FENCHONE", "HUMULÈNE", "LIMONÈNE", "LINALOL", "METHOXYCOUMARINE"], "citron-noir.jpg"],
        ["Myrte citronné", "Terpènes citronnés", ["CITRAL"],
         ["CITRONELLAL", "CYCLOCITRAL", "HEPTANONE", "LINALOL", "MYRCÈNE", "PINÈNE", "SULCATONE"],
         "myrtre-citronnee.jpg"],
        ["Citronnelle", "Terpènes citronnés", ["CITRAL"], ["CARYOPHYLLÈNE", "GÉRANIOL", "LINALOL", "MYRCÈNE", "NÉROL"],
         "citronelle.jpg"],
        ["Amchur", "Acides aigres-doux", ["OCIMÈNE"],
         ["CADINÈNE", "ACIDE CITRIQUE", "CUBEBÈNE", "LIMONÈNE", "SÉLINÈNE"], "amchour.jpg"],
        ["Grenade", "Acides aigres-doux", ["ACIDE CITRIQUE", "ACIDE MALIQUE"],
         ["CARÈNE", "HEXANAL", "LIMONÈNE", "MYRCÈNE", "COMBINAISONS DE TANNINS"], "grenade.jpg"],
        ["Sumac", "Acides aigres-doux", ["ACIDE MALIQUE"],
         ["CARYOPHYLLÈNE", "CEMBRÈNE", "ACIDE CITRIQUE", "NONANAL", "PINÈNE", "COMBINAISONS DE TANNINS",
          "ACIDE TARTRIQUE"], "sumac.jpg"],
        ["Tamarin", "Acides aigres-doux", ["FURFURAL", "2-PHÉNYLACÉTALDÉHYDE"],
         ["GÉRANIOL", "LIMONÈNE", "ACIDE TARTRIQUE"], "tamarin.jpg"],
        ["Caroube", "Acides aigres-doux", ["ACIDE HEXANOÏQUE", "ACIDE PENTANOIQUE"],
         ["ALDÉHYDE CINNAMIQUE", "FARNÉSÈNE", "FURANÉOL", "COMBINAISONS DE PYRAZINES"], "caroube.jpg"],
        ["Épine-vinette", "Aldéhydes fruités", ["HEXANAL"],
         ["ANISALDÉHYDE", "ACIDE CITRIQUE", "LINALOL", "ACIDE MALIQUE", "NONANAL", "ACIDE TARTRIQUE"],
         "epine-vinette.jpg"],
        ["Cacao", "Aldéhydes fruités", ["ISOVALÉRALDÉHYDE"],
         ["DIMÉTHYLPYRAZINE", "COMBINAISONS D'ESTERS", "FURANÉOL", "COMBINAISONS DE PHÉNOLS", "PHENYLACÉTALDÉHYDE"],
         "cacao.jpg"],
        ["Paprika", "Pyrazines grillées", ["COMBINAISONS DE PYRAZINES"],
         ["ACÉTONE", "CAPSAÏCINE", "ACIDE CITRIQUE", "ACÉTATE D'ÉTHYLE", "ISOVALÉRALDÉHYDE", "ACIDE MALIQUE"],
         "paprika.jpg"],
        ["Graines d'acacia", "Pyrazines grillées", ["COMBINAISONS DE PYRAZINES"], ["CITRAL", "COMBINAISONS DE PHÉNOLS"],
         "accacia.jpg"],
        ["Sésame", "Pyrazines grillées", ["COMBINAISONS DE PYRAZINES"], ["2-FURYLMÉTHANÉTHIOL", "HEXANAL", "SÉSAMOL"],
         "sesame.jpg"],
        ["Ail", "Composés soufrés", ["DISULFURE D'ALLYLE (DE L'ALLICINE)", "TRISULFURE D'ALLYLE (DE L'ALLICINE)"],
         ["CARÈNE", "LIMONÈNE", "SABINÈNE"], "ail.jpg"],
        ["Asafoetida", "Composés soufrés", ["COMBINAISONS DE SULFURES"],
         ["EUDESMOL", "ACIDE FÉRULIQUE", "OCIMÈNE", "PHELLANDRÈNE", "PINÈNE"], "asafoetida.jpg"],
        ["Feuille de curry", "Composés soufrés", ["1-PHÉNYLETHANETHIOL"],
         ["CINÉOL", "HEXANAL", "LIMONÈNE", "LINALOL", "MYRCÈNE", "PINÈNE"], "curry.jpg"],
        ["Moutarde", "Composés soufrés", ["ISOTHIOCYANATES"],
         ["2-ACÉTYL-1-PYRROLINE", "FURANMÉTHANÉTHIOL", "ISOVALÉRALDÉHYDE", "3-MÉTHYLBUTANAL", "PINÈNE"],
         "moutarde.jpg"],
        ["Maniguette", "Composés piquants", ["PARADOL"], ["CARYOPHYLLÈNE", "GINGÉROL", "HUMULONE"], "maniguette.jpg"],
        ["Poivre noir", "Composés piquants", ["PIPÉRINE"],
         ["LIMONÈNE", "LINALOL", "MYRCÈNE", "PHELLANDRÈNE", "PINÈNE", "ROTUNDONE"], "poivre.jpg"],
        ["Poivre du Sichuan", "Composés piquants", ["SANSHOOLS"],
         ["CINÉOL", "GÉRANIOL", "LIMONÈNE", "LINALOL", "MYRCÈNE", "TERPINÉOL"], "sishuan.jpg"],
        ["Gingembre", "Composés piquants", ["GINGÉROL", "SHOGAOL", "ZINGIBERÈNE"],
         ["CINÉOL", "CITRAL", "CURCUMÈNE", "GÉRANIOL", "LINALOL"], "gingembre.jpg"],
        ["Piment", "Composés piquants", ["CAPSAÏCINE"],
         ["CAPSAICINOÏDES", "COMBINAISONS D'ESTERS", "FURFURAL", "HEXANAL""LIMONÈNE", "COMBINAISONS DE PYRAZINES"],
         "piment.jpg"],
        ["Safran", "Composés uniques", ["PICROCROCINE"], ["CINÉOL", "LANIÉRONE", "PINÈNE", "SAFRANAL"], "safran.jpg"],
        ["Pavot", "Composés uniques", ["2-PENTYLFURAN"],
         ["CAMPHRE", "EUGÉNOL", "COMBINAISONS DE GLYCOSIDES", "HEXANAL", "LIMONÈNE", "COMBINAISONS DE PHÉNOLS",
          "COMBINAISONS DE PYRAZINES", "VINYLAMYLCÉTONE"], "pavot.jpg"],
        ["Ajowan", "Composés uniques", ["THYMOL"], ["CYMÈNE", "MYRCÈNE", "PINÈNE", "TERPINÈNE"], "ajowan.jpg"],
        ["Céleri", "Composés uniques", ["SÉDANOLIDE (PHTHALIDE)"], ["HUMULÈNE", "LIMONÈNE", "SÉLINÈNE"], "celeri.jpg"],
        ["Curcuma", "Composés uniques", ["AR-TUMÉRONE"], ["CINÉOL", "CITRAL", "ZINGIBERÈNE"], "curcuma.jpg"],
        ["Fenugrec", "Composés uniques", ["SOTOLON"], ["CARYOPHYLLÈNE", "EUGÉNOL", "VINYLAMYLCÉTONE"], "fenugrec.jpg"]],
    "compounds": [
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
js_data_file_path = path.join(path.dirname(__file__), "../zurb-foundation/src/assets/js/build-blends-data.ts")


def convert_raw_data_to_dict():
    """
    Convertis les listes en dictionnaire {"nom humain": "nom_machine", ...}
    :return: affiche à l'écran le dictionnnaire.
    """
    for list_name in lists_names:
        data[list_name] = {}
        for item in raw_data[list_name]:
            if list_name == "flavors":
                if len(item) > 1:
                    data[list_name][unidecode(item[0]).replace(" ", "_").lower()] = {"human_name": item[0].lower(),
                                                                                     "description": item[1],
                                                                                     "spices_members": {
                                                                                         "main_names": [],
                                                                                         "main_number": 0,
                                                                                         "secondary_names": [],
                                                                                         "secondary_names": 0
                                                                                     }
                                                                                     }
                else:
                    data[list_name][unidecode(item[0]).replace(" ", "_").lower()] = {"human_name": item[0].lower(),
                                                                                     "description": None,
                                                                                     "spices_members": {
                                                                                         "main_names": [],
                                                                                         "main_number": 0,
                                                                                         "secondary_names": [],
                                                                                         "secondary_names": 0
                                                                                     }
                                                                                     }
            elif list_name == "spices":
                # Ajouter l'image, le groupe aromatique, les composés aromatiques principaux et secondaires
                data[list_name][unidecode(item[0]).replace(" ", "_").lower()] = {
                    "human_name": item[0].lower(),
                    "compound": unidecode(item[1]).replace(" ", "_").lower(),
                    "main_flavors": [unidecode(a).replace(" ", "_").lower() for a in item[2]],
                    "secondary_flavors": [unidecode(a).replace(" ", "_").lower() for a in item[3]],
                    "thumbnail": item[4]
                }
            elif list_name == "compounds":
                data[list_name][unidecode(item[0]).replace(" ", "_").lower()] = {
                    "human_name": item[0].lower(),
                    "color": item[1]}


def compute_data():
    # Récupére les épices par composés aromatiques
    for flavor in data["flavors"]:
        main_number = 0
        main_names = []
        secondary_number = 0
        secondary_names = []
        for spice in data["spices"]:
            for main_elem in data["spices"][spice]['main_flavors']:
                if main_elem == flavor:
                    main_number += 1
                    main_names.append(spice)
            for secondary_elem in data["spices"][spice]['secondary_flavors']:
                if secondary_elem == flavor:
                    secondary_number += 1
                    secondary_names.append(spice)
        data["flavors"][flavor]['spices_members']['main_names'] = main_names
        data["flavors"][flavor]['spices_members']['main_number'] = main_number
        data["flavors"][flavor]['spices_members']['secondary_names'] = secondary_names
        data["flavors"][flavor]['spices_members']['secondary_number'] = secondary_number


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    convert_raw_data_to_dict()
    compute_data()
    json_data = dumps(data)
    with open(js_data_file_path, "w") as file:
        content = "let data_str = JSON.stringify(" + json_data + ")\n"
        content += "let data = JSON.parse(data_str)\n"
        content += "export {data}"
        file.write(content)
