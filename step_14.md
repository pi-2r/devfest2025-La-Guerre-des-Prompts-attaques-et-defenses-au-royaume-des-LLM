#  AI Red Teaming

[<img src="img/step15.jpg" alt="gandalf" width="800">](https://www.youtube.com/watch?v=lKSKJZ-XdAk)
> "Fight for us... and regain your honor", Aragorn, LOTR - The Return of the King


## 🎯 Objectifs de cette étape

- Comprendre les principes du red teaming appliqué aux IA génératives
- Identifier les vulnérabilités spécifiques aux systèmes d’IA générative
- Mettre en œuvre des techniques d’attaque et d’évaluation adaptées
- Proposer des stratégies de mitigation et de défense

## Sommaire

 - [Red Teaming des intelligences artificielles génératives](#red-teaming-des-intelligences-artificielles-génératives)

 - [Approche face aux IA génératives](#approche-face-aux-ia-génératives)
   - [La boîte noire](#la-boîte-noire)
   - [Dépendance aux données](#dépendance-aux-données)
   - [Composants des systèmes d’IA générative](#composants-des-systèmes-d’ia-générative)

 - [Techniques, tactiques et procédures (TTP) spécifiques](#techniques-tactiques-et-procédures-ttp-spécifiques)

 - [Étape suivante](#étape-suivante)
 - [Ressources](#ressources)

## Red Teaming des intelligences artificielles génératives

Le red teaming des intelligences artificielles génératives est une approche proactive visant à identifier les 
vulnérabilités et les faiblesses des systèmes d'IA générative. 

Cependant, le red teaming présentent des complexités et des subtilités particulières. Avec l’explosion récente des modèles 
d’apprentissage automatique (ML) et la multiplication des déploiements de systèmes basés sur ces techniques, 
le domaine évolue de manière dynamique et adaptative. 

Cette évolution perpétuelle engendre des défis spécifiques pour les administrateurs et les testeurs d’intrusion, 
notamment en raison du risque accru de mauvaise configuration ou de failles lors du déploiement des modèles, pouvant 
engendrer des vulnérabilités de sécurité.


## Approche face aux IA génératives

Lorsqu’on évalue la sécurité des systèmes reposant sur des IA génératives, il est essentiel de comprendre leur nature 
adaptative et évolutive. Pour cela, il faut rester informé·e des avancées dans ce domaine afin d’identifier en temps 
réel les failles potentielles. 

En outre, une approche d’évaluation de sécurité agile et créative est nécessaire pour exploiter ces vulnérabilités, 
surtout lorsqu’elles sont protégées par des mécanismes de mitigation spécifiques.

### La boîte noire

Un des grands défis inhérents aux modèles complexes utilisés en IA générative est leur côté « boîte noire » : 
il est souvent difficile de comprendre pourquoi un modèle réagit d’une certaine manière à une entrée donnée, et encore 
plus complexe de prédire sa réaction à de nouvelles entrées. 

Par conséquent, les évaluations de sécurité doivent adop-ter une posture de test en boîte noire, même lorsque le type 
de modèle est connu. Cela implique de développer des stratégies d’attaque innovantes pour déceler et exploiter les 
vulnérabilités.

Cependant, la connaissance du type de modèle utilisé peut faciliter ces évaluations. Par exemple, si le modèle cible 
est open source, on peut le télécharger et l’héberger soi-même, ce qui permet de tester les vulnérabilités courantes 
en toute sécurité, sans perturber le service ou susciter de suspicion. Cette approche peut aussi accélérer les tests 
face aux protections classiques comme la limitation de débit (rate limiting).


--> TODO

## Étape suivante

- [Étape 15](step_15.md)

## Ressources

| Information                                               | Lien                                                                                                                                                                                   |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Red Teaming AI Red Teaming                                | [https://arxiv.org/abs/2507.05538](https://arxiv.org/abs/2507.05538)                                                                                                                   |
| NVIDIA AI Red Team: An Introduction                       | [https://developer.nvidia.com/blog/nvidia-ai-red-team-an-introduction/](https://developer.nvidia.com/blog/nvidia-ai-red-team-an-introduction/)                                         |
| Defining LLM Red Teaming                                  | [https://developer.nvidia.com/blog/defining-llm-red-teaming/](https://developer.nvidia.com/blog/defining-llm-red-teaming/)                                                             |
| Red Teaming AI: Attacking & Defending Intelligent Systems | [https://www.amazon.com.au/Red-Teaming-Attacking-Defending-Intelligent-ebook/dp/B0F88SGMXG](https://www.amazon.com.au/Red-Teaming-Attacking-Defending-Intelligent-ebook/dp/B0F88SGMXG) |
| SAFE-AI A Framework for Securing AI-Enabled Systems       | [https://www.linkedin.com/feed/update/urn:li:activity:7346561112877821953/](https://www.linkedin.com/feed/update/urn:li:activity:7346561112877821953/)                                 |
