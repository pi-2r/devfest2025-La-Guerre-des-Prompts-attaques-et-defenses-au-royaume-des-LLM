# Once upon a time in a digital world...

[<img src="img/step1.jpg" alt="hobbiton" width="800" height="450">](https://www.youtube.com/watch?v=dDKVKG3ESsk)
> "Home is now behind you, the world is ahead!", Gandalf, The Hobbit

## 🎯 Objectives of this step

- Understand the origins of LLMs and how they work
- Discover the basic concepts of artificial intelligence, neural networks, and LLMs
- Explore the Transformer architecture and its impact on natural language processing
- Identify the most used generative AI applications, notably chatbots and copilots
- Analyze the impact of LLMs on professional productivity

## Table of contents

- [2022 The Launch](#2022-the-launch)
- [Artificial Intelligence, Neural Networks, and LLMs](#artificial-intelligence-neural-networks-and-llms)
- [Transformers: Origins and Architecture](#transformers-origins-and-architecture)
  - [Some Application Examples](#some-application-examples)
- [The 2 Most Used Generative AI Applications in the World](#the-2-most-used-generative-ai-applications-in-the-world)
  - [Chatbots](#chatbots)
    - [Some Chatbot Examples](#some-chatbot-examples)
  - [Copilots](#copilots)
    - [Some Copilot Examples](#some-copilot-examples)
  - [Chatbots vs Copilots](#chatbots-vs-copilots)
- [The Impact of LLMs on Professional Productivity](#the-impact-of-llms-on-professional-productivity)
- [Next Step](#next-step)
- [Resources](#resources)

## 2022 The Launch

LLMs (large language models) made their appearance to the general public with the official launch of ChatGPT on November 30, 2022.
In less than a week, the application capable of answering anything for anyone managed to attract its first millions of users. By January 2023, just two months after its launch, ChatGPT surpassed 100 million users, becoming the second fastest-growing digital application in computing history, far ahead of TikTok, Facebook, and Instagram.

<a href="https://www.visualcapitalist.com/threads-100-million-users/" target="_blank">
  <img src="https://www.visualcapitalist.com/wp-content/uploads/2023/07/CP_Threads-Fastest-100-Million.jpg" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://www.visualcapitalist.com/threads-100-million-users/" target="_blank"><em>source: visualcapitalist.com</em></a>

Since the appearance of ChatGPT, language models (LLMs) have been propelled to the forefront of public attention. This exposure has generated many misconceptions, sometimes exaggerated — such as fears that artificial intelligence will replace humans — as well as concerns regarding the nature of generated responses, particularly about the supposed ease of obtaining sensitive or dangerous information.

> To better understand the reality behind these misconceptions, it is relevant to refer to interviews and books by Luc Julia, co-creator of Siri, who provides an enlightened and nuanced perspective on the true capabilities of AI. As for security and reliability of generated content, I invite you to continue this codelab to explore these issues in more detail.

Moreover, since this launch, major technology companies have intensified their efforts in the race for artificial intelligence, far surpassing the initial advances of ChatGPT.

<a href="https://www.visualcapitalist.com/charted-the-growth-of-big-tech-since-chatgpts-launch/" target="_blank">
  <img src="https://www.visualcapitalist.com/wp-content/uploads/2024/12/Growth-of-Big-Tech-Firms_WEB.jpg" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://www.visualcapitalist.com/charted-the-growth-of-big-tech-since-chatgpts-launch/" target="_blank"><em>source: visualcapitalist.com</em></a>

## Artificial Intelligence, Neural Networks, and LLMs

In the media, it is common to encounter different terms used specifically to talk about artificial intelligence.
Some will use the term neural networks, others the term LLM, or simply artificial intelligence; however, these three terms represent different facets of a larger landscape of machine learning and computational intelligence.

Let's try to distinguish each of these three terms:

**AI:**
Artificial Intelligence (or Augmented Intelligence for some) is essentially a multidisciplinary field aimed at creating systems capable of performing tasks that would normally require human intelligence. Such tasks include problem-solving, perception, and language understanding.
AI corresponds to a wide range of technologies, methodologies, and systems from rule-based systems to machine learning algorithms, serving as a generic term for multiple approaches to achieve artificial intelligence.

**Neural Networks:**
This part of artificial intelligence is inspired by the functioning of the human brain. Neural networks are computational models designed to recognize patterns and make decisions based on the data they process. They can sometimes be simple (referred to as shallow neural networks) or more complex (known as deep neural networks).
In all cases, neural networks form the essential basis of many contemporary AI applications, such as image recognition, natural language processing, and autonomous vehicle driving.

**LLM:**
Simply put, LLMs (large language models) are a specific type of neural network based on advanced forms of neural networks like transformer models to understand and generate text from training data. Their strength lies in handling linguistic tasks ranging from simple text input to drafting a document of hundreds of pages without distorting the main idea.

<img src="https://i0.wp.com/www.phdata.io/wp-content/uploads/2024/10/article-image1-6.png" alt="image" width="450" style="transition:0.3s;">

<a href="https://phdata.io" target="_blank"><em>source: phdata.io</em></a>

## Transformers: Origins and Architecture

We are not talking about Michael Bay movies, but continuing to talk about AI.

The Transformer architecture was introduced in a scientific paper titled "**Attention is All You Need**",
published in 2017 by a team from Google Brain.

<img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/0*jKqypwGzmDv7KDUZ.png" alt="image" width="450" style="transition:0.3s;">

<a href="https://medium.com" target="_blank"><em>source: medium.com</em></a>

The paper presented an innovative approach for natural language processing (**NLP**), choosing to move away from traditional models that relied mainly on recurrent neural networks (**RNN**) and convolutional neural networks (**CNN**).

The **Transformer** brought a major advance: **the self-attention mechanism**.

Thanks to this process, the model can determine the relative importance of each word in a sentence, which significantly improves its understanding of context (and this is where prompt injection attacks target).

Before transformers, **traditional neural networks**, like **RNNs** and **CNNs**, had major limitations in understanding natural language, mainly because of their difficulty capturing context over long sequences. They were unable to apprehend entire texts and struggled to convey overall meaning and nuances.

The Transformer architecture filled this gap, revolutionizing language processing by AI.

Since then, the Transformer architecture has represented a real turning point in AI.
Initially designed for text understanding and generation, it quickly proved effective in many other fields, far exceeding initial expectations by researchers and engineers!

### Some Application Examples

| Domain                | Key Applications                                   | Main Impact                                               |
|-----------------------|---------------------------------------------------|-----------------------------------------------------------|
| Natural Language Processing | Translation, summarization, QA, sentiment analysis | New benchmarks, sometimes outperforming humans            |
| Computer Vision        | Image classification, object detection, segmentation (ViT) | Competitive or better performance than CNNs                |
| Speech Recognition    | Spoken language understanding, hybrid models (conformer) | New standards in voice recognition                         |
| Autonomous Systems    | Autonomous vehicles, contextual understanding     | Powers self-driving cars                                   |
| Healthcare            | Drug discovery, medical image analysis, diagnostics | Accelerates research and improves diagnostic accuracy      |

## The 2 Most Used Generative AI Applications in the World

Beyond the examples described above, we focus on two types of AI applications based on LLMs: chatbots and copilots.

### Chatbots

Chatbots are software designed to converse naturally with users. They are widely used in customer service to answer questions and assist clients, but also in diverse fields like video games or interactive storytelling.

#### Some Chatbot Examples

| Company               | Main chatbot function                               | Chatbot Link                                                                                                     |
|-----------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| SNCF Connect & Tech   | Answers customer questions about FAQs or G30       | [https://www.sncf-connect.com/bot](https://www.sncf-connect.com/bot)                                           |
| Sephora               | Advises customers on products adapted to their skin| [https://www.messenger.com/t/sephorafrance](https://www.messenger.com/t/sephorafrance)                         |
| H&M                   | Helps find clothes and accessories by style        | [https://www2.hm.com/fr_fr/service-clients/contact.html](https://www2.hm.com/fr_fr/service-clients/contact.html)|
| KLM                   | Answers questions about flights                      | [https://www.messenger.com/t/331735092583](https://www.messenger.com/t/331735092583)                           |

### Copilots

Copilots are software designed to assist with writing, coding, and research. They generate ideas, detect errors, and optimize user work.

Although still in development, they could transform our ways of working and learning.

#### Some Copilot Examples

| Tools / Services                                       | Main Function                                                         |
|------------------------------------------------------|-----------------------------------------------------------------------|
| Grammarly, ProWritingAid                             | Improve writing: correction, style, personalized feedback             |
| GitHub Copilot, Gemini Code Assist, AWS CodeWhisperer | Assist coding: suggestions, translation, error detection              |
| Copilot for Microsoft 365, Gemini for Google Workspace | Optimize productivity and creativity in office suites                 |

### Chatbots vs Copilots

Here is a comparison table highlighting the differences and similarities between chatbots and copilots:

| Aspect             | Chatbots                         | Copilots                          | Similarities                          |
|--------------------|---------------------------------|----------------------------------|-------------------------------------|
| Technology         | Based on LLMs                   | Based on LLMs                    | Generate text, assist users          |
| Primary function   | Simulate conversation           | Help accomplish specific tasks   |                                     |
| Common usage       | Customer service, interaction   | Writing, coding, research        |                                     |
| Interactivity      | Highly interactive              | More task execution oriented     |                                     |

## The Impact of LLMs on Professional Productivity

<a href="https://www.visualcapitalist.com/charted-productivity-gains-from-using-ai/" target="_blank">
  <img src="https://www.visualcapitalist.com/wp-content/uploads/2025/06/Human-vs-AI-Site.png" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://www.visualcapitalist.com/charted-productivity-gains-from-using-ai/" target="_blank"><em>source: visualcapitalist.com</em></a>

The effectiveness of large language models (LLMs) in generative AI applications is now widely recognized. As these tools integrate, and even become indispensable in professional environments, their influence on productivity is tangibly confirmed.

- Integration of generative AI in workflows has reduced the average time to complete various tasks by over 60%.
- Contrary to the misconception that AI would replace human work, data shows that professionals equipped with AI tools perform their tasks much more efficiently.

Concrete examples of improvement:

- For content writing, the average time decreased from 80 minutes to only 25 minutes thanks to generative AI.
- For complex cognitive tasks such as math, system analysis, or operations, AI saves more than an hour per task.

In short, generative AI is not limited to task automation: it multiplies professional efficiency by providing access to unprecedented productivity levels. This progress is notably explained by recent models like OpenAI’s latest o3, which exhibit reasoning abilities equivalent, or even superior, to those of a person with an IQ above 130.

<details>
  <summary>Check the typology of intelligence levels of models.</summary>

<a href="https://www.visualcapitalist.com/ranked-the-smartest-ai-models-by-iq/" target="_blank">
  <img src="https://www.visualcapitalist.com/wp-content/uploads/2025/06/IQ-of-AI_02-web.jpg" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://www.visualcapitalist.com/ranked-the-smartest-ai-models-by-iq/" target="_blank"><em>source: visualcapitalist.com</em></a>
</details>

## Next Step

- [Step 2](step_2.md)

## Resources

| Information                                                       | Link                                                                                     |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| The 7 Steps of Machine Learning                                  | [https://www.youtube.com/watch?v=nKW8Ndu7Mjw](https://www.youtube.com/watch?v=nKW8Ndu7Mjw) |
| LLM Engineer's Handbook                                          | [https://www.packtpub.com/en-fr/product/llm-engineers-handbook-9781836200062](https://www.packtpub.com/en-fr/product/llm-engineers-handbook-9781836200062) |
| AI Engineering                                                  | [https://www.oreilly.com/library/view/ai-engineering/9781098166298/](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) |
| Generative AI for Software Development                          | [https://learning.oreilly.com/library/view/generative-ai-for/9781098162269](https://learning.oreilly.com/library/view/generative-ai-for/9781098162269) |
| Developer’s Playbook for Large Language Model Security          | [https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/](https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/) |
| How AI Works: From Sorcery to Science                           | [https://www.amazon.com/How-AI-Works-Sorcery-Science/dp/1718503725](https://www.amazon.com/How-AI-Works-Sorcery-Science/dp/1718503725) |
| AI, Machine Learning, Neural Networks, Deep Learning Concept List with Samples | [https://medium.com/@anixlynch/ai-machine-learning-neural-networks-deep-learning-concept-list-w-samples-28ac4d67eb65](https://medium.com/@anixlynch/ai-machine-learning-neural-networks-deep-learning-concept-list-w-samples-28ac4d67eb65) |
| Artificial Intelligence Does Not Exist - Luc Julia              | [https://youtu.be/JdxjGZBtp_k?si=kNrcqC4snFPksmei](https://youtu.be/JdxjGZBtp_k?si=kNrcqC4snFPksmei) |
| Attention Is All You Need                                       | [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)                      |
| NLP                                                            | [https://fr.wikipedia.org/wiki/Traitement_automatique_des_langues](https://fr.wikipedia.org/wiki/Traitement_automatique_des_langues) |
| RNN                                                            | [https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents](https://fr.wikipedia.org/wiki/R%C3%A9seau_de_neurones_r%C3%A9currents) |
| CNN                                                            | [https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif](https://fr.wikipedia.org/wiki/R%C3%A9seau_neuronal_convolutif) |
| Generative Artificial Intelligence: What is it about?         | [https://bigmedia.bpifrance.fr/news/intelligence-artificielle-generative-de-quoi-parle-t](https://bigmedia.bpifrance.fr/news/intelligence-artificielle-generative-de-quoi-parle-t) |
| How Generative AI and LLMs Work                                | [https://learn.microsoft.com/fr-fr/dotnet/ai/conceptual/how-genai-and-llms-work](https://learn.microsoft.com/fr-fr/dotnet/ai/conceptual/how-genai-and-llms-work) |
| LLM vs Chatbot: Which solution for which needs?               | [https://www.hubi.ai/blogfr/llm-vs-chatbot/](https://www.hubi.ai/blogfr/llm-vs-chatbot/) |
| Sephora and its Ora Chatbot                                   | [https://www.viseo.com/fr/secteurs-activites/sephora-choisit-viseo-pour-la-creation-de-son-chatbot-ora/](https://www.viseo.com/fr/secteurs-activites/sephora-choisit-viseo-pour-la-creation-de-son-chatbot-ora/) |
| How H&M Bot Works                                             | [https://redresscompliance.com/how-hm-uses-ai-powered-chatbots-to-improve-customer-service/](https://redresscompliance.com/how-hm-uses-ai-powered-chatbots-to-improve-customer-service/) |
| KLM and their BlueBot Chatbot                                | [https://news.klm.com/klm-welcomes-bluebot-bb-to-its-service-family/](https://news.klm.com/klm-welcomes-bluebot-bb-to-its-service-family/) |
| Companies Using Chatbots                                      | [https://www.chatbotguide.org/](https://www.chatbotguide.org/)                              |
| Behind the Scenes of Copilot: Context + LLM + performance + security = ✨ | [https://www.youtube.com/watch?v=-oyZsPCpK-Q](https://www.youtube.com/watch?v=-oyZsPCpK-Q) |
| Ethical Challenges of AI-Assisted Research in Economics and Management | [https://knowledge.essec.edu/fr/economy-finance/defis-ethiques-recherche-intelligence-artificielle.html](https://knowledge.essec.edu/fr/economy-finance/defis-ethiques-recherche-intelligence-artificielle.html) |

