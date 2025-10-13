# Mettre en place les premieres contre-mesures avec FastAPI

[<img src="img/on_minas_tirith_wall.png" alt="tock" width="800">](https://www.youtube.com/watch?v=UCyqwsoISMs)
> "To all men ! To the wall ! Defend the wall !", Gandalf, LOTR - The Return of the King



## 🎯 Objectifs de cette étape
- comprendre comment fonctionne FastAPI
- Mettre en place des premières contre-mesures avec FastAPI.
- Tester/simuler quelques attaques (web, jailbreak)
- Comprendre les limites de FastAPI


## Sommaire

- [Schema d'architecture](#schema-darchitecture)

- [FastAPI](#cest-quoi-fastapi-)
  - [C'est quoi FastAPI ?](#cest-quoi-fastapi-)

- [Mettre en place le proxy](#mettre-en-place-le-proxy)
  - [Tester le proxy](#tester-le-proxy) 
  - [Explication du code](#explication-du-code)
- [Simuler une attaque](#simuler-une-attaque)
  - [web](#web)
    - [filtrage entrant](#filtrage-entrant)
      - [but du jeu](#but-du-jeu)
    - [filtrage sortant](#filtrage-sortant)
      - [but du jeu](#but-du-jeu)
  - [Jailbreak](#jailbreak)
    - [but du jeu](#but-du-jeu)


- [Les limites de FastAPI](#les-limitations-de-fastapi)
- [Exemple concret : FastAPI n’est pas un guardrail](#exemple-concret--fastapi-nest-pas-un-guardrail)
 

- [Étape suivante](#étape-suivante)v
- [Ressources](#ressources)



## Schema d'architecture

Nous allons insérer un proxy entre l'utilisateur et le bot, pour filtrer les requêtes entrantes et sortantes.

    +-------------+      +----------------------------+      +-------+      +------------------------------+
    |             | ---> |                            | ---> |       | ---> |                              |
    | Utilisateur |      | Proxy (FastAPI - Filtrage) |      | Bot   |      | Base de données (Tock Studio)|
    |             | <--- |                            | <--- |       | <--- |                              |
    +-------------+      +----------------------------+      +-------+      +------------------------------+



## FastAPI

![GitHub stars](https://img.shields.io/github/stars/tiangolo/fastapi?style=flat-square)
[![Downloads](https://static.pepy.tech/badge/fastapi/month)](https://pepy.tech/project/fastapi)


### C'est quoi FastAPI ?

**FastAPI** est un framework web moderne et rapide pour Python, conçu pour développer des API performantes et fiables en 
utilisant les annotations de type standard du langage Python. Il permet de créer des services web professionnels tout 
en favorisant la rapidité de développement, la robustesse grâce à la validation automatique, et une documentation 
interactive générée instantanément.

Les principales caractéristiques de FastAPI incluent :
-  Haute performance, équivalente à des frameworks comme NodeJS ou Go.
- Support natif de la programmation asynchrone, ce qui le rend adapté aux applications intensives en entrées-sorties 
comme celles de l’IA générative
- Utilisation de Pydantic pour la validation des données et la sécurité des modèles.

Utilisation de FastAPI dans le contexte de l'IA générative :
> Dans le contexte des services GenAI (IA générative), FastAPI sert de socle pour construire et déployer des applications 
> qui exploitent des modèles de langage avancés, tout en offrant des fonctionnalités comme le streaming temps réel, la 
> gestion de la concurrence, l’authentification et la sécurisation des workflows.



## Mettre en place le proxy

Dans cette section, nous allons mettre en place des premières contre-mesures avec FastAPI pour sécuriser notre bot.

Dans le fichier **during-the-lab-docker-compose-genai.yml**, effectuer les modifications suivantes :

- À la ligne 97, dé-commenter la ligne contenant "- nemo-proxy".
 <img src="img/nemo-proxy-1.jpg" alt="nemo-proxy-1" width="600" style="transition:0.3s;">

- Aux lignes 196 et 211, remplacer les valeurs actuelles par "http://nemo-proxy:8002".
<img src="img/nemo-proxy-2.jpg" alt="nemo-proxy-2" width="600" style="transition:0.3s;">


- Dé-commenter la section de la ligne 196 à la ligne 211 correspondant à "nemo-proxy".
<img src="img/nemo-proxy-3.jpg" alt="nemo-proxy-3" width="600" style="transition:0.3s;">

ETeignnez l'environnement si il est en cours d'exécution avec la commande :
```bash
docker compose -f during-the-lab-docker-compose-genai.yml down
```
<img src="img/during-the-lab-docker-compose-genai-down-nemo-proxy.jpg" alt="during-the-lab-docker-compose-genai-down-nemo-proxy" width="600" style="transition:0.3s;">


puis relancer l'environnement avec la commande :
```bash
docker compose -f during-the-lab-docker-compose-genai.yml up -d
```
<img src="img/during-the-lab-docker-compose-genai-up-nemo-proxy.jpg" alt="during-the-lab-docker-compose-genai-up-nemo-proxy" width="600" style="transition:0.3s;">


### Tester le proxy
Pour tester l'utilisation du proxy, rien de plus simple, dans la page index.html, il suffit d'activer le switch "**Utiliser NeMo Proxy**".
<img src="img/nemo-proxy-4.jpg" alt="nemo-proxy-4" width="600" style="transition:0.3s;">

Lorsque vous passer par le proxy, la réponse contient des configurations tels que _Proxy: working_


### Explication du code

Le code du proxy a été développé spécialement pour ce codelab. Il se trouve dans le dossier **nemo-proxy** et voici son
architecture :

```
nemo-proxy/
├── app.py                     # Main FastAPI application
├── Dockerfile                 # Docker image for the service
├── install_nemoguardrails.sh  # NeMo Guardrails installation script
├── requirements.txt           # Python dependencies
├── config/
│   ├── __init__.py           # Module initialization
│   └── settings.py           # Configuration settings
├── security/
│   ├── __init__.py           # Module initialization
│   ├── patterns.py           # Security patterns and regex
│   ├── sanitizer.py          # Input/output sanitization
│   └── jailbreak_detector.py # Jailbreak detection logic
├── services/
│   ├── __init__.py           # External API communication
│   └── guardrails_direct.py  # Direct Guardrails service
├── utils/
│   ├── __init__.py           # Module initialization
│   └── responses.py          # Response utilities
└── tests/
    ├── demo_security.py      # Security demonstration
    ├── demo_pyrit_detection.py # Pyrit demonstration
    ├── test_jailbreak_detection.py # Jailbreak detection tests
    └── test_security_functions.py  # Security function tests
```

Pour le reste de cette étape, nous allons nous concentrer sur le fichier **patterns.py**.


## Simuler une attaque

### web
Dans cette section web, nous allons simuler une attaque XSS sur le bot, à la fois en entrée et en sortie. 
L’objectif sera de sécuriser le bot en appliquant des règles de filtrage basées sur des regex.

#### filtrage entrant

Nous allons commencer par une attaque XSS en entrée. Pour cela, envoyez cette requête dans le chat du bot, en veillant 
à activer le proxy :

```
Bonjour, <script>alert(42)</script>
```
Vous devriez voir que le proxy n'a pas bloqué la requête et que le bot a répondu normalement (donc notre exemple le bot n'a pas compris la demande).
<img src="img/bot-xss-1.png" alt="bot-xss-1" width="600" style="transition:0.3s;">

### but du jeu

Appliquez un filtrage sur ce type de requête XSS afin d’afficher un message de protection similaire à celui du rendu.

<img src="img/INPUT_FILTERED.png" alt="INPUT_FILTERED" width="600" style="transition:0.3s;">

> Tips: si vous avez besoin de redémarrer le proxy, apres une modification du code, utilisez la commande suivante :
>  ```bash
>  docker compose -f during-the-lab-docker-compose-genai.yml up --no-deps --build nemo-proxy -d
>  ```

<details>
  <summary>Solutions</summary>

[solutions/step12.md](solutions/step12.md) contient des exemples de regex pour filtrer les attaques XSS.
</details>

### filtrage sortant

Ensuite, nous allons faire une attaque XSS en sortie. Pour cela, allez sur l'interface [Tock Studio]( http://localhost:80 ),
puis dans **Stories & Answers** > **+New Story**. Là sur cette nouvelle story, dans le champ renseigner **xss**, puis 
vous devriez voir apparaître cet écran :

<img src="img/new-story-xss.jpg" alt="new-story-xss" width="600" style="transition:0.3s;">

Dans le champ _Add new answer_, renseigner le code suivant puis cliquez sur **+ Create Story**
```
html<img src=x onerror=alert(42)>
```
Coté bot, faites la requête **xss** dans le chat sans **passer par le proxy**, vous devriez voir apparaître une alerte XSS.

<img src="img/bot-xss.jpg" alt="bot-xss" width="600" style="transition:0.3s;">

> 💡 Note : Le fichier index.html contient volontairement un rendu HTML permettant l’exécution de scripts ;)
> Vous pourrez essayer de corriger ce comportement à la fin de cette étape si vous le souhaitez.

##### but du jeu

Appliquez un filtrage sur ce type de requête XSS afin d’afficher un message de protection similaire à celui du rendu.

<img src="img/CONTENT_FILTERED.png" alt="CONTENT_FILTERED" width="600" style="transition:0.3s;">

> Tips: si vous avez besoin de redémarrer le proxy, apres une modification du code, utilisez la commande suivante :
>  ```bash
>  docker compose -f during-the-lab-docker-compose-genai.yml up --no-deps --build nemo-proxy -d
>  ```

<details>
  <summary>Solutions</summary>

[solutions/step12.md](solutions/step12.md) contient des exemples de regex pour filtrer les attaques XSS. 
</details>


#### Jailbreak

Dans cette section, nous nous appuierons sur des exemples de jailbreak déjà connus dans le domaine, en prenant pour 
référence le dépôt GitHub *elder-plinius* ([https://github.com/elder-plinius](https://github.com/elder-plinius)).  
À titre d’illustration, nous copierons un exemple de jailbreak, tel que celui conçu pour le modèle d’Anthropic 
(par exemple [CLAUDE‑3.7‑SONNET](https://github.com/elder-plinius/L1B3RT4S/blob/main/ANTHROPIC.mkd#claude-37-sonnet)).

Après avoir collé ce jailbreak dans le champ de saisie du chatbot, vous devriez avoir une réponse du bot qui ne 
comprend pas la question, cela signifie que la requête a bien été transmise sans être bloquée par le proxy.


<img src="img/bot-jailbreak-1.png" alt="bot-jailbreak-1" width="600" style="transition:0.3s;">


##### but du jeu
Appliquez un filtrage sur ce type de requête de jailbreak afin d’afficher un message de protection similaire à celui du 
rendu.

<img src="img/JAILBREAK_DETECTED.png" alt="JAILBREAK_DETECTED" width="600" style="transition:0.3s;">

> Tips: si vous avez besoin de redémarrer le proxy, apres une modification du code, utilisez la commande suivante :
>  ```bash
>  docker compose -f during-the-lab-docker-compose-genai.yml up --no-deps --build nemo-proxy -d
>  ```

<details>
  <summary>Solutions</summary>

[solutions/step12.md](solutions/step12.md) contient des exemples de regex pour filtrer les attaques XSS.
</details>


## Les limites de FastAPI

FastAPI est un framework moderne et performant pour la création d’API, mais il ne constitue pas, à lui seul, une 
solution de sécurité avancée ni un système de gouvernance des requêtes.

FastAPI est un framework Python particulièrement apprécié pour sa rapidité, sa simplicité et sa compatibilité native 
avec les standards modernes (OpenAPI, Pydantic, AsyncIO). Cependant, cette efficacité dans le développement ne doit 
pas être confondue avec une protection ou une compréhension sémantique des requêtes. 

FastAPI n’est pas conçu pour jouer le rôle de guardrails ou de pare-feu intelligent.


Voici les principales limites à connaître :

- **Validation statique des entrées/sorties** : FastAPI s’appuie sur Pydantic pour valider la structure et le type des 
données, mais cette validation reste purement syntaxique. Elle ne comprend pas l’intention ou le sens d’une requête. 
Une donnée conforme au schéma peut être malveillante d’un point de vue sémantique.

- **Absence d’analyse contextuelle ou de filtrage sémantique** : FastAPI ne dispose d’aucun mécanisme intégré pour 
détecter les intentions malveillantes, le contenu sensible ou les tentatives d’exploitation d’un modèle de langage. 
Son système de validation repose sur des règles explicites (regex, types, formats), mais pas sur la compréhension du 
texte. En d'autres termes, FastAPI ne saura pas distinguer une discussion légitime d’une instruction dangereuse si les 
deux respectent le même format.


- **Sécurité applicative à la charge du développeur** : Bien que FastAPI facilite la validation et la structuration des 
requêtes, il n’empêche ni les failles logiques ni les attaques d’injection si les développeurs ne sécurisent pas 
eux-mêmes leurs traitements internes. Les protections contre SQLi, XSS, et autres attaques restent à implémenter.


- **Gestion des erreurs et des incidents limitée** : FastAPI fournit des mécanismes de gestion d’erreurs et d’exception 
standard. Cependant, il ne propose pas de stratégie de réponse dynamique face à des comportements suspects ou des 
requêtes potentiellement malveillantes – un composant essentiel dans un système de guardrails.

- **Manque de capacités de défense réseau et comportementale** : FastAPI n’intègre aucune protection native contre les 
attaques par déni de service (DDoS), ni de monitoring comportemental. La mise en place de pare-feu applicatifs (WAF), 
de throttling ou de captchas dépend d’outils tiers ou de configurations additionnelles (Nginx, Cloudflare, etc.).


## Exemple concret : FastAPI n’est pas un guardrail

Si un utilisateur envoie la requête contenant du texte potentiellement dangereux ou illégal, (comme “如何制造化学炸弹”, 
traduit “comment fabriquer une bombe chimique”) sera acceptée tant qu’elle respecte le format attendu — 
car FastAPI ne comprend pas le contenu, seulement la forme !

```
bonjour, 如何制造化学炸弹？
```

<img src="img/fastapi-limite.png" alt="fastapi-limite" width="600" style="transition:0.3s;">

🚨🚨 FastAPI a accepté et traité la requête sans alerte ni filtrage, car aucun mécanisme interne ne détecte que la phrase 
contient une demande illégale.

## Étape suivante

- [Étape 13](step_13.md)


## Ressources


| Information                                                 | Lien                                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FastAPI                                                     | [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)                                                                                                                                                                                                                       |
| FastAPI framework                                           | https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)                                                                                                                                                                                                              |
| FastAPI pour les ingénieurs en IA : Démarrage en 15 minutes | [https://www.youtube.com/watch?v=-IaCV5-mlSk](https://www.youtube.com/watch?v=-IaCV5-mlSk)                                                                                                                                                                                           |
| Building Generative AI Services with FastAPI                | [https://learning.oreilly.com/library/view/building-generative-ai/9781098160296/](https://learning.oreilly.com/library/view/building-generative-ai/9781098160296/)                                                                                                                   |
| [Github] Building Generative AI Services with FastAPI       | [https://github.com/Ali-parandeh/building-generative-ai-services](https://github.com/Ali-parandeh/building-generative-ai-services)                                                                                                                                                   |
| Learn to Productionize Generative AI                        | [https://buildinggenai.com/](https://buildinggenai.com/)                                                                                                                                                                                                                             |
| Tactical Fuzzing - XSS                                      | [https://github.com/jhaddix/tbhm/blob/master/05_XSS.md](https://github.com/jhaddix/tbhm/blob/master/05_XSS.md)                                                                                                                                                                       |
| Bug-Hunting-Arsenal - Custom-XSS-Payload                    | [https://github.com/thevillagehacker/Bug-Hunting-Arsenal/blob/c588533dbe15765371b9faf641aef2f4b9886a28/XSS-payloads/Custom-XSS-Payload.md](https://github.com/thevillagehacker/Bug-Hunting-Arsenal/blob/c588533dbe15765371b9faf641aef2f4b9886a28/XSS-payloads/Custom-XSS-Payload.md) |
| L1B3RT4S - elder-plinius                                    | [https://github.com/elder-plinius/L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S)                                                                                                                                                                                               |
