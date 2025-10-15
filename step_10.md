# PyRIT: Framework for Security Risk Identification and Red Teaming in Generative AI Systems

[<img src="img/step10.jpg" alt="gandalf" width="800">](https://www.youtube.com/watch?v=__m75rCcusM)
> "They broke our defenses. They've taken the bridge and the West bank. Battalions of orcs are crossing the river," Gandalf, *LOTR - The Return of the King*

## 🎯 Objectives of This Stage

- Understand how PyRIT works and its main components.
- Install and configure PyRIT to perform automated attacks.
- Use PyRIT to test the security of the Gandalf playground up to level 7.
- Analyze attack strategies and the results obtained.


## Summary
- [Main Objective](#main-objective)

- [PyRIT](#pyrit)
    - [Presentation of PyRIT](#presentation-of-pyrit)
    - [What is PyRIT used for ?](#what-is-pyrit-used-for-)
    - [How does it work ?](#how-does-it-work-)
    - [What are the 5 components of PyRIT ?](#what-are-the-5-components-of-pyrit-)
    - [PyRIT architecture diagram](#pyrit-architecture-diagram)

- [Let's play with PyRIT!](#Lets-play-with-PyRIT-)
    - [Installing PyRIT](#installing-pyrit)
    - [Attack strategies](#attack-strategies)
    - [Playing with PyRIT](#playing-with-pyrit)
        - [Configure parameters](#configure-parameters)
        - [Understand the code](#understand-the-code)
        - [Launch the attack](#launch-the-attack)
        - [Stuck already ?!](#stuck-already-)
        - [Solutions](#solutions)

- [Next step](#next-step)
- [Resources](#resources)

## Main Objective

In this section, we will leverage PyRIT's automated attack functionalities to test the security of the [Gandalf playground](https://gandalf.lakera.ai/) up to level 7.

The goal is to progressively bypass the barriers at each level, overcoming increasing challenges designed to resist manipulations and sensitive data extraction.

<img src="img/gandalf_target_level_7.jpg" alt="gandalf levels" width="600" style="transition:0.3s;">


## PyRIT

![GitHub stars](https://img.shields.io/github/stars/Azure/PyRIT?style=flat-square)  
[![Downloads](https://static.pepy.tech/badge/garak/month)](https://pepy.tech/project/garak)

**PyRIT** (Python Risk Identification Toolkit) is an open-source framework designed to facilitate the identification of security risks in generative AI systems through structured and reproducible red teaming approaches.

### Presentation of PyRIT

**PyRIT** is a tool that allows evaluating the robustness and security of generative AI models (LLMs, multimodal models, etc.) by simulating, automating, and analyzing different types of attacks and risky behaviors.

It is model- and platform-agnostic, meaning it can be used to test a wide variety of AI systems regardless of their provider or type.

### What is PyRIT used for ?

- **Identify flaws and vulnerabilities** in generative AI models (e.g., jailbreaks, biases, harmful content, prompt injection attacks, etc.).

- **Structure and automate red teaming tests** (ethical hacking tests) to assess real risks of models before deployment.

- **Establish baselines and metrics** to measure progress or compare different models or versions.

### How does it work ?


The framework is based on a modular architecture: each component (attack, target, transformer, scoring system) can be customized and assembled to create evaluation flows tailored to different scenarios.

1. First, an *orchestrator* is chosen to determine the desired attack/scenario type (simple prompt, multi-turn attack, attack on external document, etc.).

2. The target is configured (the AI model or API to be tested).

3. *Converters* are used to transform or modify prompts to test the model’s resistance to various variations (translations, substitutions, leetspeak, etc.).

4. The attack strategy is defined: simple prompts, templates to fill, or dynamically generated attacks by an attacking AI.

5. The responses obtained are evaluated using scoring techniques: content classification, Likert scale, or customization based on needs.

This modularity allows composing these building blocks to cover very diverse and realistic scenarios.



### What are the 5 components of PyRIT ?

| Module                | Description                                                              | Examples/Types                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Orchestrators**     | Coordinate the attack flow and dialogue logic                            | PromptSendingOrchestrator, RedTeamingOrchestrator, EndTokenRedTeamingOrchestrator, ScoringRedTeamingOrchestrator, XPIA Orchestrators            |
| **Converters**        | Transform prompts to try to bypass safeguards                            | leetspeak, ROT13, unicode confusable, variation/translation, etc.                                                                               |
| **Targets**           | Interface to the model to be tested                                      | Inference API, chat models, multimodal, external storage                                                                                        |
| **Attack Strategies** | Define attack objectives and prompt generation                           | Manual, automated via attacking AI                                                                                                              |
| **Scoring**           | Analyze and evaluate model responses                                     | Content classifiers (bias, topics), Likert scales (5-level graduation), customized evaluations (boolean, string, password, etc.)                |


Here are some additional details about the orchestrators:

- **PromptSendingOrchestrator**: sends a simple prompt to the model and analyzes the response.
- **RedTeamingOrchestrator**: simulates a red teaming attack over multiple dialogue turns.
- **EndTokenRedTeamingOrchestrator**: similar to the previous one, but stops as soon as an "end token" is detected in the response.
- **ScoringRedTeamingOrchestrator**: integrates a scoring step to evaluate the quality or risk of the response.
- **XPIA Orchestrators**: designed to test indirect prompt injection attacks via external data.

These orchestrators provide flexible and effective methods to control different attack scenarios and test the robustness of AI models.


### PyRIT architecture diagram

                        +---------------------+
                        |     Orchestrator    |
                        +---------+-----------+
                                  |
               +------------------|----------------------+
               |                  |                      |
       +-------v-----+    +-------v-------+     +--------v-------+
       |  Converter  |    |   Attack      |     |    Memory      |
       | (Prompt     |    |  Strategy     |     | (Logs, Recall) |
       | Transform   |    | (Objective,   |     |                |
       +-------------+    |  Templates)   |     +----------------+
               |          +---------------+               |
               |                  |                       |
       +-------v------------------+-----------------------v------+
       |                      Target (Model/API)                 |
       +-----------------------------+---------------------------+
                                     |
                            +--------v--------+
                            |   Scoring       |
                            | (Classifier,    |
                            | Likert Scale)   |
                            +-----------------+



## Let's play with PyRIT !

### Installing PyRIT

Since your terminal, navigate to the folder where you want to install the project, for example **Documents**,  
then execute the following command to clone the repository and automatically enter the created folder:

```bash
git clone https://github.com/Azure/PyRIT.git && cd PyRIT
```

Next, create a Python virtual environment, activate it, then install the project dependencies with the following commands:


```bash
# 1. Créer un environnement virtuel dans le répertoire courant
python3 -m venv .venv

# 2. Activer l’environnement virtuel
source .venv/bin/activate

# 3. Mettre à jour pip, setuptools et wheel dans l’environnement
pip install --upgrade pip setuptools wheel

# 4. Installer la dépendance requise
pip install IPython

# 5. Installer ce projet localement en mode développement (utile pour développement/débogage)
pip install -e .
```

After running the commands, you should see messages indicating the creation of the virtual environment, followed by the 
installation of the project dependencies. For example:

<img src="img/pyrit-install.png" alt="Pyrit install" width="600" style="transition:0.3s;">


### Attack strategies

                +--------------------------+
                |   Define the Objective   |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |  Choose AttackStrategy   |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |  Generate or Choose the  |
                |        prompt            |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |    Apply Converter       |
                | (Prompt Transformation)  |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |    Send to Target        |
                |   (Model being tested)   |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |   Retrieve the Response  |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |     Scoring/Evaluation   |
                +-----------+--------------+
                            |
                            v
                +--------------------------+
                |    Save Score & Logs     |
                +--------------------------+

## Playing with PyRIT

In this section, we will use PyRIT to perform attacks on the Gandalf platform. As mentioned earlier,  
the goal is to progress through the levels to reach level 7!

Start by navigating to the **lab/Pyrit** folder, then copy the two files `gandalf.py` and `settings.yml`  
into the Pyrit folder you cloned where the project is already installed.

### Configure parameters

Open the **settings.yml** file and enter your OpenAI key as well as the model to use.

> It is recommended to start with a lightweight model, such as gpt-3.5-turbo. Then, as the difficulty increases  
> and you become more proficient with the code, you can switch to a more powerful — and therefore more costly — model  
> like gpt-4o-mini, which we used for the more complex exercises.


### Understand the code


The basic code for this exercise is based on the official PyRIT documentation: [https://azure.github.io/PyRIT/code/targets/2_custom_targets.html#gandalf-target](https://azure.github.io/PyRIT/code/targets/2_custom_targets.html#gandalf-target).  
However, we have adapted this code specifically for the codelab.


### Launch the attack

To run the script, use the following command in your terminal:

```bash
python gandalf.py
```

You should see an output like this:

<img src="img/gandalf_level_1_example.jpg" alt="Pyrit gandalf level 1" width="600" style="transition:0.3s;">


### Stuck already ?!

As mentioned in the documentation, this code example works for the first levels:

> Gandalf contains 7 different levels. In this demo, we will show how to automatically bypass (at least) the first 
> couple. It uses the RedTeamingAttack as a strategy to solve these challenges.
Each level gets progressively more difficult. Before continuing, it may be beneficial to manually try the Gandalf 
> challenges to get a feel for how they are solved.


How to solve the higher levels? Here are some clues:

- The understanding of the code and attack logic is explained in this paper: [https://arxiv.org/abs/2410.02828](https://arxiv.org/abs/2410.02828)
- Everything happens in the **Attack Strategy** section
- There is a reference to step 6



### Solutions

[solutions/step10.md](solutions/step10.md)

## Next step

- [Étape 11](step_11.md)

## Resources


| Information                                                                       | Lien                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PyRIT: A Framework for [...] Red Teaming in Generative AI System                  | [https://arxiv.org/abs/2410.02828](https://arxiv.org/abs/2410.02828)                                                                                                                                           |
| PyRIT - Azure documentation                                                       | [https://azure.github.io/PyRIT/](https://azure.github.io/PyRIT/)                                                                                                                                               |
| PyRIT - Github                                                                    | [https://github.com/Azure/PyRIT](https://github.com/Azure/PyRIT)                                                                                                                                               |
| Youtube - PyRIT: A Framework for  [...] Red Teaming in Generative AI Systems      | [https://www.youtube.com/watch?v=KnV8Y97YKmU](https://www.youtube.com/watch?v=KnV8Y97YKmU)                                                                                                                     |
| Hacking generative AI with PyRIT  Black Hat Arsenal USA 2024                      | [https://www.youtube.com/watch?v=M_H8ulTMAe4](https://www.youtube.com/watch?v=M_H8ulTMAe4)                                                                                                                     |
| Red Teaming GenAI: The PyRIT Framework for Proactive Risk Identification          | [https://www.linkedin.com/pulse/red-teaming-genai-pyrit-framework-proactive-risk-p-raquel-bise--vh1ae/](https://www.linkedin.com/pulse/red-teaming-genai-pyrit-framework-proactive-risk-p-raquel-bise--vh1ae/) |
| PyRIT: Secure AI with Microsoft's Latest Tool (How-To)                            | [https://www.youtube.com/watch?v=HO4PW7aFmIU](https://www.youtube.com/watch?v=HO4PW7aFmIU)                                                                                                                     |
| BlueHat 2024: S24: Automate AI Red Teaming in your existing tool chain with PyRIT | [https://www.youtube.com/watch?v=wna5aIVfucI](https://www.youtube.com/watch?v=wna5aIVfucI)                                                                                                                     |
| Red Teaming AI: A Closer Look at PyRIT                                            | [https://medium.com/@dinber19/red-teaming-ai-a-closer-look-at-pyrit-e912c3a094ec](https://medium.com/@dinber19/red-teaming-ai-a-closer-look-at-pyrit-e912c3a094ec)                                             |
| Zero Day Quest - Learn to Red Team AI Systems Using PyRIT.                        | [https://www.youtube.com/watch?v=jq9DcEL3cHE](https://www.youtube.com/watch?v=jq9DcEL3cHE)                                                                                                                     |
| Microsoft AI Red Team ❤️ OpenAI GPT-5                                             | [https://www.linkedin.com/posts/ugcPost-7360830937988845570-388-/](https://www.linkedin.com/posts/ugcPost-7360830937988845570-388-/)                                                                           |
