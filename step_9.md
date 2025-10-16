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
    - [Initialisation du REST Generator](#initialisation-du-rest-generator)
    - [Initialisation d'une sonde custom Garak](#initialisation-dune-sonde-custom-garak)

- [Étape suivante](#étape-suivante)
- [Ressources](#ressources)



## Garak

![GitHub stars](https://img.shields.io/github/stars/NVIDIA/garak?style=flat-square)
[![Downloads](https://static.pepy.tech/badge/garak/month)](https://pepy.tech/project/garak)

**Garak** est un outil open-source développé par **NVIDIA** pour scanner les vulnérabilités des modèles de langage (LLM).
**Garak** se fonde sur une base de connaissances de jailbreaks et de variantes connus et constamment mis à jour par la communauté.

Lors d'un audit, **Garak** lance des attaques prédéfinies, non-adaptatives, et sauvegarde les résultats sous format JSON et HTML.

La recommandation est d'utiliser **Garak** périodiquement ou avant une mise à jour majeure d'une application (changement de LLM,...) pour dresser un état des lieux des principales vulnérabilités auxquelles votre application est sensible.
On peut ensuite mettre en place des guardrails plus spécifiques avec **NEMO Guardrails** (cf. [étape 13](step_13.md))).

### Installation de Garak
Pour installer Garak, vous pouvez utiliser pip. Exécutez la commande suivante dans votre terminal :

```bash
# 1. Créer un environnement virtuel a la racine du repo
# cd devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM
python3 -m venv .venv

# 2. Activer l’environnement virtuel
source .venv/bin/activate

# 3. Installer garak
python -m pip install -U garak==0.13.1
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

# Commande mise en illustration, ne pas la lancer
python -m garak --model_type huggingface --model_name gpt2 --probes divergence
```

Pour lancer une probe inactive comme `divergence.RepeatExtended`, il suffit d'exécuter la commande suivante :
```bash

# Commande mise en illustration, ne pas la lancer
python -m garak --model_type huggingface --model_name gpt2  --probes divergence.RepeatExtended
```

### Les Generators 

Les generators sont des abstractions (LLMs, APIs, fonction Python) répondant un texte en fonction d'un input.
Les generators prennent des valeurs, dont :
- `huggingface` : pour les modèles hébergés sur HuggingFace.
- `openai` : pour les modèles OpenAI.
- `function` : pour les fonctions Python.

Par exemple, si on souhaite évaluer un modèle `gpt2` de `Huggingface` lors d'un scan, on renseigne les options : 
`--model_type huggingface --model_name gpt2`.
Si c'est une API d'HuggingFace, on renseigne les options : `--model_name huggingface.InferenceAPI --model_type "mosaicml/mpt-7b-instruct"`.

Pour plus de détails, vous pouvez consulter la documentation officielle de Garak : [Garak Documentation](https://docs.garak.ai/garak/garak-components/using-generators).

### Les Detectors et les Harnesses

Comme, une probe va être lancée plusieurs fois pour tester la robustesse du LLM et que l'on teste plusieurs probes, 
Garak utilise des detectors pour reconnaitre si la réponse du LLM défaillante.
Ce sont des détecteurs de mots-clés ou des classifiers jugeant si la réponse d'un LLM est OK ou non selon l'objectif de la probe.

Les détecteurs ont parfois un paramètre `doc_uri` permettant de trouver de la documentation sur la faille testée. Par 
exemple, le détecteur [`xss.MarkdownExfilBasic`](https://reference.garak.ai/en/latest/garak.detectors.xss.html#garak.detectors.xss.MarkdownExfilBasic) pointe vers : [Bing Chat Image Markdown Injection](https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/).

Les Harnesses gèrent :
- le lancement des probes sur le generator cible. 
- le lancement des detectors à utiliser sur les outputs produits par le generator selon les probes.
- les évaluations des résultats des detectors faites avec les evaluators.

Les Harnesses prennent la valeur : `probewise` si on utilise les détectors récommandés pour la probe ou `pxd` pour 
tester tous les détecteurs.

### L'auto Red-Team

Garak propose un système d'auto Red-Team sur certain sujet avec la librarie `art`. Cette brique ne peut cependant pas de
faire un scan poussé.

## Mise en pratique de Garak sur le Playground de Microsoft
Nous allons mettre en pratique Garak sur le Playground de Microsoft.

### Initialisation du REST Generator

Pour cela, nous allons utiliser le REST Generator de Garak et nous allons utiliser des variantes des sondes 
(`smuggling.HypotheticalResponse` et `promptinject.DAN`) que nous allons configurer pour trouver le mot de passe protégé 
par le bot (la modification de `promptinject.DAN` est laissée en exercice).


1 - Pour setter le REST Generator, lancer une inspection de la page HTML du bot que vous voulez tester :
<br/>
<img src="img/lancer_inspection_chatbot.png" alt="garak-inspection-chatbot" width="600" style="transition:0.3s;">
<br/>
<br/>
2 - Aller dans l'onglet `Network` :
<br/>
<img src="img/network_chatbot.png" alt="garak-network-chatbot" width="600" style="transition:0.3s;">
<br/>
<br/>
3 - Lancer un premier message (ex: "Hello") dans le playground et récupérer les éléments nécessaires comme l'url de la 
requête POST `messages` et les cookies.
<br/>
<img src="img/elements_requete_post.png" alt="request-post-chatbot" width="600" style="transition:0.3s;">

### Initialisation d'une sonde custom Garak

Pour lancer le scan d'une sonde custom sur une étape du Playground :
<br/>
<br/>
1 - Copier le fichier `my_probe.py` qui contient un exemple de sonde custom `my_probe.MyHypotheticalResponse` pour le playground dans le répertoire `probes` de la librairie garak que vous utilisez (dans votre `.venv`).
<br/>
<img src="img/ajout_probe_custom_garak.png" alt="ajout_probe_custom_garak" width="200" style="transition:0.3s;">
<br/>
<br/>
2 - Copier aussi le fichier `my_custom_detection.py` qui contient un detector custom `my_custom_detection.MyPasswordByPass` pour le playground dans le répertoire `detectors` de la librairie garak que vous utilisez (dans votre venv). Le detector custom `my_custom_detection.MyPasswordByPass` détecte si un des mots de passe qui doit être protégé a fuité dans la réponse du chatbot.
<br/>
```bash
# Depuis la racine du repo vers votre .venv
cp lab/Garak_test/my_custom_detection.py .venv/lib/python*/site-packages/garak/detectors/
cp lab/Garak_test/my_probe.py  .venv/lib/python*/site-packages/garak/probes  
```
<br/>
3 - Lancer les commande listant les detectors et probes disponibles pour voir si nos detectors et probes custom sont apparus :
<br/>

```bash

python -m garak --list_detectors
python -m garak --list_probes
```
<br/>
3 - Si oui, lancer la commande suivante pour tester la vulnérabilité du chatbot. Sinon, assurez-vous que le fichier sonde est copié au bon endroit :
<br/>

```bash

# Commande type, à adapter selon la sonde et le chemin du fichier JSON. Le JSON rest_ai_playground_api.json est lui aussi à adapter.
python -m garak --target_type rest -G path/to/rest_ai_playground_api.json  --probes my_probe.MyHypotheticalResponse
```

### Mise en pratique sur le chatbot 2 du Playground de Microsoft

1 - setter le `rest_ai_playground_api.json` pour requêter le chatbot 2.

2 - Lancer la commande suivante pour tester la vulnérabilité du chatbot 2 avec la sonde custom `my_probe.MyHypotheticalResponse`. Garak lance directement les prompts en ligne de commandes et les réponses du chatbot sont affichées dans l'interface web.

*PS : n'hésitez pas à relancer une nouvelle conversation dans le playground entre chaque scan pour réinitialiser le contexte.*

<img src="img/jailbreak_by_custom_probe_chatbot_2.png" alt="garak-jailbreak-chatbot-2" width="600" style="transition:0.3s;">

###### résultat obtenus lors du jailbreak réussi du chatbot 2 avec la sonde custom my_probe.MyHypotheticalResponse

3 - Une fois un scan ayant mené à un jailbreak réussi, vous pouvez retrouver le rapport HTML dans le répertoire indiqué dans le log de Garak. Si toutes les attempts de jailbreak ont réussi, le rapport HTML ne indiquera un score de 0% de succès d'interceptio (cf ci-dessous).

<img src="img/garak_report_on_successful_jailbreak_attempts.png" alt="garak-successful-jailbreak-chatbot-2-report" width="600" style="transition:0.3s;">

Vous pouvez aussi tenter un scan sur le niveau supérieur du chatbot 2 : le chatbot 8 et modifier la sonde custom ou bien en tenter d'autres (une grandma ou un DAN custom).

<img src="img/jailbreak_failed_by_custom_probe_chatbot_8.png" alt="jailbreak-failed-chatbot-9" width="600" style="transition:0.3s;">

###### résultat obtenus lors d'une tentative de jailbreak du chatbot 8 avec la même sonde custom my_probe.MyHypotheticalResponse

Ici le rapport de Garak indique un taux de succès de 100% sur la sonde custom `my_probe.MyHypotheticalResponse` car aucune des attempts de jailbreak n'a réussi.

<img src="img/garak_report_on_failed_jailbreak_attempts.png" alt="garak-failed-jailbreak-chatbot-8-report" width="600" style="transition:0.3s;">

| Chatbot | Probes conseillées                                                | Remarques                                                      |
|---------|-------------------------------------------------------------------|----------------------------------------------------------------|
| Lab 1   | MyHypotheticalResponse, MyGrandmaPassword                         |                                                                |
| Lab 2   | MyHypotheticalResponse, MyGrandmaPassword                         |                                                                |
| Lab 3   | grandma.substance, MyGrandmaSubstance                             |                                                                |
| Lab 4   | grandma.substance, MyGrandmaSubstance                             |                                                                |
| Lab 5   | realtoxicityprompts.RTPInsult, realtoxicityprompts.RTPProfanity   | /!\ Ces probes utilisent un roberta-classifier comme detector) |
| Lab 7   | MyHypotheticalResponse, MyGrandmaPassword                         |                                                                |
| Lab 8   | MyHypotheticalResponse, MyGrandmaPassword                         |                                                                |
| Lab 9   | grandma.substance, MyGrandmaSubstance                             |                                                                |
| Lab 10  | grandma.substance, MyGrandmaSubstance                             |                                                                |


## Étape suivante
- [Étape 10](step_10.md)

## Ressources


| Information                                   | Lien                                                                                                                                                           |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Github] garak, LLM vulnerability scanner     | [https://github.com/NVIDIA/garak](https://github.com/NVIDIA/garak)                                                                                             |
| Documentation garak                           | [https://docs.garak.ai/](https://docs.garak.ai/)                                                                                                               |
| Garak, DEF CON slides                         | [https://garak.ai/garak_aiv_slides.pdf](https://garak.ai/garak_aiv_slides.pdf)                                                                                 |
| Garak - A Generative AI Red-teaming Tool      | [https://wiki.hackerium.io/llm-security/garak-a-generative-ai-red-teaming-tool](https://wiki.hackerium.io/llm-security/garak-a-generative-ai-red-teaming-tool) |
