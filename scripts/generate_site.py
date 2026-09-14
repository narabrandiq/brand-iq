# -*- coding: utf-8 -*-
"""Génère le site statique Brand IQ FR + EN."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = {
    "fr": [
        ("Missions", "missions.html"),
        ("Formations", "formations.html"),
        ("Secteurs", "secteurs.html"),
        ("À propos", "a-propos.html"),
        ("Contact", "contact.html"),
    ],
    "en": [
        ("Missions", "missions.html"),
        ("Training", "formations.html"),
        ("Sectors", "secteurs.html"),
        ("About", "a-propos.html"),
        ("Contact", "contact.html"),
    ],
}

META = {
    "fr": {
        "cta": "Diagnostic express gratuit",
        "footer_tag": "Conseil et formation autour de 3 enjeux : Croissance, Innovation et IA. Missions sprint de 2 à 4 semaines. Formations sur mesure.",
        "missions": "Nos missions",
        "trainings": "Formations",
        "sectors": "Secteurs",
        "legal": "Mentions légales",
        "privacy": "Confidentialité",
        "terms": "CGV",
        "rights": "Tous droits réservés",
        "diag_href": "diagnostic.html",
        "home": "index.html",
    },
    "en": {
        "cta": "Free express diagnostic",
        "footer_tag": "Consulting and training on growth, innovation and AI. 2–4 week sprint missions. Tailor-made programs.",
        "missions": "Missions",
        "trainings": "Training",
        "sectors": "Sectors",
        "legal": "Legal notice",
        "privacy": "Privacy",
        "terms": "Terms",
        "rights": "All rights reserved",
        "diag_href": "diagnostic.html",
        "home": "index.html",
    },
}


def prefix(lang):
    return "../" if lang == "en" else ""


def lang_href(lang, page):
    if lang == "fr":
        return f"en/{page}" if page != "index.html" else "en/index.html"
    return f"../{page}"


def header(lang, page, title, description):
    m = META[lang]
    pre = prefix(lang)
    links = []
    for label, href in NAV[lang]:
        active = " active" if href == page else ""
        links.append(f'<a class="{active.strip()}" href="{href}">{label}</a>')
    fr_on = " active" if lang == "fr" else ""
    en_on = " active" if lang == "en" else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{pre}assets/img/favicon.png" type="image/png" sizes="32x32">
<link rel="icon" href="{pre}assets/img/favicon.png" type="image/png" sizes="256x256">
<link rel="apple-touch-icon" href="{pre}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/css/site.css">
</head>
<body>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="{m['home']}" aria-label="Brand IQ">
      <img src="{pre}assets/img/logo.png" alt="Brand IQ" width="136" height="32">
    </a>
    <nav class="nav-links">{''.join(links)}</nav>
    <div class="nav-right">
      <div class="lang-switch">
        <a class="{fr_on.strip()}" href="{lang_href('en', page) if lang=='en' else page}">FR</a>
        <a class="{en_on.strip()}" href="{lang_href('fr', page) if lang=='fr' else page}">EN</a>
      </div>
      <a class="btn btn-primary nav-cta" href="{m['diag_href']}">{m['cta']}</a>
      <button class="menu-toggle" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""


def footer(lang):
    m = META[lang]
    pre = prefix(lang)
    return f"""
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="logo" href="{m['home']}" aria-label="Brand IQ">
        <svg viewBox="0 0 280 72" xmlns="http://www.w3.org/2000/svg" role="img">
          <text x="0" y="62" font-family="Inter, Plus Jakarta Sans, sans-serif" font-weight="800" font-size="58" letter-spacing="-1.5" fill="#ffffff">Brand</text>
          <text x="190" y="32" font-family="Inter, Plus Jakarta Sans, sans-serif" font-weight="800" font-size="32" letter-spacing="-1.5" fill="#a5b4fc">IQ</text>
        </svg>
      </a>
      <p>{m['footer_tag']}</p>
      <p style="margin-top:16px">
        <a href="mailto:gerald.saada@brand-iq.co">gerald.saada@brand-iq.co</a><br>
        <a href="tel:+33603561455">+33 6 03 56 14 55</a><br>
        France &amp; Europe
      </p>
    </div>
    <div>
      <h4>{m['missions']}</h4>
      <ul>
        <li><a href="missions.html#growth">IQ-Growth UNLOCK</a></li>
        <li><a href="missions.html#innovation">IQ-Innovation CREATE</a></li>
        <li><a href="missions.html#ai">IQ-AI AMPLIFY</a></li>
        <li><a href="missions.html#rse">IQ-RSE SUSTAIN</a></li>
      </ul>
    </div>
    <div>
      <h4>{m['trainings']}</h4>
      <ul>
        <li><a href="formations.html">Marketing Academy</a></li>
        <li><a href="formations.html">B2C Fundamentals</a></li>
        <li><a href="formations.html">AI &amp; Marketing</a></li>
      </ul>
    </div>
    <div>
      <h4>{m['sectors']}</h4>
      <ul>
        <li><a href="secteurs.html">FMCG</a></li>
        <li><a href="secteurs.html">Beauty</a></li>
        <li><a href="secteurs.html">Health</a></li>
        <li><a href="a-propos.html">Gérald Saada</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© 2026 Brand IQ — {m['rights']}</span>
    <span>
      <a href="mentions-legales.html">{m['legal']}</a> ·
      <a href="confidentialite.html">{m['privacy']}</a> ·
      <a href="cgv.html">{m['terms']}</a>
    </span>
  </div>
</footer>
<script src="{pre}assets/js/site.js"></script>
</body>
</html>
"""


def write(lang, page, title, description, body):
    html = header(lang, page, title, description) + body + footer(lang)
    dest = ROOT / ("en" if lang == "en" else "") / page
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("wrote", dest.relative_to(ROOT))


# ---------- HOME ----------
HOME = {
    "fr": {
        "title": "Brand IQ | Conseil en stratégie marketing B2C & formation",
        "desc": "Missions de transformation de marque et formations sur mesure. Croissance, innovation et IA. Résultats en 4 semaines.",
        "h1": 'Conseil en <em>stratégie et transformation</em> de marque',
        "lede": "Missions de transformation. Formations sur mesure.",
        "pills": ["📊 Stratégie de Marque", "💡 Innovation", "🤖 AI"],
        "checks": ["Résultats en 4 semaines", "20+ ans d'expertise FMCG", "50+ marques transformées", "P&G, General Mills, Sodiaal"],
        "cta1": "Diagnostic express gratuit",
        "cta2": "Découvrir nos missions",
        "visual": "De la complexité à la <span>clarté stratégique</span>.",
        "mk": "Missions de transformation",
        "mh": "Trois leviers pour transformer votre marque",
        "ms": "Diagnostic et plan d'action livrés en 4 semaines. Accompagnement optionnel de 3 à 12 mois.",
        "missions": [
            ("📊", "", "IQ-Growth", "Méthode UNLOCK™", "Votre marque stagne ? Redéfinissez votre positionnement et relancez la croissance.",
             [("Understand", "Diagnostic 360°"), ("Navigate", "Vision business"), ("Listen", "Cibles et insights"),
              ("Own", "Positionnement"), ("Communicate", "Communication"), ("Kick into action", "Plan d'activation")]),
            ("💡", "gold", "IQ-Innovation", "Méthode CREATE™", "Pipeline vide ? Structurez votre innovation pour une croissance prévisible.",
             [("Competition", "Espaces disponibles"), ("Relevance", "Besoins non satisfaits"), ("Equity", "Capital marque"),
              ("Alignment", "Culture innovation"), ("Trajectory", "Roadmap"), ("Execution", "Test & learn")]),
            ("🤖", "green", "IQ-AI", "Méthode AMPLIFY™", "Vos équipes n'exploitent pas l'IA ? Transformez votre marketing avec l'IA.",
             [("Audit", "Maturité IA équipes"), ("Map", "Opportunités automation"), ("Prioritize", "Use cases ROI"),
              ("Learn", "Formation & agents"), ("Integrate", "Workflows"), ("Yield", "Mesure & optimisation")]),
        ],
        "fk": "Formations & workshops",
        "fh": "Développez les compétences de vos équipes",
        "fs": "Des programmes inspirés des meilleures pratiques P&G, adaptés à vos enjeux.",
        "forms": [
            ("Programme phare", "Marketing Academy", "6 mois • 12 sessions • Sur-mesure",
             "Programme complet pour transformer vos équipes marketing en experts de la croissance de marque.",
             ["Consumer Insights & Jobs-to-be-done", "Brand Building & Positionnement", "Innovation Pipeline Management",
              "Communication & Activation 360°", "Digital Marketing & Performance", "Business Case & P&L Marketing"],
             "Demander le programme →"),
            ("Tous secteurs", "Fondamentaux du Marketing B2C", "1-2 jours • Workshop intensif",
             "Maîtrisez les fondamentaux pour toucher vos clients et construire une marque puissante.",
             ["Leadership Marketing", "Consumer Insights & Segmentation", "Brand Purpose & Positionnement",
              "Communication créative", "Tunnel d'acquisition", "Activation digital & influence"],
             "Organiser un workshop →"),
            ("Innovation", "IA & Marketing Masterclass", "1 jour • Hands-on • Tous niveaux",
             "Maîtrisez les outils IA pour transformer votre productivité marketing. De ChatGPT aux agents IA.",
             ["Panorama des outils IA", "Prompt engineering avancé", "Consumer intelligence", "Contenu augmenté", "Agents IA"],
             "Réserver une session →"),
        ],
        "sk": "Expertise sectorielle",
        "sh": "Secteurs d'intervention",
        "ss": 'Une expertise approfondie des marchés B2C « produit » et de leurs enjeux spécifiques.',
        "secs": [
            ("Grande consommation", "Agroalimentaire & FMCG", "Transformation face aux défis de rentabilité et premiumisation.", ["Stratégie catégorielle", "Innovation pipeline"]),
            ("Beauté & hygiène", "Cosmétiques & Personal Care", "Transition clean beauty et expérience omnicanale.", ["Premiumisation", "D2C strategy"]),
            ("Santé & nutrition", "Pharma OTC & Nutrition", "Transformation vers des modèles B2C et patient-centric.", ["Marketing patient", "Digital health"]),
            ("Tech & digital", "Tech B2C & SaaS", "Acquisition client et stratégie de scale.", ["Brand building", "Go-to-market"]),
        ],
        "ak": "À propos",
        "ah": "L'expertise au service de votre croissance",
        "role": "Fondateur de Brand IQ",
        "bioh": "20 ans de transformation de marques",
        "bio": "Ancien CMO et directeur de BU de grandes entreprises PGC et agroalimentaires, j'ai développé une expertise unique dans la transformation de marques B2C. Mon approche : appliquer les méthodes éprouvées des multinationales avec l'agilité d'un entrepreneur.",
        "cos": ["P&G • 11 ans", "General Mills • 3 ans", "Sodiaal • 8 ans"],
        "nums": [("50+", "Marques transformées"), ("+100M€", "EBIT généré"), ("30+", "Pays couverts")],
        "quote": "« Les marques qui gagnent sont celles qui comprennent profondément leurs consommateurs et osent transformer leurs convictions en actions. Mon rôle : vous aider à faire ce saut. »",
    },
    "en": {
        "title": "Brand IQ | B2C brand strategy consulting & training",
        "desc": "Brand transformation missions and tailor-made training. Growth, innovation and AI. Results in 4 weeks.",
        "h1": 'Consulting in <em>brand strategy and transformation</em>',
        "lede": "Transformation missions. Tailor-made training programs.",
        "pills": ["📊 Brand Strategy", "💡 Innovation", "🤖 AI"],
        "checks": ["Results in 4 weeks", "20+ years of FMCG expertise", "50+ brands transformed", "P&G, General Mills, Sodiaal"],
        "cta1": "Free express diagnostic",
        "cta2": "Explore our missions",
        "visual": "From complexity to <span>strategic clarity</span>.",
        "mk": "Transformation missions",
        "mh": "Three levers to transform your brand",
        "ms": "Diagnostic and action plan delivered in 4 weeks. Optional support over 3 to 12 months.",
        "missions": [
            ("📊", "", "IQ-Growth", "UNLOCK™ method", "Growth stalled? Redefine your positioning and reignite momentum.",
             [("Understand", "360° diagnostic"), ("Navigate", "Business vision"), ("Listen", "Consumer insights"),
              ("Own", "Positioning"), ("Communicate", "Communication"), ("Kick into action", "Activation plan")]),
            ("💡", "gold", "IQ-Innovation", "CREATE™ method", "Pipeline running dry? Build a system for predictable innovation-led growth.",
             [("Competition", "White spaces"), ("Relevance", "Unmet needs"), ("Equity", "Brand equity"),
              ("Alignment", "Innovation culture"), ("Trajectory", "Roadmap"), ("Execution", "Test & learn")]),
            ("🤖", "green", "IQ-AI", "AMPLIFY™ method", "Not getting value from AI yet? Transform marketing with AI-enabled ways of working.",
             [("Audit", "Team AI maturity"), ("Map", "Automation opportunities"), ("Prioritize", "ROI use cases"),
              ("Learn", "Training & agents"), ("Integrate", "Workflows"), ("Yield", "Measurement & optimization")]),
        ],
        "fk": "Training & workshops",
        "fh": "Develop your teams' skills",
        "fs": "Programs inspired by P&G best practices, tailored to your challenges.",
        "forms": [
            ("Flagship program", "Marketing Academy", "6 months • 12 sessions • Tailored",
             "Comprehensive program to turn marketing teams into brand-growth experts, based on P&G methodologies.",
             ["Consumer Insights & Jobs-to-be-done", "Brand Building & Positioning", "Innovation Pipeline Management",
              "360° Communication & Activation", "Digital Marketing & Performance", "Business Case & Marketing P&L"],
             "Request the program →"),
            ("All industries", "B2C Marketing Fundamentals", "1–2 days • Intensive workshop",
             "Master the fundamentals to reach customers and build a powerful brand. Applies to B2C and B2B.",
             ["Marketing leadership", "Consumer insights & segmentation", "Brand purpose & positioning",
              "Creative communication", "Acquisition funnel", "Digital activation & influence"],
             "Organize a workshop →"),
            ("Innovation", "AI & Marketing Masterclass", "1 day • Hands-on • All levels",
             "Master AI tools to transform marketing productivity — from ChatGPT to custom agents.",
             ["AI marketing tools overview", "Advanced prompt engineering", "Consumer intelligence", "Augmented content", "Custom AI agents"],
             "Book a session →"),
        ],
        "sk": "Industry expertise",
        "sh": "Sectors of intervention",
        "ss": "Deep expertise in B2C product markets and their specific challenges.",
        "secs": [
            ("Consumer goods", "Food & FMCG", "Transformation facing profitability and premiumization pressure.", ["Category strategy", "Innovation pipeline"]),
            ("Beauty & care", "Cosmetics & Personal Care", "Clean beauty transition and omnichannel experience.", ["Premiumization", "D2C strategy"]),
            ("Health & nutrition", "OTC Pharma & Nutrition", "Shift towards B2C and patient-centric models.", ["Patient marketing", "Digital health"]),
            ("Tech & digital", "B2C Tech & SaaS", "Customer acquisition and scale strategy.", ["Brand building", "Go-to-market"]),
        ],
        "ak": "About",
        "ah": "Expertise at the service of your growth",
        "role": "Founder of Brand IQ",
        "bioh": "20 years of brand transformation",
        "bio": "Former CMO and BU director at major CPG and food companies, I developed unique expertise in B2C brand transformation. My approach: apply proven multinational methods with entrepreneurial agility.",
        "cos": ["P&G • 11 years", "General Mills • 3 years", "Sodiaal • 8 years"],
        "nums": [("50+", "Brands transformed"), ("+€100M", "EBIT generated"), ("30+", "Countries covered")],
        "quote": "“Winning brands are those that deeply understand their consumers and dare to turn convictions into action. My role: helping you make that leap.”",
    },
}


def home_body(lang):
    t = HOME[lang]
    pre = prefix(lang)
    cards = []
    for icon, klass, title, method, desc, pts in t["missions"]:
        lis = "".join(f"<li><strong>{a}</strong> {b}</li>" for a, b in pts)
        cards.append(f'<article class="card {klass}"><div class="icon">{icon}</div><h3>{title}</h3><p class="method">{method}</p><p>{desc}</p><ul class="points">{lis}</ul></article>')
    forms = []
    for tag, title, meta, desc, mods, cta in t["forms"]:
        lis = "".join(f"<li>— {m}</li>" for m in mods)
        forms.append(f'<article class="card"><span class="tag">{tag}</span><h3>{title}</h3><p class="meta">{meta}</p><p>{desc}</p><ul class="points">{lis}</ul><a href="contact.html">{cta}</a></article>')
    secs = []
    for badge, title, desc, tags in t["secs"]:
        chips = "".join(f'<span class="chip">{x}</span>' for x in tags)
        secs.append(f'<article class="sector"><span class="tag">{badge}</span><h3>{title}</h3><p>{desc}</p><div class="chips">{chips}</div></article>')
    nums = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in t["nums"])
    cos = "".join(f'<span class="about-company" style="margin-right:12px;font-weight:700">{c}</span>' for c in t["cos"])
    checks = "".join(f'<div class="check"><i>✓</i><span>{c}</span></div>' for c in t["checks"])
    pills = "".join(f'<div class="pill">{p}</div>' for p in t["pills"])
    return f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <h1>{t['h1']}</h1>
      <p class="lede">{t['lede']}</p>
      <div class="pills">{pills}</div>
      <div class="checks">{checks}</div>
      <div class="hero-actions">
        <a class="btn btn-primary btn-lg" href="diagnostic.html">{t['cta1']} →</a>
        <a class="btn btn-secondary btn-lg" href="missions.html">{t['cta2']}</a>
      </div>
    </div>
    <div class="hero-visual">
      <img src="{pre}assets/img/hero-visual.png" alt="De la complexité à la clarté stratégique">
    </div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head"><div class="section-kicker">{t['mk']}</div><h2>{t['mh']}</h2><p class="muted">{t['ms']}</p></div>
    <div class="grid-3">{''.join(cards)}</div>
  </div>
</section>
<section class="bg-light">
  <div class="container">
    <div class="section-head"><div class="section-kicker">{t['fk']}</div><h2>{t['fh']}</h2><p class="muted">{t['fs']}</p></div>
    <div class="grid-3">{''.join(forms)}</div>
  </div>
</section>
<section>
  <div class="container">
    <div class="section-head"><div class="section-kicker">{t['sk']}</div><h2>{t['sh']}</h2><p class="muted">{t['ss']}</p></div>
    <div class="grid-4">{''.join(secs)}</div>
  </div>
</section>
<section class="bg-soft">
  <div class="container">
    <div class="section-head"><div class="section-kicker">{t['ak']}</div><h2>{t['ah']}</h2></div>
    <div class="about-wrap">
      <div class="portrait">
        <img src="{pre}assets/img/gerald-saada.jpg" alt="Gérald Saada">
        <h3>Gérald Saada</h3>
        <p class="muted">{t['role']}</p>
      </div>
      <div>
        <h3>{t['bioh']}</h3>
        <p class="muted" style="margin:12px 0 16px">{t['bio']}</p>
        <p>{cos}</p>
        <div class="stats">{nums}</div>
        <p class="quote">{t['quote']}</p>
      </div>
    </div>
  </div>
</section>
"""


# ---------- MISSIONS ----------
def missions_body(lang):
    if lang == "fr":
        hero_t, hero_s = "Missions de transformation", "Quatre méthodes propriétaires. Diagnostic et plan d'action en 2 à 4 semaines."
        tabs = [
            ("growth", "IQ - Croissance", "🚀 Mission IQ-Growth • Méthode UNLOCK™", "Relancez la croissance de votre marque",
             "Votre marque stagne ou perd des parts de marché ? UNLOCK™ vous donne les clés pour retrouver croissance et rentabilité en 4 semaines.",
             "IQ-Growth", "Diagnostic stratégique et plan d'action pour relancer votre croissance.",
             "Votre marque fait-elle face à ces défis ?",
             [("Stagnation ou déclin", "Les initiatives marketing ne génèrent plus de croissance."),
              ("Manque de différenciation", "Impossible de justifier un premium. Les consommateurs ne voient plus la différence."),
              ("Portfolio complexe", "Trop de références, cannibalisation, rentabilité en berne."),
              ("Équipes désalignées", "Pas de vision commune, silos, exécution freinée.")],
             "L'entonnoir stratégique UNLOCK™",
             [("U Understand", "Diagnostic 360° marché, concurrence, consommateur, business."),
              ("N Navigate", "Where to play : usages, catégories, canaux."),
              ("L Listen", "Cible primaire et insight fondateur."),
              ("O Own", "Promesse, architecture, offre."),
              ("C Communicate", "Messages, expérience, média."),
              ("K Kick into action", "Innovation, prix, activation, organisation.")]),
            ("innovation", "IQ - Innovation", "💡 Mission IQ-Innovation • Méthode CREATE™", "Structurez l'innovation pour une croissance durable",
             "Idées dispersées, ROI incertain ? CREATE™ transforme vos initiatives en pipeline systématique et rentable en 2 à 4 semaines.",
             "IQ-Innovation", "Pipeline innovation prévisible, du white space au test & learn.",
             "Votre innovation fait-elle face à ces défis ?",
             [("Pipeline vide ou chaotique", "Pas de visibilité, trop de projets, aucun big bet."),
              ("Taux de succès faible", "Lancements qui ne performent pas, time-to-market trop long."),
              ("Innovation déconnectée", "Idées loin de l'équité de marque et des besoins non satisfaits."),
              ("Culture trop prudente", "Peu de test & learn, peur de l'échec, silos R&D / marketing.")],
             "6 piliers CREATE™",
             [("C Competition", "Espaces disponibles et white spaces."),
              ("R Relevance", "Besoins non satisfaits et jobs-to-be-done."),
              ("E Equity", "Capital de marque à activer."),
              ("A Alignment", "Culture et gouvernance innovation."),
              ("T Trajectory", "Roadmap 70-20-10 et big bets."),
              ("E Execution", "Stage-gate, test & learn, go-to-market.")]),
            ("ai", "IQ - IA", "🤖 Mission IQ-AI • Méthode AMPLIFY™", "Amplifiez votre marketing avec l'intelligence artificielle",
             "L'IA reste un buzzword ? AMPLIFY™ transforme vos équipes : audit, use cases ROI, formation, agents et mesure.",
             "IQ-AI", "De la maturité IA à l'intégration dans les workflows marketing.",
             "Ce que l'IA peut faire pour votre marketing",
             [("Contenu x10", "Posts, emails, scripts, copy : produisez en une heure ce qui prenait une semaine."),
              ("Insights en minutes", "Avis, posts sociaux, verbatims analysés instantanément."),
              ("Agents 24/7", "Veille, reporting, briefs : vos agents travaillent pendant que vous stratégisez."),
              ("+ROI campagnes", "Plus de variantes, optimisation temps réel, personnalisation à l'échelle.")],
             "7 piliers AMPLIFY™",
             [("A Audit", "Maturité IA et benchmark."),
              ("M Map", "Use cases à fort ROI."),
              ("P Prompt", "Maîtrise du prompting métier."),
              ("L Learn", "Formation équipes et champions."),
              ("I Integrate", "Workflows, stack, agents."),
              ("F Fine-tune", "Ton de marque et knowledge base."),
              ("Y Yield", "Dashboard ROI et qualité.")]),
            ("rse", "IQ - RSE", "🌱 Mission IQ-RSE • Méthode SUSTAIN™", "Faire de la RSE un avantage concurrentiel",
             "Valeurs fortes mais greenwashing perçu, engagement faible, ROI non démontré ? SUSTAIN™ aligne RSE et business en 2 à 4 semaines.",
             "IQ-RSE", "Alignez RSE et stratégie business pour un avantage durable.",
             "Votre RSE fait-elle face à ces défis ?",
             [("RSE déconnectée", "Initiatives isolées, vues comme un coût."),
              ("Suspicion de greenwashing", "Écart entre communication et actions réelles."),
              ("Engagement interne faible", "Collaborateurs peu mobilisés."),
              ("ROI non démontré", "Impact business difficile à mesurer.")],
             "7 piliers SUSTAIN™",
             [("S Scope", "Diagnostic cohérence RSE / marque."),
              ("U Understanding", "Attentes sociétales et willingness to pay."),
              ("S Story", "Récit authentique, preuves tangibles."),
              ("T Trust", "Mobilisation interne et ambassadeurs."),
              ("A Ambition", "Objectifs business et sociétaux."),
              ("I Integration", "RSE dans l'offre et l'éco-conception."),
              ("N Navigation", "Pilotage, dashboard, labels.")]),
        ]
        cta_h, cta_p, cta_b = "Prêt à transformer votre marque ?", "Diagnostic express gratuit, puis un échange de 30 minutes.", "Réserver mon diagnostic"
    else:
        hero_t, hero_s = "Transformation missions", "Four proprietary methods. Diagnostic and action plan in 2–4 weeks."
        tabs = [
            ("growth", "IQ - Growth", "🚀 IQ-Growth mission • UNLOCK™ method", "Reignite your brand's growth",
             "Stalling or losing share? UNLOCK™ gives you the keys to restore growth and profitability in 4 weeks.",
             "IQ-Growth", "Strategic diagnostic and action plan to restart growth.",
             "Is your brand facing these challenges?",
             [("Stagnation or decline", "Marketing initiatives no longer create growth."),
              ("No differentiation", "You cannot defend a premium. Consumers see no difference."),
              ("Complex portfolio", "Too many SKUs, cannibalization, weak profitability."),
              ("Misaligned teams", "No shared vision, silos, slow execution.")],
             "The UNLOCK™ strategic funnel",
             [("U Understand", "360° diagnostic: market, competition, consumer, business."),
              ("N Navigate", "Where to play: occasions, categories, channels."),
              ("L Listen", "Primary target and founding insight."),
              ("O Own", "Promise, architecture, offer."),
              ("C Communicate", "Messages, experience, media."),
              ("K Kick into action", "Innovation, pricing, activation, organization.")]),
            ("innovation", "IQ - Innovation", "💡 IQ-Innovation mission • CREATE™ method", "Structure innovation for durable growth",
             "Scattered ideas, uncertain ROI? CREATE™ turns initiatives into a systematic, profitable pipeline in 2–4 weeks.",
             "IQ-Innovation", "A predictable innovation pipeline, from white space to test & learn.",
             "Is your innovation facing these challenges?",
             [("Empty or chaotic pipeline", "No visibility, too many projects, no big bet."),
              ("Low success rate", "Launches underperform, time-to-market is too long."),
              ("Disconnected innovation", "Ideas far from brand equity and unmet needs."),
              ("Over-cautious culture", "Little test & learn, fear of failure, R&D / marketing silos.")],
             "6 CREATE™ pillars",
             [("C Competition", "Available spaces and white spaces."),
              ("R Relevance", "Unmet needs and jobs-to-be-done."),
              ("E Equity", "Brand equity to activate."),
              ("A Alignment", "Innovation culture and governance."),
              ("T Trajectory", "70-20-10 roadmap and big bets."),
              ("E Execution", "Stage-gate, test & learn, go-to-market.")]),
            ("ai", "IQ - AI", "🤖 IQ-AI mission • AMPLIFY™ method", "Amplify your marketing with artificial intelligence",
             "AI still a buzzword? AMPLIFY™ takes teams from audit to ROI use cases, training, agents and measurement.",
             "IQ-AI", "From AI maturity to integration in marketing workflows.",
             "What AI can do for your marketing",
             [("Content x10", "Posts, emails, scripts, copy: produce in an hour what used to take a week."),
              ("Insights in minutes", "Reviews, social posts and verbatims analyzed instantly."),
              ("24/7 agents", "Watch, reporting, briefs: agents work while you strategize."),
              ("Campaign ROI", "More variants, real-time optimization, personalization at scale.")],
             "7 AMPLIFY™ pillars",
             [("A Audit", "AI maturity and benchmark."),
              ("M Map", "High-ROI use cases."),
              ("P Prompt", "Business prompt mastery."),
              ("L Learn", "Team training and champions."),
              ("I Integrate", "Workflows, stack, agents."),
              ("F Fine-tune", "Brand voice and knowledge base."),
              ("Y Yield", "ROI dashboard and quality.")]),
            ("rse", "IQ - CSR", "🌱 IQ-CSR mission • SUSTAIN™ method", "Turn CSR into a competitive advantage",
             "Strong values but perceived greenwashing, low engagement, unproven ROI? SUSTAIN™ aligns CSR and business in 2–4 weeks.",
             "IQ-CSR", "Align CSR and business strategy for a durable advantage.",
             "Is your CSR facing these challenges?",
             [("Disconnected CSR", "Isolated initiatives, seen as a cost."),
              ("Greenwashing suspicion", "Gap between communication and real action."),
              ("Low internal engagement", "Employees are not mobilized."),
              ("Unproven ROI", "Business impact is hard to measure.")],
             "7 SUSTAIN™ pillars",
             [("S Scope", "CSR / brand coherence diagnostic."),
              ("U Understanding", "Societal expectations and willingness to pay."),
              ("S Story", "Authentic narrative and tangible proof."),
              ("T Trust", "Internal mobilization and ambassadors."),
              ("A Ambition", "Business and societal goals."),
              ("I Integration", "CSR in the offer and eco-design."),
              ("N Navigation", "Steering, dashboard, labels.")]),
        ]
        cta_h, cta_p, cta_b = "Ready to transform your brand?", "Free express diagnostic, then a 30-minute conversation.", "Book my diagnostic"

    tab_btns = "".join(f'<button class="tab{" active" if i==0 else ""}" data-tab="{tid}">{label}</button>' for i, (tid, label, *_) in enumerate(tabs))
    panels = []
    for i, (tid, _label, badge, h2, lead, card_t, card_d, ch, challenges, meth, pillars) in enumerate(tabs):
        chs = "".join(f'<article class="card"><h3>{a}</h3><p>{b}</p></article>' for a, b in challenges)
        pls = "".join(f'<div class="mini"><strong>{a}</strong><span>{b}</span></div>' for a, b in pillars)
        panels.append(f"""
        <div class="mission-panel{" active" if i==0 else ""}" id="{tid}">
          <div class="mission-hero">
            <div>
              <div class="badge">{badge}</div>
              <h2>{h2}</h2>
              <p>{lead}</p>
              <div class="hero-actions" style="margin-top:22px">
                <a class="btn btn-green" href="diagnostic.html">{cta_b} →</a>
                <a class="btn btn-secondary" href="contact.html">Contact</a>
              </div>
            </div>
            <div class="float-card">
              <h3>{card_t}</h3>
              <p class="method">{badge.split("•")[-1].strip()}</p>
              <p>{card_d}</p>
            </div>
          </div>
          <div style="margin-top:48px">
            <div class="section-head"><h2>{ch}</h2></div>
            <div class="grid-2">{chs}</div>
          </div>
          <div style="margin-top:48px">
            <div class="section-head"><h2>{meth}</h2></div>
            <div class="mini-grid">{pls}</div>
          </div>
        </div>""")
    return f"""
<section class="page-hero"><div class="container"><div class="badge">Brand IQ</div><h1>{hero_t}</h1><p>{hero_s}</p></div></section>
<section data-tabs>
  <div class="container">
    <div class="tabs">{tab_btns}</div>
    {''.join(panels)}
    <div class="cta-band" style="margin-top:56px">
      <h2>{cta_h}</h2>
      <p>{cta_p}</p>
      <a class="btn btn-primary" href="diagnostic.html">{cta_b}</a>
    </div>
  </div>
</section>
"""


# ---------- FORMATIONS ----------
def formations_body(lang):
    if lang == "fr":
        h1, sub = "Formations Marketing B2C", "Les méthodes des plus grands groupes FMCG adaptées à vos équipes. Programmes sur-mesure, formats flexibles."
        formats = [
            ("Conférences & keynotes", "45 min – 2h", "Interventions inspirantes sur les disruptions 2025 : IA, retail media, nouveaux comportements."),
            ("Workshops intensifs", "1/2 journée – 2 jours", "Sessions pratiques sur vos cas réels, avec livrables concrets."),
            ("Marketing Academy", "Programme modulaire", "Parcours complet combinant plusieurs formations selon vos priorités."),
        ]
        catalog = [
            ("Fondamentaux", "Marketing B2C moderne", "Les bases ont radicalement changé en 5 ans. Consumer-centricity, architecture de marque, P&L et équilibre brand / performance.", "1,5–2 jours"),
            ("Consumer", "Consumer insights actionnables", "De la donnée à l'insight qui transforme : truth, tension, motivation, JTBD, brand funnel, IA.", "1,5 jour"),
            ("Innovation", "Innovation & pipeline management", "De l'innovation sporadique au moteur systématique. Méthode CREATE™, règle 70-20-10, stage-gate.", "2 jours"),
            ("Transformation", "Repositionnement & brand turnaround", "Méthode UNLOCK™ pour diagnostiquer, repositionner et relancer une marque qui stagne.", "2 jours"),
            ("Disruption", "IA générative & marketing", "70% hands-on. ChatGPT, Claude, Midjourney : contenu, insights, personnalisation.", "1,5–2 jours"),
            ("Disruption", "Transformation agentique", "Au-delà du prompting : agents IA, custom GPTs, Make / Zapier, cas réel.", "1,5–2 jours"),
            ("Impact", "RSE créatrice de valeur", "Méthode SUSTAIN™ : au-delà du greenwashing, récit authentique, ambassadeurs, ROI.", "1,5 jour"),
            ("Activation", "Activation 360° & retail media", "Path to purchase, retail media, pricing, MMM et incrementality.", "1,5–2 jours"),
        ]
        cta = "Prêt à transformer vos équipes ?"
        note = "Éligible OPCO • Intra-entreprise ou distanciel • Suivi post-formation inclus"
    else:
        h1, sub = "B2C Marketing Training", "FMCG-leader methods adapted to your teams. Tailor-made programs, flexible formats."
        formats = [
            ("Talks & keynotes", "45 min – 2h", "Inspiring sessions on 2025 disruptions: AI, retail media, new consumer behaviours."),
            ("Intensive workshops", "Half day – 2 days", "Hands-on sessions on your real cases, with concrete deliverables."),
            ("Marketing Academy", "Modular program", "A complete path combining several courses according to your priorities."),
        ]
        catalog = [
            ("Fundamentals", "Modern B2C marketing", "The basics have changed in 5 years. Consumer-centricity, brand architecture, P&L and brand / performance balance.", "1.5–2 days"),
            ("Consumer", "Actionable consumer insights", "From data to the insight that transforms: truth, tension, motivation, JTBD, brand funnel, AI.", "1.5 days"),
            ("Innovation", "Innovation & pipeline management", "From sporadic innovation to a systematic engine. CREATE™, 70-20-10, stage-gate.", "2 days"),
            ("Transformation", "Repositioning & brand turnaround", "UNLOCK™ to diagnose, reposition and restart a stalling brand.", "2 days"),
            ("Disruption", "Generative AI & marketing", "70% hands-on. ChatGPT, Claude, Midjourney: content, insights, personalization.", "1.5–2 days"),
            ("Disruption", "Agentic transformation", "Beyond prompting: AI agents, custom GPTs, Make / Zapier, live case.", "1.5–2 days"),
            ("Impact", "Value-creating CSR", "SUSTAIN™: beyond greenwashing — authentic story, ambassadors, ROI.", "1.5 days"),
            ("Activation", "360° activation & retail media", "Path to purchase, retail media, pricing, MMM and incrementality.", "1.5–2 days"),
        ]
        cta = "Ready to transform your teams?"
        note = "OPCO-eligible in France • On-site or remote • Post-training follow-up included"

    fm = "".join(f'<article class="card"><span class="tag">{a}</span><h3>{b}</h3><p class="meta">{c}</p></article>' for a, b, c in formats)
    cat = "".join(f'<article class="card"><span class="tag">{a}</span><h3>{b}</h3><p>{c}</p><p class="meta">{d}</p></article>' for a, b, c, d in catalog)
    return f"""
<section class="page-hero"><div class="container"><div class="badge">Brand IQ Academy</div><h1>{h1}</h1><p>{sub}</p></div></section>
<section><div class="container"><div class="grid-3">{fm}</div></div></section>
<section class="bg-light"><div class="container"><div class="section-head"><h2>{"Catalogue de formations" if lang=="fr" else "Training catalogue"}</h2></div><div class="grid-2">{cat}</div></div></section>
<section><div class="container"><div class="cta-band"><h2>{cta}</h2><p>{note}</p><a class="btn btn-primary" href="contact.html">{"Discuter de mon projet" if lang=="fr" else "Discuss my project"}</a></div></div></section>
"""


# ---------- SECTEURS ----------
def secteurs_body(lang):
    if lang == "fr":
        h1, sub = 'Le <em>B2C</em>, notre terrain d\'excellence', "Des méthodes éprouvées pour transformer votre marque face aux défis de croissance, d'innovation et d'adoption de l'IA."
        items = [
            ("Grande consommation", "Agroalimentaire & FMCG", "Pression des marges, MDD, fragmentation des attentes, premiumisation. Brand IQ transforme ces contraintes en croissance profitable.",
             ["IQ-Croissance — rénovation & premiumisation", "IQ-Innovation — pipeline rentable", "IQ-RSE — filières valorisées", "IQ-AI — marketing augmenté"]),
            ("Santé & wellness", "Santé, nutrition & wellness", "Du B2B médical au B2C désirable, sans perdre la crédibilité scientifique ni la conformité.",
             ["Stratégie B2C santé", "Digital health & prévention", "Clean label & naturalité", "Patient engagement"]),
            ("Beauté", "Cosmétiques & personal care", "Clean beauty, inclusivité, personnalisation, influence : conjuguer authenticité, preuve et distribution complexe.",
             ["Premiumisation & DTC", "Personnalisation & tech", "Clean & recharges", "Influence & contenu IA"]),
            ("Scale-up", "Startups & scale-ups B2C", "Product-market fit validé, scale qui patine ? Brand-led growth pour passer de 1 à 10 M€.",
             ["Brand sprint 3 jours", "Product-market-brand fit", "Scale-up accelerator", "Growth stack IA"]),
        ]
    else:
        h1, sub = "B2C is our <em>home turf</em>", "Proven methods to transform your brand around growth, innovation and AI adoption."
        items = [
            ("Consumer goods", "Food & FMCG", "Margin pressure, private label, fragmented expectations, premiumization. Brand IQ turns these constraints into profitable growth.",
             ["IQ-Growth — renovation & premiumization", "IQ-Innovation — profitable pipeline", "IQ-CSR — valued supply chains", "IQ-AI — augmented marketing"]),
            ("Health & wellness", "Health, nutrition & wellness", "From medical B2B to desirable B2C, without losing scientific credibility or compliance.",
             ["B2C health strategy", "Digital health & prevention", "Clean label & naturalness", "Patient engagement"]),
            ("Beauty", "Cosmetics & personal care", "Clean beauty, inclusivity, personalization, influence: authenticity, proof and complex distribution.",
             ["Premiumization & DTC", "Personalization & tech", "Clean & refills", "Influence & AI content"]),
            ("Scale-up", "B2C startups & scale-ups", "Product-market fit validated, scale stalling? Brand-led growth from €1m to €10m.",
             ["3-day brand sprint", "Product-market-brand fit", "Scale-up accelerator", "AI growth stack"]),
        ]
    cards = []
    for badge, title, desc, pts in items:
        lis = "".join(f"<li>{p}</li>" for p in pts)
        cards.append(f'<article class="card"><span class="tag">{badge}</span><h3>{title}</h3><p>{desc}</p><ul class="points">{lis}</ul></article>')
    return f"""
<section class="page-hero"><div class="container"><div class="badge">{"Expertise sectorielle" if lang=="fr" else "Industry expertise"}</div><h1>{h1}</h1><p>{sub}</p></div></section>
<section><div class="container"><div class="grid-2">{''.join(cards)}</div></div></section>
"""


# ---------- ABOUT ----------
def about_body(lang):
    pre = prefix(lang)
    if lang == "fr":
        h1, sub = "L'expertise au service de votre transformation", "20+ ans en direction marketing et direction générale chez P&G, General Mills et Sodiaal."
        bio = """<p>Expert en <strong>stratégie, transformation de marques et IA appliquée au marketing</strong>, j'ai consacré plus de 20 ans à développer et transformer des marques emblématiques dans les plus grands groupes FMCG mondiaux.</p>
        <p>J'ai dirigé des repositionnements majeurs, des lancements disruptifs et des stratégies RSE créatrices de valeur pour Gillette, Yoplait, Candia et Entremont.</p>
        <p>Avec Brand IQ, je combine cette expertise terrain et les avancées en IA générative pour aider les entreprises à devenir des <strong>leaders connectés à leurs consommateurs</strong>.</p>"""
        values = [("Impact", "Créer des résultats tangibles et mesurables"), ("Innovation", "Challenger le status quo avec l'IA"),
                  ("Collaboration", "Co-construire avec vos équipes"), ("Durabilité", "Intégrer la RSE au cœur du business")]
        exp = [("2025 – présent", "Fondateur & CEO", "Brand IQ — Conseil & formation en stratégie de marques et IA"),
               ("2017 – 2025", "Directeur Croissance, Marketing, R&D, RSE", "Groupe Sodiaal (Candia, Entremont, AOP) — 2,5 Md€, 150 pers."),
               ("2015 – 2017", "Global Marketing Director", "Yoplait / General Mills — 3,5 Md$, 50 pays"),
               ("2003 – 2015", "Marketing Leadership", "P&G (Gillette, Head & Shoulders, Always) — 11 ans")]
        edu = [("ESSEC Business School", "Mastère Spécialisé Marketing"), ("Imperial College London", "MSc Food Industry Management"),
               ("INP – ENSAT", "Ingénieur agronome"), ("MIT Professional Education", "Certification AI & Machine Learning (2025)")]
        skills = [("Consumer insights", "Insights gagnants avec les méthodes P&G et l'IA"),
                  ("Brand building", "Plateformes de marque actionnables"),
                  ("Innovation pipeline", "Croissance durable et prévisible"),
                  ("IA & marketing", "IA générative et agents pour la productivité"),
                  ("RSE & impact", "La RSE comme avantage, pas comme contrainte"),
                  ("P&L excellence", "Portfolio, pricing, rentabilité")]
    else:
        h1, sub = "Expertise at the service of your transformation", "20+ years in marketing and general management at P&G, General Mills and Sodiaal."
        bio = """<p>Expert in <strong>strategy, brand transformation and AI applied to marketing</strong>, I spent 20+ years building and transforming iconic brands in global FMCG groups.</p>
        <p>I led major repositionings, disruptive launches and value-creating sustainability strategies for Gillette, Yoplait, Candia and Entremont.</p>
        <p>With Brand IQ, I combine that operating experience with generative AI to help companies become <strong>leaders connected to their consumers</strong>.</p>"""
        values = [("Impact", "Create tangible, measurable results"), ("Innovation", "Challenge the status quo with AI"),
                  ("Collaboration", "Co-build with your teams"), ("Sustainability", "Put CSR at the core of the business")]
        exp = [("2025 – present", "Founder & CEO", "Brand IQ — Brand strategy consulting & training"),
               ("2017 – 2025", "Growth, Marketing, R&D, CSR Director", "Sodiaal Group (Candia, Entremont, PDO) — €2.5bn, 150 people"),
               ("2015 – 2017", "Global Marketing Director", "Yoplait / General Mills — $3.5bn, 50 countries"),
               ("2003 – 2015", "Marketing Leadership", "P&G (Gillette, Head & Shoulders, Always) — 11 years")]
        edu = [("ESSEC Business School", "Specialized Master's in Marketing"), ("Imperial College London", "MSc Food Industry Management"),
               ("INP – ENSAT", "Agricultural engineer"), ("MIT Professional Education", "AI & Machine Learning certificate (2025)")]
        skills = [("Consumer insights", "Winning insights with P&G methods and AI"),
                  ("Brand building", "Actionable brand platforms"),
                  ("Innovation pipeline", "Durable, predictable growth"),
                  ("AI & marketing", "Generative AI and agents for productivity"),
                  ("CSR & impact", "CSR as an advantage, not a constraint"),
                  ("P&L excellence", "Portfolio, pricing, profitability")]
    val = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in values)
    ex = "".join(f'<div class="experience-item" style="margin-bottom:16px"><div class="tag">{a}</div><h3>{b}</h3><p class="muted">{c}</p></div>' for a, b, c in exp)
    ed = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in edu)
    sk = "".join(f'<article class="card"><h3>{a}</h3><p>{b}</p></article>' for a, b in skills)
    return f"""
<section class="page-hero">
  <div class="container" style="display:grid;grid-template-columns:1.2fr .8fr;gap:32px;align-items:center">
    <div><div class="badge">{"À propos" if lang=="fr" else "About"}</div><h1>{h1}</h1><p>{sub}</p></div>
    <div class="portrait" style="background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.12);color:#fff">
      <img src="{pre}assets/img/gerald-saada.jpg" alt="Gérald Saada">
      <h3 style="color:#fff">Gérald Saada</h3>
      <p>{"Fondateur de Brand IQ" if lang=="fr" else "Founder of Brand IQ"}</p>
    </div>
  </div>
</section>
<section class="bg-light"><div class="container grid-2"><div class="card">{bio}</div><div class="grid-2">{val}</div></div></section>
<section><div class="container grid-2"><div><h2>{"Expérience" if lang=="fr" else "Experience"}</h2>{ex}</div><div><h2>{"Formation" if lang=="fr" else "Education"}</h2><div class="grid-2">{ed}</div></div></div></section>
<section class="bg-soft"><div class="container"><div class="section-head"><h2>{"Compétences" if lang=="fr" else "Capabilities"}</h2></div><div class="grid-3">{sk}</div></div></section>
"""


# ---------- CONTACT / DIAG / LEGAL ----------
def contact_body(lang):
    thanks = "merci.html"
    if lang == "fr":
        return f"""
<section class="page-hero"><div class="container"><div class="badge">Contact</div><h1>Parlons de votre marque</h1><p>Réponse sous 24h. France & Europe.</p></div></section>
<section class="bg-light"><div class="container" style="display:grid;grid-template-columns:340px 1fr;gap:28px">
  <div>
    <div class="card"><h3>Contact direct</h3><p><a href="tel:+33603561455">+33 6 03 56 14 55</a><br><a href="mailto:gerald.saada@brand-iq.co">gerald.saada@brand-iq.co</a></p></div>
    <div class="card" style="margin-top:16px"><h3>LinkedIn</h3><p><a href="https://www.linkedin.com/in/gerald-saada/" target="_blank" rel="noopener">Profil Gérald Saada</a><br><a href="https://www.linkedin.com/company/brand-iq-co/" target="_blank" rel="noopener">Page Brand IQ</a></p></div>
    <div class="card" style="margin-top:16px"><h3>Disponibilité</h3><p>Lundi – vendredi, 9h – 18h. Réponse garantie sous 24h.</p></div>
  </div>
  <div class="card">
    <h2>Envoyez-nous un message</h2>
    <p class="muted" style="margin-bottom:16px">Réponse sous 24h à gerald.saada@brand-iq.co. Au premier envoi, confirmez l’email FormSubmit.</p>
    <form action="https://formsubmit.co/gerald.saada@brand-iq.co" method="POST">
      <input type="hidden" name="_next" value="https://www.brand-iq.co/{thanks}">
      <input type="hidden" name="_subject" value="Nouveau message — brand-iq.co">
      <input type="hidden" name="_captcha" value="false">
      <div class="form-row"><div><label>Prénom *</label><input name="firstname" required></div><div><label>Nom *</label><input name="lastname" required></div></div>
      <div><label>Entreprise *</label><input name="company" required></div>
      <div class="form-row"><div><label>Email *</label><input type="email" name="email" required></div><div><label>Téléphone</label><input name="phone"></div></div>
      <div><label>Objet *</label>
        <select name="subject" required>
          <option value="">Sélectionnez</option>
          <option>Mission IQ-Croissance</option><option>Mission IQ-Innovation</option>
          <option>Mission IQ-AI</option><option>Mission IQ-RSE</option>
          <option>Formation & Workshops</option><option>Diagnostic express</option><option>Autre</option>
        </select>
      </div>
      <div><label>Message *</label><textarea name="message" required></textarea></div>
      <button class="btn btn-primary" type="submit">Envoyer le message</button>
    </form>
  </div>
</div></section>
"""
    return f"""
<section class="page-hero"><div class="container"><div class="badge">Contact</div><h1>Let's talk about your brand</h1><p>Reply within 24 hours. France & Europe.</p></div></section>
<section class="bg-light"><div class="container" style="display:grid;grid-template-columns:340px 1fr;gap:28px">
  <div>
    <div class="card"><h3>Direct contact</h3><p><a href="tel:+33603561455">+33 6 03 56 14 55</a><br><a href="mailto:gerald.saada@brand-iq.co">gerald.saada@brand-iq.co</a></p></div>
    <div class="card" style="margin-top:16px"><h3>LinkedIn</h3><p><a href="https://www.linkedin.com/in/gerald-saada/" target="_blank" rel="noopener">Gérald Saada</a><br><a href="https://www.linkedin.com/company/brand-iq-co/" target="_blank" rel="noopener">Brand IQ page</a></p></div>
    <div class="card" style="margin-top:16px"><h3>Availability</h3><p>Monday – Friday, 9am – 6pm CET. Reply within 24 hours.</p></div>
  </div>
  <div class="card">
    <h2>Send a message</h2>
    <form action="https://formsubmit.co/gerald.saada@brand-iq.co" method="POST">
      <input type="hidden" name="_next" value="https://www.brand-iq.co/en/{thanks}">
      <input type="hidden" name="_subject" value="New message — brand-iq.co">
      <input type="hidden" name="_captcha" value="false">
      <div class="form-row"><div><label>First name *</label><input name="firstname" required></div><div><label>Last name *</label><input name="lastname" required></div></div>
      <div><label>Company *</label><input name="company" required></div>
      <div class="form-row"><div><label>Email *</label><input type="email" name="email" required></div><div><label>Phone</label><input name="phone"></div></div>
      <div><label>Topic *</label>
        <select name="subject" required>
          <option value="">Select</option>
          <option>IQ-Growth mission</option><option>IQ-Innovation mission</option>
          <option>IQ-AI mission</option><option>IQ-CSR mission</option>
          <option>Training & workshops</option><option>Express diagnostic</option><option>Other</option>
        </select>
      </div>
      <div><label>Message *</label><textarea name="message" required></textarea></div>
      <button class="btn btn-primary" type="submit">Send message</button>
    </form>
  </div>
</div></section>
"""


def diagnostic_body(lang):
    extra = f'<script src="{prefix(lang)}assets/js/diagnostic.js"></script>'
    if lang == "fr":
        body = """
<section class="page-hero"><div class="container"><h1>Diagnostic express Brand IQ</h1><p>16 questions, 4 minutes. Identifiez votre mission prioritaire : Croissance, Innovation, RSE ou IA.</p></div></section>
<div class="diag-progress"><div class="container"><div class="bar"><span id="progressFill"></span></div><p class="muted" id="progressText" style="text-align:center;margin-top:8px"></p></div></div>
<div class="container">
  <div class="intro-card" id="introScreen">
    <h2>Quelle transformation pour votre marque ?</h2>
    <p class="muted" style="margin:12px 0 24px">Ce diagnostic évalue votre situation sur les 4 axes Brand IQ et identifie votre priorité stratégique.</p>
    <div class="grid-2" style="margin-bottom:24px">
      <div class="card"><h3>IQ-Croissance</h3><p>Relancer la dynamique de votre marque</p></div>
      <div class="card"><h3>IQ-Innovation</h3><p>Structurer votre pipeline innovation</p></div>
      <div class="card"><h3>IQ-RSE</h3><p>Transformer la RSE en avantage</p></div>
      <div class="card"><h3>IQ-AI</h3><p>Intégrer l'IA dans votre marketing</p></div>
    </div>
    <button class="btn btn-primary" id="startBtn">Commencer le diagnostic</button>
  </div>
  <div id="questionsContainer"></div>
  <div id="resultContainer"></div>
</div>
"""
    else:
        body = """
<section class="page-hero"><div class="container"><h1>Brand IQ express diagnostic</h1><p>16 questions, 4 minutes. Identify your priority mission: Growth, Innovation, CSR or AI.</p></div></section>
<div class="diag-progress"><div class="container"><div class="bar"><span id="progressFill"></span></div><p class="muted" id="progressText" style="text-align:center;margin-top:8px"></p></div></div>
<div class="container">
  <div class="intro-card" id="introScreen">
    <h2>Which transformation does your brand need?</h2>
    <p class="muted" style="margin:12px 0 24px">This diagnostic scores your situation across Brand IQ's four axes and identifies your strategic priority.</p>
    <div class="grid-2" style="margin-bottom:24px">
      <div class="card"><h3>IQ-Growth</h3><p>Restart brand momentum</p></div>
      <div class="card"><h3>IQ-Innovation</h3><p>Structure your innovation pipeline</p></div>
      <div class="card"><h3>IQ-CSR</h3><p>Turn CSR into an advantage</p></div>
      <div class="card"><h3>IQ-AI</h3><p>Embed AI in your marketing</p></div>
    </div>
    <button class="btn btn-primary" id="startBtn">Start the diagnostic</button>
  </div>
  <div id="questionsContainer"></div>
  <div id="resultContainer"></div>
</div>
"""
    return body, extra


def merci_body(lang):
    if lang == "fr":
        return """<section class="hero"><div class="container" style="max-width:680px;text-align:center">
        <h1>Message bien reçu</h1>
        <p class="lede">Merci. Je vous réponds sous 24h. En attendant, vous pouvez lancer le diagnostic express ou parcourir les missions.</p>
        <div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="diagnostic.html">Diagnostic express</a><a class="btn btn-secondary" href="index.html">Retour à l'accueil</a></div>
        </div></section>"""
    return """<section class="hero"><div class="container" style="max-width:680px;text-align:center">
        <h1>Message received</h1>
        <p class="lede">Thank you. I will reply within 24 hours. Meanwhile, you can run the express diagnostic or browse the missions.</p>
        <div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="diagnostic.html">Express diagnostic</a><a class="btn btn-secondary" href="index.html">Back to home</a></div>
        </div></section>"""


def legal_body(lang, kind):
    if lang == "fr":
        if kind == "mentions":
            return """<section class="container legal" style="padding:80px 0"><h1>Mentions légales</h1>
            <p>Le site brand-iq.co est édité par Brand IQ, activité de conseil et de formation en stratégie de marque, représentée par Gérald Saada.</p>
            <h2>Contact</h2><p>14 rue Dailly, 92210 Saint-Cloud, France<br>Email : gerald.saada@brand-iq.co<br>Téléphone : +33 6 03 56 14 55</p>
            <h2>Hébergement</h2><p>Site statique hébergé chez un prestataire cloud (CDN). Le nom de domaine est enregistré chez IONOS.</p>
            <h2>Propriété intellectuelle</h2><p>Les méthodes UNLOCK™, CREATE™, AMPLIFY™ et SUSTAIN™, les textes, visuels et marques sont protégés. Toute reproduction non autorisée est interdite.</p>
            <h2>Directeur de la publication</h2><p>Gérald Saada.</p></section>"""
        if kind == "privacy":
            return """<section class="container legal" style="padding:80px 0"><h1>Politique de confidentialité</h1>
            <p>Brand IQ traite les données que vous envoyez via le formulaire de contact (identité, entreprise, email, téléphone, message) uniquement pour répondre à votre demande.</p>
            <h2>Base légale</h2><p>Intérêt légitime et mesures précontractuelles. Aucune vente de données. Pas de prospection automatisée sans accord.</p>
            <h2>Durée</h2><p>Les messages sont conservés le temps de la relation commerciale, puis archivés ou supprimés.</p>
            <h2>Vos droits</h2><p>Accès, rectification, opposition, effacement : écrivez à gerald.saada@brand-iq.co.</p>
            <h2>Cookies</h2><p>Ce site est statique et n'utilise pas de cookies publicitaires. Un hébergeur CDN peut déposer des cookies techniques de performance.</p></section>"""
        return """<section class="container legal" style="padding:80px 0"><h1>Conditions générales de vente</h1>
        <p>Les missions Brand IQ (sprints de 2 à 4 semaines, accompagnement, formations et workshops) font l'objet d'un devis et d'une proposition commerciale écrits.</p>
        <h2>Prix et paiement</h2><p>Les honoraires sont indiqués hors taxes. Acompte à la commande, solde selon jalons convenus.</p>
        <h2>Propriété des livrables</h2><p>Les livrables spécifiques au client vous sont cédés après paiement intégral. Les méthodes, outils et frameworks Brand IQ restent la propriété de Brand IQ.</p>
        <h2>Confidentialité</h2><p>Brand IQ s'engage à la confidentialité des informations clients. Un NDA peut être signé sur demande.</p>
        <h2>Droit applicable</h2><p>Droit français. Tribunal compétent : Nanterre.</p></section>"""
    if kind == "mentions":
        return """<section class="container legal" style="padding:80px 0"><h1>Legal notice</h1>
        <p>brand-iq.co is published by Brand IQ, a brand-strategy consulting and training practice represented by Gérald Saada.</p>
        <h2>Contact</h2><p>14 rue Dailly, 92210 Saint-Cloud, France<br>Email: gerald.saada@brand-iq.co<br>Phone: +33 6 03 56 14 55</p>
        <h2>Hosting</h2><p>Static site hosted on a cloud CDN. The domain is registered with IONOS.</p>
        <h2>IP</h2><p>UNLOCK™, CREATE™, AMPLIFY™, SUSTAIN™ methods, copy, visuals and trademarks are protected.</p></section>"""
    if kind == "privacy":
        return """<section class="container legal" style="padding:80px 0"><h1>Privacy policy</h1>
        <p>Brand IQ processes data you send via the contact form solely to answer your request.</p>
        <h2>Your rights</h2><p>Access, rectification, objection, erasure: email gerald.saada@brand-iq.co.</p>
        <h2>Cookies</h2><p>This is a static site with no advertising cookies. The CDN may set technical performance cookies.</p></section>"""
    return """<section class="container legal" style="padding:80px 0"><h1>Terms of sale</h1>
    <p>Brand IQ missions (2–4 week sprints, retainers, training) are confirmed by a written proposal.</p>
    <h2>Fees</h2><p>Fees are quoted exclusive of tax. Deposit on order, balance on agreed milestones.</p>
    <h2>Deliverables</h2><p>Client-specific deliverables transfer after full payment. Brand IQ methods and frameworks remain Brand IQ property.</p>
    <h2>Governing law</h2><p>French law. Courts of Nanterre.</p></section>"""


def write_diag(lang, title, desc):
    body, extra = diagnostic_body(lang)
    html = header(lang, "diagnostic.html", title, desc) + body + extra + footer(lang)
    dest = ROOT / ("en" if lang == "en" else "") / "diagnostic.html"
    dest.write_text(html, encoding="utf-8")
    print("wrote", dest.relative_to(ROOT))


def main():
    write("fr", "index.html", HOME["fr"]["title"], HOME["fr"]["desc"], home_body("fr"))
    write("en", "index.html", HOME["en"]["title"], HOME["en"]["desc"], home_body("en"))
    write("fr", "missions.html", "Missions | Brand IQ", "UNLOCK, CREATE, AMPLIFY, SUSTAIN", missions_body("fr"))
    write("en", "missions.html", "Missions | Brand IQ", "UNLOCK, CREATE, AMPLIFY, SUSTAIN", missions_body("en"))
    write("fr", "formations.html", "Formations | Brand IQ", "Brand IQ Academy", formations_body("fr"))
    write("en", "formations.html", "Training | Brand IQ", "Brand IQ Academy", formations_body("en"))
    write("fr", "secteurs.html", "Secteurs | Brand IQ", "FMCG, beauté, santé, scale-up", secteurs_body("fr"))
    write("en", "secteurs.html", "Sectors | Brand IQ", "FMCG, beauty, health, scale-up", secteurs_body("en"))
    write("fr", "a-propos.html", "À propos | Brand IQ", "Gérald Saada", about_body("fr"))
    write("en", "a-propos.html", "About | Brand IQ", "Gérald Saada", about_body("en"))
    write("fr", "contact.html", "Contact | Brand IQ", "Contacter Brand IQ", contact_body("fr"))
    write("en", "contact.html", "Contact | Brand IQ", "Contact Brand IQ", contact_body("en"))
    write_diag("fr", "Diagnostic express | Brand IQ", "16 questions pour identifier votre mission prioritaire")
    write_diag("en", "Express diagnostic | Brand IQ", "16 questions to identify your priority mission")
    write("fr", "merci.html", "Merci | Brand IQ", "Message envoyé", merci_body("fr"))
    write("en", "merci.html", "Thank you | Brand IQ", "Message sent", merci_body("en"))
    write("fr", "mentions-legales.html", "Mentions légales | Brand IQ", "Mentions légales", legal_body("fr", "mentions"))
    write("en", "mentions-legales.html", "Legal notice | Brand IQ", "Legal notice", legal_body("en", "mentions"))
    write("fr", "confidentialite.html", "Confidentialité | Brand IQ", "Confidentialité", legal_body("fr", "privacy"))
    write("en", "confidentialite.html", "Privacy | Brand IQ", "Privacy", legal_body("en", "privacy"))
    write("fr", "cgv.html", "CGV | Brand IQ", "CGV", legal_body("fr", "terms"))
    write("en", "cgv.html", "Terms | Brand IQ", "Terms", legal_body("en", "terms"))

    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://www.brand-iq.co/sitemap.xml\n", encoding="utf-8")
    pages = ["", "missions.html", "formations.html", "secteurs.html", "a-propos.html", "contact.html", "diagnostic.html",
             "en/", "en/missions.html", "en/formations.html", "en/secteurs.html", "en/a-propos.html", "en/contact.html", "en/diagnostic.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in pages:
        sm.append(f"<url><loc>https://www.brand-iq.co/{p}</loc></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
