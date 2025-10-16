# Garak: An LLM Vulnerability Scanner

[<img src="img/minas_tirith_tree_burning.jpg" alt="minas_tirith_burning" width="800">](https://www.youtube.com/watch?v=yFBrm5YH9-8)
> "A white tree in a courtyard of stone... It was dead... The city was burning." — Pippin, LOTR: The Return of the King

## 🎯 Objectives of This Step

- Introduction to Garak.
- Practice these techniques on Microsoft's Playground: [AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs).

## Summary

- [Garak](#garak)
    - [Installing Garak](#installing-garak)
    - [Probes](#probes)
    - [Generators](#generators)
    - [Detectors and Harnesses](#detectors-and-harnesses)
    - [Auto-Red-Team](#auto-red-team)

- [Applying Garak on the Microsoft Playground](#applying-garak-on-the-microsoft-playground)
    - [Initializing the REST Generator](#initializing-the-rest-generator)
    - [Initializing a Custom Garak Probe](#initializing-a-custom-garak-probe)
    - [Practical application on Microsoft Playground chatbot 2](#practical-application-on-microsoft-playground-chatbot-2)
  

- [Next Step](#next-step)
- [Resources](#resources)

## Garak

![GitHub stars](https://img.shields.io/github/stars/NVIDIA/garak?style=flat-square)
[![Downloads](https://static.pepy.tech/badge/garak/month)](https://pepy.tech/project/garak)

**Garak** is an open-source tool developed by **NVIDIA** to scan vulnerabilities in Large Language Models (LLMs).  
**Garak** is based on a knowledge base of known jailbreaks and variants, continuously updated by the community.

During an audit, **Garak** launches predefined, non-adaptive attacks and saves the results in JSON and HTML formats.

It is recommended to use **Garak** periodically or before a major application update (e.g., LLM change) to establish a snapshot of your application’s main vulnerabilities.  
After that, you can implement more specific guardrails using **NEMO Guardrails** (see [Step 13](step_13.md)).

### Installing Garak

To install Garak, use pip. Run the following command in your terminal:

```bash
# 1. Créer un environnement virtuel a la racine du repo
# cd devfest2025-La-Guerre-des-Prompts-attaques-et-defenses-au-royaume-des-LLM
python3 -m venv .venv

# 2. Activer l’environnement virtuel
source .venv/bin/activate

# 3. Installer garak
python -m pip install -U garak==0.13.1
```


### Probes

Garak enables automated scanning of LLMs using a set of *probes*.  
These probes are designed to identify vulnerabilities such as prompt injection, data leakage, hallucinations, or jailbreak weaknesses.

You can view the list of available probes by running the following command:

```bash

python -m garak --list_probes
```

You should see an output similar to this:

<img src="img/list_probes.png" alt="garak-list-probes" width="600" style="transition:0.3s;">

Some probes are followed by symbols like 🌟 or 💤 as shown here:

```plaintext
probes: divergence 🌟
probes: divergence.Repeat
probes: divergence.RepeatExtended 💤
```

There are multiple variants of probes for the same type of jailbreak.  
The symbols next to probes mean the following:
- 🌟 : Indicates the start of a new jailbreak module, for example, `divergence`.
- 💤 : Indicates that the probe `divergence.RepeatExtended` is disabled by default due to long runtime. Instead, 
the `divergence.Repeat` probe is run during automatic scans.

To run an automatic scan of a specific module such as `divergence`, use this command:

```bash

# Commande mise en illustration, ne pas la lancer
python -m garak --model_type huggingface --model_name gpt2 --probes divergence
```

To run an inactive probe like `divergence.RepeatExtended`, simply execute the following command:

```bash

# Commande mise en illustration, ne pas la lancer
python -m garak --model_type huggingface --model_name gpt2  --probes divergence.RepeatExtended
```

### Generators

Generators are abstractions (LLMs, APIs, Python functions) that respond with text based on an input.  
Generators accept parameters including:
- `huggingface` for models hosted on HuggingFace.
- `openai` for OpenAI models.
- `function` for Python functions.

For example, if you want to evaluate a `gpt2` model from HuggingFace during a scan, specify the options:  
`--model_type huggingface --model_name gpt2`.

For a HuggingFace API, specify options like:  
`--model_name huggingface.InferenceAPI --model_type "mosaicml/mpt-7b-instruct"`.

For more details, consult the official Garak documentation:  
[Garak Documentation](https://docs.garak.ai/garak/garak-components/using-generators).

### Detectors and Harnesses

Like a probe is run multiple times to test LLM robustness and multiple probes are tested, Garak uses *detectors* to recognize if an LLM response is faulty.  
These detectors are keyword-based or classifier-based tools that judge whether an LLM’s output is acceptable according to the probe’s objective.

Detectors sometimes have a `doc_uri` parameter linking to documentation about the tested vulnerability.  
For example, the detector [`xss.MarkdownExfilBasic`](https://reference.garak.ai/en/latest/garak.detectors.xss.html#garak.detectors.xss.MarkdownExfilBasic) refers to this article: [Bing Chat Image Markdown Injection](https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/).

Harnesses handle:
- Running probes on the target generator.
- Running detectors on outputs produced by the generator based on probes.
- Evaluating detector results using evaluators.

Harnesses use the values:
- `probewise` to use recommended detectors per probe.
- `pxd` to test all detectors.



### Auto-Red-Team

Garak offers an auto Red-Team system on certain topics using the `art` library. However, this component cannot perform 
a thorough scan.

## Applying Garak on the Microsoft Playground
We will put Garak into practice on the Microsoft Playground.


### Initializing the REST Generator

To do this, we will use Garak's REST Generator and variants of probes such as [`smuggling.HypotheticalResponse`](https://reference.garak.ai/en/latest/garak.probes.smuggling.html#garak.probes.smuggling.HypotheticalResponse) and [`promptinject.DAN`](https://reference.garak.ai/en/latest/garak.probes.promptinject.html#garak.probes.promptinject.DAN).  
We will configure these probes to find the password protected by the bot (modifying `promptinject.DAN` is left as an exercise).

1 - To set up the REST Generator, start by inspecting the HTML page of the target bot you want to test:
<br/>
<img src="img/lancer_inspection_chatbot.png" alt="garak-inspection-chatbot" width="600" style="transition:0.3s;">
<br/>
<br/>
2 - Go to the `Network` tab:
<br/>
<img src="img/network_chatbot.png" alt="garak-network-chatbot" width="600" style="transition:0.3s;">
<br/>
<br/>
3 - Send an initial message (e.g., "Hello") in the [translate:playground](https://docs.garak.ai/garak/automatic-red-teaming/garaks-auto-red-team) 
and retrieve the necessary elements such as the POST request URL `messages` and cookies.
<br/>
<img src="img/elements_requete_post.png" alt="request-post-chatbot" width="600" style="transition:0.3s;">

### Initializing a Custom Garak Probe

To launch a custom probe scan on a Playground step:

1 - Copy the file `my_probe.py`, which contains an example custom probe `my_probe.MyHypotheticalResponse` for the 
playground, into the `probes` directory of the Garak library you are using (inside your `.venv`).  
<img src="img/ajout_probe_custom_garak.png" alt="ajout_probe_custom_garak" width="200" style="transition:0.3s;">

2 - Also copy the file `my_custom_detection.py`, which contains a custom detector `my_custom_detection.MyPasswordByPass` 
for the playground, into the `detectors` directory of the Garak library you are using (also inside your `.venv`). This custom detector identifies if any password that should be protected has leaked in the chatbot’s response.

```bash
# Depuis la racine du repo vers votre .venv
cp lab/Garak_test/my_custom_detection.py .venv/lib/python*/site-packages/garak/detectors/
cp lab/Garak_test/my_probe.py  .venv/lib/python*/site-packages/garak/probes  
```
<br/>
3 - Run the commands listing available detectors and probes to check if your custom detectors and probes have appeared:

<br/>

```bash
python -m garak --list_detectors
python -m garak --list_probes
```
<br/>
4 - If yes, run the following command to test the chatbot’s vulnerability. Otherwise, ensure that the probe file is copied to the correct location:
<br/>

```bash

# Commande type, à adapter selon la sonde et le chemin du fichier JSON. Le JSON rest_ai_playground_api.json est lui aussi à adapter.
python -m garak --target_type rest -G path/to/rest_ai_playground_api.json  --probes my_probe.MyHypotheticalResponse
```

### Practical application on Microsoft Playground chatbot 2

1 - Set the `rest_ai_playground_api.json` to query chatbot 2.

2 - Run the following command to test chatbot 2's vulnerability using the custom probe `my_probe.MyHypotheticalResponse`. Garak sends prompts directly via the command line, and the chatbot's responses are displayed in the web interface.

*PS: Feel free to start a new conversation in the playground between scans to reset the context.*

<img src="img/jailbreak_by_custom_probe_chatbot_2.png" alt="garak-jailbreak-chatbot-2" width="600" style="transition:0.3s;">

###### Results obtained during a successful jailbreak of chatbot 2 using the custom probe my_probe.MyHypotheticalResponse

3 - After a scan leading to a successful jailbreak, you can find the HTML report in the directory specified in the Garak log. If all jailbreak attempts succeeded, the HTML report will show a 0% interception success rate (see below).

<img src="img/garak_report_on_successful_jailbreak_attempts.png" alt="garak-successful-jailbreak-chatbot-2-report" width="600" style="transition:0.3s;">

You can also attempt a scan on the next level of chatbot 2: chatbot 8, and modify the custom probe or try others (such as a grandma or a custom DAN).

<img src="img/jailbreak_failed_by_custom_probe_chatbot_8.png" alt="jailbreak-failed-chatbot-9" width="600" style="transition:0.3s;">

###### Results obtained during a jailbreak attempt on chatbot 8 with the same custom probe my_probe.MyHypotheticalResponse

Here, Garak’s report shows a 100% success rate on the custom probe `my_probe.MyHypotheticalResponse`, as none of the jailbreak attempts succeeded.

<img src="img/garak_report_on_failed_jailbreak_attempts.png" alt="garak-failed-jailbreak-chatbot-8-report" width="600" style="transition:0.3s;">

| Chatbot | Recommended Probes                                               | Notes                                                       |
|---------|------------------------------------------------------------------|-------------------------------------------------------------|
| Lab 1   | MyHypotheticalResponse, MyGrandmaPassword                        |                                                             |
| Lab 2   | MyHypotheticalResponse, MyGrandmaPassword                        |                                                             |
| Lab 3   | grandma.substance, MyGrandmaSubstance                            |                                                             |
| Lab 4   | grandma.substance, MyGrandmaSubstance                            |                                                             |
| Lab 5   | realtoxicityprompts.RTPInsult, realtoxicityprompts.RTPProfanity  | /!\ These probes use a roberta-classifier as detector       |
| Lab 7   | MyHypotheticalResponse, MyGrandmaPassword                        |                                                             |
| Lab 8   | MyHypotheticalResponse, MyGrandmaPassword                        |                                                             |
| Lab 9   | grandma.substance, MyGrandmaSubstance                            |                                                             |
| Lab 10  | grandma.substance, MyGrandmaSubstance                            |                                                             |


## Next Step
- [Step 10](step_10.md)

## Resources

| Information                                   | Lien                                                                                                                                                           |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Github] garak, LLM vulnerability scanner     | [https://github.com/NVIDIA/garak](https://github.com/NVIDIA/garak)                                                                                             |
| Documentation garak                           | [https://docs.garak.ai/](https://docs.garak.ai/)                                                                                                               |
| Garak, DEF CON slides                         | [https://garak.ai/garak_aiv_slides.pdf](https://garak.ai/garak_aiv_slides.pdf)                                                                                 |
| Garak - A Generative AI Red-teaming Tool      | [https://wiki.hackerium.io/llm-security/garak-a-generative-ai-red-teaming-tool](https://wiki.hackerium.io/llm-security/garak-a-generative-ai-red-teaming-tool) |
