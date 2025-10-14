#  AI Red Teaming

[![gandalf](img/step15.jpg)](https://www.youtube.com/watch?v=lKSKJZ-XdAk)
> "Fight for us... and regain your honor" — Aragorn, LOTR – The Return of the King

## 🎯 Objectives of this step

- Understand the principles of red teaming applied to generative AI
- Identify vulnerabilities specific to generative AI systems
- Implement adapted attack and evaluation techniques
- Propose mitigation and defense strategies

## Table of Contents

- [Red Teaming of Generative Artificial Intelligence](#red-teaming-of-generative-artificial-intelligence)

- [Approach to Generative AI](#approach-to-generative-ai)
    - [The Black Box](#the-black-box)
    - [Data Dependence](#data-dependence)
    - [Components of Generative AI Systems](#components-of-generative-ai-systems)

- [Specific Techniques, Tactics, and Procedures (TTPs)](#specific-techniques-tactics-and-procedures-ttps)
- [The Recipe for Success](#the-recipe-for-success)

- [Next Step](#next-step)
- [Resources](#resources)


## Red Teaming of Generative Artificial Intelligence

Red teaming for generative AI should not be limited to identifying isolated technical flaws in models. It is a critical and systematic approach that must cover the entire AI system lifecycle—from design through deployment and operation—taking into account the complex interactions between models, users, and the operational environment.

This holistic vision requires multidisciplinary teams combining technical, socio-cultural, ethical, and legal expertise to identify emerging risks, systemic vulnerabilities, and unexpected behaviors that may arise in real-world settings.

As an exercise in critical thinking, red teaming goes beyond mere vulnerability hunting by incorporating analysis of socio-technical risks, including those related to human interactions and misuse.

## Approach to Generative AI

The evaluation approach must be agile and adaptive, grounded in an understanding of the continuous evolution of AI systems. It is essential to monitor and integrate information throughout the development-to-production pipeline, including rigorous and continuous control over data, design, code, training environments, and real-world behaviors.

Evaluation should occur at multiple levels, combining testing of the models themselves (micro-level) with assessment of the overall system, including its interfaces, technical components, and human factors (macro-level).

### The Black Box

The "black box" nature of models requires specific approaches:

- Test models in black-box conditions while leveraging, when possible, open-source versions in controlled environments to reproduce and understand vulnerabilities.
- Examine system design and architecture to identify upstream systemic vulnerabilities, particularly in interfaces, observability mechanisms, and governance systems integrated from the outset.

This includes anticipating failure modes related to edge cases, unexpected interactions between components, or manipulation of data flows.

### Data Dependence

Data quality and management are critical factors. Red teaming must assess the entire data pipeline:

- Collection, storage, access, and traceability,
- Data representativeness and bias,
- Protection against attacks such as data poisoning,
- Risks related to de-anonymization or combining seemingly harmless data.

Rigorous control of data pipelines and consideration of data drift, bias, and attacks are essential.

### Components of Generative AI Systems

Vulnerabilities must be analyzed across all critical components:

| Component   | Description of Specific Vulnerabilities                                                                 |
|-------------|--------------------------------------------------------------------------------------------------------|
| Model       | Algorithmic flaws, prompt injections, optimization errors, or exploitable biases.                      |
| Data        | Quality, provenance, bias, poisoning attacks, access controls, and data lifecycle management.          |
| Application | Classic application security flaws that could serve as attack vectors toward the model.                |
| System      | Infrastructure, networks, development tools, and supply chains that could be compromised.              |

Red teaming should include evaluation of development environments, deployment pipelines, access controls, and system resilience to failures.

### Specific Techniques, Tactics, and Procedures (TTPs)

Beyond traditional cybersecurity TTPs (phishing, vulnerability exploitation, lateral movement, exfiltration), red teaming campaigns must include:

- Prompt injection and manipulation (model-level red teaming),
- Attacks on data and component supply chains,
- Socio-technical attack scenarios involving user behaviors and human interactions,
- Consideration of diverse cultural, linguistic, and demographic contexts for comprehensive and representative evaluation.

### The Recipe for Success

Red teaming success relies on collaboration between technical and non-technical disciplines, aiming to embrace the complexity of AI systems. It involves combining red teaming (risk identification) with complementary methods such as violet teaming, which integrates blue teaming (response and remediation).

Team diversity—across skills, user perspectives, and cultural aspects—is essential to detect risks invisible to homogeneous approaches.

## Next Step

- [Step 15](step_15.md)

## Resources

| Information                                                   | Link                                                                                                                                                                                                     |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OWASP GEN AI SECURITY Project Initiatives                     | [https://genai.owasp.org/initiatives/](https://genai.owasp.org/initiatives/)                                                                                                                             |
| NVIDIA AI Red Team: An Introduction                           | [https://developer.nvidia.com/blog/nvidia-ai-red-team-an-introduction/](https://developer.nvidia.com/blog/nvidia-ai-red-team-an-introduction/)                                                           |
| Defining LLM Red Teaming                                      | [https://developer.nvidia.com/blog/defining-llm-red-teaming/](https://developer.nvidia.com/blog/defining-llm-red-teaming/)                                                                               |
| Red Teaming AI Red Teaming                                    | [https://arxiv.org/abs/2507.05538](https://arxiv.org/abs/2507.05538)                                                                                                                                     |
| Red Teaming AI: Attacking & Defending Intelligent Systems     | [https://www.amazon.com.au/Red-Teaming-Attacking-Defending-Intelligent-ebook/dp/B0F88SGMXG](https://www.amazon.com.au/Red-Teaming-Attacking-Defending-Intelligent-ebook/dp/B0F88SGMXG)                   |
| SAFE-AI A Framework for Securing AI-Enabled Systems           | [https://www.linkedin.com/feed/update/urn:li:activity:7346561112877821953/](https://www.linkedin.com/feed/update/urn:li:activity:7346561112877821953/)                                                   |
| RedTWIZ: Diverse LLM Red Teaming via Adaptive Attack Planning | [https://arxiv.org/abs/2510.06994](https://arxiv.org/abs/2510.06994)                                                                                                                                     |
| Prompt Injection Taxonomy                                     | [https://github.com/Arcanum-Sec/arc_pi_taxonomy/](https://github.com/Arcanum-Sec/arc_pi_taxonomy/)                                                                                                       |
| OWASP Red Teaming: A Practical Guide to Getting Started       | [https://www.promptfoo.dev/blog/owasp-red-teaming/](https://www.promptfoo.dev/blog/owasp-red-teaming/)                                                                                                   |
| OWASP GenAI Red Teaming Guide                                 | [https://genai.owasp.org/resource/genai-red-teaming-guide/](https://genai.owasp.org/resource/genai-red-teaming-guide/)                                                                                   |
| MITRE ATLAS                                                   | [https://atlas.mitre.org/](https://atlas.mitre.org/)                                                                                                                                                     |
