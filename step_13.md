# Mettre en place NeMo Guardrails

[<img src="img/step11.png" alt="tock" width="800">]()
> "..", X, LOTR - The Return of the King



## 🎯 Objectifs de cette étape
- Découvrir la solution Nemo Guardrails.



## Sommaire
- [Schema d'architecture](#schema-darchitecture)


- [C'est quoi NeMo Guardrails ?](#cest-quoi-nemo-guardrails-)
- [Mise en place de NeMo Guardrails](#mise-en-place-de-nemo-guardrails)

- [Pourquoi avoir mis en place un proxy avant NeMo Guardrails ?](#pourquoi-avoir-mis-en-place-un-proxy-avant-nemo-guardrails-)
  - [Exemple sur un cas d'utilisation](#exemple-sur-un-cas-dutilisation)

- [Étape suivante](#étape-suivante)
- [Ressources](#ressources)


## Schema d'architecture

Nous allons insérer la brique Nemo Guardrails entre le proxy et le bot, pour filtrer les requêtes entrantes et sortantes.

    +-------------+      +----------------------------+      +-----------------+      +-----+      +------------------------------+
    |             | ---> |                            | ---> |                 | ---> |     | ---> |                              |
    | Utilisateur |      | Proxy (FastAPI - Filtrage) |      | NeMo Guardrails |      | Bot |      | Base de données (Tock Studio)|
    |             | <--- |                            | <--- |                 | <--- |     | <--- |                              |
    +-------------+      +----------------------------+      +-----------------+      +-----+      +------------------------------+



## C'est quoi NeMo Guardrails ?

**NeMo Guardrails** est un framework open-source développé par **NVIDIA**, conçu pour renforcer la sécurité et la 
fiabilité des applications basées sur des modèles de langage (LLM). 

Il permet aux développeurs de définir des règles et des contraintes fines pour contrôler précisément le comportement 
des grands modèles de langage (LLM), garantissant que les réponses générées respectent les politiques internes de 
l’entreprise ainsi que les normes éthiques et réglementaires. 

Ces règles, appelées "garde-fous" (guardrails en anglais), s’intercalent entre le code applicatif et le modèle LLM pour 
assurer un contrôle granulaire et adaptable.

Ces garde-fous programmables peuvent notamment :

- Empêcher les applications de dévier vers des sujets non souhaités (garde-corps thématiques).
- Garantir que les réponses sont précises, appropriées et ne comportent pas de langage indésirable (garde-corps de sûreté)
- Limiter les interactions avec des applications tierces uniquement à des services sûrs (garde-corps de sécurité)


**NeMo Guardrails** facilite la création de règles personnalisées avec peu de lignes de code, permettant de bloquer, 
reformuler ou guider les réponses du LLM en temps réel, ce qui aide à prévoir et éviter les comportements inappropriés, 
biaisés ou dangereux. 
Ce framework est compatible avec la plupart des LLM, y compris ChatGPT d’OpenAI, et peut s’intégrer au sein 
d’environnements existants comme FastAPI.


## Mise en place de NeMo Guardrails





## Pourquoi avoir mis en place un proxy avant NeMo Guardrails ?

Plusieurs raisons stratégiques et techniques motivent l'utilisation d'un proxy avant d'acheminer les requêtes vers 
NeMo Guardrails :

-  **Filtrage préliminaire** : Le proxy sert de première barrière en interceptant les requêtes entrantes pour éliminer 
d’emblée les contenus manifestement inappropriés ou malveillants. Ce pré-filtrage réduit la charge de travail de 
**NeMo Guardrails** et optimise l’efficacité globale du système.

- **Séparation des fonctions** : En déléguant au proxy les tâches de filtrage simples et rapides, **NeMo Guardrails** 
peut se concentrer sur des analyses plus pointues et spécifiques aux modèles de langage, ce qui améliore 
la qualité des contrôles.

- **Modularité et évolutivité** : L’utilisation d’un proxy permet d’adapter ou d’ajouter des règles de filtrage sans 
impacter directement **NeMo Guardrails**. Cette modularité facilite la maintenance et l’adaptation du système face à des 
besoins évolutifs.

- **Optimisation des performances** : En traitant rapidement certaines requêtes au niveau du proxy, le volume de 
données envoyé à **NeMo Guardrails** est réduit, ce qui améliore la réactivité et la scalabilité, notamment en 
contexte de trafic élevé.


Cette architecture en deux temps favorise une meilleure robustesse dans la détection des contenus problématiques tout 
en préservant efficacité et rapidité dans le traitement des interactions IA.


## Exemple sur un cas d'utilisation

L'exemple ci-dessous illustre un cas simple de jailbreak qui n'a pas été intercepté (bloqué) par le proxy. 
En laissant passer cette requête, NeMo Guardrails s'est activé pour analyser la demande et déterminer si elle était 
légitime ou non.

<img src="img/price_jailbreak_guardrails.jpg" alt="price_jailbreak_guardrails" width="600" style="transition:0.3s;">

Dans ce scénario, le travail d'analyse effectué par Guardrails aurait pu être évité, car il a consommé 966 tokens 
inutilement. **Avec un modèle comme gpt-3.5-turbo-0125, cela représente un coût d'environ 0,00193 €**. 


Rapporté au nombre de visiteurs, cette dépense peut rapidement s'accumuler sans toutefois apporter de réelle valeur 
ajoutée au service client.



## Étape suivante

- [Étape 14](step_14.md)

## Ressources


| Information                   | Lien                                                                                                                   |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------|
| NVIDIA-NeMo                   | [https://github.com/NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)                                 |
| NeMo Guardrails documentation | [https://docs.nvidia.com/nemo/guardrails/latest/index.html](https://docs.nvidia.com/nemo/guardrails/latest/index.html) |
