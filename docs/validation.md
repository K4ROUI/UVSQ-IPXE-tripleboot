# Validation : résultats rapportés et essais reproductibles

## Résultats de l'expérimentation universitaire

Ces résultats sont **rapportés par l'équipe ayant réalisé les essais** ; le dépôt ne contient pas encore de captures d'écran, journaux de séances ou mesures chronométrées permettant de les corroborer indépendamment.

| Essai | Résultat rapporté |
| --- | --- |
| Démarrage de 6 postes physiques | Réussi, première phase |
| Extension à plus de 20 postes | Réussi, phase étendue |
| Machines virtuelles sans disque dur | Réussi |
| Ubuntu Live | Session utilisable |
| Debian Live | Session utilisable |
| Windows PE | Session utilisable |
| Exécution d'applications pendant les sessions | Réussie |

Ces observations soutiennent un **démarrage réseau sans disque local**, pas une installation persistante ni un benchmark. Le qualificatif « rapide » est une impression des utilisateurs, **pas un résultat mesuré**. Le nombre de démarrages exactement simultanés n'est pas connu.

Le responsable de formation IRS a évoqué l'idée d'une future utilisation dans les laboratoires ; **aucune adoption institutionnelle n'est présentée comme déjà réalisée**.

## Vérifications à effectuer lors d'une reproduction

- [ ] Réseau isolé et absence de DHCP concurrent.
- [ ] Chemin `root` valide et médias non versionnés disponibles.
- [ ] Client UEFI récupérant `ipxe.efi`.
- [ ] Menu iPXE avec ses trois entrées.
- [ ] Ubuntu Live démarre et lance une application.
- [ ] Debian Live démarre et lance une application.
- [ ] Windows PE démarre et lance un outil.
- [ ] VM sans disque dur virtuel démarrant un environnement.
- [ ] Nombre de clients et simultanéité relevés.
- [ ] Durées et charge réseau mesurées, si nécessaires.

Les cases ci-dessus sont **volontairement décochées** : elles constituent un protocole futur, non un faux historique de tests.

| Date | Client | Environnement | Résultat | Durée | Remarques |
| --- | --- | --- | --- | --- | --- |
| À renseigner | À renseigner | À renseigner | À vérifier | À mesurer | À renseigner |

## Tests statiques inclus

```bash
python -m unittest discover -s tests -v
```

Les **7 contrôles** testent la cohérence des fichiers texte `config.ini` et `menu.ipxe`. Ils **ne démarrent pas d'OS**, ne téléchargent pas d'ISO et ne remplacent pas les essais sur le réseau physique.
