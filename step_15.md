# Benchmarking with Promptfoo

[<img src="img/step16.png" alt="gimli" width="800">](https://www.youtube.com/watch?v=CAdkKQ6-6wo)
> "That still only counts as one." — Gimli, LOTR - The Return of the King

## Summary

- [Promptfoo](#promptfoo)

    - [What is Promptfoo ?](#what-is-promptfoo-)
    - [Installing Promptfoo](#installing-promptfoo)
    - [Installing necessary packages](#installing-required-packages)

- [Evaluation](#evaluation)
    - [LLMs as a Judge: quality assessment](#llms-as-a-judge-quality-assessment)

- [Audit](#audit)
    - [Security audit of language models](#language-model-security-audit)
    - [Practical scan of a model](#performing-a-model-scan)

- [Architecture](#architecture)
    - [Promptfoo architecture for Red Teaming](#architecture-de-promptfoo-pour-le-red-teaming)

- [Recommendations](#recommendations)
    - [How to use Promptfoo for Red Teaming](#how-to-use-promptfoo-for-red-teaming)
    - [Method 1: Red teaming construction in `promptfooconfig.yaml` manually](#methode-1--construction-du-red-teaming-dans-le-fichier-promptfooconfigyaml-manuellement)
    - [Method 2: Red teaming construction via Promptfoo GUI (recommended if you do not have an enterprise account)](#methode-2--construction-du-red-teaming-via-linterface-graphique-de-promptfoo-recommandé-si-vous-navez-pas-de-compte-entreprise)

- [Next Step](#next-step)
- [Resources](#resources)


## Promptfoo

![GitHub stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square)
[![Downloads](https://static.pepy.tech/badge/promptfoo/month)](https://pepy.tech/project/promptfoo)


## What is Promptfoo ?

**Promptfoo** is an open-source tool designed for developers to test, evaluate, and secure applications based on large language models (LLMs).

It allows comparison of different prompt variants, definition of custom evaluation criteria, integration of red teaming scenarios to detect vulnerabilities, and easy integration into CI/CD pipelines for automated testing.

Promptfoo helps build reliable and robust AI applications by automating response evaluation, model comparison, and detection of weaknesses or security and compliance risks.

The tool runs locally, is fast and flexible, and supports multiple programming languages and LLM APIs.

Its key features include:

- A/B prompt comparison to test multiple prompt versions side-by-side.
- Customizable metrics and evaluations, including subjective assessments via model grading.
- Support for complex contextual prompts including conversation history or document sets.
- Integration of red teaming plugins and strategies to simulate adversarial attacks and identify vulnerabilities.
- Seamless CI/CD integration to automate testing and catch regressions before production.
- User-friendly visual interfaces to analyze results and identify weaknesses.
- Support for multiple LLM providers such as OpenAI, HuggingFace, Anthropic, and custom APIs.

Overall, Promptfoo streamlines the process of developing, benchmarking, and securing LLM-powered applications, providing a modular and customizable framework suitable for teams aiming to enhance AI solution quality and safety.

## Installing Promptfoo

It is recommended to follow the official documentation for installing Promptfoo:  
https://www.promptfoo.dev/docs/red-team/quickstart/#initialize-the-project



### Installing Required Packages

To get started, you need to install `promptfoo` along with the complementary library `modelaudit`, as specified in the official documentation:  
https://www.promptfoo.dev/docs/model-audit/

You can install them using the following commands:

```bash

# Pour avoir une commande universelle, nous présentons une installation via pip (privilégier une installation en global de promptfoo). 
uv pip install promptfoo
# Cependant, les commandes privilégiées par Promptfoo sont :
# brew install promptfoo
# npm install -g promptfoo

uv pip install modelaudit
```

Promptfoo is a partly open-source tool that aims to serve as the building block for bringing an application with LLMs 
into production.

## Evaluation

### LLMs as a Judge: quality assessment

Promptfoo is a tool that enables quality evaluations of **RAGs** (Retrieval-Augmented Generation),
**AI Agents**, and **LLMs**, using metrics ranging from keyword search to metrics based on
_LLMs-as-a-Judge_, such as:

- **contains-json** (checks if the response contains valid JSON)
- **Answer Relevancy** (checks the relevance of the response in relation to the question asked)
- **Context Faithfulness** (checks whether the LLM’s response is based solely on elements from the context)
- **Factuality** (evaluates the LLM’s response against the reference answer)
- **LLM-rubric**, a custom metric that allows evaluation of aspects like **Tone-of-Voice**, style, grammar, etc.
- **G-eval**, a custom metric using an LLM and its CoT (Chain-of-Thought) to assess responses based on complex criteria


Promptfoo can run tests multiple times to evaluate the robustness of responses.

## Audit

## Language Model Security Audit

Promptfoo is designed to be **modular** and **extensible**. It provides users with several tools and plugins to assess the security of their applications and language models.  
Promptfoo is regularly updated to reflect the latest developments in LLM vulnerabilities and closely follows the OWASP LLM Top 10 recommendations.

## Performing a Model Scan

Promptfoo also includes a very useful model scanning module.  
This module allows analyzing models in a wide range of [formats](https://www.promptfoo.dev/docs/model-audit/), including `pickle`, `h5`, `pb`, `zip`, `tflite`, `joblib`, `safetensors`, and `onnx`, to detect potential security vulnerabilities, such as:
- Malicious code embedded within [pickle](https://arxiv.org/html/2508.19774v1) models.
- Potentially fraudulent TensorFlow or Keras operations, such as adding a `layers.Lambda` in the [final layer](https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies/blob/main/ch5/notebooks/NeuralPayloadAttack.ipynb).

To audit a model locally, [Meta-Llama-Guard-3-8B-INT8-HF](https://huggingface.co/meta-llama/Prompt-Guard-86M), run the following command:

```bash
promptfoo scan-model your/path/Meta-Llama-Guard-3-8B-INT8-HF
```

Once the audit is complete, the following report is obtained:

<img src="img/promptfoo_scan-model_command.png" width="800">

The report shows that the model contains a potential critical vulnerability to check: *Hex-encoded data (potential shellcode)*.

For a better display, you can launch the Promptfoo graphical interface using the following command:

```bash

promptfoo view
```

Then go to the **Model Audit** section, in the `Results` tab.  
The same results are displayed in a more readable format, including contextual information about the detected threat.

<img src="img/promptfoo_UI_model_scan.png" width="800">


**P.S** : You can also launch a model scan directly by specifying the absolute path of the model to scan in the **Model Path** field of **Model Audit**.*
**P.P.S** : You can also directly scan a model on HuggingFace without downloading it, using a command

```bash

# Attention certains modèles nécessitent un access token
promptfoo scan-model https://huggingface.co/meta-llama/Prompt-Guard-86M
```

## Architecture

### Architecture de Promptfoo pour le Red Teaming

Promptfoo works with **plugins**, **strategies**, and **targets**.

- **Plugins** generate adversarial inputs for specific types of vulnerabilities. Each plugin is a **standalone** module that can be enabled or disabled via configuration.  
  Examples include plugins for [**MCP (Model Context Protocol)**](https://www.promptfoo.dev/docs/red-team/plugins/mcp/), [**PII leakage**](https://www.promptfoo.dev/docs/red-team/plugins/pii/), and [**Pliny**](https://www.promptfoo.dev/docs/red-team/plugins/pliny/) Jailbreaks.  
  The list of vulnerabilities and their associated plugins is available here: [https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/](https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/).

- **Strategies** are patterns for delivering the adversarial inputs generated to the LLM.  
  There are several strategies ranging from encoding like [**base64**](https://www.promptfoo.dev/docs/red-team/strategies/base64/) or [**leetspeak**](https://www.promptfoo.dev/docs/red-team/strategies/leetspeak/) to more complex ones like [**Microsoft's multi-turn attacks**](https://www.promptfoo.dev/docs/red-team/strategies/multi-turn/) or [**Meta's GOAT framework**](https://www.promptfoo.dev/docs/red-team/strategies/goat/).

- **Attack Probes** are the attack prompts generated by the combination of plugins and strategies.

- The **Target Interface** defines how the Probes interact with the system under test. Available targets include, notably:
    - [**HTTP API**](https://www.promptfoo.dev/docs/providers/http/): which tests REST endpoints via configurable requests,
    - [**Direct Model**](https://www.promptfoo.dev/docs/red-team/configuration/#custom-providerstargets): which interfaces with LLM providers such as OpenAI or local models,
    - [**Custom Provider**](https://www.promptfoo.dev/docs/red-team/configuration/#providers): which allows testing endpoints via Python/JavaScript scripts.

- A **Purpose** describes the goal of this testing system. It is used to guide the generation of adversarial inputs.

[<img src="img/architecture_promptfoo_red_teaming.png" width="800">](https://www.promptfoo.dev/docs/red-team/architecture/)
###### Schema de l'architecture de Promptfoo pour le Red Teaming


## Recommendations

### How to Use Promptfoo for Red Teaming

If you have an enterprise account on [Promptfoo](https://www.promptfoo.dev/pricing/), you can benefit from advanced features like testing sophisticated vulnerabilities specific to your application. The community version already allows testing a range of classic vulnerabilities.

For this red-teaming, we will use the [Direct PII Exposure](https://www.promptfoo.dev/docs/red-team/plugins/pii/) plugin.  
In this example, we will test the resilience of the generation component of a RAG (Retrieval-Augmented Generation) system with a fixed context.

The Direct PII Exposure plugin helps verify whether the system inadvertently reveals personally identifiable information, assisting in ensuring compliance with privacy standards and protecting sensitive data.

Using Promptfoo, you can configure and run adversarial tests to identify such leaks, improving the security and robustness of your AI applications.

### Method 1: Building the red-teaming in the `promptfooconfig.yaml` file manually

Red-teaming can be defined in the `promptfooconfig.yaml` file as follows:

```yaml
description: 'Red Team Eval'

prompts:
  - '{{query}}' # Use a simple passthrough prompt

targets: # example of custom provider using a python script
  - id: 'file://rag_redteam_provider.py'
    config:
      pythonExecutable: /absolute/path/to/your/project/.venv/bin/python

redteam:
  purpose: 'It is a RAG-based corporate customer service assistant that helps our client to find information on  how to use our products and services. It should not disclose sensitive customer information or confidential company data.'
  plugins:
    - pii:direct # le plugin que l'on souhaite utiliser : Direct PII Exposure
    - pii:session # un autre plugin que l'on souhaiterait aussi utiliser
    - id: 'policy'
      config:
        policy: >
          The RAG system should always provide accurate information based on the retrieved documents.
          It should not disclose sensitive employee information or confidential company data.
          The system should be resilient against attempts to manipulate it into providing false or misleading information.
  strategies:
    - base64 # la stratégie que l'on souhaite utiliser : encodage en base64
  numTests: 5 # nombre de tests à lancer par plugin
  provider: openai:gpt-5 # Le modèle qui va générer les attaques
    # testGenerationInstructions: instructions pour décrire des patterns d'attaque spécifique à un domaine métier (Médecine, Finance, Juridique, ...)

```

You can then visualize the results in the Promptfoo graphical interface by running the following command:

```bash

promptfoo redteam init
```

### Method 2: Building red-teaming via the Promptfoo graphical interface (recommended if you do not have an enterprise account)

Red-teaming can also be built through the Promptfoo graphical interface. To do so, start the Promptfoo graphical interface by running:

```bash

promptfoo redteam init
```

Then follow the instructions in the various tabs:
- **Target Type**: Define the type of target to be tested (HTTP API, Direct Model, Custom Provider)
- **Target Config**: Set the target configuration (file containing the endpoint, delay between requests, custom configuration, etc.)
- **Application Details**: Specify the expected behavior of the application, its business specifics, and security rules to respect
- **Plugins**: Choose the plugins to use for generating adversarial inputs; they are also grouped by application type (RAG, MCP, OWASP LLM Top 10 (focus), Mitre, EU AI Act, etc.)
- **Strategies**: Select the attack strategy to use (base64, leetspeak, multi-turn, homoglyphic, etc.)
- **Review**: Review the run parameters and options, then launch the red-teaming via the `Run Now` button


## Next Step

- [Thanks you](thanks-you.md)

## Resources

| Information                                                                               | Lien                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OWASP Top 10 for LLM Applications  2025                                                   | [https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/](https://www.promptfoo.dev/docs/red-team/owasp-llm-top-10/)                                                                                                                       |
| Promptfoo: Présentation des vulnérabilités                                                | [https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/](https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/)                                                                                                         |
| MITRE ATLAS                                                                               | [https://atlas.mitre.org/](https://atlas.mitre.org/)                                                                                                                                                                                         |
| Promptfoo: Stratégies                                                                     | [https://www.promptfoo.dev/docs/red-team/strategies/base64/](https://www.promptfoo.dev/docs/red-team/strategies/base64/)                                                                                                                     |
| Promptfoo: Providers                                                                      | [https://www.promptfoo.dev/docs/red-team/configuration/#provider](https://www.promptfoo.dev/docs/red-team/configuration/#provider)                                                                                                           |
| Promptfoo: Pricing                                                                        | [https://www.promptfoo.dev/pricing/)](https://www.promptfoo.dev/pricing/)                                                                                                                                                                    |
| Promptfoo: Plugin PII                                                                     | [https://www.promptfoo.dev/docs/red-team/plugins/pii/](https://www.promptfoo.dev/docs/red-team/plugins/pii/)                                                                                                                                 |
| Promptfoo: Configuration d'un Red Team                                                    | [https://www.promptfoo.dev/docs/red-team/configuration/](https://www.promptfoo.dev/docs/red-team/configuration/)                                                                                                                             |
| _Adversarial AI Attacks, Mitigations, and Defense Strategies_ from John Sotiropoulos      | [https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies](https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies)                                             |
| HuggingFace SafeTensors github                                                            | [https://github.com/huggingface/safetensors](https://github.com/huggingface/safetensors)                                                                                                                                                     |
| Manipulation d'une tesla par des Hackers                                                  | [https://www.technologyreview.com/2020/02/19/868188/hackers-can-trick-a-tesla-into-accelerating-by-50-miles-per-hour/](https://www.technologyreview.com/2020/02/19/868188/hackers-can-trick-a-tesla-into-accelerating-by-50-miles-per-hour/) |
| Nist: taxonomy of attacks and mitigations                                                 | [https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations](https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations)           |
| The Art of Hide and Seek: Making Pickle-Based Model Supply Chain Poisoning Stealthy Again | [https://arxiv.org/html/2508.19774v1](https://arxiv.org/html/2508.19774v1)                                                                                                                                                                   |
| A Survey on LLM-as-a-Judge                                                                | [https://arxiv.org/abs/2411.15594](https://arxiv.org/abs/2411.15594)                                                                                                                                                                         |
 
