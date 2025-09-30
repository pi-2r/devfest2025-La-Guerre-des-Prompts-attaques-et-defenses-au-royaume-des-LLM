# Garak: An LLM vulnerability scanner

[<img src="img/minas_tirith_tree_burning.jpg" alt="minas_tirith_burning" width="800" >](https://www.youtube.com/watch?v=yFBrm5YH9-8)
> "A white tree in a courtyard of stone.. It was dead.. The city was burning.", Pippin, LOTR - The Return of the King

## 🎯 Objectifs de cette étape

- Présentation de garak.
- Mettre en pratique ces techniques sur ce Playground de Microsoft : [AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs).

## Sommaire


- [Garak](#présentation-de-garak)

    - [Présentation de Garak](#présentation-de-garak)
    - [Les generators](#les-generators)

- [Mise en pratique de Garak](#mise-en-pratique-de-garak)


## Garak

Garak est un outil open-source développé par NVIDIA pour scanner les vulnérabilités des modèles de langage (LLM).
Il est conçu pour identifier les failles de sécurité potentielles dans les systèmes utilisant les LLMs.

### Présentation de Garak

**Garak** se fonde sur une base de connaissances de jailbreaks prompts connus et constamment mis à jour par la communauté.
Garak permet de faire un scanning automatisé des LLM en utilisant un certain nombre de sondes (probes).
Vous pouvez voir la liste des probes disponibles en exécutant la commande suivante :

```bash

python -m garak --list_probes
```

Certaines probes sont suivies de symboles 🌟 ou 💤 comme ceci :
```plaintext
probes: divergence 🌟
probes: divergence.Repeat
probes: divergence.RepeatExtended 💤
```
En fait, il existe plusieurs variantes de probes pour un même jailbreak prompt.
Ces symboles ont la signification suivante :
- 🌟 : indique qu'on passe à un nouveau module de jailbreak ici `divergence`.
- 💤 : indique que la probe `divergence.RepeatExtended` est inactive par défaut, car son lancement serait long. C'est la version `divergence.Repeat` qui sera lancée en cas de scan automatique.

Pour lancer un scan automatique d'un module en particulier comme `divergence`, il suffit d'exécuter la commande suivante :
```bash

python -m garak --model_type huggingface --model_name gpt2 --probes divergence
```

Pour lancer une probe inactive comme `divergence.RepeatExtended`, il suffit d'exécuter la commande suivante :
```bash

python -m garak --model_type huggingface --model_name gpt2  --probes divergence.RepeatExtended
```

### Les generators

Les generators sont des abstractions (LLMs, APIs, fonction Python) répondant un texte en fonction d'un input.
Les generators prennent les valeurs, dont :
- `huggingface` : pour les modèles hébergés sur HuggingFace.
- `openai` : pour les modèles OpenAI.
- `function` : pour les fonctions Python.

Par exemple, si on souhaite évaluer un modèle `gpt2` de `Huggingface` lors d'un scan, on renseigne les options : `--model_type huggingface --model_name gpt2`.
Si c'est une API d'HuggingFace, on renseigne les options : `--model_name huggingface.InferenceAPI --model_type "mosaicml/mpt-7b-instruct"`.

Pour plus de détails, vous pouvez consulter la documentation officielle de Garak : [Garak Documentation](https://docs.garak.ai/garak/garak-components/using-generators)

### Les detectors et les Harnesses

Comme, une probe va être lancée plusieurs fois pour tester la robustesse du LLM et que l'on teste plusieurs probes, Garak utilise des detectors pour reconnaitre si la réponse du LLM défaillante.
Ce sont des détecteurs de mots-clés ou des classifiers jugeant si la réponse d'un LLM est OK ou non.

Les Harnesses désignent quel détector est utilisé avec quelle probe. Les Harnesses prennent la valeur : `probewise` si on utilise les détectors récommandés à la probe ou `pxd` pour tester tous les détecteurs.


## Mise en pratique de Garak

