# Test de robustesse ?

[<img src="img/step8.png" alt="hobbiton" width="800">](https://www.youtube.com/watch?v=NFBXilomkPk)
> "Oh... you would not part an old man from his walking stick?", Gandalf, LOTR - The Two Towers

## 🎯 Objectifs de cette étape

- Comprendre l'importance des tests de robustesse pour la sécurité des modèles d'IA.
- Identifier les principales menaces adversariales (empoisonnement, évasion) et leurs impacts.
- Découvrir les méthodes courantes pour tester la robustesse des modèles.
- Explorer l'intégration des tests de robustesse dans le cycle de vie de l'IA (MLOps, CI/CD, red teaming).
- Comparer les outils Garak et PyRIT pour le red teaming et la robustesse des LLM.


## Sommaire

- [Introduction](#introduction)
- [Objectif principal](#objectif-principal)


- [Contexte des Attaques ciblées](#contexte-des-attaques-ciblées)
- [Méthodes](#méthodes)
- [Intégration dans le Cycle de Vie de l'IA](#intégration-dans-le-cycle-de-vie-de-lia)


- [AI Red Teaming: Garak vs PyRIT](#ai-red-teaming-garak-vs-pyrit)
  - [Garak](#garak)
  - [PyRIT](#pyrit)
  - [Tableau comparatif](#tableau-comparatif)
  


- [Étape suivante](#étape-suivante)
- [Ressources](#ressources)


## Introduction

Les **tests de robustesse**, également appelés **tests adversariaux**, représentent un élément clé de la sécurité des systèmes 
d’intelligence artificielle (IA) et d’apprentissage automatique (ML). Ils visent avant tout **à mesurer la capacité d’un 
modèle à rester fiable et performant** lorsqu’il est confronté à des données volontairement conçues pour l’induire en 
erreur ou le manipuler.


## Objectif principal

L'objectif principal des tests de robustesse ont pour but d’évaluer la capacité d’un modèle à préserver ses 
performances et son intégrité face à des entrées malveillantes ou altérées de manière subtile. Ils cherchent à s’assurer
que le modèle conserve un comportement conforme aux attentes et ne génère pas de résultats erronés ou potentiellement
dangereux lorsqu’il est soumis à des attaques.

## Contexte des Attaques ciblées

Ces tests sont cruciaux pour se défendre contre deux catégories principales d'attaques adversariales :

- **Attaques par Empoisonnement des Données (Poisoning Attacks)** Ces attaques ciblent la phase d'entraînement du 
modèle. Les adversaires manipulent subtilement les données d'entraînement pour compromettre le processus d'apprentissage
et influencer malicieusement les résultats du modèle lors de l'inférence. Les tests de robustesse évaluent la 
susceptibilité d'un modèle aux backdoors (portes dérobées) insérées via l'empoisonnement et peuvent aider à détecter 
la présence de données altérées.


- **Attaques par Évasion (Evasion Attacks)**: Ces attaques se produisent pendant la phase d'inférence sur un modèle 
déjà entraîné. Les attaquants créent des "exemples adversariaux" – des entrées qui ont été légèrement modifiées 
(souvent de manière imperceptible pour un humain) – pour provoquer une classification incorrecte par le modèle. 
Les tests de robustesse vérifient la capacité du modèle à résister à ces tentatives de manipulation.

## Méthodes

Quelques apparoches courantes pour réaliser des tests de robustesse incluent :

- **Tests personnalisés** : Ils sont développés pour évaluer la défense contre des types spécifiques d'attaques
par empoisonnement.

- **Enregistrements "Canary"** : Une méthode simple pour détecter l'empoisonnement des données, consistant à inclure 
une petite sélection d'enregistrements clairement identifiables. Si ces enregistrements sont mal classifiés, cela peut 
signaler un empoisonnement. Cependant, cette méthode ne détecte pas les backdoors.

- **Entraînement Adversarial** : Cette technique consiste à fortifier le modèle en incorporant des exemples 
adversariaux (normaux et malveillants) dans son jeu de données d'entraînement. L'objectif est d'enseigner au 
modèle à identifier et à neutraliser de manière autonome les entrées nuisibles.


## Intégration dans le Cycle de Vie de l'IA
Les tests de robustesse sont des activités clés dans la sécurité de l'IA et sont intégrés à plusieurs niveaux :

- **MLOps et pipelines CI/CD** : Ils sont de plus en plus intégrés dans les pipelines MLOps et CI/CD pour automatiser 
l'évaluation des modèles, en particulier après le fine-tuning ou la mise à jour.

- **Évaluation des modèles tiers** : Lors de l'acquisition de modèles pré-entraînés, ces tests sont essentiels pour é
valuer leur intégrité et détecter d'éventuels empoisonnements ou altérations.

- **Red Teaming** : Les tests de robustesse sont une composante fondamentale du "red teaming" en IA, une approche 
offensive qui simule des cyberattaques pour identifier de manière proactive les vulnérabilités avant le déploiement 
du modèle.

- **Benchmarking** : Ils complètent les benchmarks de sécurité et d'éthique pour les LLM (comme DecodingTrust) en 
fournissant une évaluation spécifique de la résistance aux attaques.

## AI Red Teaming: Garak vs PyRIT
Deux outils open source populaires pour effectuer des tests de robustesse sur les modèles d'IA générative 
sont **Garak** et **PyRIT**.

**Garak** repose sur une bibliothèque d’attaques déjà connues qu’il lance pour tester, tandis que **PyRIT** permet de 
personnaliser, chaîner et automatiser des scénarios d’attaque complexes selon la politique de sécurité souhaitée.

### Garak

**Garak** est un framework développé par **NVIDIA**, pour mener des tests adversariaux sur les modèles de langage (LLM). 
En quelques points:

- Il génère automatiquement des entrées piégeuses (prompts adversariaux) pour détecter les vulnérabilités, comme 
la propagation de contenus biaisés, dangereux ou mensongers.

- Il est muni d’une bibliothèque très large d’attaques connues, dont des jail-breaks, fuites, contournements de filtres
et plusieurs variantes.

- Garak se concentre principalement sur les attaques "one-shot" et l’analyse statique, en documentant explicitement 
chaque prompt et résultat.

### PyRIT

**PyRIT (Python Risk Identification Tool)** est aussi un outil open source, développé par **Microsoft**, spécialisé dans 
l’automatisation du « red teaming » pour tester la sécurité des modèles génératifs d’IA.
En quelques points:

- Il permet de créer et personnaliser des séquences d’attaques selon des politiques ou des scénarios de risque 
spécifiques, avec une architecture modulaire qui s’adapte à différents contextes et risques.

- PyRIT facilite les tests structurés, le chainage d’étapes et la simulation de comportements d’attaque complexes et 
longs, contrairement à Garak qui attaque principalement en "one-shot"

### Tableau comparatif

| Outil  | Approche principale                |  Atouts            |  Personnalisation    | Focus technique                              |                     
|--------|------------------------------------|--------------------|----------------------|----------------------------------------------|
| Garak  | Bibliothèque d’attaques            |  Large couverture  |  Limité              | Attaques one-shot, analyse statique          |    
| PyRIT  | Génération par scénarios/policy    |  Attaques ciblées  |  Élevée (templates)  | Séquences d’attaques, architecture modulaire |


## Étape suivante
- [Étape 9](step_9.md)

## Ressources


| Information                                                                                    | Lien                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Promptfoo vs Deepteam vs PyRIT vs Garak: The Ultimate Red Teaming Showdown for LLMs            | [https://dev.to/ayush7614/promptfoo-vs-deepteam-vs-pyrit-vs-garak-the-ultimate-red-teaming-showdown-for-llms-48if](https://dev.to/ayush7614/promptfoo-vs-deepteam-vs-pyrit-vs-garak-the-ultimate-red-teaming-showdown-for-llms-48if) |
| AI Security in Action: Applying NVIDIA’s Garak to LLMs on Databricks                           | [https://www.databricks.com/blog/ai-security-action-applying-nvidias-garak-llms-databricks](https://www.databricks.com/blog/ai-security-action-applying-nvidias-garak-llms-databricks)                                               |
| Garak: A Framework for Security Probing Large Language Models                                  | [https://arxiv.org/abs/2407.13499](https://arxiv.org/abs/2407.13499)                                                                                                                                                                 |
| PyRIT: Framework for Security Risk Identification and Red Teaming in Generative AI System      | [https://arxiv.org/abs/2407.13498](https://arxiv.org/abs/2407.13498)                                                                                                                                                                 |
| AI’s Achilles’ Heel: Identifying and Securing Against Hidden Risks                             | [https://techstrong.ai/building-with-ai/ais-achilles-heel-identifying-and-securing-against-hidden-risks/](https://techstrong.ai/building-with-ai/ais-achilles-heel-identifying-and-securing-against-hidden-risks/)                   |                                                              | [
| Insights and Current Gaps in Open-Source LLM Vulnerability Scanners: A Comparative Analysis    | [https://arxiv.org/abs/2410.16527](https://arxiv.org/abs/2410.16527)                                                                                                                                                                 |                                                                                                                                                                | [
