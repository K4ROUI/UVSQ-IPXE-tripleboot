# Architecture technique

## Objectif

Démarrer plusieurs environnements depuis un serveur commun sur des clients **sans disque local** (PC physiques ou VM).

| Composant | Rôle |
| --- | --- |
| Tiny PXE Server sur Windows | Services DHCP, TFTP et HTTP du montage de laboratoire |
| `config.ini` | Configuration du serveur et chaînage iPXE |
| `ipxe.efi` | Chargeur UEFI transféré par TFTP |
| `menu.ipxe` | Choix d'Ubuntu Live, Debian Live ou Windows PE |
| Fichiers système | Médias servis via HTTP, non versionnés |
| Clients | Démarrent sans OS installé sur un disque local |

## Séquence d'amorçage

1. Le firmware UEFI du client lance une requête PXE.
2. DHCP communique les paramètres réseau et le nom du chargeur.
3. TFTP transmet `ipxe.efi`.
4. iPXE récupère le menu, puis l'utilisateur choisit un système.
5. Les composants de démarrage arrivent via HTTP.
6. Une session temporaire démarre sur le client.

## Entrées définies dans `menu.ipxe`

- **Ubuntu Live :** `casper/vmlinuz`, `casper/initrd`, `casper/ubuntu.iso`, avec `boot=casper`, `ip=dhcp` et `url=`.
- **Debian Live :** `debian/vmlinuz`, `debian/initrd.img`, `debian/debian-live.iso`, avec `boot=live` et `fetch=`.
- **Windows PE :** `windows/wimboot`, `windows/bcd`, `windows/boot.sdi` et `windows/boot.wim`.

L'entrée Windows lance un **environnement Windows PE**, et non une installation classique du système Windows sur disque.

## Compromis

- Le **démarrage sans disque** convient à des sessions temporaires mais n'implique pas que les données persistent après l'arrêt.
- TFTP sert au chargeur initial ; HTTP facilite le transfert des fichiers volumineux.
- Le serveur commun simplifie la distribution des médias, mais crée une dépendance au réseau et au serveur.
- `${dhcp-server}` doit être ajusté si DHCP et HTTP sont hébergés sur des machines différentes.
- Le réseau doit être isolé pour éviter les conflits de DHCP.

## Points à vérifier avant une réutilisation

Compatibilité UEFI et des médias (noyau/initrd/ISO), prise en charge de Secure Boot, droits de distribution des images, sécurité du serveur et de son réseau. Pour un usage multi-clients, **mesurer** les temps de démarrage et la charge réseau : aucune performance chiffrée n'est documentée ici.
