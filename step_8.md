# Test de Robustesse ?

[<img src="img/step8.png" alt="hobbiton" width="800">](https://www.youtube.com/watch?v=NFBXilomkPk)
> "Oh... you would not part an old man from his walking stick?", Gandalf, LOTR - The Two Towers

## 🎯 Objectifs de cette étape

- Todo


## Sommaire

- [Introduction](#introduction)
- [Objectif principal](#objectif-principal)

- [Contexte des Attaques ciblées](#contexte-des-attaques-ciblées)

- [Garak vs PyRIT](#garak-vs-pyrit)
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

Ces tests sont cruciaux pour se défendre contre deux catégories principales d'attaques adversariales:
- **Attaques par Empoisonnement des Données (Poisoning Attacks)**
- **Attaques par Évasion (Evasion Attacks)**
- 

## Garak vs PyRIT
Deux outils open source populaires pour effectuer des tests de robustesse sur les modèles d'IA générative 
sont **Garak** et **PyRIT**.

**Garak** repose sur une bibliothèque d’attaques déjà connues qu’il lance pour tester, tandis que **PyRIT** permet de 
personnaliser, chaîner et automatiser des scénarios d’attaque complexes selon la politique de sécurité souhaitée.



## Étape suivante
- [Étape 9](step_9.md)

## Ressources


| Information                                                                               | Lien                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Promptfoo vs Deepteam vs PyRIT vs Garak: The Ultimate Red Teaming Showdown for LLMs       | [https://dev.to/ayush7614/promptfoo-vs-deepteam-vs-pyrit-vs-garak-the-ultimate-red-teaming-showdown-for-llms-48if](https://dev.to/ayush7614/promptfoo-vs-deepteam-vs-pyrit-vs-garak-the-ultimate-red-teaming-showdown-for-llms-48if) |
| AI Security in Action: Applying NVIDIA’s Garak to LLMs on Databricks                      | [https://www.databricks.com/blog/ai-security-action-applying-nvidias-garak-llms-databricks](https://www.databricks.com/blog/ai-security-action-applying-nvidias-garak-llms-databricks)                                               |
| Garak: A Framework for Security Probing Large Language Models                             | [https://arxiv.org/abs/2407.13499](https://arxiv.org/abs/2407.13499)                                                                                                                                                                 |
| PyRIT: Framework for Security Risk Identification and Red Teaming in Generative AI System | [https://arxiv.org/abs/2407.13498](https://arxiv.org/abs/2407.13498)                                                                                                                                                                 |
