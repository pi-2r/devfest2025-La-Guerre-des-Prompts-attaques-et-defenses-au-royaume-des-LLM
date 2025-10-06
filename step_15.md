#  Benchmarking avec Promptfoo


[<img src="img/step16.png" alt="gimli" width="800">](https://www.youtube.com/watch?v=CAdkKQ6-6wo)
> "That still only counts as one.", Gimli, LOTR - The Return of the King


## Sommaire

- [Promptfoo](#promptfoo)
    - [L'évaluation de la qualité des réponses d'un LLM](#lévaluation-de-la-qualité-des-réponses-dun-llm)
    - [L'audit de sécurité de modèles de langage](#laudit-de-sécurité-de-modèles-de-langage)


- [Mise en pratique d'un scan d'un modèle](#mise-en-pratique-dun-scan-dun-modèle)

## Promptfoo

Promptfoo est un outil en partie open-source qui se veut être la brique permettant un passage en production d'une application avec des LLMs.

### L'évaluation de la qualité des réponses d'un LLM

Promptfoo est un outil permettant de faire des évaluations de la qualité des **RAGs** (Retrieval-Augmented Generation), des **Agents IA** et des **LLMs** avec métriques allant de la recherche de mots-clés à des métriques utilisant des _LLMs-as-a-Judge_, comme :
- le **contains-json** (vérifiant si la réponse contient un JSON valide),
- l'**Answer Relevancy** (vérifiant la pertinence de la réponse vis-a-vis de la question posée),
- la **Context Faithfulness** (vérifiant si la réponse du LLM se fonde uniquement sur des éléments du contexte).
- la **Factuality** (évaluant la réponse du LLM vis-à-vis de la réponse de référence).
- la **LLM-rubric**, une métrique custom, permettant, par exemple, d'évaluer des éléments de **Tone-of-Voice**, de Style, de Grammaires, etc.
- la **G-eval**, une métrique custom, utilisant un LLM et leur CoT (Chain-of-Thought) pour évaluer des réponses sur des critères complexes.

Promptfoo peut lancer les tests plusieurs fois pour tester la robustesse des réponses.


### L'audit de sécurité de modèles de langage

Promptfoo se veut **modulaire** et **extensible**. Il met à disposition des utilisateurs plusieurs outils et plugins pour évaluer la sécurité de leur application et des modèles de langage.
Promptfoo se met régulièrement à jour concernant les dernières évolutions des vulnérabilités des LLMs et suit notamment les recommandations OWASPs LLM Top 10.

#### Architecture de Promptfoo pour le Red Teaming


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

[<img src="img/architecture_promptfoo_red_teaming.png" width="800">](https://www.promptfoo.dev/docs/red-team/architecture/)
##### Schema de l'architecture de Promptfoo pour le Red Teaming

#### Recommandations sur comment utiliser Promptfoo pour le Red Teaming


## Mise en pratique d'un scan d'un modèle

Pour cela, il faut installer `promptfoo` et une librairie complémentaire `modelaudit` :

```bash

pip install promptfoo
pip install modelaudit
```

Une fois la librairie installée, lancer la commande suivante :
```bash

promptfoo view
```

Puis aller dans la section **Model Audit**

<img src="img/promptfoo_scan_entry_page.png" width="800">




<img src="img/promptfoo_result_security_audit.png" width="800">

