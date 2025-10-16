[<img src="img/la_guerre_des_prompts___attaques___defenses_au_royaume_des_llm.png"  alt="La Guerre des Prompts : attaques & défenses au royaume des LLM">](https://devfest2025.gdgnantes.com/en/sessions/la_guerre_des_prompts___attaques___defenses_au_royaume_des_llm________)

[<img src="img/gandalf_you_shall_not_pass.png" alt="minas_tirith_burning" width="800" >](https://www.youtube.com/watch?v=xMglp0hAvbc)
> "You shall not pass !", Gandalf, LOTR - The Followship of the Ring


Ce tutorial est proposé en amont de la session [La Guerre des Prompts : attaques & défenses au royaume des LLM ⚔️🛡️🤖](https://devfest2025.gdgnantes.com/en/sessions/la_guerre_des_prompts___attaques___defenses_au_royaume_des_llm________) à Devfest Nantes 2025.


## Sommaire

- [Codelab](#codelab)
  - [Récupérer l'atelier](#récupérer-latelier)
  - [Python](#python)
  - [L'outil Docker](#loutil-docker)


- [OpenAi](#openai)
  - [Récupérer une clé OpenAi](#récupérer-une-clé-openai)


- [Ollama](#ollama)
  - [L'outil Ollama](#loutil-ollama)
  - [Les modèles Ollama](#les-modèles-ollama)


- [Les images Docker](#les-images-docker)
  - [AI Red Teaming Playground Labs](#ai-red-teaming-playground-labs)
  - [Tock](#tock)


- [Installation des outils de tests de robustesse](#installation-des-outils-de-tests-de-robustesse)
  - [Installation de Garak](#installation-de-garak)
  - [Installation de PyRIT](#installation-de-pyrit)
  - [Installation de Promptfoo](#installation-de-promptfoo)


    
### Récupérer l'atelier

Depuis votre terminal, récupérez le projet en clonant le dépôt :
  ```bash
  git clone git@github.com:pi-2r/devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM.git
  ```
  
Vous pouvez également télécharger l’archive .zip du projet, puis la décompresser sur votre machine : https://github.com/pi-2r/devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM/archive/refs/heads/main.zip

### Python

Installer Python 3.10 ou supérieur sur votre machine: https://www.python.org/downloads/
<img src="img/install_python.png" alt="python">


### L'outil Docker

Assurez-vous d’avoir installé  [Docker Desktop](https://www.docker.com/products/docker-desktop/) sur votre machine.
<img src="img/docker-desktop-install.png" alt="docker-desktop" >


### Récupérer une clé OpenAi
Allez sur https://platform.openai.com/signup pour créer un compte et récupérer une clé API. Dés que vous etes connecté, 
allez dans la section [API Keys](https://platform.openai.com/api-keys) pour créer une nouvelle clé. Vous devrez avoir cette page :

<img src="img/openai-api-keys.jpg" alt="openai api keys" width="600" style="transition:0.3s;">

Puis cliquez sur le bouton **Create new secret key** pour générer une nouvelle clé au moment voulu dans le lab.

> **Note** : OpenAI offre un crédit gratuit de 5$ pour les nouveaux utilisateurs, ce qui est suffisant pour réaliser 
les exercices de ce workshop. Cependant, une fois ce crédit épuisé, vous devrez fournir des informations de paiement 
pour continuer à utiliser les services d'OpenAI. Assurez-vous de surveiller votre utilisation pour
éviter des frais inattendus : https://termsoup.crisp.help/en-us/article/openai-free-trial-payment-token-limits-wds3wd/


<details>
  <summary>🚧 💡 🚧 Combien ça va me couter ? moins de 5 $ 🚧 💡 🚧</summary>

De notre côté, lors de la réalisation du workshop, avec une **utilisation régulière** de **gpt-3.5-turbo** et 
une **utilisation modérée** de **gpt-5-nano**, n’avons pas dépassé 5 $ de consommation.

<img src="img/openai-price.jpg">

</details>

Vous pouvez tester votre clef OpenAi par exemple avec une requête simple en curl :

```bash
curl https://api.openai.com/v1/responses \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
"model": "gpt-3.5-turbo",
"input": "Tell me a three sentence bedtime story about a unicorn."
}'
```

### L'outil Ollama

Commencez par installer [Ollama](https://ollama.com/download) sur votre machine.

<img src="img/ollama.png" alt="ollama">


### Les modèles Ollama

Pour préparer l’atelier, installez les modèles principaux en exécutant les commandes suivantes dans votre terminal :
```bash
ollama pull tinyllama
ollama pull mistral
ollama pull nomic-embed-text
```

Afin de confirmer que les modèles ont bien été téléchargés, lancez la commande :
```bash
 ollama list
 ```

Vous devriez obtenir un affichage similaire à l’exemple suivant :

<img src="img/ollama_list.png" alt="ollama list">


### Les images Docker

### AI Red Teaming Playground Labs

Depuis votre terminal, placez-vous dans le dossier où vous souhaitez installer le projet, par exemple **Documents**,
puis exécutez la commande suivante pour cloner le dépôt et entrer automatiquement dans le dossier créé :

```bash
git clone https://github.com/microsoft/AI-Red-Teaming-Playground-Labs.git && cd AI-Red-Teaming-Playground-Labs
```

Renommez le fichier **.env.example** en **.env**, puis commentez toutes les variables relatives à Microsoft OpenAI et
décommentez celles concernant OpenAI "classique". 

Ensuite, renseignez les valeurs attendues, comme la clé **OPENAI_API_KEY**, en lui attribuant votre clé d’API OpenAI à la place indiquée, selon l’exemple suivant :

<img src="img/apply_microsoft_playground.jpg" alt="apply_microsoft_playground" width="600" style="transition:0.3s;">

Commentez les champs concernant Azure ou Microsoft, et assurez-vous que seules les variables nécessaires au 
service OpenAI "standard" restent actives dans le fichier **.env**.

Depuis le dossier **AI-Red-Teaming-Playground-Labs**, exécutez les commandes suivantes dans votre terminal :

```bash
source .env
docker compose -f docker-compose-openai.yaml up
```

Si tout est correctement configuré, vous devriez voir un affichage similaire à celui-ci :

<img src="img/microsoft_playground_docker_up.png" alt="microsoft_playground_docker_up" width="600" style="transition:0.3s;">

Pour accéder à l’interface web, ouvrez votre navigateur et allez à l’adresse suivante :  http://localhost:5000/login?auth=YOUR_AUTH_KEY (la valeur de **YOUR_AUTH_KEY** est indiquée dans le fichier **.env**).


#### Tock

Retournez dans le dépôt du codelab et accédez au dossier **lab/tock** :

```bash
cd devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM/lab/tock/
pwd
```

Dans le fichier **template-internet.env**, complétez ensuite la variable d'environnement **OPENAI_API_KEY** avec la clé obtenue précédemment.

Une fois modifié, renommez ce fichier **template-internet.env** en **.env**.


Depuis le dossier **lab/tock**, exécutez les commandes suivantes dans votre terminal :

```bash
source .env
docker compose -f prerequisites-docker-compose-genai.yml pull
```

Vous devriez voir un affichage similaire à celui-ci :

<img src="img/tock-docker-compose.png" alt="tock-docker-compose" width="600" style="transition:0.3s;">

Démarrez ensuite l’environnement avec la commande :

```bash
docker compose -f prerequisites-docker-compose-genai.yml up -d
```
Vous devriez voir un affichage similaire à celui-ci :

<img src="img/tock-docker-up.png" alt="tock-docker-up" width="600" style="transition:0.3s;">

Après quelques instants, vous devriez pouvoir accéder à l’interface Tock Studio à l’adresse suivante : http://localhost/login

<img src="img/tock-studio-login-page.png" alt="tock-docker-up" width="600" style="transition:0.3s;">

Enfin, pour arrêter l'environnement, utilisez la commande :

```bash
docker compose -f prerequisites-docker-compose-genai.yml down
```
 
### Installation de Garak

Depuis votre terminal, placez-vous dans le dossier où vous souhaitez installer le projet, par exemple **Documents**,
puis exécutez la commande suivante pour cloner le dépôt et entrer automatiquement dans le dossier créé :

```bash
# 1. Créer un environnement virtuel a la racine du repo
# cd devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM
python3 -m venv .venv

# 2. Activer l’environnement virtuel
source .venv/bin/activate

# 3. Installer garak
python -m pip install -U garak
```

### Installation de PyRIT

Depuis votre terminal, placez-vous dans le dossier où vous souhaitez installer le projet, par exemple **Documents**,
puis exécutez la commande suivante pour cloner le dépôt et entrer automatiquement dans le dossier créé :

```bash
git clone https://github.com/Azure/PyRIT.git && cd PyRIT
```

Ensuite, créez un environnement virtuel Python, activez-le, puis installez les dépendances du projet avec les commandes
suivantes :

```bash
# Assurez d'être dans le venv créé à la racine du projet du lab
# 1. Créer un environnement virtuel a la racine du repo
# cd devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM
source devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM/.venv/bin/activate

# 2. Activer l’environnement virtuel
source .venv/bin/activate

# 3. Mettre à jour pip, setuptools et wheel dans l’environnement
pip install --upgrade pip setuptools wheel

# 4. Installer la dépendance requise
pip install IPython

# 5. Installer ce projet localement en mode développement (utile pour développement/débogage)
pip install -e .
```

Après exécution, vous devriez obtenir des messages indiquant la création de l’environnement virtuel, puis l’installation
des dépendances du projet. Par exemple :

<img src="img/pyrit-install.png" alt="Pyrit install" width="600" style="transition:0.3s;">

### Installation de Promptfoo

Nous vous invitons à suivre la documentation officielle pour l’installation de Promptfoo :
https://www.promptfoo.dev/docs/red-team/quickstart/#initialize-the-project
