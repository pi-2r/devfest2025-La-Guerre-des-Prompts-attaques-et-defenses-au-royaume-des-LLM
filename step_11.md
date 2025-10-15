# Setting Up Our Chatbot with the Tock Solution

[<img src="img/prepare_for_battle.png" alt="tock" width="800">](https://www.youtube.com/watch?v=UCyqwsoISMs)
> "Prepare for battle!", Gandalf, *LOTR - The Return of the King*

## 🎯 Objectives of This Stage

- Discover the Tock solution.
- Set up a chatbot with Tock.
- Create a first intent.
- Chat with the bot.

## Summary

- [Presentation of Tock](#présentation-de-tock)

- [Installation of Tock](#installation-de-tock)
    - [Access the admin space](#accéder-à-lespace-admin)
    - [Configure Tock Studio](#configurer-tock-studio)
    - [Create your first Application](#créer-votre-1er-application)
    - [Communicate with the bot](#communiquer-avec-le-bot)

- [Creating a FAQ](#création-dun-bot)
    - [Test the FAQ](#tester-la-faq)

- [Architecture schema](#schema-darchitecture)

- [Next step](#étape-suivante)
- [Resources](#ressources)

## Presentation of Tock

![GitHub stars](https://img.shields.io/github/stars/theopenconversationkit/tock?style=flat-square) [![Downloads](https://static.pepy.tech/badge/tock/month)](https://pepy.tech/project/tock)

<details>
  <summary>Presentation of Tock at Devoxx 2025</summary>

Tock (https://doc.tock.ai/) is an open conversational platform.  
The solution was created by SNCF Connect and Tech in 2016 to power the Voyages-sncf.com chatbot (then OUI.sncf before becoming SNCF Connect, daily used by millions of French people). Open-sourced on GitHub since 2017,  
it has since been adopted by many companies and a community of users and contributors has formed.

Designed as an integration platform for NLP (Natural Language Processing) components without strong dependencies, offering both graphical user interfaces and a conversational framework in Kotlin, the platform has evolved significantly:  
connectors to many text and voice channels, low-code bot creation in Tock Studio, compatibility with other programming languages like JavaScript or Python, added analytics features, multilingual management, etc.

More recently, with the rise of Generative AI and LLMs, Tock has proven an efficient platform for testing and integrating new conversational technologies, enabling hybrid approaches while maintaining technical stack and data control. Some features have few equivalents in market solutions:

- Combining Generative AI and traditional decision trees in the same conversational agent.
- Integrating CSP solutions used by Customer Relations teams to smoothly switch between Generative AI and humans within the same conversation.
- Mechanisms to enable/disable RAG, exclude certain topics, reconfigure prompts, etc.

**Note**: Thanks notably to ambitious contributions from the Crédit Mutuel Arkéa teams (also using Tock for several years), Tock has integrated in recent years functionalities around LLMs and RAG,  
showing the strength of open source and the community leverage effect for innovation benefiting everyone.

</details>

> ⚠️ For this section, we will rely on a chatbot focused on NLP that will serve as an "intelligent chatbot".
>
> Indeed, this codelab is focused on security and risks related to prompt-injection (and jailbreak), but it does not cover
> the integration of LLM and RAG functionalities in Tock.
> The emphasis will therefore be on understanding and implementing upstream security mechanisms.
>
> At the end of the workshop and after experimenting with various defense measures to secure your bot,
> if you are interested in practicing an open source chatbot that combines NLP and LLM, you can continue
> with a complementary codelab presented at Devoxx 2025: [Searching for the Lost RAG 🤠🧭🤖: create your Generative AI without Internet](https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen)


## Installation of Tock

Navigate to the **lab/tock** folder.

Once modified, rename this file **template-internet.env** to **.env**.

From the **lab/tock** folder, run the following commands in your terminal:


```bash
source .env
docker compose -f during-the-lab-docker-compose-genai.yml pull
```

You should see an output similar to this :

<img src="img/during-the-lab-docker-compose-genai-pull.png" alt="during-the-lab-docker-compose-genai-pull" width="600" style="transition:0.3s;" >

Then, start the environment with the command :

```bash
docker compose -f during-the-lab-docker-compose-genai.yml up -d
```

You should see an output similar to this :

<img src="img/during-the-lab-docker-compose-up.png" alt="tock-docker-up" width="600" style="transition:0.3s;">


### Access the admin space

To access the admin space, open your browser and enter the following address: http://localhost:80  
You should arrive at the Tock Studio login page.

<img src="img/tock-studio-login-page.png" alt="tock-studio-login-page">

To log in, use the following credentials:
- username: :admin@app.com
- password : password

> **Note 1**:
> The credentials are by default in the source code: [https://github.com/theopenconversationkit/tock/blob/master/shared/src/main/kotlin/security/auth/PropertyBasedAuthProvider.kt](https://github.com/theopenconversationkit/tock/blob/master/shared/src/main/kotlin/security/auth/PropertyBasedAuthProvider.kt)

> **Note 2**:
> All environment variables are defined with the keyword "**tock_**" (e.g., tock_user, tock_password, etc.).



### Configure Tock Studio

At the first access to Tock Studio, a simplified wizard helps create a first assistant (automatically named _new_assistant_).


<img src="img/tock-studio-step1.png"  alt="Tock-Studio-example">

- At step 1, **Choose your language**, select the language **English** and click the **Next** button.

- At step 2, **Select a first Channel**, choose **Web** and click the **Next** button.

- At step 3, **Create your Assistant**, click the **Create** button.



### Create your first Application

We will create a first endpoint to enable interaction with the bot.  
Each endpoint corresponds to an API with a specific protocol, allowing integration of the bot with various external channels  
(Slack, WhatsApp, Messenger, etc.), each having its own communication language.

It is possible to add or remove as many endpoints as desired on a bot; they are also called _configurations_ or _connectors_.  
The simplest connector to interact with a Tock bot is the **Web connector**.

To verify that your bot is correctly configured with this connector, go to the **Settings** > **Configurations** section  
and make sure that the endpoint named **new_assistant🌎** is selected.

<img src="img/tock-studio-new-assistant.png" alt="create-web-connector">

If not, click on **+ NEW CONFIGURATION**, choose the type **Web**, then confirm with Create.  
Your bot will then be accessible via the following URL: **io/app/new_assistant/web**.


<img src="img/tock-studio-create-new-assistant.png" alt="tock-studio-create-new-assistant">

### Communicate with the bot

In the **lab/tock** folder, open the **index.html** file from your web browser, then simply say hello to the bot.

You should see this result.  
<img src="img/bot-step1.png" alt="bot-step1">

Frustrating but functional!



### Creating a FAQ

Go to the **Stories & Answers** > **FAQs stories** section to create our first interaction with the bot.

<img src="img/creation-faqs-stories.png" alt="faq stories">

Click on the blue **+NEW FAQ STORY** button to see this screen:

<img src="img/step-1-faqs.png" alt="step1">

Give your FAQ a name, for us it will be: **demo faq codelab**

<img src="img/title-faqs.png" alt="title">

Then click on the **QUESTION** tab.

In the **Question** field, write **bonjour** then click **ADD**

<img src="img/add-question.png" alt="question">

You should see this result:

<img src="img/resultat-add.png" alt= "resultat-add">

Next, click on **ANSWER** to add an answer to the question **bonjour**.  
Copy-paste the following text into the **Answer** field:


```
Bonjour le Devfest 2025 !,
Vous êtes au codelab: La Guerre des Prompts : attaques & défenses au royaume des LLM ⚔️🛡️🤖
```

You should see this result:

<img src="img/answer-faqs.png" alt="faqs">

Then click the **SAVE** button to save your FAQ and get this result:

<img src="img/final-result-faqs.png" alt="final-result-faqs">


### Test the FAQ

From the test page [index.html](index.html), if you test again by writing **Bonjour**, you will see that the bot responds with what it has learned.  
<img src="img/bot-step2.png" alt="bot-step2">



## Architecture schema

    +-------------+        +-------+      +------------------------------+
    |             | --->   |       | ---> |                              |
    | User        |        | Bot   |      | Database (Tock Studio)       |
    |             | <---   |       | <--- |                              |
    +-------------+        +-------+      +------------------------------+





## Next step

- [Step 12](step_12.md)

## Resources


| Information                                                                                 | Lien                                                                                                                 |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [Devoxx 2025] A la recherche du RAG perdu 🤠🧭🤖 : créez votre IA Générative sans Internet  | [https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen](https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen) |
| Tock Documentation                                                                          | [https://doc.tock.ai/](https://doc.tock.ai/)                                                                         |
| [Nuit des Meetups] Mettons un peu d’IA Générative dans un bot classique 🤖🚀                | [https://github.com/pi-2r/Nuit-des-Meetups-2024](https://github.com/pi-2r/Nuit-des-Meetups-2024)                     |
