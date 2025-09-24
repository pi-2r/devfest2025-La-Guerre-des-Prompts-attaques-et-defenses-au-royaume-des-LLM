# Garak: An LLM vulnerability scanner

[<img src="img/minas_tirith_tree_burning.jpg" alt="minas_tirith_burning" width="800" >](https://www.youtube.com/watch?v=yFBrm5YH9-8)
> "A white tree in a courtyard of stone.. It was dead.. The city was burning.", Pippin, LOTR - The Return of the King

## 🎯 Objectifs de cette étape

- Présentation de garak.
- Mettre en pratique ces techniques sur ce Playground de Microsoft : [AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs).

## Sommaire


- [Garak](#présentation-de-garak)

    - [Présentation de Garak](#présentation-de-garak)


## Garak

Garak est un outil open-source développé par NVIDIA pour scanner les vulnérabilités des modèles de langage (LLM).
Il est conçu pour identifier les failles de sécurité potentielles dans les systèmes utilisant les LLMs.

### Présentation de Garak

**Garak** se fonde sur une base de connaissances de jailbreaks prompts connus et constamment mis à jour par la communauté.
Garak permet de faire un scanning automatisé des LLM en utilisant un certain nombre de sondes (probes).
