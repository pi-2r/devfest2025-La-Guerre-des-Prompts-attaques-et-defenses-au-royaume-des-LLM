# Reference Security Frameworks

[<img src="img/step4.jpg" alt="Arwen" >](https://www.youtube.com/watch?v=fd2AO0gr3Rc)
> "If you want him come and claim him", Arwen, LOTR - The Fellowship of the Ring

## 🎯 Objectives of this step

- Understand existing security frameworks for LLMs (Large Language Models)
- Identify main risks and vulnerabilities related to the use of LLMs
- Discover dedicated security frameworks and references (OWASP Top 10 LLM, SAIF, MITRE ATLAS)
- Understand legislative regulations governing LLMs (United States, European Union)
- Access resources to deepen the security of AI applications

## Table of Contents

- [OWASP Top 10 for LLM Applications](#owasp-top-10-for-llm-applications)
  - [More details](#more-details)

- [Be SAIF with the Secure AI Framework](#be-saif-with-the-secure-ai-framework)
  - [Google's Secure AI Framework (SAIF)](#googles-secure-ai-framework-saif)
  - [The four main categories of SAIF](#the-four-main-categories-of-saif)
  - [The six fundamental elements of SAIF](#the-six-fundamental-elements-of-saif)
  - [SAIF risk and control mapping](#saif-risk-and-control-mapping)
  - [Implementation and SAIF community](#implementation-and-saif-community)

- [MITRE ATLAS, the Ariadne's thread of AI attack techniques](#mitre-atlas-the-ariadnes-thread-of-ai-attack-techniques)
  - [Purpose of MITRE ATLAS](#purpose-of-mitre-atlas)
  - [Framework](#framework)
  - [Fundamental elements of MITRE ATLAS](#fundamental-elements-of-mitre-atlas)
  - [How to use it](#how-to-use-it)

- [Legislative regulation of LLMs](#legislative-regulation-of-llms)
  - [Issues and principles](#issues-and-principles)
    - [United States: sectoral regulation focused on freedom of expression](#united-states-sectoral-regulation-focused-on-freedom-of-expression)
    - [European Union: structured risk-based framework](#european-union-structured-risk-based-framework)
      - [Digital Services Act (DSA)](#digital-services-act-dsa)
      - [AI Act](#ai-act)
  - [Convergences and divergences](#convergences-and-divergences)

- [Next step](#next-step)
- [Resources](#resources)

## OWASP Top 10 for LLM Applications

<a href="https://genai.owasp.org/2023/10/18/llm-to-10-v1-1/" target="_blank">
  <img src="https://genai.owasp.org/wp-content/uploads/2024/05/1697599021768.jpeg" alt="image" width="950" style="transition:0.3s;">
</a>

<a href="https://genai.owasp.org/2023/10/18/llm-to-10-v1-1/" target="_blank"><em>source: genai.owasp.org</em></a>

The **OWASP Top 10 for Large Language Model Applications** is today the reference tool to list, analyze, and mitigate the main security risks specific to the use of large language models.

This collaboratively developed list is an essential guide for developers, architects, and security managers who want to integrate generative AI reliably and securely into their information systems. This ranking was created thanks to the commitment of [John Sotiropoulos](https://www.linkedin.com/in/jsotiropoulos/), project co-pilot, and [Ads Dawson](https://www.linkedin.com/in/adamdawson0/), technical lead in charge of coordinating the writing of the repository's technical aspects.

Here is a summary of the OWASP Top 10 for LLM Applications 2025:

| ID       | Description                                                                                                                                        |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **LLM01**| **Prompt Injection**: Attackers manipulate LLM input directly or indirectly to cause malicious or illegal behavior.                              |
| **LLM02**| **Sensitive Information Disclosure**: Attackers trick the LLM to reveal sensitive information in its response.                                     |
| **LLM03**| **Supply Chain Vulnerabilities**: Attackers exploit vulnerabilities in any part of the LLM's supply chain.                                         |
| **LLM04**| **Data and Model Poisoning**: Attackers inject malicious or misleading data into the LLM training data, compromising performance or creating backdoors. |
| **LLM05**| **Unsecure Output Handling**: LLM output is handled insecurely, leading to injection vulnerabilities such as Cross-Site Scripting (XSS), SQL injection, or command injection. |
| **LLM06**| **Excessive Access (Agency)**: Attackers exploit insufficiently restricted LLM access to sensitive systems or actions.                             |
| **LLM07**| **System Prompt Leakage**: Sensitive information contained in system prompts is accidentally disclosed.                                            |
| **LLM08**| **Vector and Embedding Vulnerabilities**: Exploitation of weaknesses in vector and embedding management in RAG systems, causing data leakage or alteration. |
| **LLM09**| **Disinformation**: The LLM generates false or misleading information, causing security and reputational risks.                                     |
| **LLM10**| **Unbounded Consumption**: Attacks exploit excessive resource consumption, causing denial of service or financial costs.                           |

### More details

<details>
  <summary>Prompt Injection (LLM01)</summary>

Prompt injection is a security vulnerability that occurs when a malicious user manages to manipulate the input instructions given to a language model (LLM), causing it to adopt unexpected or undesired behavior.

Some manipulations may appear harmless—e.g., diverting a technical support chatbot to provide cooking recipes—but others can have much more serious consequences. This technique can be exploited to encourage the LLM to produce false information, hate speech, or harmful or even illegal content.

In some cases, prompt injection may also allow an attacker to extract sensitive data previously provided to the model, thus compromising the confidentiality of the processed information.
</details>
<br/>
<br/>
<details>
  <summary>Sensitive Information Disclosure (LLM02)</summary>

Language models (LLMs) can unintentionally disclose confidential data in their responses. Such exposure can lead to unauthorized access to sensitive information, privacy breaches, or security vulnerabilities. It is essential to strictly restrict access to information that the LLM is authorized to consult. 

This is especially important when the model is used to process sensitive or strategic data, such as customer information. In these cases, requests to the LLM should be subject to rigorous access controls to limit data leakage risk.

If the LLM was trained or fine-tuned using a custom dataset, it is crucial to bear in mind that it can be manipulated (for example, by prompt injection attacks) to reveal elements of this training data. Therefore, any sensitive information included in the training corpus must be carefully identified, assessed according to its criticality, and protected accordingly.

Furthermore, sensitive data provided to the LLM via user prompts may be exposed by injection attacks (see LLM01), even if the model was explicitly requested to keep this information confidential. This highlights the need for security measures adapted to each contact point between the user and the model.
</details>
<br/>
<br/>
<details>
  <summary>Supply Chain Vulnerabilities (LLM03)</summary>

Supply chain vulnerabilities in the context of LLMs concern all elements involved in their development or deployment. This notably includes datasets used for training (see LLM03), pre-trained models provided by third parties, as well as plugins, extensions, or other systems interacting with the LLM (cf. LLM07).

The impact of these vulnerabilities can vary considerably, ranging from simple malfunctions to critical consequences. One of the most common scenarios is the leakage of sensitive data or disclosure of intellectual property, compromising the confidentiality or strategic assets of the organization.
</details>

<details>
  <summary>Data and Model Poisoning (LLM04)</summary>

The quality and performance of a language model (LLM) largely depend on the data used during its training phase. Training Data Poisoning consists of manipulating all or part of these data to introduce deliberate biases, causing the model to produce incorrect or malicious results.

Depending on the compromised LLM's use, consequences can range from loss of credibility to critical security vulnerabilities, especially if the model generates code reused in other software components.

To succeed in a training data poisoning attack, an attacker must first have access to the data corpus used to train the model. When training relies on publicly accessible data (such as web content), it is crucial to clean and verify their integrity to eliminate any source of bias or manipulated content.

Mitigation strategies include:
- Fine and regular verification of the training data supply chain
- Assessment of the legitimacy and provenance of sources
- Implementation of filters capable of identifying and excluding incorrect or malicious data

In short, rigorous attention to training data quality is essential to guarantee reliable and ethical behavior of LLMs.
</details>
<br/>
<br/>
<details>
<summary>Unsecure Output Handling (LLM05)</summary>

Unsecure output handling refers to the lack of proper validation, sanitation, and control of the responses generated by the LLM before their transmission to other systems or the end user. Since model outputs can be influenced by malicious inputs, this amounts to granting indirect access to additional functionalities, potentially causing serious vulnerabilities.

This poor handling exposes the system to attacks such as Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), Server Side Request Forgery (SSRF), privilege escalation, or even remote code execution (RCE) on backend systems processing the outputs.

Common causes include lack of appropriate encoding of outputs, absence of context-specific filtering (HTML, SQL, system commands), and limited monitoring of abnormal output behaviors.

To prevent these flaws, it is recommended to:

- Treat LLM outputs as coming from an untrusted user (zero-trust model).

- Rigorously validate and sanitize all output before use or display.

- Apply specific contextual encoding (HTML, JavaScript, SQL, etc.).

- Use strict security policies, such as Content Security Policies (CSP) for the web.

- Introduce monitoring and alert mechanisms for suspicious or abnormal outputs.

In summary, unsecure output handling is a critical vulnerability that can compromise the overall security of the application by allowing unwanted executions and attacks via LLM responses.
</details>
<details> 
<summary>Excessive Access (Agency) LLM06</summary>

Excessive access (agency) is a major vulnerability in applications using large language models (LLMs), where the model or LLM agent has overly broad privileges or authorizations, allowing it to interact with sensitive systems, databases, or functions beyond what is strictly necessary.

This overexposure can allow an attacker, by manipulating the model through malicious prompts or requests, to perform unauthorized actions such as modifying, stealing, or deleting data, triggering critical operations, or extending control in the target environment.

Typical causes include poor permission management, insufficient isolation between automated functions, or an overly permissive agent architecture, for example with LLMs acting as autonomous agents capable of executing system commands without supervision.

To mitigate this risk, it is recommended to:

- Apply the principle of least privilege: strictly limit LLM access and capabilities to what is essential.

- Implement granular access controls and verify every LLM request before execution.

- Employ manual or automatic validation mechanisms (human-in-the-loop) for any sensitive operation.

- Functional segmentation and strict isolation of LLM agents when multiple are used.

- Actively monitor interactions and detect any abnormal or suspicious activity.

In short, excessive access is a critical attack vector making an LLM potentially capable of causing significant damage and requires strong governance and secure design from the development phase.
</details>
<br/>
<br/>

<details>
<summary>System Prompt Leakage (LLM07)</summary>

System prompt leakage refers to the vulnerability where internal instructions or system prompts used to guide the behavior of a large language model (LLM) are accidentally exposed or disclosed to unauthorized users. These system prompts often contain sensitive information such as access keys, security parameters, business rules, or filtering controls, which should not be visible.

The real vulnerability lies not so much in the disclosure itself but in the fact that this information is used to delegate access, privilege, or security controls to the model itself. Leakage therefore allows attackers to bypass these controls and perform unauthorized actions by manipulating the model.

Recommended preventive measures include:

- Separating sensitive information from system prompts by storing them in secure independent environments inaccessible directly to the LLM.

- Not relying on system prompts as the sole security mechanism; implement external controls, such as guardrails inspecting model outputs.

- Strictly apply the principle of least privilege in configuring agents or systems integrated with LLMs.

- Use multiple distinct LLM agents, each with adapted and limited access to their tasks to minimize risks.

In short, system prompt leakage is a critical vulnerability because it compromises fundamental security mechanisms, exposing LLM applications to widespread attacks such as jailbreak, data disclosure, or malicious actions.
</details>
<details>
<summary>Vector and Embedding Vulnerabilities (LLM08)</summary>

Vector and embedding vulnerabilities (LLM08) concern security flaws related to how LLMs process, store, and use numerical representations (vectors, embeddings) of data. These vectors allow the model to quickly retrieve information and provide contextual responses, notably in retrieval augmented generation (RAG) systems.

Major risks include unauthorized access to sensitive data contained in vectors, information leakage between different users or contexts (in a multi-tenant environment), as well as embedding inversion attacks that reconstruct original data from vectors. Furthermore, poisoning of embeddings can manipulate model outputs, affecting the reliability and security of responses.

To reduce these risks, it is essential to apply strict access and authentication controls to vector databases, validate the source and integrity of inserted data, classify and separate data according to access scopes, and continuously monitor retrieval activities to detect anomalies.

These vulnerabilities represent a subtle but critical threat as they can create invisible backdoors, durably integrated into the internal functioning of the model, escaping classical protections based on prompts or outputs.

</details>
<br/>
<br/>
<details>
<summary>Misinformation (LLM09)</summary>

Misinformation refers to the ability of language models (LLMs) to generate false, inaccurate, or misleading content that may appear credible at first glance. This vulnerability often stems from errors, biases, or limitations in training data, where the model "guesses" or hallucinates answers even in the absence of confirmed facts.

This misinformation can lead to serious risks, such as security breaches, damage to organizations' reputations, or legal liabilities if decisions are made based on erroneous information. For example, an LLM could provide an incorrect emergency number in a critical context, potentially endangering users' lives.

To limit this risk, it is advised to use reliable and validated sources for training, regularly verify data accuracy, integrate real-time fact-checking APIs, and filter or validate model outputs before publication or use. Human-in-the-loop control is also recommended to approve results in high-risk contexts.

Misinformation is a key issue for trust in LLM-based systems and requires approaches combining technical measures, processes, and user awareness.
</details>

<details>
<summary>Unbounded Consumption (LLM10)</summary>

Unbounded consumption refers to a vulnerability where an application using a large language model (LLM) allows users to generate excessive and uncontrolled queries or inputs. This leads to abusive use of computational resources, such as memory and CPU, potentially causing denial of service (DoS), service degradation, or very high financial costs.

Attackers exploit this flaw by submitting long or numerous inputs, triggering heavy processing, often in cloud environments, which can saturate resources and make the service unavailable to legitimate users. This excessive consumption can also lead to indirect theft of intellectual property by extraction or cloning of the model.

To mitigate this risk, it is recommended to impose strict limits on request size and number, continuously monitor and log resource usage, implement rigorous access controls, as well as load balancing and scaling strategies to manage usage peaks. The system should be designed to degrade performance gracefully in case of overload rather than fail completely.

In short, unbounded consumption is a major risk since it directly impacts availability, economic security, and resilience of LLM-based applications.

</details>

## Be SAIF with the Secure AI Framework
