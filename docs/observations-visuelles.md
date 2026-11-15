# Captures et observations des essais iPXE

Cette page décrit **cinq captures authentiques communiquées par un participant au projet universitaire**. Les cinq fichiers image sont maintenant disponibles dans [le dossier `docs/screenshots/`](screenshots/). Ils montrent le menu, les environnements démarrés et les échanges réseau observés.

## 1. Menu de démarrage iPXE

**Capture publiée :** `docs/screenshots/01-menu-ipxe.webp`

La capture montre un écran intitulé « UVSQ Hybrid Boot Menu » avec les choix :

- Boot Lubuntu Desktop (HTTP)
- Boot Windows PE (HTTP)
- Boot Debian Live Desktop (HTTP)

**Attention :** le menu photographié emploie le nom « Lubuntu », tandis que le script `menu.ipxe` publié utilise « Ubuntu Live ». Les fichiers peuvent provenir de versions différentes du projet ; la capture ne doit pas être présentée comme un rendu certain du script actuellement versionné.

## 2. Environnements graphiques démarrés

**Capture publiée :** `docs/screenshots/02-environnements-winpe-debian-lubuntu.webp`

Trois vues montrent un environnement Windows et des bureaux Debian et Lubuntu. La légende de la première image du rapport original mentionne « Windows 11 », mais une invite de commande avec un lecteur `X:` est caractéristique de **Windows PE**. Il ne faut **pas** en déduire qu'une édition complète de Windows 11 a démarré sans disque.

## 3. Communications réseau entre machines virtuelles

**Capture publiée :** `docs/screenshots/03-tests-ping-entre-clients.webp`

La capture présente plusieurs fenêtres **Oracle VirtualBox**, avec des consoles Linux et Windows effectuant des commandes `ping`. Les échanges visibles entre plusieurs adresses du réseau de test aboutissent à des réponses ; certains relevés affichent **0 % de perte de paquets**.

Ce résultat confirme le fonctionnement des communications testées à cet instant, sans mesurer un débit soutenu ni prouver l'absence d'erreurs sur la totalité du déploiement.

## 4. Ping depuis Windows PE vers le serveur

**Capture publiée :** `docs/screenshots/04-test-ping-windows-pe.webp`

La console Windows montre une configuration IPv4 locale et un `ping` vers l'adresse du serveur sur le réseau de laboratoire. Le relevé visible indique **4 paquets transmis, 4 reçus, 0 % de perte**.

## 5. Ping depuis Lubuntu vers le serveur

**Capture publiée :** `docs/screenshots/05-test-ping-lubuntu-serveur.webp`

Le terminal Lubuntu montre l'adressage de l'interface `enp0s3` et un `ping` vers le serveur du laboratoire. Le relevé visible affiche **3 paquets transmis, 3 reçus, 0 % de perte**.

## Rôle personnel et interprétation

Selon le participant ayant transmis ces captures, sa contribution personnelle portait principalement sur **la partie Windows/Windows PE et la partie serveur**, au sein d'un projet réalisé en équipe.

Les captures fournissent des **preuves visuelles de sessions système et de connectivité réseau**. Elles ne constituent pas un banc d'essai de performance et ne permettent pas, à elles seules, de compter les plus de 20 postes physiques rapportés lors du projet. Les démarrages ont été décrits comme rapides et sans problème bloquant, mais aucun temps exact n'a été mesuré.

### Précautions relatives aux images publiées

Les captures sont désormais publiques. Il convient de vérifier qu'elles ne révèlent ni identifiants, ni secrets, ni informations internes du laboratoire et que leur publication est autorisée. Les adresses réseau privées visibles peuvent être conservées ou masquées selon les règles applicables.
