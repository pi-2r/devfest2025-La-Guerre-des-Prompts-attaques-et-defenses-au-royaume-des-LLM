# Mettre en place notre chatbot avec la solution Tock

[<img src="img/step11.png" alt="tock" width="800">]()
> "..", X, LOTR - The Return of the King



## 🎯 Objectifs de cette étape
- Découvrir la solution Tock.
- Mettre en place un chatbot avec Tock.
- Créer une premiere intention
- Le connecter à l'IA


## Sommaire
- [Présentation de Tock](#présentation-de-tock)
- [Installation de Tock](#installation-de-tock)


- [Création d'un bot](#création-dun-bot)
- [Création d'une intention](#création-dune-intention)
- [Connexion à l'IA](#connexion-à-lia)


- [Étape suivante](#étape-suivante)
- [Ressources](#ressources)



## Présentation de Tock

<details>
  <summary>Présentation de Tock lors du Devoxx 2025</summary>

Tock (https://doc.tock.ai/) est une plateforme conversationnelle ouverte.
La solution fut créée par SNCF Connect and Tech en 2016 pour motoriser le chatbot Voyages-sncf.com (puis OUI.sncf avant de devenir
SNCF Connect utilisé quotidiennement par des millions de français). Partagée en opensource sur GitHub dès 2017,
la solution a depuis été reprise par de nombreuses entreprises et une communauté d'utilisateurs et de contributeurs s'est créée.

Conçue comme une plateforme d'intégration de briques NLP (Natural Language Processing) sans dépendance forte et apportant
à la fois des interfaces graphiques utilisateur et un framework conversationnel en Kotlin, la plateforme a ensuite bien
évolué : connecteurs à de nombreux canaux textuels et vocaux, création de bots en mode "low code" dans Tock Studio,
compatibilité avec d'autres langages de programmation comme Javascript ou Python, ajout de fonctionnalités analytiques,
gestion multilingue, etc.

Plus récemment, avec l'essor de l'IA Générative et des LLM, Tock s'est révélée une plateforme efficace pour tester
et intégrer de nouvelles technologies conversationnelles, permettant des approches hybrides tout en restant en maîtrise
de la stack technique et des données. Certaines de ses fonctionnalités ont encore peu d'équivalents dans les solutions du marché :


- Combiner dans un même agent conversationnel IA Générative et arbres de décisions traditionnels
- Intégrer des solutions CSP utilisées par les équipes de Relation Client, pour passer facilement de l'IA Générative
- à un humain dans la même conversation
- Mécanismes pour activer/désactiver le RAG, exclure certains sujets, reconfigurer les prompts, etc.


A noter : c'est notamment grâce à des contributions ambitieuses des équipes Crédit Mutuel Arkéa (qui utilisent également
Tock depuis plusieurs années) que Tock a intégré ces dernières années des fonctionnalités autour des LLM et du RAG.
Cela montre toute la force de l'opensource et l'effet levier de la communauté pour une innovation qui profite à tous.
</a>
</details>


### Installation de Tock


Accédez au dossier **lab/tock**.


Une fois modifié, renommez ce fichier **template-internet.env** en **.env**.

Depuis le dossier **lab/tock**, exécutez les commandes suivantes dans votre terminal :

```bash
source .env
docker compose -f during-the-lab-docker-compose-genai.yml pull
```

Vous devriez voir un affichage similaire à celui-ci :

<img src="img/during-the-lab-docker-compose-genai-pull.png" alt="during-the-lab-docker-compose-genai-pull" width="600" style="transition:0.3s;" >

Démarrez ensuite l’environnement avec la commande :

```bash
docker compose -f during-the-lab-docker-compose-genai.yml up -d
```
Vous devriez voir un affichage similaire à celui-ci :
<img src="img/during-the-lab-docker-compose-up.png" alt="tock-docker-up" width="600" style="transition:0.3s;">

Après quelques instants, vous devriez pouvoir accéder à l’interface Tock Studio à l’adresse suivante : http://localhost/login

<img src="img/tock-studio-login-page.png" alt="tock-docker-up" width="600" style="transition:0.3s;">


## Ressources


| Information                                                                                     | Lien                                                                                                                            |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [Devoxx 2025] A la recherche du RAG perdu 🤠🧭🤖 : créez votre IA Générative sans Internet      | [https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen](https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen)            |
