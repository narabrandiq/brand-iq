# Brand IQ — site vitrine

Site statique bilingue (FR / EN) recréé à partir du contenu Webflow du 6 septembre 2026. Aucun abonnement Webflow n’est nécessaire.

## Aperçu local

```powershell
cd C:\Users\geral\Projects\brand-iq
python -m http.server 8080
```

Ouvrir http://localhost:8080

Pour régénérer les pages après une modification de contenu :

```powershell
python scripts\generate_site.py
```

## Coût : passer de 39 $/mois à ~0 €/mois

| Poste | Aujourd’hui | Recommandé |
|---|---|---|
| Site (Webflow) | **39 $/mois** (~468 $/an) | **0 €** (GitHub Pages) |
| Nom de domaine IONOS | Pack domaine (déjà payé) | **À garder** |
| Email Gmail / Google | MX déjà en place | **Ne rien changer** |
| SSL | Alerte IONOS « non sécurisé » | **Inclus et automatique** chez GitHub Pages |

Économie : environ **470 $/an**, sans toucher aux emails `gerald.saada@brand-iq.co`.

## Hébergeur en place : GitHub Pages (gratuit)

Le site est publié depuis le dépôt GitHub. Chaque `git push` sur `main` redéploie automatiquement.

- URL de secours : `https://narabrandiq.github.io/brand-iq/`
- Domaine prévu : `https://www.brand-iq.co` (après changement DNS IONOS)

Cloudflare Pages et Netlify restent possibles (compte à relier au même repo). Ils ne remplacent pas le changement DNS chez IONOS.

### DNS IONOS à appliquer (hébergement web uniquement)

Garder les **serveurs de noms IONOS**. Ne pas basculer vers Cloudflare.

| Type | Hôte | Nouvelle valeur |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `narabrandiq.github.io` |

Remplacer l’actuel A `@` `198.202.211.1` et le CNAME `www` `cdn.webflow.com`.

## DNS IONOS — quoi changer, quoi ne pas toucher

Garder les **serveurs de noms IONOS** (`ns1103.ui-dns.de`, etc.). Ne pas cliquer sur « Utiliser des serveurs de noms personnalisés ».

### À modifier (hébergement web uniquement)

Voir le tableau GitHub Pages plus haut (4 enregistrements A pour `@`, CNAME `www` → `narabrandiq.github.io`).

### À supprimer après bascule

- TXT `_webflow` (vérification Webflow, devenue inutile)

### À ne surtout pas toucher (email Google)

- Les 5 MX (`aspmx.l.google.com` et `alt1`…`alt4`)
- TXT `@` `v=spf1 include:_spf.google.com ~all`
- TXT `@` `google-site-verification=...`
- CNAME `_domainconnect` (outil IONOS)

Propagation : 15 minutes à quelques heures. Tester `https://www.brand-iq.co` **avant** d’annuler Webflow.

## SSL

Ne pas activer le bouton SSL IONOS (il sert leur offre hébergement). Le certificat HTTPS est fourni automatiquement par GitHub Pages une fois le DNS pointé.

## Formulaire de contact

Le formulaire utilise [FormSubmit](https://formsubmit.co) vers `gerald.saada@brand-iq.co`. Au premier envoi, un email de confirmation FormSubmit arrive : cliquer le lien une fois.

## Annuler Webflow

Seulement après :

1. `https://www.brand-iq.co` et `https://brand-iq.co` affichent le nouveau site en HTTPS
2. Un envoi test du formulaire arrive bien
3. Un email Gmail de test arrive toujours

Puis résilier l’abonnement Webflow (39 $/mois). Les images du site sont déjà copiées en local (`assets/img`), plus de dépendance au CDN Webflow.
