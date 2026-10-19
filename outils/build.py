#!/usr/bin/env python3
"""Génère les pages HTML de la maquette ALBIZZIA. Usage : python3 outils/build.py (depuis la racine du dépôt)."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO_URL = "https://webaunet.github.io/ALBIZZIA/"
TEL, TEL_RAW, MAIL = "06 24 36 33 76", "+33624363376", "contact@albizzia-paysage.com"

NAV = [("index.html", "Accueil"), ("prestations.html", "Prestations"), ("realisations.html", "Réalisations"),
       ("economie-impots.html", "Économie d'impôts"), ("qui-sommes-nous.html", "Qui sommes-nous"), ("contact.html", "Contact")]


def img(name, alt, w, h, lazy=True, cls=""):
    c = f' class="{cls}"' if cls else ""
    l = ' loading="lazy"' if lazy else ""
    return f'<img{c} src="img/{name}.webp" width="{w}" height="{h}"{l} alt="{html.escape(alt)}">'


A = {  # (fichier, largeur, hauteur, alt exact)
    "hero": ("hero-elagage-chene", 1376, 768, "Un élagueur encordé taille un grand chêne au-dessus d'un jardin et d'une maison en briques"),
    "creation": ("creation-espace-vert", 900, 491, "Jardinière à genoux plantant un massif le long d'une pelouse sinueuse devant une maison moderne"),
    "entretien": ("entretien-jardin", 900, 491, "Jardin soigné avec allée gravillonnée, pelouse tondue et massifs devant une maison en pierre"),
    "elagage": ("elagage-chene", 900, 491, "Élagueur encordé travaillant à la tronçonneuse dans un chêne"),
    "dessouchage": ("dessouchage", 900, 491, "Machine de dessouchage broyant une souche dans une pelouse"),
    "plantation": ("plantation", 900, 491, "Jardinier plantant un arbuste dans une terre fraîchement travaillée"),
    "haie_allee": ("taille-haies-allee", 900, 491, "Jardinier taillant une haie au taille-haie thermique devant une maison en briques"),
    "haie_laurier": ("taille-haies-laurier", 900, 672, "Jardinier avec casque antibruit taillant une haie de laurier"),
    "terrassement": ("terrassement", 900, 502, "Jardinier bêchant la terre au pied d'une maison, brouette à côté"),
    "tonte_casque": ("tonte-entretien", 900, 502, "Jardinier casqué poussant une tondeuse devant une maison en pierre"),
    "tonte_volets": ("tonte-volets", 900, 502, "Jardinier tondant une pelouse devant une maison à volets bleus"),
    "desherbage": ("desherbage", 900, 491, "Jardinier agenouillé désherbant un massif fleuri au bord d'une allée"),
    "feuilles": ("feuilles", 900, 491, "Jardinier ramassant des feuilles mortes dans un sac sur une allée de gravier"),
    "dechets": ("dechets-verts", 900, 491, "Jardinier chargeant des déchets verts sur une remorque près d'une camionnette"),
    "nettoyage": ("nettoyage", 900, 502, "Jardinier ratissant des tailles de haie à côté d'une brouette"),
    "nivellement": ("nivellement", 900, 491, "Jardinier ratissant la terre pour niveler un terrain"),
}


def I(key, lazy=True, cls="", alt=None):
    n, w, h, a = A[key]
    return img(n, alt or a, w, h, lazy, cls)


def header(current):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items += f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header>
  <div class="wrap bar">
    <a class="logo" href="{LOGO_URL}" aria-label="Albizzia Paysage, accueil"><i></i>Albizzia <small>Paysage</small></a>
    <nav id="menu" aria-label="Navigation principale"><ul>{items}</ul></nav>
    <a class="btn call" href="tel:{TEL_RAW}" aria-label="Appeler le {TEL}"><span>{TEL}</span><i class="ph" aria-hidden="true"></i></a>
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Ouvrir le menu"><span></span></button>
  </div>
</header>'''


FOOTER = f'''<footer>
  <div class="wrap">
    <b>Albizzia Paysage</b>
    <span>Angerville (91) · <a href="tel:{TEL_RAW}">{TEL}</a> · <a href="mailto:{MAIL}">{MAIL}</a></span>
    <a href="mentions-legales.html">Mentions légales</a>
  </div>
</footer>'''


def page(fname, title, desc, body, main_cls=""):
    cur = fname
    out = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Instrument+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
{header(cur)}
<main id="contenu">
{body}
</main>
{FOOTER}
<script src="js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(out)


def cta(eyebrow, h2, p, key, flip=False, btn="Nous contacter"):
    fl = " flip" if flip else ""
    return f'''<section class="cta{fl}" aria-labelledby="cta-t">
  <div class="wrap cols">
    <div>
      <span class="eyebrow">{eyebrow}</span>
      <h2 id="cta-t">{h2}</h2>
      <p>{p}</p>
      <div class="actions"><a class="btn" href="contact.html">{btn}</a><a class="btn ghost" href="tel:{TEL_RAW}">Appeler le {TEL}</a></div>
    </div>
    <div class="ctimg">{I(key)}</div>
  </div>
</section>'''


def fig(key, cap, w6=False):
    c = ' class="w6"' if w6 else ""
    return f"<figure{c}>{I(key)}<figcaption>{cap}</figcaption></figure>"

# ---------------------------------------------------------------- ACCUEIL
home = f'''
  <section class="hero">
    {I("hero", lazy=False).replace('<img ', '<img fetchpriority="high" ')}
    <div class="wrap">
      <span class="eyebrow">Paysagiste à Angerville, Essonne</span>
      <h1>Avec Albizzia, faites pousser vos envies.</h1>
      <p>Création de jardins, entretien, élagage, abattage et dessouchage. Une équipe qui vous garantit sérieux, savoir-faire et disponibilité.</p>
      <div class="actions"><a class="btn" href="contact.html">Demander un devis</a><a class="btn ghost" href="prestations.html">Voir nos prestations</a></div>
    </div>
  </section>

  <section class="sec screen" id="prestations">
    <div class="wrap">
      <div class="head">
        <span class="eyebrow">Nos prestations</span>
        <h2>Du premier plan de jardin à l'entretien de chaque saison</h2>
        <p>Particuliers et propriétaires d'Île-de-France : nous créons vos espaces verts, nous les entretenons et nous intervenons sur vos arbres.</p>
      </div>
      <div class="grid five">
        <article class="card">{I("creation")}<div><h3>Création et aménagement extérieur</h3><p>Massifs, pelouses, allées et plantations pensés pour votre terrain et votre façon de vivre dehors.</p></div></article>
        <article class="card">{I("entretien")}<div><h3>Entretien de jardins et espaces verts</h3><p>Tonte, taille des haies, désherbage et nettoyage pour un jardin soigné toute l'année.</p></div></article>
        <article class="card">{I("elagage")}<div><h3>Élagage et abattage</h3><p>Intervention sur vos arbres, du simple élagage à l'abattage.</p></div></article>
        <article class="card">{I("dessouchage")}<div><h3>Dessouchage</h3><p>La souche est broyée sur place et le terrain redevient utilisable.</p></div></article>
        <article class="card text"><div><h3>Aménagement intérieur, terrasses et balcons</h3><p>Aménagement de vos espaces intérieurs, de vos terrasses et de vos balcons.</p></div></article>
      </div>
      <div class="more"><a class="btn line" href="prestations.html">Toutes nos prestations</a></div>
    </div>
  </section>

  <section class="band screen" aria-labelledby="fisc">
    <div class="wrap cols">
      <div>
        <span class="eyebrow">Avantage fiscal</span>
        <h2 id="fisc">Une partie de vos travaux de jardinage peut être déduite</h2>
        <p>Pour les services à la personne, la réduction d'impôt atteint 50 % des sommes versées, dans la limite de 2 500 € pour le jardinage. Parlez-nous de votre projet, nous vous indiquerons ce qui est concerné.</p>
        <div class="more"><a class="btn ghost" href="economie-impots.html">Tout savoir sur l'économie d'impôts</a></div>
      </div>
      <div class="big50"><b>50&nbsp;%</b><span>de réduction d'impôt, plafonnée à 2 500 € pour le jardinage</span></div>
    </div>
  </section>

  <section class="about screen" id="a-propos">
    <div class="wrap cols">
      <figure>
        {I("plantation")}
        <figcaption>Depuis 1996<small>Reprise en octobre 2020</small></figcaption>
      </figure>
      <div>
        <span class="eyebrow">Qui sommes-nous</span>
        <h2>Une entreprise de paysage installée à Angerville</h2>
        <p>Albizzia a été créée en 1996 par Nathalie Ponthieux. Elle est reprise en octobre 2020 par Dany et Ronan Nedelec, qui la dirigent aujourd'hui.</p>
        <p>L'équipe est pluridisciplinaire et travaille avec du matériel de qualité, pour mener un chantier de la plantation à l'abattage.</p>
        <ul class="facts"><li>Essonne (91)</li><li>Île-de-France</li><li>Équipe pluridisciplinaire</li></ul>
        <div class="more"><a class="btn line" href="qui-sommes-nous.html">Notre histoire</a></div>
      </div>
    </div>
  </section>

  <section class="contact screen" id="contact">
    <div class="wrap cols">
      <div>
        <span class="eyebrow" style="color:#e9a3bb">Contact</span>
        <h2 style="margin-top:14px">Un jardin à créer, un arbre à traiter ?</h2>
        <p>Décrivez-nous votre projet par téléphone ou par e-mail. Nous revenons vers vous pour en parler.</p>
        <div class="actions"><a class="btn" href="contact.html">Demander un devis</a><a class="btn ghost" href="tel:{TEL_RAW}">Appeler le {TEL}</a></div>
      </div>
      <dl class="coords" style="margin:0">
        <div><dt>Téléphone</dt><dd><span id="tel">{TEL}</span><button class="copy" type="button" data-copy="tel">Copier</button></dd></div>
        <div><dt>E-mail</dt><dd><span id="mail">{MAIL}</span><button class="copy" type="button" data-copy="mail">Copier</button></dd></div>
        <div><dt>Commune</dt><dd>Angerville (91)</dd></div>
      </dl>
    </div>
  </section>'''
page("index.html", "Albizzia Paysage, paysagiste à Angerville (91)",
     "Albizzia, paysagiste à Angerville en Essonne : création et aménagement de jardins, entretien, élagage, abattage et dessouchage en Île-de-France.", home)

# ---------------------------------------------------------------- PRESTATIONS
prest = f'''
  <section class="ph-hero">
    <div class="wrap cols">
      <div>
        <span class="eyebrow">Nos prestations</span>
        <h1>Aménager, entretenir, abattre&nbsp;: tout pour vos extérieurs</h1>
        <p>Albizzia intervient chez les particuliers à Angerville et partout en Île-de-France. Choisissez ce qui vous concerne.</p>
        <div class="actions"><a class="btn" href="#amenager">Aménager</a><a class="btn ghost" href="#entretenir">Entretenir</a></div>
      </div>
      <div class="mosaic">{I("creation", lazy=False)}{I("tonte_volets", lazy=False)}{I("elagage", lazy=False)}</div>
    </div>
  </section>

  <section class="sec screen" id="amenager">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Aménager</span><h2>Donner forme à votre jardin, à votre terrasse, à votre balcon</h2></div>
      <div class="row">
        <div class="rimg">{I("nivellement")}</div>
        <div><h3>Création et aménagement extérieur</h3><p>De la terre nivelée à la plantation, nous préparons le terrain puis installons massifs, pelouses et allées selon votre projet.</p></div>
      </div>
      <div class="row rev">
        <div class="rimg"><div class="panel"><p style="color:var(--onDeepMuted)">Photo à ajouter : aucune image du dossier ne montre un aménagement de terrasse, de balcon ou d'intérieur.</p></div></div>
        <div><h3>Aménagement intérieur, terrasses et balcons</h3><p>Nous aménageons aussi vos espaces intérieurs, vos terrasses et vos balcons. Dites-nous ce que vous imaginez, nous en discutons ensemble.</p></div>
      </div>
    </div>
  </section>

  <section class="alt screen" id="entretenir">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Entretenir</span><h2>Un jardin suivi tout au long de l'année</h2></div>
      <div class="row">
        <div class="rimg">{I("haie_allee")}</div>
        <div><h3>Entretien de jardins et espaces verts</h3><p>Taille des haies, tonte, désherbage, ramassage des feuilles et évacuation des déchets verts : un entretien régulier pour un jardin net.</p></div>
      </div>
      <div class="gal">{fig("desherbage","Désherbage")}{fig("feuilles","Ramassage des feuilles")}{fig("dechets","Évacuation des déchets verts")}</div>
    </div>
  </section>

  <section class="sec screen" id="arbres">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Les arbres</span><h2>Intervenir en hauteur, libérer le terrain</h2></div>
      <div class="row">
        <div class="rimg">{I("hero")}</div>
        <div><h3>Élagage et abattage</h3><p>Nous intervenons dans vos arbres, de l'élagage d'un chêne à l'abattage lorsqu'il le faut.</p></div>
      </div>
      <div class="row rev">
        <div class="rimg">{I("dessouchage")}</div>
        <div><h3>Dessouchage</h3><p>Après l'abattage, la souche est broyée sur place pour libérer le terrain.</p></div>
      </div>
    </div>
  </section>
  {cta("Un projet particulier ?", "Votre besoin n'est pas dans la liste ? Décrivez-le nous.", "Un jardin, un balcon, un arbre gênant : expliquez la situation et nous voyons ensemble ce qu'il est possible de faire.", "plantation", btn="Décrire mon projet")}'''
page("prestations.html", "Prestations paysagiste à Angerville | Albizzia",
     "Création et aménagement de jardins, entretien, élagage, abattage, dessouchage, terrasses et balcons : les prestations d'Albizzia à Angerville (91) et en Île-de-France.", prest)

# ---------------------------------------------------------------- RÉALISATIONS
real = f'''
  <section class="ph-hero">
    <div class="wrap cols">
      <div>
        <span class="eyebrow">Nos réalisations en image</span>
        <h1>Des chantiers de jardin, vus de près</h1>
        <p>Création, entretien, travail en hauteur : un aperçu des types de chantiers qu'Albizzia mène chez ses clients.</p>
        <div class="actions"><a class="btn" href="#creations">Voir les créations</a><a class="btn ghost" href="#entretien">Voir l'entretien</a></div>
      </div>
      <div class="fan">{I("creation", lazy=False)}{I("entretien", lazy=False)}{I("dessouchage", lazy=False)}</div>
    </div>
  </section>

  <section class="sec screen" id="creations">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Créer</span><h2>Préparer la terre, planter, structurer l'espace</h2></div>
      <div class="gal">{fig("terrassement","Terrassement au pied de la maison")}{fig("nivellement","Nivellement du terrain")}{fig("plantation","Plantation d'un arbuste")}</div>
      <p class="note">Images d'illustration. Les photos de vos chantiers réels viendront les remplacer.</p>
    </div>
  </section>

  <section class="alt screen" id="entretien">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Entretenir</span><h2>Haies, pelouses, massifs et allées</h2></div>
      <div class="gal">{fig("tonte_volets","Tonte de la pelouse", True)}{fig("haie_allee","Taille d'une haie", True)}{fig("desherbage","Désherbage d'un massif", True)}{fig("feuilles","Ramassage des feuilles", True)}</div>
    </div>
  </section>

  <section class="sec screen" id="arbres">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Arbres et déchets verts</span><h2>Élagage, dessouchage et évacuation</h2></div>
      <div class="gal">{fig("elagage","Élagage d'un chêne")}{fig("hero","Travail en hauteur dans un chêne")}{fig("dechets","Chargement des déchets verts")}{fig("nettoyage","Nettoyage après la taille", True)}{fig("tonte_casque","Entretien à la tondeuse", True)}</div>
    </div>
  </section>
  {cta("Votre projet", "Un chantier qui ressemble au vôtre ?", "Montrez-nous votre terrain ou décrivez-le. Nous regardons ce qui peut être fait et nous revenons vers vous.", "haie_laurier", flip=True, btn="Parler de mon chantier")}'''
page("realisations.html", "Réalisations de jardins et élagages | Albizzia Angerville",
     "Galerie d'images des chantiers d'Albizzia, paysagiste à Angerville (91) : création de jardin, entretien, élagage et dessouchage.", real)

# ---------------------------------------------------------------- ÉCONOMIE D'IMPÔTS
eco = f'''
  <section class="ph-hero">
    <div class="wrap cols">
      <div>
        <span class="eyebrow">Économie d'impôts</span>
        <h1>Jusqu'à 50 % de vos dépenses de jardinage en réduction d'impôt</h1>
        <p>Les services à la personne ouvrent droit à un avantage fiscal. Il peut concerner l'entretien de votre jardin.</p>
        <div class="actions"><a class="btn" href="contact.html">Poser ma question</a></div>
      </div>
      <div class="bigfig"><b>50&nbsp;%</b><span>des sommes versées, dans la limite de 2 500 € pour le jardinage</span></div>
    </div>
  </section>

  <section class="sec screen">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">À retenir</span><h2>Trois repères sur l'avantage fiscal</h2></div>
      <div class="facts3">
        <div class="fact"><b>50 %</b><h3>Réduction d'impôt</h3><p>Elle porte sur les sommes versées pour les services à la personne.</p></div>
        <div class="fact"><b>2 500 €</b><h3>Limite pour le jardinage</h3><p>C'est le plafond indiqué pour les travaux de jardinage.</p></div>
        <div class="fact"><b>Services</b><h3>À la personne</h3><p>L'avantage concerne ce type de services rendus à votre domicile.</p></div>
      </div>
    </div>
  </section>

  <section class="alt screen">
    <div class="wrap split">
      <div>
        <span class="eyebrow">Votre situation</span>
        <h2>Savoir ce qui est concerné dans votre projet</h2>
        <p>Toutes les prestations ne relèvent pas forcément des services à la personne. Décrivez-nous votre projet : nous vous disons ce qui est concerné.</p>
        <p>Pour votre déclaration, référez-vous aux règles en vigueur sur impots.gouv.fr. Ces informations sont données à titre indicatif.</p>
        <div class="more"><a class="btn line" href="contact.html">Décrire mon projet</a></div>
      </div>
      <div>{I("tonte_casque")}</div>
    </div>
  </section>
  {cta("Gardons le contact", "Un doute sur votre éligibilité ?", "Appelez-nous avec les grandes lignes de votre projet. Nous partons de votre jardin pour vous répondre.", "desherbage", btn="Poser ma question")}'''
page("economie-impots.html", "Économie d'impôts jardinage | Albizzia Angerville",
     "Réduction d'impôt de 50 % pour les services à la personne, dans la limite de 2 500 € pour le jardinage : ce qu'il faut savoir avec Albizzia, paysagiste à Angerville.", eco)

# ---------------------------------------------------------------- QUI SOMMES-NOUS
qui = f'''
  <section class="ph-hero">
    <div class="wrap cols">
      <div>
        <span class="eyebrow">Qui sommes-nous</span>
        <h1>Une entreprise de paysage qui change de mains, pas d'exigence</h1>
        <p>Créée en 1996, reprise en 2020 par Dany et Ronan Nedelec, Albizzia travaille depuis Angerville.</p>
        <div class="actions"><a class="btn" href="contact.html">Nous rencontrer</a></div>
      </div>
      <div>{I("haie_laurier", lazy=False, cls="solo")}</div>
    </div>
  </section>

  <section class="sec screen">
    <div class="wrap">
      <div class="sub"><span class="eyebrow">Notre histoire</span><h2>Trois repères dans la vie de l'entreprise</h2></div>
      <ol class="tl">
        <li><time>1996</time><h3>Création</h3><p>Nathalie Ponthieux fonde Albizzia.</p></li>
        <li><time>Octobre 2020</time><h3>Reprise</h3><p>Dany et Ronan Nedelec reprennent l'entreprise et la dirigent.</p></li>
        <li><time>Aujourd'hui</time><h3>Angerville, Essonne</h3><p>L'équipe intervient en Île-de-France, chez les particuliers.</p></li>
      </ol>
    </div>
  </section>

  <section class="alt screen">
    <div class="wrap split">
      <div>{I("nettoyage")}</div>
      <div>
        <span class="eyebrow">Notre engagement</span>
        <h2>Sérieux, savoir-faire et disponibilité</h2>
        <p>C'est la promesse d'Albizzia à chaque client. Elle s'appuie sur une équipe pluridisciplinaire et du matériel de qualité, du jardin à l'arbre.</p>
        <p>Pour échanger sur votre projet, appelez-nous au {TEL}.</p>
        <div class="more"><a class="btn line" href="prestations.html">Voir ce que nous faisons</a></div>
      </div>
    </div>
  </section>
  {cta("Faisons connaissance", "Parlons de votre jardin", "Le plus simple pour un devis : nous décrire votre terrain par téléphone, SMS ou e-mail.", "feuilles", btn="Prendre contact")}'''
page("qui-sommes-nous.html", "Qui sommes-nous | Albizzia, paysagiste à Angerville",
     "Albizzia, entreprise de paysage créée en 1996 et reprise en octobre 2020 par Dany et Ronan Nedelec, installée à Angerville (91).", qui)

# ---------------------------------------------------------------- CONTACT
contact = f'''
  <section class="ph-hero">
    <div class="wrap cols">
      <div>
        <span class="eyebrow">Contact</span>
        <h1>Parlons de votre jardin</h1>
        <p>Remplissez le formulaire : vous obtenez un message prêt à envoyer par SMS ou par e-mail. Vous pouvez aussi nous appeler.</p>
      </div>
      <div>{I("tonte_volets", lazy=False, cls="solo")}</div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap formwrap">
      <div>
        <form id="contact-form" novalidate>
          <div class="f2">
            <div><label for="nom">Nom <span class="req">*</span></label><input id="nom" name="nom" autocomplete="name" aria-describedby="err-nom"><p class="err" id="err-nom" aria-live="polite"></p></div>
            <div><label for="tel">Téléphone <span class="req">*</span></label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" aria-describedby="err-tel"><p class="err" id="err-tel" aria-live="polite"></p></div>
          </div>
          <div class="f2">
            <div><label for="email">E-mail</label><input id="email" name="email" type="email" autocomplete="email" aria-describedby="err-email"><p class="err" id="err-email" aria-live="polite"></p></div>
            <div><label for="commune">Commune du chantier <span class="req">*</span></label><input id="commune" name="commune" aria-describedby="err-commune"><p class="err" id="err-commune" aria-live="polite"></p></div>
          </div>
          <div><label for="prestation">Prestation <span class="req">*</span></label>
            <select id="prestation" name="prestation" aria-describedby="err-prestation"><option value="">Choisir…</option><option>Création et aménagement extérieur</option><option>Entretien de jardins et espaces verts</option><option>Élagage et abattage</option><option>Dessouchage</option><option>Aménagement intérieur, terrasses et balcons</option><option>Autre demande</option></select><p class="err" id="err-prestation" aria-live="polite"></p></div>
          <div><label for="message">Votre projet <span class="req">*</span></label><textarea id="message" name="message" aria-describedby="err-message"></textarea><p class="err" id="err-message" aria-live="polite"></p></div>
          <div><button class="btn" type="submit">Préparer mon message</button></div>
        </form>
        <section class="recap" id="recap" hidden aria-labelledby="recap-title" style="margin-top:24px">
          <h2 id="recap-title" tabindex="-1" style="font-size:26px">Votre message est prêt</h2>
          <pre id="recap-text"></pre>
          <div class="actions"><a class="btn" id="recap-sms" href="sms:{TEL_RAW}">Envoyer par SMS</a><button class="btn ghost" id="recap-copy" type="button">Copier</button><a class="btn ghost" href="tel:{TEL_RAW}">Appeler</a><a class="btn ghost" id="recap-mail" href="mailto:{MAIL}">Envoyer par e-mail</a></div>
          <p class="ok" style="color:var(--onDeepMuted);font-weight:400;font-size:15px">Ce site ne transmet rien automatiquement : le message part depuis votre téléphone ou votre messagerie.</p>
        </section>
      </div>
      <aside class="side">
        <dl class="coords" style="margin:0">
          <div><dt>Téléphone</dt><dd><a href="tel:{TEL_RAW}">{TEL}</a></dd></div>
          <div><dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
          <div><dt>Commune</dt><dd>Angerville (91)</dd></div>
          <div><dt>Zone d'intervention</dt><dd>Île-de-France</dd></div>
        </dl>
      </aside>
    </div>
  </section>'''
page("contact.html", "Contact et devis | Albizzia, paysagiste à Angerville",
     "Contactez Albizzia, paysagiste à Angerville (91) : formulaire de demande de devis, téléphone 06 24 36 33 76 et e-mail.", contact)

# ---------------------------------------------------------------- MENTIONS LÉGALES
legal = f'''
  <section class="sec">
    <div class="wrap legal">
      <h1 style="font-size:clamp(34px,5vw,52px)">Mentions légales</h1>
      <h2>Éditeur du site</h2>
      <dl>
        <dt>Dénomination</dt><dd>ALBIZZIA</dd>
        <dt>SIREN</dt><dd>477860787</dd>
        <dt>Commune</dt><dd>Angerville (91)</dd>
        <dt>Dirigeants (registre)</dt><dd>Dany Francois Yves Nedelec, Ronan Paul Hamon Nedelec</dd>
        <dt>Téléphone</dt><dd><a href="tel:{TEL_RAW}">{TEL}</a></dd>
        <dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
      </dl>
      <h2>À propos de ce site</h2>
      <p>Ce site est une maquette. Les images sont des visuels d'illustration. Les informations légales complémentaires (forme juridique, adresse complète, hébergeur, responsable de la publication) seront ajoutées avant la mise en ligne définitive.</p>
    </div>
  </section>'''
page("mentions-legales.html", "Mentions légales | Albizzia, Angerville",
     "Mentions légales du site d'Albizzia, paysagiste à Angerville (91) : dénomination, SIREN, contact.", legal)
print("pages générées")
