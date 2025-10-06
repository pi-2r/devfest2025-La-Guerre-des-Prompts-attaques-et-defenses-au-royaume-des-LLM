# Mettre en place NeMo Guardrails

[<img src="img/step11.png" alt="tock" width="800">]()
> "..", X, LOTR - The Return of the King



## 🎯 Objectifs de cette étape
- Découvrir la solution Nemo Guardrails.



## Sommaire


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

## Étape suivante

- [Étape 14](step_14.md)

## Ressources


| Information                   | Lien                                                                                                                   |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------|
| NVIDIA-NeMo                   | [https://github.com/NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)                                 |
| NeMo Guardrails documentation | [https://docs.nvidia.com/nemo/guardrails/latest/index.html](https://docs.nvidia.com/nemo/guardrails/latest/index.html) |
