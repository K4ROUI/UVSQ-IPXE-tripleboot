# Reproduire le laboratoire dans un réseau isolé

Ce guide décrit une reproduction **de test**, et non un déploiement en production.

## 1. Préparer l'environnement

- Utiliser un réseau **isolé** ou un réseau virtuel dédié.
- Éviter deux serveurs DHCP actifs sur le même segment.
- Autoriser les échanges nécessaires à **DHCP, TFTP et HTTP**.
- Activer le démarrage **PXE/UEFI** côté client.
- Prévoir un hôte Windows avec Tiny PXE Server.

**Ne pas activer un serveur DHCP de test sur un réseau universitaire ou domestique administré sans autorisation.**

## 2. Préparer les médias du serveur

Le script `menu.ipxe` suppose cette arborescence (les médias ne sont pas présents dans le dépôt) :

```text
<racine-serveur>/
├── config.ini
├── menu.ipxe
├── ipxe.efi
├── casper/
│   ├── ubuntu.iso
│   ├── vmlinuz
│   └── initrd
├── debian/
│   ├── debian-live.iso
│   ├── vmlinuz
│   └── initrd.img
└── windows/
    ├── wimboot
    ├── bcd
    ├── boot.sdi
    └── boot.wim
```

Fournir séparément des images et composants compatibles, dans le respect des licences correspondantes.

## 3. Adapter la configuration

Le fichier `config.ini` contient notamment :

```ini
root=C:\studies\TER
filename=ipxe.efi
altfilename=menu.ipxe
httpd=1
```

1. Remplacer la valeur `root` par le chemin réel des fichiers.
2. Vérifier les fichiers `ipxe.efi` et `menu.ipxe` dans cette racine.
3. Sélectionner la bonne interface réseau dans Tiny PXE Server.
4. Vérifier que l'URL construite à partir de `${dhcp-server}` pointe vers le **serveur HTTP**. Si DHCP et HTTP sont séparés, adapter le menu.

## 4. Tester le démarrage

1. Démarrer Tiny PXE Server sur le réseau de test.
2. Vérifier les services DHCP, TFTP et HTTP.
3. Démarrer un client UEFI sur sa carte réseau.
4. Vérifier l'arrivée du chargeur et du menu iPXE.
5. Tester successivement Ubuntu Live, Debian Live et Windows PE.
6. Ouvrir une application dans chaque session.
7. Répéter éventuellement avec une VM sans disque virtuel.
8. Remplir le protocole de [validation](validation.md).

## 5. Dépannage

| Symptôme | Vérification |
| --- | --- |
| Aucun bail réseau | DHCP, interface, réseau virtuel, pare-feu |
| Chargeur inaccessible | Racine du serveur, `ipxe.efi`, transfert TFTP |
| Menu absent | `menu.ipxe`, `altfilename`, HTTP, adresse serveur |
| Linux ne démarre pas | Fichiers ISO/noyau/initrd, compatibilité, HTTP |
| Windows PE ne démarre pas | Ensemble `wimboot` / BCD / `boot.sdi` / `boot.wim` |
| Démarrage lent | Réseau, tailles des images, charge du serveur ; effectuer des mesures |

Ne publier que des captures et journaux vérifiés et autorisés, après retrait des données sensibles.
