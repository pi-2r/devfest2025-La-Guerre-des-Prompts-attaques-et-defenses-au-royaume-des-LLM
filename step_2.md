# Why LLM Security is Crucial?

[<img src="img/step2.png" alt="gandalf" >](https://www.youtube.com/watch?v=whF2na8AIbw)
> "The year 3434 of the Second Age. Here follows the account of Isildur, High King of Gondor, and the finding of the ring of power. It has come to me. The One Ring", Gandalf, LOTR - The Fellowship of the Ring

## 🎯 Objectives of this step

- Get an overview of the new technological era of generative AI.
- Understand the importance of LLM security in the context of generative AI.

## Table of contents

- [The emergence of AI, a new technological era](#the-emergence-of-ai-a-new-technological-era)
- [The LLM, a brain connected to your programs](#the-llm-a-brain-connected-to-your-programs)
- [The different control points](#the-different-control-points)
  - [User interaction](#user-interaction)
  - [Public training data](#public-training-data)
  - [Internal training data](#internal-training-data)
  - [Internal services](#internal-services)
  - [Access to public data](#access-to-public-data)
- [The LLM model](#the-llm-model)
  - [API model](#api-model)
  - [Hosted model](#hosted-model)
- [Next step](#next-step)
- [Resources](#resources)

## The emergence of AI, a new technological era

The rapid rise of artificial intelligence, notably driven by ChatGPT, has pushed this technology into the spotlight. Its massive adoption is no longer limited to the general public: companies, attracted by the efficiency of large language models (LLM) in generative AI applications, now make it an essential lever of productivity.

<a href="https://www.visualcapitalist.com/charted-top-10-companies-leading-the-new-era-of-ai/" target="_blank">
  <img src="https://www.visualcapitalist.com/wp-content/uploads/2025/06/Companies-Leading-the-New-Era-of-AI_WEB-1.jpg" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://www.visualcapitalist.com/charted-top-10-companies-leading-the-new-era-of-ai/" target="_blank"><em>source: visualcapitalist.com</em></a>

However, this popularity comes with major new security challenges. LLMs introduce specific risks, different from classic cyber threats such as DDoS attacks, SQL/XSS injections, or ransomware. Their ability to interpret and generate natural language via prompts opens the way to novel vulnerabilities: query manipulation, generation of malicious or inappropriate content, exfiltration of sensitive information, or actions unforeseen by system designers. Let's look at this in more detail.

# The LLM, a brain connected to your programs

Developers, as well as the companies that employ them, often perceive large language models (LLM) as autonomous systems capable of remarkable feats in understanding and content generation. Yet, in software engineering reality, LLMs rarely operate in isolation: they generally integrate into complex decision-making architectures designed to increase application autonomy.

These architectures rely on the interconnection of multiple components, each playing a specific role in the processing chain. This modular organization is essential to guarantee coherence, robustness, and overall performance of generative AI-based solutions. Thus, the LLM acts as a central link but depends closely on the whole system to deliver reliable and relevant results. It is therefore essential to have an overview of the architecture surrounding the deployed LLM.

The diagram below presents a simplified version of LLM integration in an enterprise environment.

 <img src="img/llm-inside.png" alt="llm-inside" width="450" style="transition:0.3s;">

In itself, the approach remains relatively simple. However, it is essential to implement control points on the connections the LLM can access. These controls can take various forms, such as authentication, data validation, or access permission management.

The diagram below offers a simplified view of the main control points to consider.

 <img src="img/llm-inside-secure.png" alt="llm-inside" width="450" style="transition:0.3s;">

## The different control points

### User interaction
It is important to consider that users may, intentionally or not, introduce errors. It is therefore essential to set up mechanisms to protect the LLM model against potentially contradictory or misleading inputs, whether they come from users or other systems. Particular vigilance must also be paid to toxic, inaccurate, or sensitive content that the model could generate and transmit to the user.

<details>
  <summary>Example</summary>
<a href="https://twitter.com/MathisHammel/status/1600413492636307456?s=20&t=fPcFwvq05Oe8JHkvVi95xw" target="_blank">
  <img src="https://pbs.twimg.com/media/FjXOpGiWYAAG-9r?format=jpg&name=small" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://twitter.com/MathisHammel/status/1600413492636307456?s=20&t=fPcFwvq05Oe8JHkvVi95xw" target="_blank"><em>source: twitter.com</em></a>
</details>

### Public training data
LLMs are generally trained on vast datasets sourced from the internet. It is therefore essential to consider these sources as potentially unreliable and to remain vigilant against the risks of toxicity, bias, or data poisoning from contradictory information. Example: Grok and its model from platform X (formerly Twitter), which relies mainly on users' comments (Troll?).

<details>
  <summary>Example</summary>
<a href="https://bsky.app/profile/epyon.bsky.social/post/3ltcxxxv22s2k" target="_blank">
  <img src="https://cdn.bsky.app/img/feed_thumbnail/plain/did:plc:ltgm2ysjnysy4hnpxjdwuwn3/bafkreicd5bm65vhtvn47ykkzfnzrunqyqjgsu6whkcgdaowhacspg2gzzm@jpeg" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://bsky.app/profile/epyon.bsky.social/post/3ltcxxxv22s2k" target="_blank"><em>source: bsky.app</em></a>
</details>

### Internal training data

It is possible to use internal data to optimize the model, which can significantly increase its accuracy.
However, it is imperative to ensure that sensitive, confidential, or personal information is neither integrated nor exposed during this process.

<details>
  <summary>Example</summary>
<a href="https://neuraltrust.ai/fr/blog/ai-model-data-leakage-prevention" target="_blank">
  <img src="https://a.storyblok.com/f/322249/900x507/4a8eae1fdb/why-your-ai-model-might-be-leaking-sensitive-data-and-how-to-stop-it.png" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://neuraltrust.ai/fr/blog/ai-model-data-leakage-prevention" target="_blank"><em>source: neuraltrust.ai</em></a>
</details>

### Internal services
It is essential to control how the LLM interacts with the company's connected services, such as databases or APIs, to prevent unauthorized interactions or data leakage, such as SQL injections or abusive API requests.

<details>
  <summary>Example</summary>

<a href="https://snyk.io/fr/articles/llm-weaponized-via-prompt-injection-to-generate-sql-injection-payloads/" target="_blank">
  <img src="img/sql-injection-llm.png" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://snyk.io/fr/articles/llm-weaponized-via-prompt-injection-to-generate-sql-injection-payloads/" target="_blank"><em>source: snyk.io</em></a>
</details>

### Access to public data
Real-time data extraction from the Web, notably via scraping techniques, can be an effective lever to enrich your application's functionality. However, it is essential to consider this information as potentially unreliable and stay aware of risks such as indirect prompt injection. This vigilance must be strengthened if you allow users to suggest websites to explore or upload potentially compromised documents.

<details>
  <summary>Example</summary>
<a href="https://arxiv.org/html/2505.22998v1" target="_blank">
  <img src="img/arxiv-faill-injection.png" alt="image" width="450" style="transition:0.3s;">
</a>

<a href="https://arxiv.org/html/2505.22998v1" target="_blank"><em>source: arxiv.org</em></a>
</details>

# The LLM Model

The language model is the core of any application based on an LLM. It plays a central role in gathering and interpreting information to allow action execution within a computing environment.

Depending on the configuration of your infrastructure and your specific needs, two options are available to let your ecosystem interact with the model:
- **API model**: Through a public API, hosted by an external provider (e.g., OpenAI, Google, Amazon Bedrock, etc.), which allows access to a pre-trained model and use it to generate responses or actions.

- **Hosted model**: By deploying a model hosted locally, within your own installations (on-premises) or in the cloud, which allows full control of the model and adaptation to your specific needs.

## API Model
Using public APIs to connect to one or several models has the advantage of great ease of use and generally lower costs. Moreover, model management and updates are handled by the service provider, considerably reducing maintenance for the user company (usually only a model name change is required in your application code).

**However, this choice implies an important trade-off:** the risk of exposure of sensitive data transmitted via the API.
Indeed, every request sent to a third-party model crosses your secure environment's boundary to be processed by an external system.

> This transfer potentially exposes your information to confidentiality issues and, depending on the security level implemented by the provider, may increase vulnerability to possible data breaches.

## Hosted Model
Choosing private hosting of a model, especially in sensitive sectors such as banking or healthcare, offers increased control over your data and allows the establishment of clearly defined security barriers. This solution also facilitates adapting the model to the specifics of your business domain.

**However, this choice implies an important trade-off:** hosting the model internally means you are responsible for its maintenance, updates, and management of potential vulnerabilities.

> If you choose an open-source model, it becomes essential to ensure its reliability and integrity to prevent any security breach or inherent bias risk.

## Next Step

- [Step 3](step_3.md)

## Resources

| Information                                                                                         | Link                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| How AI can move from hype to global solutions                                                       | [https://www.weforum.org/stories/2025/01/ai-transformation-industries-responsible-innovation/](https://www.weforum.org/stories/2025/01/ai-transformation-industries-responsible-innovation/)                                                                                                                                       |
| ChatGPT wins over professionals: 32% of US companies use OpenAI, far ahead of Google and Anthropic | [https://siecledigital.fr/2025/05/12/chatgpt-seduit-les-pros-32-des-entreprises-us-utilisent-openai-loin-devant-google-et-anthropic/](https://siecledigital.fr/2025/05/12/chatgpt-seduit-les-pros-32-des-entreprises-us-utilisent-openai-loin-devant-google-et-anthropic/)                                                         |
| Large language models: upcoming cybersecurity challenges                                            | [https://www.journaldunet.com/intelligence-artificielle/1542135-large-language-models-les-nouveaux-enjeux-a-venir-dans-la-cybersecurite/](https://www.journaldunet.com/intelligence-artificielle/1542135-large-language-models-les-nouveaux-enjeux-a-venir-dans-la-cybersecurite/)                                                 |
| LLM vulnerabilities and generative AI security                                                     | [https://www.vaadata.com/blog/fr/vulnerabilites-llm-et-securite-des-ia-generatives/](https://www.vaadata.com/blog/fr/vulnerabilites-llm-et-securite-des-ia-generatives/)                                                                                                                                                           |
| AI in cybersecurity: understanding risks                                                          | [https://www.malwarebytes.com/fr/cybersecurity/basics/risks-of-ai-in-cyber-security](https://www.malwarebytes.com/fr/cybersecurity/basics/risks-of-ai-in-cyber-security)                                                                                                                                                           |
| LLM pitfalls                                                                                      | [https://learnprompting.org/fr/docs/basics/pitfalls](https://learnprompting.org/fr/docs/basics/pitfalls)                                                                                                                                                                                                                           |
| Grok: Elon Musk’s AI calls itself “MechaHitler,” promotes rape and conspiracy theories             | [https://www.lesnumeriques.com/intelligence-artificielle/grok-l-ia-d-elon-musk-se-fait-appeler-mechahitler-prone-le-viol-et-les-theories-du-complot-n239464.html](https://www.lesnumeriques.com/intelligence-artificielle/grok-l-ia-d-elon-musk-se-fait-appeler-mechahitler-prone-le-viol-et-les-theories-du-complot-n239464.html) |
| LLM in enterprise: combining AI power and data privacy                                             | [https://www.linkedin.com/pulse/llm-en-entreprise-allier-puissance-de-lia-et-des-donn%C3%A9es-leprince-fkpte/](https://www.linkedin.com/pulse/llm-en-entreprise-allier-puissance-de-lia-et-des-donn%C3%A9es-leprince-fkpte/)                                                                                                       |
