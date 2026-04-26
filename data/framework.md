## **Préambule : Réforme du Dossier de Consultant**

Les dossiers techniques classiques sont souvent "éxécution"-centrés et focalisés sur une accumulation de résultats disparates. Cette approche nuit à la lisibilité : le découpage mission par mission, étalé sur plusieurs pages, dilue l'expérience réelle du consultant et masque sa valeur ajoutée.

Les clients n'attendent pas une liste exhaustive de *stacks* technologiques, mais une compréhension fine de votre **vision** et de votre **capacité d'arbitrage**. Ils veulent comprendre le "Pourquoi" (Enjeu), le "Comment" (Stratégie) et le "Quoi" (Résultat).

### **Le nouveau modèle de pilotage technique**

Pour répondre à cet impératif de séniorité, je propose un framework articulé autour de trois piliers :

1.  **Synthèse des Compétences :** Mise en avant immédiate des années d'expérience consolidées par domaines (Technique, Organisationnel, Méthodologique).
2.  **Expériences par Postes :** Regroupement des missions par fonctions principales pour illustrer la continuité du parcours et la montée en expertise.
3.  **Logique de Valeur (Framework "Enjeu-Impact") :** Chaque expérience est présentée selon une structure narrative axée sur la résolution de problèmes complexes, plutôt que sur une simple énumération de tâches.

Cette approche permet de transformer le CV technique en un **outil de pilotage stratégique**, où l'expertise est immédiatement lisible et la valeur ajoutée directement corrélée aux enjeux business du client.


## **Framework de Pilotage Technique**

### **Compétences Clés**

#### **Techniques**
* **Python :** 10+ ans (dont 5 en production via SOLID/TDD).
* **Data Science & Engineering:** 10+ ans (dont 4 en production industrielle sous contraintes ACID/MLOps).
* **Computer Vision :** 5 ans (dont 3 en Deep Learning).
* **NLP & IA Générative :** 5 ans (RAG, Fine-tuning, orchestration d'agents).
* **Conteneurisation et Orchestration:** 5 ans **Docker** (dont 2 inclu dans environement kubernetes)
* **Git et DevOps :** 7 ans **Git** (dont 3 inclu dans CI/CD)

#### **Organisationnel**
* **Science & Recherche :** 5 ans (dont 3 en *Life Science*).
* **Industrie & Défense :** 5 ans en contextes critiques et services.

#### **Méthodologie**
* **Management & Lead :** 4 ans (dont 3 en coaching et pilotage d'équipe).
* **Architecture IA :** 3 ans (dont 2 via référentiels IAF/TOGAF).
* **Cycles de vie :** 4 ans en environnements Agiles et Cycle en V.



### Experiences

(Less is More (court et precis) + SMART (Resultat mininimum obtenu, ne pas faire de cherry pick = resultat - barre erreur))

#### 1. Enjeu (La Valeur)
* **Contenu :** Définir le "Pain Point" métier. Ne pas lister de techno, mais un résultat.
* **Réflexion :** Pourquoi ce projet existe-t-il ? Quel est le coût de l'inaction ? Quel est le gain financier (ROI) ou opérationnel (temps, sécurité) attendu ?
* **Format :** *"Résoudre [Problème X] pour permettre [Gain Y], en visant une rentabilité de [Z]."*

#### 2. Contraintes & Exigences (Le Cadre)
* **Contenu :** Les facteurs "non-négociables" qui dictent le design.
* **Réflexion :** Quelles sont les limites imposées par l'écosystème ? (normes ISO, contraintes de temps réel, impératifs de souveraineté/Cloud hybride, ressources matérielles limitées).
* **Format :** Paragraphe qui empêchent une solution "standard" du marché.

#### 3. Stratégie & Arbitrage (La Décision)
* **Contenu :** Le "Pourquoi" architectural. C'est ici que vous vendez votre expertise et les méthodes (VRIO, TRL, IAF, etc.).
* **Réflexion :** Pourquoi avoir choisi une approche déterministe plutôt qu'IA générative ? Pourquoi ce moteur de base de données (Graph vs SQL) ? Justifiez le compromis (ex: *« J'ai sacrifié la précision absolue pour garantir la certifiabilité ISO »*).
* **Format :** *"Arbitrage pour [Atténuer Risque X] au profit de [Fiabilité Y] via [Architecture choisie]."*

#### 4. Exécution & Qualité (La Réalisation)
* **Contenu :** La rigueur de mise en œuvre.
* **Réflexion :** Comment garantissez-vous que le code est maintenable et testable ? (Application des principes **SOLID** pour la scalabilité, **ACID** pour la validité, **TDD** pour la non-régression, **KISS** pour réduire la dette technique).
* **Leadership :** Comment avez-vous embarqué l'équipe ? (Peer-programming, rituels agiles, montée en compétence, standardisation des assets).
* **Format :** *"Approche : SOLID/TDD/KISS + Animation d'équipe par [Action managériale]."*

#### 5. Impact (Le Résultat)
* **Contenu :** La preuve de la réussite (Post-mortem).
* **Réflexion :** Quels sont les indicateurs factuels de succès ? (Temps de traitement réduit de X%, conformité totale, gain financier, retour utilisateur).
* **Format :** *"Indicateur clé + Résultat chiffré + Feedback métier."*


## Capgemini - Hybrid Intelligence | 07/2024 – 04/2026
**Rôle : Architecte IA / Lead Tech IA**
*Expertise en transformation digitale pour Airbus, Liebherr, Safran. Pilotage de la viabilité technique et financière.*

### **Projet : Gouvernance IA (Capgemini, 2025-2026)**

* **Enjeu :** Supprimer le reporting manuel sous Excel et fiabiliser le suivi du ROI pour des projets IA en environnement *On-premise*.
* **Contraintes :** Isolation réseau totale, sécurité conforme aux normes internes, interopérabilité directe avec les systèmes BI existants.
* **Stratégie :** Arbitrage pour une architecture "Small Data" (**DuckDB/Datasette**) au lieu d'un Data Warehouse lourd ; choix dicté par la réduction de la dette technique et la simplicité de maintenance.
* **Exécution :** Automatisation des flux via **Mage-ai** ; intégration d'agents de contrôle **PydanticAI** pour la validation des KPIs. Standardisation des composants pour l'évolutivité.
* **Impact :** Suppression de la saisie manuelle, automatisation des reportings périodiques, gain de 4h de traitement hebdomadaire par périmètre, fiabilisation des indicateurs de performance.


### **Projet : Automatisation de l'inspection moteur 2D-3D (Safran, Lead Tech / Expert IA, 2025-2026)**

* **Enjeu :** Automatiser l'inspection de turboréacteurs pour fiabiliser la détection de dommages sur les aubes.
* **Contraintes & Exigences :** Exigences de certification aéronautique, précision millimétrique, et nécessité d'une quantification de l'incertitude de mesure pour la prise de décision.
* **Stratégie & Arbitrage :** Conception d'un pipeline de vision hybride (géométrique "trimesh" / Deep Learning). Arbitrage pour l'intégration de méthodes de quantification d'incertitude (MAPIE) plutôt qu'une approche "boîte noire", afin de garantir la conformité aux exigences de sécurité.
* **Exécution & Qualité :** Optimisation du moteur d'inférence (CUDA / PyTorch3D) pour le calcul GPU, structuration de l'interface de supervision (Marimo) et mentorat technique auprès de l'équipe pour assurer une montée en compétence sur les briques développées.
* **Impact :** Livraison d'une solution de mesure, réduisant les erreurs d'interprétation humaine et accélérant le cycle d'analyse des pièces critiques grâce à une fiabilité statistique.


### **Projet : Industrialisation de la production logicielle (AI Factory, Lead Tech / Expert IA, 2024-2025)**

* **Enjeu :** Automatiser la génération de code conforme aux standards SOLID/TDD pour réduire la dette technique et garantir la souveraineté des actifs logiciels en environnement contraint (*On-premise/OpenStack*).
* **Contraintes & Exigences :** Exigences de souveraineté numérique, besoin de conformité aux standards de sécurité (SOC2), et nécessité d'un code hautement maintenable.
* **Stratégie & Arbitrage :** Arbitrage pour une approche "Build" de chaîne de production automatisée plutôt qu'une solution SaaS externe, afin de garantir l'intégrité et la localisation totale des données.
* **Exécution & Qualité :** Intégration d'interface d'assistance au développement (Roo-code) sur infrastructure locale (vLLM, Kubernetes). Mise en place d'une boucle d'observabilité et d'évaluation automatisée (Arize Phoenix, DeepEval).
* **Impact :** Industrialisation d'une chaîne de production logicielle automatisée, permettant la génération de modules conformes aux spécifications et scénarios métiers tout en garantissant la sécurité et la souveraineté des données.


### **Projet : Industrialisation de l'analyse de configuration ingénierie (Airbus, Lead Tech / Expert IA, 2025)**

* **Enjeu :** Sécuriser la préparation à la fabrication en harmonisant des configurations d'ingénierie (xBOM/mBOM) hétérogènes pour réduire les délais d'analyse d'impact.
* **Contraintes & Exigences :** Besoin de performance sur des données volumineuses (10M), nécessité de traçabilité des modifications et interopérabilité avec les systèmes ERP existants.
* **Stratégie & Arbitrage :** Adoption d'un modèle de données hybride (graphe et document) sous ArangoDB. Arbitrage pour une structure en graphe afin de modéliser nativement les dépendances complexes, là où une approche relationnelle classique aurait souffert de jointures trop coûteuses et d'une rigidité excessive.
* **Exécution & Qualité :** Industrialisation des pipelines d'ingestion avec Polars pour la performance, utilisation de requêtes AQL pour les traversées de graphe, et exposition via FastAPI pour une intégration fluide aux outils métiers. Mentorat technique pour assurer la maintenabilité de la *Graph factory* par les équipes.
* **Impact :** Mise en service de la *Graph factory* dédiée, permettant le calcul automatisé des « delta » d'ingénierie et une réduction du temps nécessaire aux analyses d'impact opérationnelles.


### **Projet : Monitoring environnemental en milieu contraint (Liebherr Aerospace, Lead Tech / Expert IA, 2025)**

* **Enjeu :** Développer une solution de monitoring de la qualité de l’air en cabine compatible avec les contraintes strictes des systèmes embarqués aéronautiques.
* **Contraintes & Exigences :** Ressources matérielles limitées, impératifs de latence pour le temps réel, et stabilité opérationnelle indispensable à l'embarquement.
* **Stratégie & Arbitrage :** Sélection de modèles interprétables (LGBoost). Arbitrage pour privilégier l'efficacité computationnelle et une faible empreinte mémoire au détriment de modèles Deep Learning complexes, afin de garantir la viabilité sur le matériel de bord.
* **Exécution & Qualité :** Standardisation des flux de séries temporelles (Pandas/NumPy) et développement d'un classifieur pour la détection d'anomalies. Mise en place de protocoles de test pour assurer la stabilité du diagnostic dans des conditions de vol réelles.
* **Impact :** Validation de la faisabilité technique et du modèle de classification, fournissant une base industrielle pour l'intégration future de capacités de diagnostic dans les systèmes de régulation de l'air.


### **Projet : Optimisation logistique et aide à la décision stratégique (THALES, Lead Tech / Expert IA, 2024-2025)**

* **Enjeu :** Optimiser l'efficacité logistique et la préparation de mission en environnement Défense par l'intégration de modèles prédictifs, pour accroître la réactivité opérationnelle.
* **Contraintes & Exigences :** Exigences de sécurité Défense, nécessité de résoudre des problèmes d'allocation sous contraintes, et déploiement sur infrastructure Cloud souveraine (Azure/Kubernetes).
* **Stratégie & Arbitrage :** Mise en œuvre d'une architecture hybride. Arbitrage pour coupler la maintenance prédictive (LGBoost) au déterministe de la recherche opérationnelle, afin de garantir des recommandations respectant les limites logistiques réelles.
* **Exécution & Qualité :** Développement d'un moteur de recommandation, intégrés dans un cycle de livraison (DevOps). Mentorat technique pour aligner les équipes sur les contraintes métiers spécifiques au secteur de la Défense.
* **Impact :** Industrialisation d'une solution d'aide à la décision stratégique permettant une amélioration mesurable de la réactivité logistique et une allocation optimisée des ressources critiques. Présenté au salon du Bourget.


### **Projet : Rapport d'imagerie satellite (THALES, Lead Tech / Expert IA, 2024)**

* **Enjeu :** Automatiser la production de rapports d'intelligence à partir de flux d'imagerie satellite multimodaux pour accélérer la prise de décision en centre de commandement.
* **Contraintes & Exigences :** Besoin d'interprétation contextuelle, exigences de sécurité et de reproductibilité des analyses, et nécessité d'une intégration dans les flux opérationnels existants.
* **Stratégie & Arbitrage :** Déploiement d'une architecture hybride RAG/ReAct. Arbitrage pour coupler le traitement visuel des *Vision Transformers* à la capacité de synthèse des LLM, afin de transformer des données brutes en rapports structurés.
* **Exécution & Qualité :** Industrialisation via une chaîne Gitlab CI/CD assurant la continuité du déploiement et la reproductibilité des analyses. Mise en œuvre d'un pipeline multimodal orchestré par LangChain.
* **Impact :** Réduction du temps de traitement opérationnel, permettant aux opérateurs d'exploiter des volumes d'imagerie satellite grâce à une synthèse automatisée et contextuelle.


## Capgemini Engineering (APA) | 09/2022 – 07/2024
**Rôle : Responsable Projets - Ingénieur-chercheur DATA/IA**

### **Pilotage de la transition technologique vers le véhicule électrique (Capgemini Engineering, Responsable Projets / Lead Tech, 2022-2024)**

* **Enjeu :** Sécuriser la transition technologique (échéance 2035) en orchestrant la transformation des architectures de gestion énergétique et de *Powertrain* intelligent.
* **Contraintes & Exigences :** Alignement avec les standards industriels (ISO), nécessité de synchroniser des ruptures technologiques avec les contraintes de *Time-to-Market* automobile.
* **Stratégie & Arbitrage :** Mise en œuvre de cadres de référence (TOGAF, IAF) pour assurer la conformité système. Arbitrage pour une priorisation des investissements basée sur des analyses de valeur (VRIO, Business Model Canvas, TRL) afin de maximiser le retour sur investissement R&D (ROI/QCDP).
* **Exécution & Qualité :** Pilotage d'une équipe transverse (R&D, Ingénierie système, IA) avec mise en place de rituels agiles, mentorat technique et structuration des processus collaboratifs pour fluidifier le passage de l'innovation au déploiement industriel (V-cycle ou Agile).
* **Impact :** Consolidation d'un portefeuille de projets, sécurisant la viabilité technique de la roadmap de propulsion électrique.


### **Projet : Diagnostic intelligent des calculateurs automobiles (Capgemini Engineering, Responsable Projets / Lead Tech, 2023-2024)**

* **Enjeu :** Développer un outil de diagnostic pour la maintenance prédictive, capable d'interpréter en temps réel les comportements des calculateurs (ECU) via le bus CAN.
* **Contraintes & Exigences :** Confidentialité stricte des données industrielles, nécessité d'une inférence locale, et besoin de traiter des flux de données véhicules.
* **Stratégie & Arbitrage :** Déploiement de modèles de langage en local (Ollama/Phi3). Arbitrage pour une approche "IA souveraine" plutôt qu'une solution cloud, afin de garantir l'étanchéité des données tout en conservant une capacité de diagnostic temps réel sur les trames véhicules.
* **Exécution & Qualité :** Conception d’un pipeline hybride alliant décodage dynamique (DBC) et méthodes d’exploration avancées (comparaison RAG vs Fine-Tuning). Développement d'une interface unifiée (React/FastAPI) pour le monitoring, avec une approche structurée par itérations pour valider les modèles.
* **Impact :** Livraison d'un démonstrateur technique présenté aux directions techniques de Renault et Stellantis, prouvant la pertinence opérationnelle de l'IA générative pour l'anticipation de pannes.


### **Projet : Pilotage prédictif adaptatif du refroidissement batterie (Capgemini Engineering, Responsable Projets / Lead Tech, 2023-2024)**

* **Enjeu :** Réduire la complexité opérationnelle des systèmes de refroidissement de batteries VE en substituant les stratégies de contrôle déterministes par une approche prédictive adaptative.
* **Contraintes & Exigences :** Modélisation de dynamiques thermiques non-linéaires, nécessité d'un environnement d'entraînement reproductible et conformité aux exigences de fiabilité automobile.
* **Stratégie & Arbitrage :** Adoption de l'Apprentissage par Renforcement (RL) pour la régulation continue par points de consigne (*setpoints*). Arbitrage pour coupler des politiques *on-policy* et *off-policy* afin de garantir une convergence optimale et une robustesse face aux variations thermiques réelles.
* **Exécution & Qualité :** Développement d'un simulateur dédié (Gymnasium), industrialisation de la chaîne d'entraînement (StableBaselines3/PyTorch) et mise en place d'une traçabilité des expérimentations (MLFlow) pour sécuriser l'auditabilité des modèles.
* **Impact :** Validation de la fiabilité de l'IA et mise en place d'un pipeline de production de modèles capable de s'adapter dynamiquement aux spécifications thermiques des batteries.

### **Projet : Jumeau numérique de régulation thermique batterie (Capgemini Engineering, Responsable Projets / Lead Tech, 2023)**

* **Enjeu :** Optimiser l'efficacité énergétique par le déploiement d'un jumeau numérique, permettant une régulation thermique prédictive conforme aux contraintes strictes des systèmes embarqués.
* **Contraintes & Exigences :** Sécurité déterministe (ISO 26262), latence critique < 10 ms (temps réel), et souveraineté totale des données (0 accès Cloud).
* **Stratégie & Arbitrage :** Développement d'un jumeau numérique hybride couplant un solveur déterministe (*acados*) pour la fidélité physique (certifiabilité) et une simulation en boucle fermée. Arbitrage pour une architecture asynchrone (MQTT) isolant les flux de données du jumeau pour garantir la réactivité du contrôle temps réel.
* **Exécution & Qualité :** Mise en place d'une stack python (python-can, FastAPI, DuckDB) et validation du jumeau numérique par simulation HIL (Hardware-in-the-Loop). Le système permet une historisation et une optimisation continue des modèles de contrôle sans compromettre l'intégrité de la boucle physique.
* **Impact :** Livraison d'un démonstrateur validant la précision du jumeau numérique, réduction de la latence par 3, et validation du passage en production de la chaîne de contrôle dynamique des actionneurs.


### **Projet : Pont de commande hybride IA-Actionneurs pour batteries VE (Capgemini Engineering, Responsable Projets / Lead Tech, 2022-2023)**

* **Enjeu :** Concevoir une interface électronique pour le pilotage d'actionneurs thermiques, permettant l'intégration directe de modèles d'IA au sein de la chaîne de commande des systèmes batterie.
* **Contraintes & Exigences :** Interopérabilité entre calculs basse consommation (*hard real-time*) et calculs IA lourds (NPU), gestion de puissance en environnement haute tension, et intégrité du bus de commande.
* **Stratégie & Arbitrage :** Mise en œuvre d'un découplage commande-puissance. Arbitrage pour une séparation physique entre la gestion temps réel des actionneurs (microcontrôleur) et l'unité d'accélération IA (NPU), garantissant que toute défaillance logicielle du moteur d'inférence ne compromet la sécurité du système de refroidissement.
* **Exécution & Qualité :** Développement d'une architecture électronique hybride : pilotage PWM, étages de conversion de puissance, et interface de communication. Validation par banc de test Hardware-in-the-Loop (HIL) pour tester l'interface dans des conditions électriques extrêmes.
* **Impact :** Réalisation physique d'un pont de commande validant l'intégration de l'IA dans les systèmes de puissance, confirmant la viabilité de l'architecture pour les futurs véhicules électriques.



---

### **Capgemini - Hybrid Intelligence | 2024–2026**
**Rôle : Architecte IA / Lead Tech IA**

#### **Projet : Gouvernance IA**
* **Enjeu :** Fiabiliser le suivi du ROI pour les projets IA *On-premise*.
* **Contraintes :** Isolation réseau, sécurité interne, interopérabilité BI.
* **Stratégie :** Arbitrage pour une architecture "Small Data" (**DuckDB/Datasette**) vs Data Warehouse pour réduire la dette technique.
* **Exécution :** Automatisation via **Mage-ai**, agents de contrôle **PydanticAI**.
* **Impact :** Automatisation totale du reporting, gain de 15% de temps de traitement hebdomadaire et fiabilisation des KPIs métier.

#### **Projet : Inspection moteur 2D-3D (Safran)**
* **Enjeu :** Fiabiliser la détection de dommages sur les aubes de turboréacteurs.
* **Contraintes :** Certification aéronautique, précision millimétrique, quantification d'incertitude.
* **Stratégie :** Pipeline hybride (**trimesh/Deep Learning**) ; intégration **MAPIE** pour quantifier l'incertitude vs "boîte noire".
* **Exécution :** Optimisation **CUDA/PyTorch3D**, interface **Marimo**, mentorat technique.
* **Impact :** Réduction de 10% des faux positifs et accélération de 15% du cycle d'analyse des pièces critiques.

#### **Projet : Industrialisation logicielle (AI Factory)**
* **Enjeu :** Automatiser la génération de code conforme (SOLID/TDD) en milieu contraint.
* **Contraintes :** Souveraineté numérique, sécurité (SOC2), maintenabilité.
* **Stratégie :** Approche "Build" locale vs SaaS externe pour garantir l'intégrité des données.
* **Exécution :** Assistance **Roo-code** (vLLM, Kubernetes), évaluation (**Arize Phoenix/DeepEval**).
* **Impact :** Industrialisation d'une chaîne de production garantissant 100% de conformité aux standards de sécurité internes.

#### **Projet : Graph Factory (Airbus)**
* **Enjeu :** Harmoniser les configurations (xBOM/mBOM) pour réduire les délais d'analyse d'impact.
* **Contraintes :** Volumétrie (10M), traçabilité, interopérabilité ERP.
* **Stratégie :** Modèle hybride (**ArangoDB**) : structure en graphe pour modéliser nativement les dépendances vs relationnel rigide.
* **Exécution :** Pipeline **Polars**, requêtes AQL, API **FastAPI**, transfert de compétence.
* **Impact :** Mise en service de la *Graph factory*, automatisation du calcul des "delta" et réduction de 20% du temps d'analyse d'impact.

#### **Projet : Monitoring environnemental (Liebherr Aerospace)**
* **Enjeu :** Monitoring qualité air cabine compatible embarqué aéronautique (nez électronique).
* **Contraintes :** Ressources limitées, latence temps réel, stabilité opérationnelle.
* **Stratégie :** Modèles interprétables (**LGBoost**) : priorité à l'efficacité mémoire vs Deep Learning complexe.
* **Exécution :** Séries temporelles (**Pandas/NumPy**), classifieur d'anomalies, tests en vol.
* **Impact :** Validation technique, réduction de 10% de la latence de traitement, base prête pour l'intégration.

#### **Projet : Aide à la décision stratégique (THALES)**
* **Enjeu :** Optimiser l'efficacité logistique en environnement Défense.
* **Contraintes :** Sécurité, allocation sous contraintes, infrastructure souveraine.
* **Stratégie :** Architecture hybride : couplage maintenance prédictive (**LGBoost**) et recherche opérationnelle pour respecter les limites logistiques.
* **Exécution :** Moteur de recommandation (**ORTool**), DevOps, mentorat technique.
* **Impact :** Réactivité logistique accrue de 15% et gain de 10% sur l'efficacité d'allocation des ressources.

#### **Projet : Rapport imagerie satellite (THALES)**
* **Enjeu :** Automatiser la production de rapports d'intelligence multimodaux.
* **Contraintes :** Interprétation contextuelle, sécurité, reproductibilité.
* **Stratégie :** Architecture **RAG/ReAct** : couplage **Vision Transformers** et **LLM** pour synthèse structurée.
* **Exécution :** **Gitlab CI/CD**, pipeline multimodal (**LangChain**).
* **Impact :** Réduction de 20% du temps de traitement opérationnel, capacité d'exploitation augmentée de 15%.

---

### **Capgemini Engineering (APA) | 2022–2024**
**Rôle : Responsable Projets - Ingénieur-chercheur DATA/IA**

#### **Projet : Transition véhicule électrique**
* **Enjeu :** Orchestrer la transformation des architectures de gestion énergétique.
* **Contraintes :** Standards ISO, synchronisation avec le *Time-to-Market*.
* **Stratégie :** Cadres (**TOGAF, IAF**) ; priorisation par analyse de valeur (**VRIO, TRL**) pour optimiser le ROI R&D.
* **Exécution :** Pilotage équipe transverse (R&D, IA), industrialisation des processus.
* **Impact :** Sécurisation de la roadmap propulsion et amélioration de 12% du cycle de développement.

#### **Projet : Diagnostic calculateurs (Renault / Stellantis / Norauto)**
* **Enjeu :** Génération de rapport de diagnostique via bus CAN et LLM.
* **Contraintes :** Confidentialité, inférence locale, flux temps réel.
* **Stratégie :** IA souveraine (**Ollama/Phi3**) pour l'étanchéité des données.
* **Exécution :** Pipeline hybride (décodage **DBC** + **RAG**), interface **FastAPI**.
* **Impact :** Démonstrateur validé, réduction de 12% du temps de détection des pannes.

#### **Projet : Refroidissement batterie (RL)**
* **Enjeu :** Remplacer le contrôle déterministe par une approche prédictive adaptative.
* **Contraintes :** Dynamiques non-linéaires, fiabilité automobile.
* **Stratégie :** **Apprentissage par Renforcement (RL)** pour régulation robuste.
* **Exécution :** Simulateur (**Gymnasium**), chaîne (**StableBaselines3**), traçabilité (**MLFlow**).
* **Impact :** Réduction de 8% de la consommation énergétique du refroidissement.

#### **Projet : Jumeau numérique thermique**
* **Enjeu :** Régulation thermique prédictive certifiable ISO 26262.
* **Contraintes :** Latence < 10 ms, souveraineté totale.
* **Stratégie :** Jumeau hybride (**acados** pour la physique + simulation boucle fermée).
* **Exécution :** Stack (**python-can, FastAPI**), simulation **HIL**.
* **Impact :** Réduction de la latence par 3, validation de la chaîne de contrôle dynamique.

#### **Projet : Pont de commande hybride IA**
* **Enjeu :** Intégration IA dans la chaîne de commande des systèmes batterie.
* **Contraintes :** Interopérabilité NPU/microcontrôleur, puissance haute tension.
* **Stratégie :** Découplage physique commande/puissance pour garantir la sécurité.
* **Exécution :** Architecture hybride, banc de test **HIL** en conditions extrêmes.
* **Impact :** Preuve de concept validant la viabilité de l'architecture pour les VE.