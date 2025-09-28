# Des ressources pour aller plus loin sur le sujet de sécurité des LLMs et des chatbots

<img src="img/Cthulhu.png"  alt="resources">

> "Nous vivons sur une île paisible d'ignorance au milieu des mers noires de l'infini, et il n'était pas prévu que nous voyagions loin.", H.P. Lovecraft


## Sommaire

- [Lecture web](#lecture-web)
- [Livres](#livres)
- [Vidéos et conférences](#vidéos-et-conférences)
- [Lecture académique](#lecture-académique)


- [Cours et certifications](#cours-et-certifications)
  - [Cours](#cours)
  - [Certifications](#certifications)


- [Techniques d'attaques](#techniques-dattaques)
  - [Prompt Injection](#prompt-injection)
  - [Jailbreak](#jailbreak)

- [Playgrounds](#playgrounds)
  - [Top 5](#top-5)
  - [Autres Playgrounds](#autres-playgrounds)


- [Réseaux sociaux](#réseaux-sociaux)
  - [Twitter](#twitter)
    - [Top 10 Twitter comptes AI Sécurité et Prompt Injection](#top-10-twitter-comptes-ai-sécurité-et-prompt-injection)
    - [Autres Comptes Twitter AI Sécurité et Prompt Injection](#autres-comptes-twitter-ai-sécurité-et-prompt-injection)
  - [LinkedIn](#linkedin)


- [Outils et Scanners pour la Sécurité des LLM](#outils-et-scanners-pour-la-sécurité-des-llm)
- [Programmes Bug Bounty dédiés à la sécurité des modèles IA](#programmes-bug-bounty-dédiés-à-la-sécurité-des-modèles-ia)
  - [Détails clés sur le programme Anthropic](#détails-clés-sur-le-programme-anthropic)
  - [Détails clés sur le programme OpenAI](#détails-clés-sur-le-programme-openai)



## Lecture web

| Information                                                                                                                                  | Lien                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChatGPT Jailbreak Prompts: How to Unchain ChatGPT                                                                                            | [https://docs.kanaries.net/articles/chatgpt-jailbreak-prompt](https://docs.kanaries.net/articles/chatgpt-jailbreak-prompt)                                                                                                                                                                                                                                                                                                                                                                                         |
| ChatGPT jailbreak                                                                                                                            | [https://www.lebigdata.fr/chatgpt-dan](https://www.lebigdata.fr/chatgpt-dan)                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| How to Jailbreak ChatGPT 4 in 2024 (Prompt + Examples)                                                                                       | [https://weam.ai/blog/guide/jailbreak-chatgpt/](https://weam.ai/blog/guide/jailbreak-chatgpt/)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| The Developer's Playbook for Large Language Model Security: Building Secure AI Applications                                                  | [https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/](https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/)                                                                                                                                                                                                                                                                                                                                                         |
| Playing Language Game with LLMs Leads to Jailbreaking                                                                                        | [https://arxiv.org/pdf/2411.12762](https://arxiv.org/pdf/2411.12762)                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Unleashing Worms and Extracting Data: Escalating the Outcome of Attacks against RAG-based Inference in Scale and Severity Using Jailbreaking | [https://arxiv.org/pdf/2409.08045](https://arxiv.org/pdf/2409.08045)                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| La méthode "Crescendo" permet de jailbreaker l'IA de type LLM, en utilisant des invites en apparence inoffensives                            | [https://intelligence-artificielle.developpez.com/actu/356562/La-methode-Crescendo-permet-de-jailbreaker-l-IA-de-type-LLM-en-utilisant-des-invites-en-apparence-inoffensives-afin-de-produire-des-resultats-qui-seraient-normalement-filtres-et-refuses/](https://intelligence-artificielle.developpez.com/actu/356562/La-methode-Crescendo-permet-de-jailbreaker-l-IA-de-type-LLM-en-utilisant-des-invites-en-apparence-inoffensives-afin-de-produire-des-resultats-qui-seraient-normalement-filtres-et-refuses/) |
| Jailbreaking LLMs: A Comprehensive Guide (With Examples)                                                                                     | [https://www.promptfoo.dev/blog/how-to-jailbreak-llms/](https://www.promptfoo.dev/blog/how-to-jailbreak-llms/)                                                                                                                                                                                                                                                                                                                                                                                                     |
| Récentes Avancées dans la Recherche sur le Jailbreak des LLM                                                                                 | [hhttps://docs.kanaries.net/fr/topics/ChatGPT/llm-jailbreak-papers](https://docs.kanaries.net/fr/topics/ChatGPT/llm-jailbreak-papers)                                                                                                                                                                                                                                                                                                                                                                              |
| Defining LLM Red Teaming                                                                                                                     | [https://developer.nvidia.com/blog/defining-llm-red-teaming/](https://developer.nvidia.com/blog/defining-llm-red-teaming/)                                                                                                                                                                                                                                                                                                                                                                                         |
| Red Teaming LLMs: The Ultimate Step-by-Step LLM Red Teaming Guide                                                                            | [https://www.confident-ai.com/blog/red-teaming-llms-a-step-by-step-guide](https://www.confident-ai.com/blog/red-teaming-llms-a-step-by-step-guide)                                                                                                                                                                                                                                                                                                                                                                 |
| Planification de la Red Team pour les modèles de langage volumineux (LLMs) et leurs applications                                             | [https://learn.microsoft.com/fr-fr/azure/ai-services/openai/concepts/red-teaming](https://learn.microsoft.com/fr-fr/azure/ai-services/openai/concepts/red-teaming)                                                                                                                                                                                                                                                                                                                                                 |
| Red-Teaming Large Language Models                                                                                                            | [https://huggingface.co/blog/red-teaming](https://huggingface.co/blog/red-teaming)                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Multi-Chain Prompt Injection Attacks                                                                                                         | [https://labs.withsecure.com/publications/multi-chain-prompt-injection-attacks](https://labs.withsecure.com/publications/multi-chain-prompt-injection-attacks)                                                                                                                                                                                                                                                                                                                                                     |
| The State of Attacks on GenAI                                                                                                                | [https://45700826.fs1.hubspotusercontent-na1.net/hubfs/45700826/The%20State%20of%20Attacks%20on%20GenAI%20-%20Pillar%20Security.pdf](https://45700826.fs1.hubspotusercontent-na1.net/hubfs/45700826/The%20State%20of%20Attacks%20on%20GenAI%20-%20Pillar%20Security.pdf)                                                                                                                                                                                                                                           |
| Embrace The Red                                                                                                                              | [https://embracethered.com](https://embracethered.com)                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| LLM Security                                                                                                                                 | [https://llmsecurity.net/](https://llmsecurity.net/)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Offensive ML Playbook                                                                                                                        | [https://wiki.offsecml.com/](https://wiki.offsecml.com/)                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Intelligence Artificielle : les travaux de l’ANSSI                                                                                           | [https://cyber.gouv.fr/intelligence-artificielle-les-travaux-de-lanssi](https://cyber.gouv.fr/intelligence-artificielle-les-travaux-de-lanssi)                                                                                                                                                                                                                                                                                                                                                                     | 
| Arcanum AI Sec Resource Hub                                                                                                                  | [https://arcanum-sec.github.io/ai-sec-resources/](https://arcanum-sec.github.io/ai-sec-resources/)                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                         |
| Announcing the OWASP Gen AI Red Teaming Guide                                                                                                | [https://genai.owasp.org/2025/01/22/announcing-the-owasp-gen-ai-red-teaming-guide/](https://genai.owasp.org/2025/01/22/announcing-the-owasp-gen-ai-red-teaming-guide/)                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                         |
| Impact of AI on cyber threat from now to 2027                                                                                                | [https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027](https://www.ncsc.gov.uk/report/impact-ai-cyber-threat-now-2027)                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                         |


## Livres

| Titre                                                                                                             | Auteur(s)                           | Partie concernée  | Lien                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------------------|----------------------------------------------------------------------------------------------------------------|
| Generative AI for Software Development                                                                            | Sergio Pereira                      | Tout le livre     | https://learning.oreilly.com/library/view/generative-ai-for/9781098162269                                      |
| The Developer's Playbook for Large Language Model Security: Building Secure AI Applications                       | Steve Wilson                        | Tout le livre     | https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/                                    |
| AI Engineering: Building Applications with Foundation Models                                                      | Chip Huyen                          | Tout le livre     | https://www.oreilly.com/library/view/ai-engineering/9781098166298/                                             |
| Hands-On Large Language Models: Language Understanding and Generation                                             | Jay Alammar, Maarten Grootendorst   | Tout le livre     | https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/                                    |
| Adversarial ai attacks, mitigations, and defense strategies                                                       | John Sotiropoulos                   | Tout le livre     | https://www.packtpub.com/en-ch/product/adversarial-ai-attacks-mitigations-and-defense-strategies-9781835087985 |
| AI-Driven Cybersecurity and Threat Intelligence: Cyber Automation, Intelligent Decision-Making and Explainability | Iqbal H. Sarker                     | Tout le livre     | https://link.springer.com/book/10.1007/978-3-031-54497-2                                                       |
| Red Teaming AI: Attacking & Defending Intelligent Systems                                                         | Philip A. Dursey                    | Tout le livre     | https://www.amazon.com.au/Red-Teaming-Attacking-Defending-Intelligent-ebook/dp/B0F88SGMXG                      |
| Building Generative AI Services with FastAPI                                                                      | Alireza Parandeh                    | Tout le livre     | https://www.oreilly.com/library/view/building-generative-ai/9781098160296/                                     |


## Vidéos et conférences

| Titre                                                                          | Intervenant(s)                    | Événement                            | Lien                                                |
|--------------------------------------------------------------------------------|-----------------------------------|--------------------------------------|-----------------------------------------------------|
| Hijacking AI Memory: Inside Johann Rehberger's Chat GPT Security Breakthrough  | Strike Graph                      | Vidéo Youtube                        | https://www.youtube.com/watch?v=_wFNroN9g_0         |  
| jhaddix                                                                        | jhaddix                           | Vidéo Youtube                        | https://www.youtube.com/c/jhaddix                   |
| Hacking AI is TOO EASY (it should be illegal)                                  | NetworkChuck                      | Vidéo Youtube                        | https://www.youtube.com/watch?v=Qvx2sVgQ-u0s        |
| Attacking AI Version 1.1 w/ Jason Haddix                                       | Antisyphon Training               | Vidéo Youtube                        | https://www.youtube.com/watch?v=0MDfKTJQQyE         |
| MITRE ATLAS™ Introduction                                                      | mitrecorp (The MITRE Corporation) | Vidéo Youtube                        | https://www.youtube.com/watch?v=3FN9v-y-C-w         |
| Anatomy of an AI ATTACK: MITRE ATLAS                                           | IBM Technology                    | Vidéo Youtube                        | https://www.youtube.com/watch?v=QhoG74PDFyc         |
| LLM Hacking Defense: Strategies for Secure AI                                  | IBM Technology                    | Vidéo Youtube                        | https://www.youtube.com/watch?v=y8iDGA4Y650         |
| What Is a Prompt Injection Attack?                                             | IBM Technology                    | Vidéo Youtube                        | https://www.youtube.com/watch?v=jrHRe9lSqqA         |
| [DevLille 2025] Je malmène ton LLM en direct avec 10 failles de sécurités      | DevLille                          | Vidéo Youtube                        | https://www.youtube.com/watch?v=un50L6Kdszg         |




## Lecture académique

| Titre                                                                                  | Type                         | Auteur(s)        | Lien                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Attention Is All You Need                                                              | Article scientifique (arXiv) | Vaswani et al.   | https://arxiv.org/abs/1706.03762                                                                                      |
| ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs                      | Article scientifique (arXiv) | -                | https://arxiv.org/abs/2402.11753                                                                                      |
| Trust No AI: Prompt Injection Along The CIA Security Triad                             | Article scientifique (arXiv) | Johann Rehberger | https://arxiv.org/abs/2412.06090                                                                                      |
| owasp llm TOP 10                                                                       | Livre blanc                  | OWASP            | https://owasp.org/www-project-top-10-for-large-language-model-applications/                                           |
| GenAI Incident Response Guide                                                          | Livre blanc                  | OWASP            | https://genai.owasp.org/resource/genai-incident-response-guide-1-0/                                                   |
| Generative AI: UNESCO study reveals alarming evidence of regressive gender stereotypes | Étude                        | UNESCO           | https://www.unesco.org/en/articles/generative-ai-unesco-study-reveals-alarming-evidence-regressive-gender-stereotypes |
| Papers on ArXiv                                                                        | Paper stack                  | Dreadnode        | http://dreadnode.notion.site/?v=74ab79ed1452441dab8a1fa02099fedb                                                      |


## Cours et certifications

### Cours

| Titre                                                                                 | Plateforme                     | Lien                                                                                                                              |
|---------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Artificial Intelligence for Beginners - A Curriculum                                  | GitHub                         | https://microsoft.github.io/AI-For-Beginners/                                                                                     |
| Beginner: Introduction to Generative AI Learning Path                                 | Google Cloud Skills Boost      | https://www.cloudskillsboost.google/paths/118                                                                                     |
| HarvardX: CS50's Introduction to Artificial Intelligence with Python                  | edX                            | https://www.edx.org/course/cs50s-introduction-to-artificial-intelligence-with-python                                              |
| Prompt Engineering for ChatGPT                                                        | Coursera                       | https://www.coursera.org/learn/prompt-engineering                                                                                 |
| Big Data, Artificial Intelligence, and Ethics                                         | Coursera                       | https://www.coursera.org/learn/big-data-ai-ethics                                                                                 |
| Generative AI with Large Language Models                                              | Coursera                       | https://www.coursera.org/learn/generative-ai-with-llms                                                                            |
| Présentation de la sécurité dans le monde de l'IA                                     | Google                         | https://www.cloudskillsboost.google/paths/1283/course_templates/1147?locale=fr                                                    |
| Red Teaming LLM Applications                                                          | DeepLearning.AI                | https://learn.deeplearning.ai/courses/red-teaming-llm-applications                                                                |
| Exploring Adversarial Machine Learning                                                | NVIDIA                         | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-DS-03+V1                                                 |
| Microsoft AI Red Team                                                                 | Microsoft Learn                | https://learn.microsoft.com/en-us/security/ai-red-team/                                                                           |
| LLM Red Teaming                                                                       | OffSec                         | https://www.offsec.com/learning/paths/llm-red-teaming                                                                             |
| IBM: Spécialisation L'IA générative d'IBM pour les professionnels de la cybersécurité | Coursera                       | https://www.coursera.org/specializations/generative-ai-for-cybersecurity-professionals                                            |
| Certified AI/ML Pentester (C-AI/MLPen)                                                | Pentesting Exams               | https://pentestingexams.com/product/certified-ai-ml-pentester/                                                                    |
| Portswigger Web Security Academy                                                      | Portswigger                    | https://portswigger.net/web-security/llm-attacks                                                                                  |
| Gandalf                                                                               | Lakera                         | https://gandalf.lakera.ai/                                                                                                        |
| IBM                                                                                   | IBM                            | https://www.ibm.com/topics/prompt-injection                                                                                       |

### Certifications

| Titre                                                                                 | Plateforme                     | Lien                                                                                                                              |
|---------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Certified AI/ML Pentester (C-AI/MLPen)                                                | Pentesting Exams               | https://pentestingexams.com/product/certified-ai-ml-pentester/                                                                    |

## Techniques d'attaques

### Prompt Injection

| Titre / Description                           | Type                | Lien                                                                                                                                                     |
|-----------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| SecLists - LLM Testing                        | Liste de tests      | [https://github.com/danielmiessler/SecLists/tree/master/Ai/LLM_Testing](https://github.com/danielmiessler/SecLists/tree/master/Ai/LLM_Testing)           |
| PIPE                                          | Projet GitHub       | [https://github.com/jthack/PIPE](https://github.com/jthack/PIPE)                                                                                         |
| Adversarial Prompts - Chetan-k-p              | Dataset Huggingface | [https://huggingface.co/datasets/Chetan-k-p/adversarial-prompts](https://huggingface.co/datasets/Chetan-k-p/adversarial-prompts)                         |
| Successful Adversarial Prompts - rishitchugh  | Dataset Huggingface | [https://huggingface.co/datasets/rishitchugh/successful_adversarial_prompts](https://huggingface.co/datasets/rishitchugh/successful_adversarial_prompts) |
| Prompt Injection Cleaned Dataset - imoxto     | Dataset Huggingface | [https://huggingface.co/datasets/imoxto/prompt_injection_cleaned_dataset](https://huggingface.co/datasets/imoxto/prompt_injection_cleaned_dataset)       |
| Datasets collection - Harelix                 | Dataset Huggingface | [https://huggingface.co/Harelix/datasets](https://huggingface.co/Harelix/datasets)                                                                       |
| Prompt Injections - yanismiraoui              | Dataset Huggingface | [https://huggingface.co/datasets/yanismiraoui/prompt_injections](https://huggingface.co/datasets/yanismiraoui/prompt_injections)                         |
| Hackaprompt Dataset - hackaprompt             | Dataset Huggingface | [https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset](https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset)                       |
| Prompt Injections - deepset                   | Dataset Huggingface | [https://huggingface.co/datasets/deepset/prompt-injections](https://huggingface.co/datasets/deepset/prompt-injections)                                   |


### Jailbreak

| Titre / Description                         | Type                | Lien                                                                                                                                                   |
|---------------------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| L1B3RT4S - elder-plinius                    | Projet GitHub       | [https://github.com/elder-plinius/L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S)                                                                 |
| J2 Playground - Scale                       | Démo/Playground     | [https://scale.com/research/j2/playground](https://scale.com/research/j2/playground)                                                                   |
| ChatGPT Jailbreak Prompts - rubend18        | Dataset Huggingface | [https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts](https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts)               |
| In-the-wild Jailbreak Prompts - TrustAIRLab | Dataset Huggingface | [https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts) |
| Jailbreak Classification - jackhhao         | Dataset Huggingface | [https://huggingface.co/datasets/jackhhao/jailbreak-classification](https://huggingface.co/datasets/jackhhao/jailbreak-classification)                 |
| JailBreakV-28k - JailbreakV-28K             | Dataset Huggingface | [https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k](https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k)                         |
| Vigil Jailbreak ada-002 - deadbits          | Dataset Huggingface | [https://huggingface.co/datasets/deadbits/vigil-jailbreak-ada-002](https://huggingface.co/datasets/deadbits/vigil-jailbreak-ada-002)                   |
| JailbreakHub - walledai                     | Dataset Huggingface | [https://huggingface.co/datasets/walledai/JailbreakHub](https://huggingface.co/datasets/walledai/JailbreakHub)                                         |
| JBB-Behaviors - JailbreakBench              | Dataset Huggingface | [https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors)                           |


## Playgrounds

### Top 5

| Titre / Description                       | Type                 | Lien                                                                                                 |
|-------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------|
| Web LLM Attacks - PortSwigger             | Playground / Guide   | [https://portswigger.net/web-security/llm-attacks](https://portswigger.net/web-security/llm-attacks) |
| Prompt Airlines - AI Security CTF by Wiz  | Playground / CTF     | [https://promptairlines.com/](https://promptairlines.com/)                                           |
| MyLLMBank                                 | Démo LLM Web         | [https://myllmbank.com/](https://myllmbank.com/)                                                     |
| MyLLMDOC                                  | Démo LLM Web         | [https://myllmdoc.com/](https://myllmdoc.com/)                                                       |
| TensorTrust.ai                            | Démo LLM Sécurité    | [https://tensortrust.ai/](https://tensortrust.ai/)                                                   |


### Autres Playgrounds

| Titre / Description                              | Type                           | Lien                                                                                                                    |
|--------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Gandalf Baseline                                 | Playground LLM                 | [https://gandalf.lakera.ai/baseline](https://gandalf.lakera.ai/baseline)                                                |
| Prompt Injection Guide - Learn Prompting         | Guide pédagogique              | [https://learnprompting.org/docs/prompt_hacking/injection](https://learnprompting.org/docs/prompt_hacking/injection)    |
| HackAPrompt Playground                           | Playground de compétition      | [https://learnprompting.org/hackaprompt-playground](https://learnprompting.org/hackaprompt-playground)                  |
| HackAPrompt 2023 - AI Red Teaming Challenge      | Compétition AI red-teaming     | [https://www.aicrowd.com/challenges/hackaprompt-2023](https://www.aicrowd.com/challenges/hackaprompt-2023)              |
| GPA (Generative Prompt Assistant)                | Playground LLM                 | [https://gpa.43z.one/](https://gpa.43z.one/)                                                                            |
| Pokebot - Detox AI                               | Playground d'interaction       | [https://huggingface.co/spaces/detoxioai/Pokebot](https://huggingface.co/spaces/detoxioai/Pokebot)                      |
| Wrong Secrets Challenge #32                      | Challenge de sécurité          | [https://wrongsecrets.herokuapp.com/challenge/challenge-32](https://wrongsecrets.herokuapp.com/challenge/challenge-32)  |
| HackMerlin                                       | Plateforme de hacking AI       | [https://hackmerlin.io/](https://hackmerlin.io/)                                                                        |
| Hack The Box Academy - Module sur prompt hacking | Formation en cybersécurité     | [https://academy.hackthebox.com/module/details/297](https://academy.hackthebox.com/module/details/297)                  |
| Immersive Labs Prompting.ai                      | Formation en sécurité IA       | [https://prompting.ai.immersivelabs.com/](https://prompting.ai.immersivelabs.com/)                                      |


## Réseaux sociaux

### Twitter

#### Top 10 Twitter comptes AI Sécurité et Prompt Injection

| Compte Twitter                       | Description courte                                             | Lien                                                           |
|--------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------|
| wunderwuzzi23                        | Expert en sécurité IA et prompt hacking                        | [https://x.com/wunderwuzzi23](https://x.com/wunderwuzzi23)     |
| elder_plinius (Pliny the Liberator)  | Chercheur en sécurité des LLMs, jailbreaks et prompt injection | [https://x.com/elder_plinius](https://x.com/elder_plinius)     |
| rez0__                               | Spécialiste sécurité IA                                        | [https://x.com/rez0__](https://x.com/rez0__)                   |
| llm_sec                              | Actualités et analyses sécurité LLM                            | [https://x.com/llm_sec](https://x.com/llm_sec)                 |
| JS0N Haddix                          | Chercheur et consultant en sécurité IA                         | [https://x.com/jhaddix](https://x.com/jhaddix)                 |
| dcapitella                           | Expert en IA et cybersécurité                                  | [https://x.com/dcapitella](https://x.com/dcapitella)           |
| mbrg0                                | Analyste sécurité IA                                           | [https://x.com/mbrg0](https://x.com/mbrg0)                     |
| kgreshake                            | Recherche et défense IA                                        | [https://x.com/kgreshake](https://x.com/kgreshake)             |
| adonis_singh                         | Expert en AI red teaming                                       | [https://x.com/adonis_singh](https://x.com/adonis_singh)       |
| sanderschulhoff                      | CEO HackAPrompt, expert prompt engineering et sécurité IA      | [https://x.com/sanderschulhoff](https://x.com/sanderschulhoff) |


#### Autres Comptes Twitter AI Sécurité et Prompt Injection

| Compte Twitter    | Description courte                                                                            | Lien                                                         |
|-------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| LeonDerczynski    | Professeur associé en informatique, expert LLM, NLP, sécurité IA (@NVIDIA, @ITU Copenhagen)   | [https://x.com/LeonDerczynski](https://x.com/LeonDerczynski) |
| goodside          | Chercheur en sécurité IA et prompt injection                                                  | [https://x.com/goodside](https://x.com/goodside)             |
| p1njc70r          | Expert en sécurité informatique et IA                                                         | [https://x.com/p1njc70r](https://x.com/p1njc70r)             |
| richlundeen       | Spécialiste cybersécurité et IA                                                               | [https://x.com/richlundeen](https://x.com/richlundeen)       |
| GalMalka6         | Chercheur en IA et sécurité                                                                   | [https://x.com/GalMalka6](https://x.com/GalMalka6)           |
| tamirishaysh      | Analyste en sécurité IA et red teaming                                                        | [https://x.com/tamirishaysh](https://x.com/tamirishaysh)     |
| martinvoelk       | Chercheur et consultant en sécurité IA                                                        | [https://x.com/martinvoelk](https://x.com/martinvoelk)       |
| simonw            | Chercheur AI, spécialiste sécurité et NLP                                                     | [https://x.com/simonw](https://x.com/simonw)                 |
| LakeraAI          | Organisation spécialisée en sécurité LLM                                                      | [https://x.com/LakeraAI](https://x.com/LakeraAI)             |


### LinkedIn

| Profil LinkedIn             | Description courte                                                                 | Lien                                                                                                             |
|-----------------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Leon Derczynski             | LLM security at NVIDIA. Prof at ITU Copenhagen. Founder of garak. ACL SIGSEC Chair | [https://www.linkedin.com/in/leon-derczynski/](https://www.linkedin.com/in/leon-derczynski/)                     |
| Nchikanov (Nikita Chikanov) | Security Software Engineer II at Microsoft                                         | [https://www.linkedin.com/in/nchikanov/](https://www.linkedin.com/in/nchikanov/)                                 |
| Martin Pouliot              | Senior Security Researcher at Microsoft                                            | [https://www.linkedin.com/in/martin-pouliot-266ab0105/](https://www.linkedin.com/in/martin-pouliot-266ab0105/)   |
| Joseph T Lucas              | Data and AI Security at Nvidia                                                     | [https://www.linkedin.com/in/josephtlucas/](https://www.linkedin.com/in/josephtlucas/)                           |
| J Sotiropoulos              | Cyber for the Era of AI [...]  Best-selling author ( Adversarial AI)               | [https://www.linkedin.com/in/jsotiropoulos/](https://www.linkedin.com/in/jsotiropoulos/)                         |
| Ads Dawson                  | Staff AI Security Researcher [...] OWASP LLM Apps Tech Lead, Toronto Lead, ASVS    | [https://www.linkedin.com/in/adamdawson0/](https://www.linkedin.com/in/adamdawson0/)                             |
| Kristian Fagerlie           | AI -YouTube - KI - Generative AI -AI Engineer                                      | [https://www.linkedin.com/in/kristian-fagerlie/](https://www.linkedin.com/in/kristian-fagerlie/)                 |
| Jason Haddix                | Hacker, CEO, CISO [...] in the Cyber Security and AI spaces                        | [https://www.linkedin.com/in/jhaddix/](https://www.linkedin.com/in/jhaddix/)                                     |
| Sam Bent                    | Journalist [...] Darknet Expert (Ex Vendor & DNM Admin) - DEFCON/SANS Speaker      | [https://www.linkedin.com/in/sam-bent/](https://www.linkedin.com/in/sam-bent/)                                   |
| Dreadnode                   | Advancing the state of offensive security                                          | [https://www.linkedin.com/company/dreadnode/](https://www.linkedin.com/company/dreadnode/)                       |


## Outils et Scanners pour la Sécurité des LLM

| Outil / Projet                  | Description                                                                             | Lien                                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Prompt Injection Taxonomy       | Taxonomie de menaces et analyse des vulnérabilités en IA                                | [https://github.com/Arcanum-Sec/arc_pi_taxonomy/](https://github.com/Arcanum-Sec/arc_pi_taxonomy/)     |
| Promptfoo                       | Plateforme de tests automatisés pour détecter vulnérabilités dans les prompts LLM       | [https://www.promptfoo.dev](https://www.promptfoo.dev)                                                 |
| Agentic Radar                   | Outil d’analyse et détection des vulnérabilités des LLM                                 | [https://github.com/spix-ai/agentic-radar](https://github.com/spix-ai/agentic-radar)                   |
| Garak                           | Scanner de vulnérabilités LLM par NVIDIA, testant hallucinations, injections, jailbreak | [https://github.com/NVIDIA/garak](https://github.com/NVIDIA/garak)                                     |
| Spikee                          | Outil d’analyse sécurité LLM en open source                                             | [https://github.com/WithSecureLabs/spikee](https://github.com/WithSecureLabs/spikee)                   |
| Promptmap                       | Évalue la sensibilité aux injections de prompt par analyse ciblée                       | [https://github.com/utkusen/promptmap](https://github.com/utkusen/promptmap)                           |
| LLMmap                          | Cartographie et tests de sécurité pour LLM                                              | [https://github.com/pasquini-dario/LLMmap](https://github.com/pasquini-dario/LLMmap)                   |
| Eiskard                         | Plateforme d’évaluation de la qualité et des risques des modèles IA                     | [https://github.com/Giskard-Al/eiskard](https://github.com/Giskard-Al/eiskard)                         |
| PyRIT                           | Outil d’analyse statique et dynamique par Microsoft pour évaluer la robustesse des LLM  | [https://github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)                                       |
| MCP Scan                        | Framework d’analyse de vulnérabilités LLM                                               | [https://github.com/invariantlabs-ai/mcp-scan](https://github.com/invariantlabs-ai/mcp-scan)           |
| CoSAI                           | Coalition for Secure AI (CoSAI) OASIS Open Project                                      | [https://github.com/cosai-oasis/oasis-open-project](https://github.com/cosai-oasis/oasis-open-project) |
| AGNTCY                          | réferencecement de standards                                                            | [https://github.com/agntcy](https://github.com/agntcy)                                                 |
| oss-fuzz-gen                    | Outil de sécurité pour LLM par Google                                                   | [https://github.com/google/oss-fuzz-gen](https://github.com/google/oss-fuzz-gen)                       |
 

## Programmes Bug Bounty dédiés à la sécurité des modèles IA

| Programme                            | Description                                                                                                                                              | Lien                                                                                                             |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Pangea AI Escape Room                | Environnement de test ludique pour défis de sécurité IA                                                                                                  | [https://pangea.cloud/landing/ai-escape-room/](https://pangea.cloud/landing/ai-escape-room/)                     |
| Anthropic Model Safety Bug Bounty    | Programme invite-only pour détecter des vulnérabilités universelles et jailbreaks critiques, récompenses jusqu'à 25 000 USD, focus CBRN et cybersécurité | [https://www.anthropic.com/news/model-safety-bug-bounty](https://www.anthropic.com/news/model-safety-bug-bounty) |
| OpenAI Bug Bounty Program            | Programme public récompensant la découverte de vulnérabilités dans les systèmes OpenAI, avec une gestion via Bugcrowd, récompenses jusqu'à 20 000 USD    | [https://openai.com/index/bug-bounty-program/](https://openai.com/index/bug-bounty-program/)                     |
| RedArena AI                          | Plateforme proposant des challenges de sécurité et tests de red teaming IA                                                                               | [https://redarena.ai](https://redarena.ai)                                                                       |

### Détails clés sur le programme Anthropic

- Objectif : Identifier et corriger les failles permettant de contourner les protections de sécurité des modèles, notamment les attaques dites "universal jailbreak".
- Récompenses : Jusqu'à 25 000 USD pour les découvertes majeures.
- Cibles : Vulnérabilités à haut risque, avec un accent sur les domaines chimiques, biologiques, radiologiques, nucléaires (CBRN) et cybersécurité.
- Format : Programme initialement sur invitation via HackerOne, avec accès anticipé aux systèmes de mitigation en test.
- Collaboration : Souligne l'importance d'une collaboration étroite avec la communauté mondiale de chercheurs en sécurité IA.

### Détails clés sur le programme OpenAI

- Objectif : Encourager la communauté à signaler failles, bugs et vulnérabilités dans les systèmes OpenAI.
- Récompenses : De 200 USD pour des problèmes mineurs à 20 000 USD pour failles majeures.
- Gestion : Programmé via la plateforme Bugcrowd pour faciliter la soumission et la gestion.
- Accessibilité : Programme ouvert à tous les chercheurs en sécurité.
