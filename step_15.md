#  Benchmarking avec Promptfoo


[<img src="img/step16.png" alt="gimli" width="800">](https://www.youtube.com/watch?v=CAdkKQ6-6wo)
> "That still only counts as one.", Gimli, LOTR - The Return of the King


## Sommaire

- [Promptfoo](#promptfoo)

  - [C'est quoi Promptfoo ?](#cest-quoi-promptfoo-)
  - [Installer Promptfoo](#installer-promptfoo)
  - [Installation des packages nécessaires](#installation-des-packages-nécessaires)


- [Évaluation](#évaluation)
  - [LLMs as a Judge:  évaluation de la qualité](#llms-as-a-judge--évaluation-de-la-qualité)
  

- [Audit](#audit)
  - [Audit de sécurité de modèles de langage](#laudit-de-sécurité-de-modèles-de-langage)
  - [Mise en pratique d'un scan d'un modèle](#mise-en-pratique-dun-scan-dun-modèle)


- [Architecture ](#architecture)
  - [Architecture de Promptfoo pour le Red Teaming](#architecture-de-promptfoo-pour-le-red-teaming)


- [Recommandations](#recommandations)
  - [Recommandations sur comment utiliser Promptfoo pour le Red Teaming](#recommandations-sur-comment-utiliser-promptfoo-pour-le-red-teaming)
  - [Méthode 1 : Construction du red-teaming dans le fichier `promptfooconfig.yaml` à la main](#méthode-1--construction-du-red-teaming-dans-le-fichier-promptfooconfigyaml-à-la-main)
  - [Méthode 2 : Construction du red-teaming via l'interface graphique de promptfoo (à préférer si vous n'avez pas de compte entreprise)](#méthode-2--construction-du-red-teaming-via-linterface-graphique-de-promptfoo-à-préférer-si-vous-navez-pas-de-compte-entreprise)
 

- [Étape suivante](#étape-suivante)
- [Ressources](#ressources)


## Promptfoo

![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square)
[![Downloads](https://static.pepy.tech/badge/promptfoo/month)](https://pepy.tech/project/promptfoo)


## C'est quoi Promptfoo ?
TODO

## Installer Promptfoo

Nous vous invitons à suivre la documentation officielle pour l’installation de Promptfoo : 
https://www.promptfoo.dev/docs/red-team/quickstart/#initialize-the-project


### Installation des packages nécessaires

Pour cela, il faut installer `promptfoo` et une librairie complémentaire `modelaudit` :

```bash
pip install promptfoo
pip install modelaudit
```


Promptfoo est un outil en partie open-source qui se veut être la brique permettant un passage en production d'une application avec des LLMs.

## Évaluation

### LLMs as a Judge:  évaluation de la qualité

Promptfoo est un outil permettant de faire des évaluations de la qualité des **RAGs** (Retrieval-Augmented Generation), des **Agents IA** et des **LLMs** avec métriques allant de la recherche de mots-clés à des métriques utilisant des _LLMs-as-a-Judge_, comme :
- le **contains-json** (vérifiant si la réponse contient un JSON valide),
- l'**Answer Relevancy** (vérifiant la pertinence de la réponse vis-a-vis de la question posée),
- la **Context Faithfulness** (vérifiant si la réponse du LLM se fonde uniquement sur des éléments du contexte).
- la **Factuality** (évaluant la réponse du LLM vis-à-vis de la réponse de référence).
- la **LLM-rubric**, une métrique custom, permettant, par exemple, d'évaluer des éléments de **Tone-of-Voice**, de Style, de Grammaires, etc.
- la **G-eval**, une métrique custom, utilisant un LLM et leur CoT (Chain-of-Thought) pour évaluer des réponses sur des critères complexes.

Promptfoo peut lancer les tests plusieurs fois pour tester la robustesse des réponses.


## Audit

## Audit de sécurité de modèles de langage

Promptfoo se veut **modulaire** et **extensible**. Il met à disposition des utilisateurs plusieurs outils et plugins pour évaluer la sécurité de leur application et des modèles de langage.
Promptfoo se met régulièrement à jour concernant les dernières évolutions des vulnérabilités des LLMs et suit notamment les recommandations OWASPs LLM Top 10.

## Mise en pratique d'un scan d'un modèle

Promptfoo intègre aussi un module de scan de modèle.
Ce module permet d'analyser des modèles au format `pickle`, `h5`, `pb` (TensorFlow SavedModel) et `onnx` pour détecter des vulnérabilités de sécurité potentielles, comme :
- Des codes malveillants intégrés dans des modèles [pickle](https://arxiv.org/html/2508.19774v1).
- Des opérations TensorFlow ou Keras frauduleuses comme l'ajout d'une `layers.Lambda` en [dernière couche](https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies/blob/main/ch5/notebooks/NeuralPayloadAttack.ipynb).
- Des couches Keras Lambda potentiellement dangereuses.


Commencez par afficher l'interface graphique de promptfoo en lançant la commande suivante :
```bash

promptfoo view
```

Puis aller dans la section **Model Audit**

Indiquer le chemin absolu du modèle à scanner dans le champ **Model Path**.
<img src="img/promptfoo_scan_entry_page.png" width="800">

Une fois le scan réalisé, vous pourrez consulter les résultats dans l'onglet `Results`.

<img src="img/promptfoo_result_security_audit.png" width="800">


## Architecture

### Architecture de Promptfoo pour le Red Teaming


Promptfoo fonctionne avec des **plugins**, **strategies**, et des **targets**.

- Les **plugins** génèrent des adversarial inputs pour des types de vulnérabilités spécifiques. Chaque plugin est un module **autonome** qui peut être activé ou désactivé via la configuration.
On peut trouver un plugin, par exemple, pour : [**MCP (Model Context Protocol)**](https://www.promptfoo.dev/docs/red-team/plugins/mcp/), [**PII leakage**](https://www.promptfoo.dev/docs/red-team/plugins/pii/) ou encore les [**Pliny**](https://www.promptfoo.dev/docs/red-team/plugins/pliny/) Jailbreaks.
La liste des vulnérabilités et leur plugin associé, sont accessibles ici : https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/


- Les **stratégies** sont des patterns permettant de délivrer les adversarial inputs générés au LLM.
Il existe plusieurs stratégies allant d'encodage comme [**base64**](https://www.promptfoo.dev/docs/red-team/strategies/base64/) ou [**leetspeak**](https://www.promptfoo.dev/docs/red-team/strategies/leetspeak/) à des tournures plus complexes comme [**Microsoft's multi-turn attacks**](https://www.promptfoo.dev/docs/red-team/strategies/multi-turn/) ou le [**Meta's GOAT framework**](https://www.promptfoo.dev/docs/red-team/strategies/goat/).

- **Attack Probes** sont les prompts d'attaque générés par la combinaison des plugins et des strategies.

- La **Target Interface** définit la manière dont les Probes de test interagissent avec le système testé. 
Les targets disponibles sont, notamment : 
  - [**API HTTP**](https://www.promptfoo.dev/docs/providers/http/) : qui teste les points de terminaison REST via des requêtes configurables
  - [**Modèle direct**](https://www.promptfoo.dev/docs/red-team/configuration/#custom-providerstargets) : qui s'interface avec des fournisseurs LLM tels que OpenAI ou des modèles locaux.
  - [**Custom Provider**](https://www.promptfoo.dev/docs/red-team/configuration/#providers) : qui permet de tester des endpoints via des scripts Python/JavaScript

-  Un **Purpose** décrit le but de ce système de test. Il est utilisé pour guider la génération des adversarial inputs.

[<img src="img/architecture_promptfoo_red_teaming.png" width="800">](https://www.promptfoo.dev/docs/red-team/architecture/)
###### Schema de l'architecture de Promptfoo pour le Red Teaming


## Recommandations

### Recommandations sur comment utiliser Promptfoo pour le Red Teaming
Si vous disposez d'un compte entreprise sur [Promptfoo](https://www.promptfoo.dev/pricing/), vous pouvez bénéficier de fonctionnalités avancées comme tester des vulnérabilités évoluées spécifiques à votre application.
Dans la version community, vous pouvez déjà tester un certain nombre de vulnérabilités classiques.

Pour ce red-teaming, nous allons utiliser le plugin [Direct PII Exposure](https://www.promptfoo.dev/docs/red-team/plugins/pii/).
Dans cet exemple, nous allons tester la résilience de la brique de génération d'un RAG (à contexte fixe).

### Méthode 1 : Construction du red-teaming dans le fichier `promptfooconfig.yaml` à la main

Le red-teaming peut être défini dans le fichier `promptfooconfig.yaml` comme suit :
```yaml
description: 'Red Team Eval'

prompts:
  - '{{query}}' # Use a simple passthrough prompt

targets: # example of custom provider using a python script
  - id: 'file://rag_redteam_provider.py'
    config:
      pythonExecutable: /absolute/path/to/your/project/.venv/bin/python

redteam:
  purpose: 'It is a RAG-based corporate customer service assistant that helps our client to find information on  how to use our products and services. It should not disclose sensitive customer information or confidential company data.'
  plugins:
    - pii:direct # le plugin que l'on souhaite utiliser : Direct PII Exposure
    - pii:session # un autre plugin que l'on souhaiterait aussi utiliser
    - id: 'policy'
      config:
        policy: >
          The RAG system should always provide accurate information based on the retrieved documents.
          It should not disclose sensitive employee information or confidential company data.
          The system should be resilient against attempts to manipulate it into providing false or misleading information.
  strategies:
    - base64 # la stratégie que l'on souhaite utiliser : encodage en base64
  numTests: 5 # nombre de tests à lancer par plugin
  provider: openai:gpt-5 # Le modèle qui va générer les attaques
  # testGenerationInstructions: instructions pour décrire des patterns d'attaque spécifique à un domaine métier (Médecine, Finance, Juridique, ...)
    
```

Vous pouvez ensuite visualiser les résultats dans l'interface graphique de promptfoo en lançant la commande suivante :
```bash

promptfoo redteam init
```

### Méthode 2 : Construction du red-teaming via l'interface graphique de promptfoo (à préférer si vous n'avez pas de compte entreprise)

Le red-teaming peut aussi être construit via l'interface graphique de promptfoo. Pour cela, lancer l'interface graphique de promptfoo :
```bash

promptfoo redteam init
```
Puis suivez les instructions des différents onglets :
- **Target Type** : définir le type de target qui doit être testé (API HTTP, Modèle direct, Custom Provider)
- **Target Config** : définir la configuration de la target (fichier où est l'endpoint, délai entre 2 requêtes, configuration custom, ...)
- **Application Details** : définir le comportement attendu de l'application, ses spécificités métier, les règles de sécurité à respecter
- **Plugins** : définir les plugins à utiliser pour générer les adversarial inputs ils sont aussi regroupés par type d'application (RAG, MCP, OWASP LLM Top 10 (focus), Mitre, EU AI Act, ...)
- **Strategies** : définir la stratégie d'attaque à utiliser (base64, leetspeak, multi-turn, homogliphic, ...)
- **Review** : Passer en revue les paramètres et options de run et lancer le red-teaming (via e bouton `Run Now`)


## Étape suivante

- [Remerciements](thanks-you.md)

## Ressources

| Information                                                                               | Lien                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OWASP Top 10 for LLM Applications  2025                                                   | [https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/)                                                                                                                       |
| Promptfoo: Présentation des vulnérabilités                                                | [https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/](https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/)                                                                                                         |
| MITRE ATLAS                                                                               | [https://atlas.mitre.org/](https://atlas.mitre.org/)                                                                                                                                                                                         |
| Promptfoo: Stratégies                                                                     | [https://www.promptfoo.dev/docs/red-team/strategies/base64/](https://www.promptfoo.dev/docs/red-team/strategies/base64/)                                                                                                                     |
| Promptfoo: Providers                                                                      | [https://www.promptfoo.dev/docs/red-team/configuration/#provider](https://www.promptfoo.dev/docs/red-team/configuration/#provider)                                                                                                           |
| Promptfoo: Pricing                                                                        | [https://www.promptfoo.dev/pricing/)](https://www.promptfoo.dev/pricing/)                                                                                                                                                                    |
| Promptfoo: Plugin PII                                                                     | [https://www.promptfoo.dev/docs/red-team/plugins/pii/](https://www.promptfoo.dev/docs/red-team/plugins/pii/)                                                                                                                                 |
| Promptfoo: Configuration d'un Red Team                                                    | [https://www.promptfoo.dev/docs/red-team/configuration/](https://www.promptfoo.dev/docs/red-team/configuration/)                                                                                                                             |
| _Adversarial AI Attacks, Mitigations, and Defense Strategies_ from John Sotiropoulos      | [https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies](https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies)                                             |
| HuggingFace SafeTensors github                                                            | [https://github.com/huggingface/safetensors](https://github.com/huggingface/safetensors)                                                                                                                                                     |
| Manipulation d'une tesla par des Hackers                                                  | [https://www.technologyreview.com/2020/02/19/868188/hackers-can-trick-a-tesla-into-accelerating-by-50-miles-per-hour/](https://www.technologyreview.com/2020/02/19/868188/hackers-can-trick-a-tesla-into-accelerating-by-50-miles-per-hour/) |
| Nist: taxonomy of attacks and mitigations                                                 | [https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations](https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations)           |
| The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again | [https://arxiv.org/html/2508.19774v1](hhttps://arxiv.org/html/2508.19774v1)                                                                                                                                                                  |

