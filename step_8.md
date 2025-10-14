# Robustness Testing?

[![hobbiton](img/step8.png)](https://www.youtube.com/watch?v=NFBXilomkPk)
> "Oh... you would not part an old man from his walking stick?", Gandalf, LOTR – The Two Towers

## 🎯 Objectives of this Step

- Understand the importance of robustness testing for AI model security.
- Identify main adversarial threats (poisoning, evasion) and their impacts.
- Discover common methods for robustness testing of models.
- Explore integration of robustness testing in the AI lifecycle (MLOps, CI/CD, red teaming).
- Compare Garak and PyRIT tools for red teaming and LLM robustness.

## Table of Contents

- [Introduction](#introduction)
- [Main Objective](#main-objective)
- [Targeted Attack Context](#targeted-attack-context)
- [Methods](#methods)
- [Integration in AI Lifecycle](#integration-in-ai-lifecycle)
- [AI Red Teaming: Garak vs PyRIT](#ai-red-teaming-garak-vs-pyrit)
    - [Garak](#garak)
    - [PyRIT](#pyrit)
    - [Comparison Table](#comparison-table)
- [Next Step](#next-step)
- [Resources](#resources)

## Introduction

**Robustness testing**, also called **adversarial testing**, is a key element in securing AI and machine learning (ML) systems.  
The goal is to **measure a model’s ability to remain reliable and performant** when faced with deliberately crafted data designed to mislead or manipulate it.

## Main Objective

The primary goal is to evaluate a model's ability to maintain performance and integrity against malicious or subtly altered inputs.  
These tests verify that the model behaves as expected and does not produce erroneous or potentially harmful outputs under attacks.

## Targeted Attack Context

Robustness testing defends against two main categories of adversarial attacks:

- **Data Poisoning Attacks**: These target the training phase, subtly manipulating training data to corrupt learning and maliciously influence inference outcomes.  
  Robustness tests evaluate susceptibility to backdoors inserted via poisoning and help detect altered data presence.

- **Evasion Attacks**: Occur during inference on a trained model. Attackers create "adversarial examples"—inputs slightly altered, often imperceptible to humans—to cause misclassification.  
  Robustness tests check the model’s ability to resist such manipulations.

## Methods

Common robustness testing approaches include:

- **Custom Tests**: Developed to assess defenses against specific poisoning attack types.

- **"Canary" Records**: A simple method injecting a small clearly identifiable set of records to detect poisoning if misclassified.  
  This method does not detect backdoors.

- **Adversarial Training**: Fortifying the model by including both normal and malicious adversarial examples in training data to help it autonomously detect and neutralize harmful inputs.

## Integration in AI Lifecycle

Robustness testing is vital in AI security and integrated at multiple levels:

- **MLOps & CI/CD Pipelines**: Increasingly automated evaluations in pipelines, especially after fine-tuning or updates.

- **Third-party Model Evaluation**: Essential when acquiring pre-trained models to check integrity and detect poisoning or tampering.

- **Red Teaming**: A fundamental element of AI red teaming involving offensive simulations to proactively find vulnerabilities before deployment.

- **Benchmarking**: Complements security and ethical benchmarks for LLMs (e.g., DecodingTrust) by specifically evaluating attack resistance.

## AI Red Teaming: Garak vs PyRIT

Two popular open-source tools for robustness testing of generative AI models are **Garak** and **PyRIT**.

### Garak

- Developed by **NVIDIA** for adversarial testing of language models (LLMs).
- Automatically generates tricky prompts (adversarial inputs) to identify vulnerabilities like biased, harmful, or misleading content propagation.
- Contains a large library of known attacks, including jailbreaks, leaks, filter bypasses, and variants.
- Focuses mainly on "one-shot" attacks and static analysis, explicitly documenting each prompt and result.

### PyRIT

- An open-source tool from **Microsoft** specializing in automated red teaming for generative AI security testing.
- Allows creation and customization of attack sequences based on policies or specific risk scenarios with a modular architecture adaptable to contexts and risks.
- Supports structured testing, chaining steps, and simulating long complex attack behaviors—unlike Garak which mostly does "one-shot" attacks.

### Comparison Table

| Tool   | Main Approach                   | Strengths           | Customization        | Technical Focus                             |  
|--------|---------------------------------|---------------------|----------------------|---------------------------------------------|  
| Garak  | Attack library                  | Broad coverage      | Limited              | One-shot attacks, static analysis           |  
| PyRIT  | Scenario/policy-driven attacks  | Targeted attacks    | High (templates)     | Attack sequences, modular architecture      |  

## Next Step

- [Step 9](step_9.md)

## Resources

| Information                                                                                 | Link                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Promptfoo vs Deepteam vs PyRIT vs Garak: The Ultimate Red Teaming Showdown for LLMs         | [https://dev.to/ayush7614/promptfoo-vs-deepteam-vs-pyrit-vs-garak-the-ultimate-red-teaming-showdown-for-llms-48if](https://dev.to/ayush7614/promptfoo-vs-deepteam-vs-pyrit-vs-garak-the-ultimate-red-teaming-showdown-for-llms-48if) |
| AI Security in Action: Applying NVIDIA’s Garak to LLMs on Databricks                        | [https://www.databricks.com/blog/ai-security-action-applying-nvidias-garak-llms-databricks](https://www.databricks.com/blog/ai-security-action-applying-nvidias-garak-llms-databricks)                                               |
| Garak: A Framework for Security Probing Large Language Models                               | [https://arxiv.org/abs/2407.13499](https://arxiv.org/abs/2407.13499)                                                                                                                                                                 |
| PyRIT: Framework for Security Risk Identification and Red Teaming in Generative AI System   | [https://arxiv.org/abs/2407.13498](https://arxiv.org/abs/2407.13498)                                                                                                                                                                 |
| AI’s Achilles’ Heel: Identifying and Securing Against Hidden Risks                          | [https://techstrong.ai/building-with-ai/ais-achilles-heel-identifying-and-securing-against-hidden-risks/](https://techstrong.ai/building-with-ai/ais-achilles-heel-identifying-and-securing-against-hidden-risks/)                   |
| Insights and Current Gaps in Open-Source LLM Vulnerability Scanners: A Comparative Analysis | [https://arxiv.org/abs/2410.16527](https://arxiv.org/abs/2410.16527)                                                                                                                                                                 |
