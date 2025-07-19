# Cadres de Sécurité Référents

[<img src="img/step4.jpg" alt="Arwen" >](https://www.youtube.com/watch?v=fd2AO0gr3Rc)
> "if you want him come and claim him", Arwen, LOTR - The Followship of the Ring

## 🎯 Objectifs de cette étape
- Comprendre les cadres de sécurité existants pour les LLM


## Sommaire

- [OWASP Top 10 for LLM Applications](#owasp-top-10-for-llm-applications)


- [Mitre ATLAS, le fil d'Ariane des techniques d'attaque sur l'IA](#mitre-atlas-le-file-dariane-des-techniques-dattaque-sur-lia)


- [Soyez SAIF avec le Secure AI Framework](#soyez-saif-avec-le-secure-ai-framework)


- [Réglementation législative des LLM](#réglementation-législative-des-llm)
    - [Enjeux et principes](#enjeux-et-principes)
      - [États-Unis: une régulation sectorielle et centrée sur la liberté d’expression](#états-unis-une-régulation-sectorielle-et-centrée-sur-la-liberté-dexpression)
      - [Union européenne: un encadrement structuré et fondé sur les risques](#union-européenne-un-encadrement-structuré-et-fondé-sur-les-risques)
        - [Digital Services Act (DSA)](#digital-services-act-dsa)
        - [AI Act](#ai-act)
    - [Points de convergence et divergences](#points-de-convergence-et-divergences)
  

- [Ressources](#ressources)

## OWASP Top 10 for LLM Applications


| IDENTIFIANT  | Description                                                                                                                                                                                                                    |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LLM01**    | **Injection de prompt** : Les attaquants manipulent l'entrée du LLM directement ou indirectement pour provoquer un comportement malveillant ou illégal.                                                                        |
| **LLM02**    | **Gestion non sécurisée de la sortie** : La sortie du LLM est gérée de manière non sécurisée, entraînant des vulnérabilités d'injection telles que le Cross-Site Scripting (XSS), l'injection SQL ou l'injection de commandes. |
| **LLM03**    | **Empoisonnement des données d'entraînement** : Les attaquants injectent des données malveillantes ou trompeuses dans les données d'entraînement du LLM, compromettant ses performances ou créant des portes dérobées.         |
| **LLM04**    | **Déni de service du modèle** : Les attaquants fournissent au LLM des entrées provoquant une consommation excessive de ressources, causant potentiellement des perturbations du service.                                       |
| **LLM05**    | **Vulnérabilités de la chaîne d'approvisionnement** : Les attaquants exploitent les vulnérabilités dans n’importe quelle partie de la chaîne d’approvisionnement du LLM.                                                       |
| **LLM06**    | **Divulgation d’informations sensibles** : Les attaquants trompent le LLM pour qu'il révèle des informations sensibles dans sa réponse.                                                                                        |
| **LLM07**    | **Conception de plugins non sécurisée** : Les attaquants exploitent des vulnérabilités dans la sécurité des plugins LLM.                                                                                                       |
| **LLM08**    | **Accès excessif (agency)** : Les attaquants exploitent l’accès insuffisamment restreint du LLM à des systèmes ou à des actions sensibles.                                                                                     |
| **LLM09**    | **Dépendance excessive** : Une organisation dépend de manière excessive des résultats d’un LLM pour prendre des décisions critiques, exposant ainsi la sécurité à des comportements inattendus du modèle.                      |
| **LLM10**    | **Vol de modèle** : Les attaquants obtiennent un accès non autorisé au LLM, volant de la propriété intellectuelle et causant potentiellement des pertes financières.                                                           |


## Mitre ATLAS, le file d'Ariane des techniques d'attaque sur l'IA



## Soyez SAIF avec le Secure AI Framework

<img src="img/saif-map.png" alt="SAIF">


## Réglementation législative des LLM

Entre 2013 et 2023, les entreprises américaines ont attiré un volume de capitaux privés plus de six fois supérieur à 
celui investi dans les entreprises européennes, favorisant ainsi l’émergence d’un écosystème incomparable en matière 
d’innovation dans le domaine de l’intelligence artificielle.

À titre de comparaison, les sociétés **américaines** ont levé environ **486,1 milliards de dollars** de financements privés sur 
cette période, contre seulement **75,7 milliards** pour leurs homologues **européennes**.

<details>
  <summary>Comparatif graphique : 10 ans d’investissements en IA aux États-Unis et dans l’Union européenne.</summary>

<a href="https://actonline.org/2025/06/02/to-win-the-ai-race-congress-must-learn-from-europes-missteps/" target="_blank">
  <img src="https://actonline.org/wp-content/uploads/AI-blog-.png" alt="image" width="450" style="transition:0.3s;">
</a>
</details>

Ainsi, ces dernières années, de nombreux pays ont mis en place de nouvelles régulations afin de faire face aux dérives 
liées aux technologies d’intelligence artificielle, notamment pour freiner la diffusion de la désinformation et des 
discours de haine.
Voici un aperçu des approches adoptées par les États-Unis et l’Union européenne en matière de régulation des modèles de langage de grande taille (LLM).

### Enjeux et principes

- **Équilibre responsabilité/innovation :** Réguler les LLM exige de maintenir un juste équilibre entre la 
responsabilisation des acteurs (développeurs, déployeurs, utilisateurs) et la préservation de l’innovation. Les LLM 
présentent des avantages majeurs (éducation, accessibilité, créativité) mais comportent aussi des risques, comme la 
génération de contenus préjudiciables.


- **Définition de la responsabilité :** L’identification des responsables des contenus générés par les LLM reste un 
enjeu. La responsabilité peut-elle incomber au développeur, à celui qui déploie la solution, ou à l’utilisateur ?


- **Respect des droits fondamentaux :** La lutte contre les abus ne doit pas compromettre des droits humains tels que la 
liberté d’expression. Les réglementations doivent donc viser la protection sans imposer une censure excessive.


## États-Unis: une régulation sectorielle et centrée sur la liberté d’expression

- **Liberté d’expression :** Aux États-Unis, la diffusion d’informations fausses ou controversées, sauf en cas de 
diffamation, d’incitation à la violence ou de fraude, reste protégée par le premier amendement, rendant difficile 
l’instauration de mesures de fond contre la désinformation.


- **Take It Down Act :** Cette législation fédérale récente cible la diffusion sur Internet de contenus abusifs, 
particulièrement les deepfakes et images intimes non consenties, y compris si elles sont générées par l’IA. Elle impose 
aux plateformes un dispositif de signalement rapide et des obligations de retrait sous peine de sanctions administratives. 
La loi vient combler une lacune juridique majeure en matière de deepfakes.


- **Obligations pour les plateformes :** Les réseaux sociaux et sites d’hébergement doivent retirer, dans un délai court, 
les contenus signalés comme illégaux. En cas de non-respect, ils s’exposent à des sanctions importantes.  


- **Bonnes pratiques et autorégulation :** Les organismes publics comme le [NIST (National Institute of Standards and 
Technology)](https://www.nist.gov/) recommandent des pratiques de gestion des risques (AI RMF). D’autre part, 
la [Federal Trade Commission (FTC)](https://www.ftc.gov/) peut agir contre les pratiques commerciales trompeuses recourant à l’IA.


## Union européenne: un encadrement structuré et fondé sur les risques
La régulation européenne s’articule autour de deux textes principaux :

### Digital Services Act (DSA)

- **Obligations générales :** Mécanismes de signalement et suppression des contenus illégaux ; droit de recours pour les 
utilisateurs en cas de suppression abusive.


- **Champ d’application large :** S’applique à tous les fournisseurs de services numériques opérant dans l’UE, même 
s’ils sont basés à l’étranger.

- **Évaluations de risques récurrentes :** Pour certains acteurs majeurs, le DSA impose des évaluations régulières sur 
des problématiques comme la désinformation. Les plateformes doivent agir efficacement pour atténuer ces risques 
(modification d’algorithmes, transparence accrue, etc.).


- **Renforcement de la transparence et des droits fondamentaux :** Protection contre les contenus nuisibles, respect de 
la vie privée et de la liberté d’expression, publication claire des politiques de modération et de publicité.

### AI Act

- Une approche fondée sur 4 niveaux de risques :

  - **Risque inacceptable :** Systèmes interdits (ex. : social scoring, manipulation de masse).
  - **Risque élevé :** Secteurs critiques (santé, éducation, sécurité). Obligations strictes : gestion des risques, 
  gouvernance des données, supervision humaine.
  - **Risque limité :** Systèmes interagissant avec le public ou générant du contenu, comme les LLM. Exigences de 
  transparence (divulguer si un contenu est généré par IA), documentation, mesures pour prévenir les usages abusifs.
  - **Risque minimal :** Applications simples telles que filtres anti-spam, largement non réglementées.


- **Innovations spécifiques :** L’AI Act prévoit des obligations particulières pour les modèles d’IA à usage général 
présentant un risque systémique important (capacités computationnelles massives).


- **Pénalités et contrôles :** Les contrevenants s’exposent à des contrôles accrus et à des sanctions financières 
dissuasives.


### Points de convergence et divergences

Voici un tableau récapitulatif des différences et similitudes entre les approches réglementaires des États-Unis et 
de l’Union européenne concernant les LLM :

| Points                            | États-Unis                                                                                            | Union européenne                                                                                             |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| **Priorité fondamentale**         | Liberté d’expression préservée, interventions ciblées sur des enjeux précis (deepfakes, fraude).      | Approche globale couvrant l’ensemble du cycle de vie de l’IA selon le niveau de risque .                     |
| **Philosophie de régulation**     | Focalisée sur les cas particuliers et défense du Premier Amendement.                                  | Préventive, systémique, avec exigence de transparence, documentation et gestion du risque à chaque étape .   |
| **Responsabilisation**            | Obligations ciblées sur certaines plateformes ; sanctions et normes variables selon les États et cas. | Responsabilisation claire et harmonisée pour plateformes et fournisseurs, régime de sanction structuré .     |
| **Transparence et documentation** | Exigences limitées à certains cas spécifiques (deepfakes, fraude), pas de cadre général harmonisé.    | Forte exigence de transparence, documentation, accès public à l’information pour systèmes IA à risque .      |
| **Harmonisation des sanctions**   | Fragmentée, grandes variations selon États fédérés et interventions fédérales ponctuelles.            | Sanctions harmonisées, régulièrement renforcées et uniformisées au niveau de l’UE.                           |


## Ressources

| Information                                                                                          | Lien                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MITRE ATLAS™ Introduction                                                                            | [https://www.youtube.com/watch?v=3FN9v-y-C-w](https://www.youtube.com/watch?v=3FN9v-y-C-w)                                                                                                                                                             |
| OWASP Top 10 for LLM Applications                                                                    | [https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf) |
| Secure AI Framework (SAIF)                                                                           | [https://saif.google/](https://saif.google/)                                                                                                                                                                                                           |
| Anatomy of an AI ATTACK: MITRE ATLAS                                                                 | [https://www.youtube.com/watch?v=QhoG74PDFyc](https://www.youtube.com/watch?v=QhoG74PDFyc)                                                                                                                                                             |
| Faut-il investir sur la tech européenne ? L'analyse d'un insider - Finary Talk #60 & Olivier Coste - | [https://youtu.be/Tw-HRXlVIa0?si=ZRHWRjy_vzHcQ6Af](https://youtu.be/Tw-HRXlVIa0?si=ZRHWRjy_vzHcQ6Af)                                                                                                                                                   |
| AI Act                                                                                               | [https://artificialintelligenceact.eu/fr/](https://artificialintelligenceact.eu/fr/)                                                                                                                                                                   |
| AI Act - European Commission                                                                         | [https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)                                                                                                 |
| Digital Services Act (DSA)                                                                           | [https://www.vie-publique.fr/eclairage/285115-dsa-le-reglement-sur-les-services-numeriques-ou-digital-services-act](https://www.vie-publique.fr/eclairage/285115-dsa-le-reglement-sur-les-services-numeriques-ou-digital-services-act)                 |
| Take It Down Act                                                                                     | [https://www.congress.gov/bill/119th-congress/senate-bill/146](https://www.congress.gov/bill/119th-congress/senate-bill/146)                                                                                                                           |
| NIST AI RMF                                                                                          | [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)                                                                                                                                         |
| Artificial Intelligence Regulation Threatens Free Expression                                         | [https://www.cato.org/briefing-paper/artificial-intelligence-regulation-threatens-free-expression](https://www.cato.org/briefing-paper/artificial-intelligence-regulation-threatens-free-expression)                                                   |
| AI regulation: EU vs. USA - opportunities and challenges for companies                               | [https://www.tucan.ai/blog/ai-regulation-eu-vs-usa-opportunities-and-challenges-for-companies/](https://www.tucan.ai/blog/ai-regulation-eu-vs-usa-opportunities-and-challenges-for-companies/)                                                         |
| Comparing the EU AI Act to Proposed AI-Related Legislation in the US                                 | [https://businesslawreview.uchicago.edu/online-archive/comparing-eu-ai-act-proposed-ai-related-legislation-us](https://businesslawreview.uchicago.edu/online-archive/comparing-eu-ai-act-proposed-ai-related-legislation-us)                           |
 
