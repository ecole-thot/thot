# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config.update(
    BABEL_DEFAULT_LOCALE='fr_FR',
    BABEL_DEFAULT_TIMEZONE='Europe/Paris')
babel = Babel(app)

REGISTRATION_OPEN = False

DONATION_LINK = "https://thot.iraiser.eu/b/mon-don"
REGISTRATION_LINKS = {
  "fr": "https://docs.google.com/forms/d/e/1FAIpQLSeTdZofJkmIv6LYaX_90H-QfovX_r0arHdr6a5bVa5DJUPfbQ/viewform",
  "en": "https://docs.google.com/forms/d/e/1FAIpQLSdC_1CmwxlcpnqsWpxxitIuFePZvTt5OFaRCPmEIx74o3fI4A/viewform",
  "ar": "https://docs.google.com/forms/d/e/1FAIpQLSfNEe29Red2i5ZX-DC3mcTHfXmn6p5oqJj756YkpP6ajcGIeQ/viewform",
  "ps": "https://docs.google.com/forms/d/e/1FAIpQLSfVDZtN5BmtaWPRnXA58hnSBi8qB0s3RSSwhRrMqVp07bY7uw/viewform",
  "fa": "https://docs.google.com/forms/d/e/1FAIpQLScel6CoGtm796dgMGHm8oufh9ojfyaUgx6y5_dIzd1bg_uDJQ/viewform"
}
VOLUNTEER_OPEN = False
VOLUNTEER_LINK = "https://docs.google.com/forms/d/1wiG256MUSOQWaz9sO-3xdVXoLdnNRVqZD4kUZQnO3Zc"
BUDGET_AVAILABLE = False
NB_STUDENTS = 40

PRESS = [
    { "link": "http://www.lepoint.fr/innovation/l-echappee-volee-au-chevet-du-bonheur-11-05-2017-2126695_1928.php",
      "title": "Le Point ",
      "text": "'L'Échappée volée' au chevet du bonheur (11/05/2017)",
    },
    { "link": "https://www.franceinter.fr/idees/une-ecole-de-francais-pour-les-refugies-et-les-demandeurs-d-asile",
      "title": "France Inter",
      "text": "Une école de français pour les réfugiés et les demandeurs d’asile (11/05/2017)",
    },
    { "link": "http://www.ladn.eu/entreprises-innovantes/exponential-happiness/le-bonheur-a-portee-de-mots/",
      "title": "L'ADN",
      "text": "Le bonheur à portée de mots (27/04/2017)",
    },
    { "link": "http://www.centredelanguefrancaise.paris/partenariat-avec-l-ecole-thot/",
      "title": "Centre de langue française (CCI Paris)",
      "text": "Partenariat avec Thot, l’école de français pour les réfugiés et demandeurs d’asile (27/04/2017)",
    },
    { "link": "static/pdf/Society54.pdf",
      "title": "Society",
      "text": "Judith Aquien - La directrice (n°54 du 13 avril au 10 mai 2017)",
    },
    { "link": "static/pdf/HumaniteDimanche555.pdf",
      "title": "L’Humanité Dimanche",
      "text": "Réfugiés - En lisant, en écrivant (n°555 du 6 au 12 avril 2017)",
    },
    { "link": "http://www.liberation.fr/debats/2017/03/23/en-plus-de-l-exil-le-transfert_1557838",
      "title": "Libération",
      "text": "Tribune : En plus de l’exil, le transfert (23/03/2017)",
    },
    { "link": "http://www.humanite.fr/citoyennete-parler-francais-un-horizon-pour-tous-632957",
      "title": "L’Humanité",
      "text": "Citoyenneté. Parler français, un horizon pour tous (09/03/2017)",
    },
    { "link": "http://www.solidarum.org/inclusion-sociale/l-ecole-thot-outil-d-integration-pour-migrants",
      "title": "Solidarum",
      "text": "L’école Thot : outil d’intégration pour les migrants (08/03/2017)",
    },
    { "link": "https://laruche.wizbii.com/entrepreneures-2017/",
      "title": "WizBii",
      "text": "8 jeunes femmes entrepreneures qui comptent pour la France (08/03/2017)",
    },
    { "link": "http://www.france24.com/fr/20170301-thot-ecole-francais-migrants-refugies-paris",
      "title": "France 24",
      "text": "Thot, à l’école du français et de la dignité retrouvée (01/03/2017)",
    },
    { "link": "https://www.youtube.com/watch?v=MTTyZeAZD5I",
      "title": "BC Afrique",
      "text": "Grand reportage : L’école où les migrants apprennent le français (31/01/2017)",
    },
    { "link": "https://www.youtube.com/watch?v=pVp7FLPxOmw",
      "title": "Arte (28 Minutes)",
      "text": "Abd Al Malik parle de Thot (26/01/2017)",
    },
    { "link": "http://www.carenews.com/fr/news/6961-la-france-s-engage-pour-l-enseignement-du-francais-aux-refugies",
      "title": "Carenews",
      "text": "'La France s'engage' pour l’enseignement du français aux réfugiés (23/01/2017)",
    },
    { "link": "http://www.lejdd.fr/Societe/La-France-s-engage-l-ecole-des-migrants-recompensee-839965",
      "title": "JDD",
      "text": "'La France s'engage' : l'école des migrants récompensée (15/01/2017)",
    },
    { "link": "http://www.lci.fr/replay/replay-tous-acteurs-du-changement-du-15-janvier-2017-thot-l-ecole-qui-apprend-le-francais-aux-migrants-2021820.html ",
      "title": "LCI",
      "text": "Jennifer Leblond invitée à l’émission “Tous acteurs du changement” (15/01/2017)",
    },
    { "link": "http://www.rfi.fr/emission/20170113-thot-une-ecole-diplomante-francais-reservee-migrants",
      "title": "RFI",
      "text": "Thot, une école diplômante de français réservée aux migrants (13/01/2017)",
    },
    { "link": "http://www.madmoizelle.com/role-modele-femmes-2016-692887",
      "title": "Madmoizelle",
      "text": "Les 29 femmes qu’on retiendra de 2016 (31/12/2016)",
    },
    { "link": "http://www.huffingtonpost.fr/2016/12/06/lecole-de-francais-pour-les-refugies-obtient-93-de-reussite-ch/",
      "title": "Huffington Post",
      "text": "L'école de français pour les réfugiés obtient 93% de réussite chez ses premiers élèves (06/12/2016)",
    },
    { "link": "https://www.youtube.com/watch?v=WaW0rLa2nAA",
      "title": "TedX 2016 Université Paris-Dauphine",
      "text": "Héloïse Nio, intervenante à la conférence Ted 'Rien de bien méchant' (25/11/2016)",
    },
    { "link": "https://fr.petitsfrenchies.com/interview-judith-aquien-lune-des-fondatrices-de-lecole-thot/",
      "title": "Les petits Frenchies",
      "text": "Interview : Judith Aquien, l'une des fondatrices de l’école Thot (20/11/2016)",
    },
    { "link": "http://www.rtl.fr/girls/identites/en-images-semaine-mondiale-de-l-entrepreneur-ces-francaises-qui-deboitent-7785768739",
      "title": "RTL Girls",
      "text": "Semaine mondiale de l'entrepreneur : ces Françaises qui déboîtent (15/11/2016)",
    },
    { "link": "http://chouette.ulule.com/post/152895488187/thot-l%C3%A9cole-de-fran%C3%A7ais-pour-les-r%C3%A9fugi%C3%A9s",
      "title": "Blog Ulule",
      "text": "Thot, l’école de français pour les réfugiés : infographie (09/11/2016)",
    },
    { "link": "https://www.franceinter.fr/emissions/peripheries/peripheries-28-octobre-2016",
      "title": "France Inter",
      "text": "Périphéries (Édouard Zambeaux) - 'C'est le temps de rire maintenant' (28/10/2016)",
    },
    { "link": "http://www.franceinter.fr/emissions/la-revue-de-presse-de-frederic-pommier/la-revue-de-presse-de-frederic-pommier-09-octobre-2016",
      "title": "France Inter",
      "text": "Revue de presse de Frédéric Pommier - de 2'16 à 3'33 (09/10/2016)",
    },
    { "link": "static/pdf/ELLE_Integration_Langue.pdf",
      "title": "ELLE",
      "text": "L’intégration sur le bout de la langue (numéro du 07/10/2016)",
    },
    { "link": "https://www.youtube.com/watch?v=QONw7MZ5FBM",
      "title": "RFI >> Accents d’Europe",
      "text": "Reportage chez Thot par Frédérique Lebel (22/09/2016)"
    },
    { "link": "http://www.psychologies.com/Planete/Societe/Interviews/Des-seances-psy-pour-les-migrants",
      "title": "Psychologies",
      "text": "Des séances psy pour les migrants (09/2016)"
    },
    { "link": "http://www.psychologies.com/Planete/Societe/Articles-et-Dossiers/Ali-demandeur-d-asile-tente-de-construire-sa-vie-loin-de-sa-famille",
      "title": "Psychologies",
      "text": "Ali, demandeur d’asile, tente de construire sa vie loin de sa famille (09/2016)"
    },
    { "link": "http://www.kiyoblog.com/single-post/2016/09/08/Thot-l%C3%A9cole-de-langue-pour-les-r%C3%A9fugi%C3%A9s",
      "title": "Kiyo",
      "text": "Thot, une école diplômante pour les réfugiés (08/09/2016)"
    },
    { "link": "http://weareup.com/des-solutions-pour-une-integration-reussie-des-refugies/?utm_campaign=IntegrationRefugies&utm_medium=newsletterdirex7&utm_source=NewsletterDirex7&utm_content=postdu30082016&utm_term=VF",
      "title": "We Are Up",
      "text": "Des solutions pour une intégration réussie des réfugiés (30/08/2016)"
    },
    { "link": "https://www.youtube.com/watch?v=zIvNMosII0g",
      "title": "BBC Afrique",
      "text": "Thot dans le Grand Reportage de BBC Afrique (27/08/2016)"
    },
    { "link": "http://www.happyproject.world/single-post/2016/07/06/Judith-Aquien-elle-a-cr%C3%A9%C3%A9-une-%C3%A9cole-de-fran%C3%A7ais-pour-les-r%C3%A9fugi%C3%A9s",
      "title": "Happy Project",
      "text": "Judith Aquien a créé Thot, une école de français pour les réfugiés (06/07/2016)"
    },
    { "link": "http://www.marianne.net/ecole-les-migrants-100244200.html",
      "title": "Marianne",
      "text": "Une école pour les migrants (numéro du 1er au 7 juillet 2016)"
    },
    { "link": "https://www.youtube.com/watch?v=NHo02x-xUkc&",
      "title": "TV5MONDE",
      "text": "Judith Aquien invitée au Grand Angle du 64 Minutes (30/06/2016)"
    },
    { "link": "http://tedxchampselyseesed.com/articles/en-exil-leducation-pour-se-reconnecter-avec-les-autres-et-avec-son-avenir-10/",
      "title": "TedX Champs-Elysées",
      "text": "TedX Champs-Elysées Salon En exil : l’éducation pour se reconnecter avec les autres et avec son avenir (24/06/2016)"
    },
    { "link": "http://www.up-inspirer.fr/26826-thot-une-ecole-de-francais-au-service-des-refugies",
      "title": "UP Le Mag",
      "text": "Thot : Une école de français au service des réfugiés (24/062016)"
    },
    { "link": "http://www.20minutes.fr/paris/1867675-20160620-ecole-thot-cours-francais-redonner-voix-refugies",
      "title": "20 Minutes",
      "text": "Ecole Thot : Des cours de français, pour redonner une voix aux réfugiés (20/06/2016)"
    },
    { "link": "http://www.huffingtonpost.fr/jennifer-leblond/journee-mondiale-des-refugies-video_b_10522138.html",
      "title": "Huffington Post",
      "text": "Où apprendre le français et être diplômé quand on est réfugié ? (20/06/2016)"
    },
    { "link": "http://up-conferences.fr/fest/",
      "title": "UP Fest 'Le temps des héros'",
      "text": "Judith Aquien parle de Thot (18/06/2016)"
    },
    { "link": "http://www.faiseursdeboite.fr/thot-association-ecole-langue-francaise",
      "title": "Faiseurs de boîte",
      "text": "Thot, une école diplômante pour les demandeurs d’asile et les réfugiés (13/062016)"
    },
    { "link": "http://www.lemonde.fr/immigration-et-diversite/article/2016/06/13/l-association-thot-ouvre-a-paris-une-ecole-de-francais-pour-les-migrants_4949471_1654200.html",
      "title": "Le Monde",
      "text": "L’association Thot ouvre à Paris une école de français pour les migrants (13/06/2016)"
    },
    { "link": "http://www.leparisien.fr/societe/paris-c-est-la-rentree-des-classes-pour-40-refugies-09-06-2016-5869837.php",
      "title": "Le Parisien",
      "text": "Paris : c'est la rentrée des classes pour 40 réfugiés (13/06/2016)"
    },
    { "link": "http://www.la-croix.com/Famille/Education/A-Paris-une-ecole-pour-l-insertion-des-migrants-2016-06-13-1200768298",
      "title": "La Croix",
      "text": "À Paris, une école pour l'insertion des migrants (13/06/2016)"
    },
    { "link": "http://www.carenews.com/fr/news/5337-thot-une-ecole-de-francais-pour-transmettre-un-horizon-aux-migrants",
      "title": "Carenews",
      "text": "Thot, une école de français pour transmettre un horizon aux migrants (06/06/2016)"
    },
    { "link": "http://www.leparisien.fr/montreuil-93100/montreuil-elles-ont-monte-une-ecole-de-francais-pour-refugies-02-06-2016-5851387.php",
      "title": "Le Parisien",
      "text": "Montreuil : elles ont monté une école de français pour réfugiés (02/06/2016)"
    },
    { "link": "http://www.lefigaro.fr/actualite-france/2016/06/02/01016-20160602ARTFIG00161-paris-une-association-lance-une-ecole-de-langue-francaise-pour-les-refugies.php",
      "title": "Le Figaro",
      "text": "Paris : une association lance une école de langue française pour les réfugiés (02/06/2016)"
    },
    { "link": "http://www.lesinrocks.com/2016/05/31/actualite/12-femmes-bousculer-quotidien-11826880/",
      "title": "Les Inrocks",
      "text": "12 femmes qui vont bousculer votre quotidien (31/05/2016)"
    },
    { "link": "http://www.franceculture.fr/emissions/rue-des-ecoles/rue-des-ecoles-dimanche-29-mai-2016",
      "title": "France Culture (\"Rue des écoles\")",
      "text": "Focus : \"Thot, une école pour les migrants\", avec Judith Aquien, présidente de Thot à 48' (29/05/2016)"
    },
    { "link": "https://www.mediapart.fr/journal/france/260516/migrants-comment-aider",
      "title": "Mediapart",
      "text": "Migrants: comment aider? (26/05/2016)"
    },
    { "link": "http://www.goodmorningcrowdfunding.com/international-refugies-leducation-problematique-preoccupante-02260516/",
      "title": "Good Morning Crowdfunding",
      "text": "Les réfugiés et l’éducation, une problématique préoccupante (26/05/2016)"
    },
    { "link": "http://lapartducolibri.fr/?p=837",
      "title": "La Part du colibri",
      "text": "Une école diplômante pour apprendre le français aux réfugiés (23/05/2016)"
    },
    { "link": "http://2016.wetalk-community.org/modeles-feminins/",
      "title": "W(e) Talk",
      "text": "Judith Aquien, Présidente de Thot, sélectionnée parmi les 8 modèles féminins 2016, à la conférence \"Artisanes du commun, qui forment ensemble pour un autre demain\" (21/05/2016)"
    },
    { "link": "http://www.lexpress.fr/actualites/1/styles/a-paris-une-ecole-des-refugies-pour-apprendre-le-francais_1794126.html",
      "title": "L’Express via l’AFP",
      "text": "A Paris, une \"école des réfugiés\" pour apprendre le français (20/05/2016)"
    },
    { "link": "http://tempsreel.nouvelobs.com/societe/20160520.AFP5837/a-paris-une-ecole-des-refugies-pour-apprendre-le-francais.html",
      "title": "L'Obs",
      "text": "A Paris, une \"école des réfugiés\" pour apprendre le français (20/05/2016)"
    },
    { "link": "http://www.rtl.be/info/monde/international/a-paris-une-ecole-des-refugies-pour-apprendre-le-francais-819890.aspx",
      "title": "RTL",
      "text": "A Paris, une \"école des réfugiés\" pour apprendre le français (20/05/2016)"
    },
    { "link": "http://www.lepoint.fr/societe/thot-l-ecole-qui-apprend-le-francais-aux-refugies-20-05-2016-2040741_23.php",
      "title": "Le Point",
      "text": "Thot, l'école qui apprend le français aux réfugiés (20/05/2016)"
    },
    { "link": "http://www.letudiant.fr/jobsstages/creation-entreprise/heloise-nio-25-ans-cofondatrice-d-une-ecole-pour-former-les-exiles-a-la-langue-francaise.html",
      "title": "L'Etudiant",
      "text": "Héloïse a cofondé une école pour former les exilés à la langue française (19/05/2016)"
    },
    { "link": "http://www.leparisien.fr/montreuil-93100/montreuil-elles-veulent-creer-une-ecole-de-francais-pour-les-refugies-19-05-2016-5810251.php",
      "title": "Le Parisien",
      "text": "Elles veulent créer une école de français pour les réfugiés (19/05/2016)"
    },
    { "link": "http://www.lecourrierdelatlas.com/1138518052016Une-ecole-pour-apprendre-le-francais-aux-refugies.html",
      "title": "Le Courrier de l'Atlas",
      "text": "\"Une école pour apprendre le français aux réfugiés\" (18/05/2016)"
    },
    { "link": "https://savoir.actualitte.com/article/scolarite/1798/du-crowdfunding-pour-creer-une-ecole-apprenant-le-francais-aux-refugies",
      "title": "Actualitté",
      "text": "Du crowdfunding pour créer une école apprenant le français aux réfugiés (13/05/2016)"
    },
    { "link": "http://www.clique.tv/thot-lecole-diplomante-pour-les-refugies/",
      "title": "Clique.tv",
      "text": "Thot, l’école diplômante pour les réfugiés qui veulent apprendre le français (11/05/2016)"
    },
    { "link": "http://pressee.fr/judith-aquien-il-faut-transmettre-un-horizon-aux-refugies/#more-898",
      "title": "Pressée",
      "text": "« Avec Thot, on transmet un horizon aux réfugiés. » (11/05/2016)"
    },
    { "link": "http://www.redattoresociale.it/Notiziario/Articolo/507633/In-Francia-apre-Thot-scuola-di-francese-per-richiedenti-asilo-e-rifugiati",
      "title": "Redattore Sociale",
      "text": "In Francia apre “Thot”, scuola di francese per richiedenti asilo e rifugiati (11/05/2016)"
    },
    { "link": "http://www.novaplanet.com/radionova/bientot-2h-14-avant-la-fin-du-monde-thot-la-formation-qui-apprend-le-francais-aux-refugies",
      "title": "Nova - 2h 1/4 avant la fin du monde",
      "text": "Judith Aquien invitée de Marie Misset et Armel Hemme (09/05/2016)"
    },
    { "link": "https://youtu.be/eWT6qQ79b-g?t=1m34s",
      "title": "L'Autre JT",
      "text": "Sarah Constantin met 20/20 à Thot - 20'24'' (05/05/2016)"
    },
    { "link": "http://www.telerama.fr/monde/le-resome-pour-que-l-ecole-accueille-les-refugies-dans-la-dignite,141947.php",
      "title": "Télérama",
      "text": "Le Resome, pour que l’école accueille les réfugiés dans la dignité (05/05/2016)"
    },
    { "link": "https://www.youtube.com/watch?v=KqqYWuFPRpE&feature=youtu.be",
      "title": "LCI",
      "text": "Thot invité au journal de midi (05/05/2016)"
    },
    { "link": "http://annieallmusic.blogspot.fr/2016/05/thot-un-grand-pas-vers-lintegration.html",
      "title": "Annie All Music",
      "text": "Thot, un grand pas vers l'intégration (02/05/2016)"
    },
    { "link": "http://www.liberation.fr/debats/2016/05/02/ils-ferment-les-frontieres-ouvrons-nos-ecoles_1450031",
      "title": "Libération",
      "text": "\"Ils ferment les frontières, ouvrons nos écoles\" - tribune du Résome dans Libération (02/05/2016)"
    },
    { "link": "http://bit.ly/1SVONvB",
      "title": "Cosmopolitaine, France Inter",
      "text": "Chronique de Marie-Madeleine Rigopoulos sur Thot - 26'30\" (01/05/2016)"
    },
    { "link": "http://issuu.com/lcf-magazine/docs/lcff_magazine_n__40-_issuu/43?e=6017579/35344828",
      "title": "Langue et culture françaises & francophones",
      "text": "Le magazine LCFF nous offre une page de publicité (numéro 40, mai 2016) (01/05/2016)"
    },
    { "link": "http://www.integrales-productions.com/2016/04/30/thot-lecole-diplomante-de-francais-pour-eleves-en-migration/",
      "title": "Intégrales Mag",
      "text": "Thot, l’école diplomante de français pour élèves en migration (30/04/2016)"
    },
    { "link": "http://www.novaplanet.com/radionova/61238/episode-thot-la-formation-qui-apprend-le-francais-aux-refugies",
      "title": "Le futur c'est maintenant, Nova",
      "text": "Chronique de Côme Bastin sur Thot (30/04/2016)"
    },
    { "link": "http://cheekmagazine.fr/societe/thot-judith-aquien-ecole-francais-refugies/",
      "title": "Cheek Magazine",
      "text": "Elle a quitté son job pour créer Thot, une école de français destinée aux réfugiés (29/04/2016)"
    },
    { "link": "http://bit.ly/1QPVrPj",
      "title": "One Heart",
      "text": "Thot, une école pour les réfugiés à soutenir sur Ulule (29/04/2016)"
    },
    { "link": "http://www.lecourrier-du-soir.com/articles/h%C3%A9lo%C3%AFse-%C2%AB-le-de-l%E2%80%99association-thot-est-que-les-r%C3%A9fugi%C3%A9s-fassent-partie-de-la-france-%C2%BB",
      "title": "Le Courrier du Soir", 
      "text": "Le but de l’association Thot est que les réfugiés fassent partie de la France (27/04/2016)"
    },
    { "link": "http://consocollaborative.com/article/elles-lancent-une-ecole-de-francais-pour-les-refugies-grace-au-crowdfunding/",
      "title": "Conso Collaborative",
      "text": "Elles lancent une école de français pour les réfugiés (26/04/2016)"
    },
    { "link": "https://rcf.fr/actualite/journal-regional-du-mardi-26-avril",
      "title": "RCF",
      "text": "Journal Régional — 1'36\" (26/04/2016)"
    },
    { "link": "http://agi.to/agitox-actualite-fle-edu-76/",
      "title": "Agito", 
      "text": "Thot FLE, une école diplômante pour migrants (22/04/2016)"
    },
    { "link": "http://www.liberation.fr/direct/element/une-ecole-pour-migrants-gratuite-et-diplomante-pourrait-voir-le-jour-en-france_35401/",
      "title": "Libération",
      "text": "Une école pour migrants gratuite et diplômante pourrait voir le jour en France (18/04/2016)"
    },
    { "link": "http://www.rfi.fr/emission/20160418-institut-francais-bucarest",
      "title": "RFI",
      "text": "Chronique « Ma Parole » : Interview d'Imaad Ali, directeur pédagogique de l'école Thot - 17'55 (18/04/16)"
    },
    { "link": "https://savoirs.rfi.fr/fr/communaute/langue-francaise/ma-parole-on-vous-presente-thot",
      "title": "RFI — Émission « Danse avec les mots »",
      "text": "Chronique « Ma Parole » : on vous présente Thot (11/04/2016)"
    }
]

@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    locale = getattr(request, 'locale', None)
    if locale is not None:
        return locale
    return 'fr'


def render_home():
    return render_template(
        'home.html',
        donation_link=DONATION_LINK,
        registration_links=REGISTRATION_LINKS,
        registration_open=REGISTRATION_OPEN,
        volunteer_link=VOLUNTEER_LINK,
        volunteer_open=VOLUNTEER_OPEN,
        budget_available=BUDGET_AVAILABLE,
        nb_students=NB_STUDENTS,
        press=PRESS,
        locale=request.locale)


@app.route('/')
def homepage_fr():
    request.locale = 'fr'
    return render_home()


@app.route('/en.html')
def homepage_en():
    request.locale = 'en'
    return render_home()


@app.route('/ar.html')
def homepage_ar():
    request.locale = 'ar'
    return render_home()


@app.route('/ps.html')
def homepage_ps():
    request.locale = 'ps'
    return render_home()


@app.route('/fa.html')
def homepage_fa():
    request.locale = 'fa'
    return render_home()


if __name__ == '__main__':
    app.run(port=8080, debug=True)
