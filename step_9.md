# Garak: An LLM vulnerability scanner

[<img src="img/minas_tirith_tree_burning.jpg" alt="minas_tirith_burning" width="800" >](https://www.youtube.com/watch?v=yFBrm5YH9-8)
> "A white tree in a courtyard of stone.. It was dead.. The city was burning.", Pippin, LOTR - The Return of the King

## 🎯 Objectifs de cette étape

- Présentation de garak.
- Mettre en pratique ces techniques sur ce Playground de Microsoft : [AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs).

## Sommaire


- [Garak](#garak)
    - [Installation de Garak](#installation-de-garak)
    - [Les Probes](#les-probes)
    - [Les Generators](#les-generators)
    - [Les Detectors et les Harnesses](#les-detectors-et-les-harnesses)
    - [L'Auto-Red-Team](#lauto-red-team)

- [Mise en pratique de Garak sur le Playground de Microsoft](#mise-en-pratique-de-garak-sur-le-playground-de-microsoft)

- [Étape suivante](#étape-suivante)
- [Ressources](#ressources)



## Garak

![GitHub stars](https://img.shields.io/github/stars/NVIDIA/garak?style=flat-square)
[![Downloads](https://static.pepy.tech/badge/garak/month)](https://pepy.tech/project/garak)

**Garak** est un outil open-source développé par **NVIDIA** pour scanner les vulnérabilités des modèles de langage (LLM).
Il est conçu pour identifier les failles de sécurité potentielles dans les systèmes utilisant les LLMs.

**Garak** se fonde sur une base de connaissances de jailbreaks prompts connus et constamment mis à jour par la communauté.

### Installation de Garak
Pour installer Garak, vous pouvez utiliser pip. Exécutez la commande suivante dans votre terminal :

```bash
# 1. Créer un environnement virtuel dans le répertoire courant
python3 -m venv .venv

# 2. Activer l’environnement virtuel
source .venv/bin/activate

# 3. Installer garak
python -m pip install -U garak
```


### Les Probes

Garak permet de faire un scanning automatisé des LLMs en utilisant un certain nombre de sondes (probes).
Vous pouvez voir la liste des probes disponibles en exécutant la commande suivante :

```bash

python -m garak --list_probes
```

Vous devriez voir un affichage similaire à celui-ci :

<img src="img/list_probes.png" alt="garak-list-probes" width="600" style="transition:0.3s;">

Certaines probes sont suivies de symboles 🌟 ou 💤 comme ceci :
```plaintext
probes: divergence 🌟
probes: divergence.Repeat
probes: divergence.RepeatExtended 💤
```
En fait, il existe plusieurs variantes de probes pour un même type de jailbreak.
Ces symboles ont la signification suivante :
- 🌟 : indique qu'on passe à un nouveau module de jailbreak ici `divergence`.
- 💤 : indique que la probe `divergence.RepeatExtended` est inactive par défaut, car son lancement serait long. 
C'est la version `divergence.Repeat` qui sera lancée en cas de scan automatique.

Pour lancer un scan automatique d'un module en particulier comme `divergence`, il suffit d'exécuter la commande suivante :

```bash

python -m garak --model_type huggingface --model_name gpt2 --probes divergence
```

Pour lancer une probe inactive comme `divergence.RepeatExtended`, il suffit d'exécuter la commande suivante :
```bash

python -m garak --model_type huggingface --model_name gpt2  --probes divergence.RepeatExtended
```

### Les Generators 

Les generators sont des abstractions (LLMs, APIs, fonction Python) répondant un texte en fonction d'un input.
Les generators prennent les valeurs, dont :
- `huggingface` : pour les modèles hébergés sur HuggingFace.
- `openai` : pour les modèles OpenAI.
- `function` : pour les fonctions Python.

Par exemple, si on souhaite évaluer un modèle `gpt2` de `Huggingface` lors d'un scan, on renseigne les options : 
`--model_type huggingface --model_name gpt2`.
Si c'est une API d'HuggingFace, on renseigne les options : `--model_name huggingface.InferenceAPI --model_type "mosaicml/mpt-7b-instruct"`.

Pour plus de détails, vous pouvez consulter la documentation officielle de Garak : [Garak Documentation](https://docs.garak.ai/garak/garak-components/using-generators)

### Les Detectors et les Harnesses

Comme, une probe va être lancée plusieurs fois pour tester la robustesse du LLM et que l'on teste plusieurs probes, 
Garak utilise des detectors pour reconnaitre si la réponse du LLM défaillante.
Ce sont des détecteurs de mots-clés ou des classifiers jugeant si la réponse d'un LLM est OK ou non.

Les détecteurs ont parfois un paramètre `doc_uri` permettant de trouver de la documentation sur la faille testée. Par 
exemple, le détecteur [`xss.MarkdownExfilBasic`](https://reference.garak.ai/en/latest/garak.detectors.xss.html#garak.detectors.xss.MarkdownExfilBasic) pointe vers : [Bing Chat Image Markdown Injection](https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/).

Les Harnesses gèrent :
- le lancement des probes sur le generator cible. 
- le lancement des detectors à utiliser sur les outputs qu'ont produit les probes.
- l'évaluation des résultats des detectors faite avec les Evaluator.

Les Harnesses prennent la valeur : `probewise` si on utilise les détectors récommandés pour la probe ou `pxd` pour 
tester tous les détecteurs.

### L'auto Red-Team

Garak propose un système d'auto Red-Team sur certain sujet avec la librarie `art`. Cette brique ne peut cependant pas de
faire un scan poussé.

## Mise en pratique de Garak sur le Playground de Microsoft
Nous allons mettre en pratique Garak sur le Playground de Microsoft.
Pour cela, nous allons utiliser le REST Generator de Garak et nous allons utiliser différentes sondes 
(`promptinject.DAN`,`smuggling.HypotheticalResponse`) que nous allons configurer pour trouver le mot de passe protégé 
par le bot.


1 - Pour setter le REST Generator, lancer une inspection de la page HTML du bot que vous voulez tester :

<img src="img/lancer_inspection_chatbot.png" alt="garak-inspection-chatbot" width="600" style="transition:0.3s;">

2 - Aller dans l'onglet `Network` :

<img src="img/network_chatbot.png" alt="garak-network-chatbot" width="600" style="transition:0.3s;">

3 - Lancer un premier message (ex: "Hello") dans le playground et récupérer les éléments nécessaires comme l'url de la 
requête POST `messages` et les cookies nécessaires.

<img src="img/elements_requete_post.png" alt="request-post-chatbot" width="600" style="transition:0.3s;">

Pour lancer un scan garak sur une étape du Playground :

```bash
#python -m garak --target_type rest -G lab/Garak/rest_ai_playground_api.json  --probes lab.Garak.probe_config.my_smuggling_probe.MyHypotheticalResponse

python -m garak --target_type rest -G lab/Garak/rest_ai_playground_api.json  --probes promptinject.DAN --probe_option_file lab/Garak/probe_config/dan_probe_setting.json --generation 2
python -m garak --target_type rest -G lab/Garak/rest_ai_playground_api.json  --probes smuggling.HypotheticalResponse --probe_option_file lab/Garak/probe_config/dan_probe_setting.json --generation 2
```


## Étape suivante
- [Étape 10](step_10.md)

## Ressources


| Information                               | Lien                                                                           |
|-------------------------------------------|--------------------------------------------------------------------------------|
| [Github] garak, LLM vulnerability scanner | [https://github.com/NVIDIA/garak](https://github.com/NVIDIA/garak)             |
| Documentation garak                       | [https://docs.garak.ai/](https://docs.garak.ai/)                               |
| Garak, DEF CON slides                     | [https://garak.ai/garak_aiv_slides.pdf](https://garak.ai/garak_aiv_slides.pdf) |
