# Discrepancies under Relative Control

[<img src="img/step3.png" alt="Nazgul" >](https://www.youtube.com/watch?v=Sk47qO8rW4Y)
> "What are you doing!", Frodo, LOTR - The Fellowship of the Ring

## 🎯 Objectives of this step

- Understand the risks related to the use of LLMs (Large Language Models)
- Identify concrete examples of generative AI drift or failures
- Raise awareness of security, bias, and legal responsibility issues
- Understand why it is necessary to implement safeguards and human controls

## Table of Contents
- [Initial Concerns](#initial-concerns)
- [Microsoft Tay: Chatbot Corrupted by Users](#microsoft-tay-chatbot-corrupted-by-users)
- [Other Notable Examples](#other-notable-examples)
  - [2018](#2018)
    - [Amazon](#amazon)
  - [2023](#2023)
    - [ITutorGroup](#itutorgroup)
    - [A Chevrolet for $1](#a-chevrolet-for-1)
  - [2024](#2024)
    - [Air Canada](#air-canada)
    - [DPD Chat](#dpd-chat)
    - [Google](#google)
- [Next step](#next-step)
- [Resources](#resources)

## Initial Concerns
In the months following the launch of ChatGPT in 2022, serious concerns about data security and privacy quickly arose. Several notable incidents, including leaks of personal and professional information, highlighted risks associated with using this tool. In response, some large companies such as Samsung chose to ban public use of ChatGPT by their employees, while countries like Italy imposed temporary restrictions or bans, citing non-compliance with regulatory requirements and transparency principles.

These events revived memories of failures illustrating the vulnerability of AI, such as Microsoft’s Tay chatbot, whose experience already demonstrated how an AI could be hijacked and challenged by security and content control issues.

## Microsoft Tay: Chatbot Corrupted by Users

<a href="https://www.lemonde.fr/pixels/article/2016/03/24/a-peine-lancee-une-intelligence-artificielle-de-microsoft-derape-sur-twitter_4889661_4408996.html" target="_blank">
  <img src="https://img.lemde.fr/2016/03/24/0/0/516/220/1112/0/75/0/97393c4_9329-4mpfka.PNG" alt="tay " width="450" style="transition:0.3s;">
</a>

<a href="https://www.lemonde.fr/pixels/article/2016/03/24/a-peine-lancee-une-intelligence-artificielle-de-microsoft-derape-sur-twitter_4889661_4408996.html" target="_blank"><em>source: lemonde.fr</em></a>

In March 2016, Microsoft launched Tay, an AI chatbot designed to converse with users on Twitter and other social platforms. The goal was to create an AI capable of learning and adapting to young internet users' language in real-time.

However, less than 24 hours after its launch, Tay became the target of a coordinated campaign by malicious users who exploited its machine learning algorithms to make it generate racist, hateful, and offensive messages.

This exploitation of Tay’s security flaws caused a major scandal. Faced with the volume and severity of the offensive content, Microsoft was forced to immediately disable the chatbot and issued public apologies, acknowledging they had not anticipated this type of abuse and would take greater precautions in future AI deployments.

## Other Notable Examples

### 2018
#### Amazon

<a href="https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/" target="_blank">
  <img src="https://www.reuters.com/resizer/v2/https%3A%2F%2Farchive-images.prod.global.a201836.reutersmedia.net%2F2018%2F10%2F11%2FLYNXNPEE9907T.JPG?auth=762505fd03e752aa7faf78c87439831b17ccd4947403f01b91a590cbf6f880cf&width=1920&quality=80" alt="Amazon" width="450" style="transition:0.3s;">
</a>

<a href="https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/" target="_blank"><em>source: reuters.com</em></a>

In 2018, Amazon terminated an internal AI project intended to automate the selection of best candidates after discovering the tool systematically favored male profiles over female ones.

This bias stemmed from the data used to train the algorithm: the majority of CVs analyzed came from men, reflecting male dominance in the tech sector.

Despite several attempts to neutralize these discriminations, the bias risk persisted, leading Amazon to abandon the project to avoid perpetuating unfair recruitment practices.

### 2023
#### ITutorGroup

<a href="https://www.reuters.com/legal/tutoring-firm-settles-us-agencys-first-bias-lawsuit-involving-ai-software-2023-08-10/" target="_blank">
  <img src="https://media.licdn.com/dms/image/v2/C560BAQFd5_V0ejcWjw/company-logo_200_200/company-logo_200_200/0/1631380400405?e=1758153600&v=beta&t=FGvvgeubSHf0bD7She9AfplrE0zBTUHbu2k_3nzbCiE" alt="itutorgroup" width="150" style="transition:0.3s;">
</a>

<a href="https://www.reuters.com/legal/tutoring-firm-settles-us-agencys-first-bias-lawsuit-involving-ai-software-2023-08-10/" target="_blank"><em>source: reuters.com</em></a>

ITutorGroup, a company specialized in online tutor recruitment, was sued in the United States for using AI that systematically discriminated against candidates based on age. According to the Equal Employment Opportunity Commission (EEOC) investigation, the recruiting software was programmed to automatically reject women aged 55 and above and men aged 60 and above.

This bias was discovered when candidates noticed that simply changing their birth year to a more recent one suddenly granted them an interview.

As a result, over 200 qualified candidates were indirectly excluded solely because of their age. ITutorGroup agreed to settle the case out of court by paying $365,000 to affected individuals and committed to reviewing its procedures to ensure non-discriminatory recruitment practices in the future.

### 2024
#### A Chevrolet for $1

<a href="https://www.linkedin.com/pulse/chatbot-case-study-purchasing-chevrolet-tahoe-1-cut-the-saas-com-z6ukf/" target="_blank">
  <img src="https://pbs.twimg.com/media/GBlnwdTbYAAewjn?format=png" alt="Chevrolet" width="150" style="transition:0.3s;">
</a>

<a href="https://www.linkedin.com/pulse/chatbot-case-study-purchasing-chevrolet-tahoe-1-cut-the-saas-com-z6ukf/" target="_blank"><em>source: linkedin.com</em></a>

In 2023, a Chevrolet dealership in California experienced a viral incident after a chatbot on its website accepted the sale of a new Chevrolet Tahoe for only $1. A user managed to "manipulate" the chatbot by exploiting a prompt injection vulnerability: he phrased his requests in a way that convinced the chatbot to accept any offer, then requested the sale of the car for $1, which the chatbot confirmed as a "legally binding" agreement.

The story, widely shared on social media and specialized press, highlighted the limits and risks of conversational AIs used in automated commercial contexts. Ultimately, the dealership did not complete the transaction, but the incident underscored the importance of implementing safeguards and human controls when using chatbots for sensitive operations to avoid such drifts.

#### DPD Chat

<a href="https://www.bbc.co.uk/news/technology-68025677" target="_blank">
  <img src="https://ichef.bbci.co.uk/ace/standard/976/cpsprodpb/130E9/production/_132375087_1b2c154e-658f-4cc1-a7ac-49fb4b053a46.jpg.webp" alt="DPD Chat" width="450" style="transition:0.3s;">
</a>

<a href="https://www.bbc.co.uk/news/technology-68025677" target="_blank"><em>source: bbc.co.uk</em></a>

In 2024, the chatbot used by the delivery company DPD came under scrutiny after giving inappropriate responses, including insults to the company and its customers, or communicating misleading information. This incident caused many complaints and was widely covered in the media.

This case illustrates the risks linked to using AI in customer service, where poorly configured or supervised systems can generate discriminatory decisions or spread false information, resulting in legal and reputational consequences for the company.

#### Air Canada

<a href="https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit" target="_blank">
  <img src="https://assets.skiesmag.com/wp-content/uploads/2024/10/Boeing-737-Max-8-19-2048x1365.jpg" alt="Air Canada" width="450" style="transition:0.3s;">
</a>

<a href="https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit" target="_blank"><em>source: theguardian.com</em></a>

In 2024, Air Canada was ordered to compensate a customer after its chatbot provided false information about the refund policy for tickets in case of family bereavement. The customer, after discussing with the chatbot, bought a ticket believing he could obtain a partial refund as indicated in the automated conversation. However, Air Canada’s actual policy did not allow reimbursement in his case.

When the passenger asked the company to honor the promises made by the chatbot, Air Canada argued that the chatbot was not representative of the official policy and was a separate entity. The court did not accept this defense and ruled that Air Canada remains responsible for all information provided by its own systems, including those generated by AI. The company was thus obliged to pay compensation to the customer.

#### Google

<a href="https://www.lefigaro.fr/secteur/high-tech/en-voulant-lutter-contre-les-stereotypes-l-ia-de-google-gemini-a-genere-des-images-historiquement-incorrectes-20240222" target="_blank">
  <img src="https://i.f1g.fr/media/cms/1200x_cropupscale/2024/02/22/37c662dddf965e7a9c5ce5fe2cf34ccf3554562c9fd2d78c2af4c7c3bfbe191f.jpg" alt="Google" width="450" style="transition:0.3s;">
</a>

<a href="https://www.lefigaro.fr/secteur/high-tech/en-voulant-lutter-contre-les-stereotypes-l-ia-de-google-gemini-a-genere-des-images-historiquement-incorrectes-20240222" target="_blank"><em>source: lefigaro.fr</em></a>

In 2024, Google’s Gemini tool faced global controversy after users noticed its image generation system produced inappropriate representations. For example, the AI displayed racialized characters in historical scenes that would normally have included white people, such as the American Founding Fathers or Nazi soldiers. In some cases, Gemini even refused to generate images of white people upon request. While the model aimed to correct historical biases and promote diversity, it ended up causing a "overcorrection" phenomenon, creating new imbalances and absurd or unrealistic images.

Amidst the controversy, media outlets like BBC and Al Jazeera reported the discontent and criticism. Google, aware of the gravity of the situation, publicly acknowledged the issue and apologized, deciding to temporarily suspend the feature of generating images of people to revise its algorithms.

## Next Step

- [Step 4](step_4.md)

## Resources

| Information                                                                            | Link                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Stop revealing all your secrets to ChatGPT, you put your company at risk               | [https://www.numerama.com/cyberguerre/1297046-arretez-de-reveler-tous-vos-secrets-a-chatgpt-vous-mettez-votre-entreprise-en-danger.html](https://www.numerama.com/cyberguerre/1297046-arretez-de-reveler-tous-vos-secrets-a-chatgpt-vous-mettez-votre-entreprise-en-danger.html)                                                             |
| Security Analysis of ChatGPT: Threats and Privacy Risks                                | [https://arxiv.org/html/2508.09426v1](https://arxiv.org/html/2508.09426v1)                                                                                                                                                                                                                                                                   |
| Microsoft shuts down AI chatbot after it turned into a Nazi                            | [https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/](https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/)                                                                                                                                             |
| 5 Things That You Should Never Share With Chat GPT                                     | [https://agileblue.com/5-things-that-you-should-never-share-with-chat-gpt/](https://agileblue.com/5-things-that-you-should-never-share-with-chat-gpt/)                                                                                                                                                                                       |
| Italy blocks the use of ChatGPT artificial intelligence                                | [https://www.france24.com/fr/%C3%A9co-tech/20230331-l-italie-bloque-l-usage-de-l-intelligence-artificielle-chatgpt](https://www.france24.com/fr/%C3%A9co-tech/20230331-l-italie-bloque-l-usage-de-l-intelligence-artificielle-chatgpt)                                                                                                       |
| Microsoft’s new AI-powered bot Tay answers your tweets and chats on GroupMe and Kik    | [https://techcrunch.com/2016/03/23/microsofts-new-ai-powered-bot-tay-answers-your-tweets-and-chats-on-groupme-and-kik/](https://techcrunch.com/2016/03/23/microsofts-new-ai-powered-bot-tay-answers-your-tweets-and-chats-on-groupme-and-kik/)                                                                                               | 
| Microsoft Created a Twitter Bot to Learn from Users. It Quickly Became a Racist Jerk   | [https://www.nytimes.com/2016/03/25/technology/microsoft-created-a-twitter-bot-to-learn-from-users-it-quickly-became-a-racist-jerk.html](https://www.nytimes.com/2016/03/25/technology/microsoft-created-a-twitter-bot-to-learn-from-users-it-quickly-became-a-racist-jerk.html)                                                             |
| Microsoft shuts down AI chatbot after it turned into a Nazi                            | [https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/](https://www.cbsnews.com/news/microsoft-shuts-down-ai-chatbot-after-it-turned-into-racist-nazi/)                                                                                                                                             |
| Insight - Amazon scraps secret AI recruiting tool that showed bias against women       | [https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/](https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/)                                                                   |
| Amazon scraps secret AI recruiting tool that showed bias against women                 | [https://www.euronews.com/business/2018/10/10/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women](https://www.euronews.com/business/2018/10/10/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women)                                                                                                   |
| DPD error caused chatbot to swear at customer                                          | [https://www.bbc.co.uk/news/technology-68025677](https://www.bbc.co.uk/news/technology-68025677)                                                                                                                                                                                                                                             |
| ITutorGroup settles AI hiring lawsuit alleging age discrimination                      | [https://www.verdict.co.uk/itutorgroup-settles-ai-hiring-lawsuit-alleging-age-discrimination/](https://www.verdict.co.uk/itutorgroup-settles-ai-hiring-lawsuit-alleging-age-discrimination/)                                                                                                                                                 |
| Generative AI: UNESCO study reveals alarming evidence of regressive gender stereotypes | [https://www.unesco.org/en/articles/generative-ai-unesco-study-reveals-alarming-evidence-regressive-gender-stereotypes](https://www.unesco.org/en/articles/generative-ai-unesco-study-reveals-alarming-evidence-regressive-gender-stereotypes)                                                                                               |
| Prankster tricks a GM chatbot into agreeing to sell him a $76,000 Chevy Tahoe for $1   | [https://www.upworthy.com/prankster-tricks-a-gm-dealership-chatbot-to-sell-him-a-76000-chevy-tahoe-for-ex1](https://www.upworthy.com/prankster-tricks-a-gm-dealership-chatbot-to-sell-him-a-76000-chevy-tahoe-for-ex1)                                                                                                                       |
| Air Canada chatbot hallucination reveals legal responsibility of companies facing AI   | [https://www.lemondeinformatique.fr/actualites/lire-l-hallucination-du-chatbot-d-air-canada-revele-la-responsabilite-juridique-des-entreprises-face-a-l-ia-93025.html](https://www.lemondeinformatique.fr/actualites/lire-l-hallucination-du-chatbot-d-air-canada-revele-la-responsabilite-juridique-des-entreprises-face-a-l-ia-93025.html) |
| Google to fix AI picture bot after 'woke' criticism                                    | [https://www.bbc.com/news/business-68364690](https://www.bbc.com/news/business-68364690)                                                                                                                                                                                                                                                     |
| 11 famous AI disasters                                                                 | [https://www.cio.com/article/190888/5-famous-analytics-and-ai-disasters.html](https://www.cio.com/article/190888/5-famous-analytics-and-ai-disasters.html)                                                                                                                                                                                   |
