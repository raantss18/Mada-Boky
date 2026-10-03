# Point de reprise — brouillon T11 S

Vingt chapitres, quatre DS et deux sujets de synthèse sont présents. Sources communes aux éditions élève et professeur. Aucun statut de release vérifiée.

Le 3 octobre 2026, reprise après interruption de la sauvegarde : la branche distante main avait avancé sur des livres Terminales, sans modification concurrente des sources T11 existantes. Le nouvel arbre est fondé sur 63f13d306db8a936939ac374282266f6f130b227 pour conserver ces changements.

Compilation complète : aux du chapitre 1 tronquée à 4096 octets, même après nettoyage. L’assemblage utilise maintenant input précédé de clearpage; pas de diagnostic de cause racine établi. La formule des règles de dérivation a été répartie sur deux lignes pour corriger le débordement signalé. Les deux compilations complètes terminent maintenant avec code 0. PDF élève 120 pages, professeur 128 pages; voir build-result.json. Aucune inspection finale globale effectuée.

Inspection réellement effectuée auparavant : chapitre limites/continuité dans un assemblage partiel, pages physiques élève 25–27 et professeur 27–30. Les PDF partiels de 34/36 pages ne représentent pas le livre complet. Aucune inspection de l’ensemble ne peut en être déduite.

Prochaine unité : terminer compilation, puis inventaire/curriculum et résolution séparée des exercices. Voir issues.json pour les contrôles manquants.

## Revue complète du 3 octobre 2026 — 2026-10-03T06:30:11.959261+00:00

La mention « aucune inspection finale globale » ci-dessus décrit le checkpoint antérieur. Elle ne décrit plus les PDF finaux actuels. La reprise depuis 91223e0 a conservé les autres livres. 206 groupes résolus et comparés, 947 objets inventoriés, 87 exigences curriculaires réconciliées. Calcul des huit temps réparé : Σx²=692, V=159/16, σ=√159/4. Domaines, hypothèses et prérequis corrigés; activités manquantes ajoutées. Quatre rapports de résolution et un audit du cours documentent les contrôles du même modèle.

Après deux réparations visuelles (titre de corrigés élève vide et légende débordante), les deux compilations propres terminent avec code 0. Les PDF 120/128 pages sont ceux du snapshot d8e0177459644755457cd0d406d5ed2dcaab4977b68aadc707c8fa862851d91e. Les 248 pages ont été inspectées individuellement à résolution lisible, avec réinspection des pages modifiées et comparaison des rendus identiques pour les pages élève conservées. Aucun contenu mathématique coupé, glyphe manquant ou chevauchement non résolu trouvé; la pagination recto verso reste normale.

Checker original SHA256 ca067449445a953d2dc371fa31c4d06d8522571af40ee9ad43742c800b0b40b5, code 0, 1 898 enregistrements; limites de certification clairement indiquées. Sources et PDF/preuves sauvés puis relus aux commits 3e5a1258 et 5318824ff0b4a9a8545159ff1b7d7aabcee71313; toutes les nouvelles entrées comparées, octets PDF relus et égaux. Le checkpoint suivant sauvegarde les gates et ces métadonnées et sera relu à son tour.

Brouillon relu, pas d'approbation humaine ou ministérielle finale. Ancienne cause d'aux tronquée toujours inconnue; succès opérationnel des rebuilds uniquement. Les avertissements de paquets et absence de césure française sont conservés dans build-result. Guide de reprise dédié HANDOFF.md; pas de fiche élève supplémentaire à cette phase.

## Réouverture pédagogique — 3 octobre 2026

Le retour utilisateur remet en cause la profondeur et certaines consignes malgré les gates du snapshot précédent. Ceux-ci sont historiques, pas une validation utilisateur. Méthodes commentées et problèmes de transfert des chapitres 2–5 rédigés; quatre DS reformulés avec barèmes et corrigés développés. Autres chapitres, revue séparée, assemblage, pages et nouveaux gates encore en cours. Statut brouillon en révision.
