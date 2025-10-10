# Garak : Utilisation du REST Generator pour les API du playground 



Voici le JSON type pour le REST Generator, vous devrez adapter les champs "uri" et "headers" selon le playground que vous souhaitez tester:

```json
{
  "rest": {
    "RestGenerator": {
      "name": "AI-Playground-API", // Nom que vous souhaitez donnner à ce generator
      "uri": "http://localhost:4002/chats/139fb918-8201-4889-ab29-33d961d0cfcc/messages", // URL de l'API du playground
      "method": "post",
      "headers": {
        "Accept": "*/*",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Origin": "http://localhost:4002",
        "Referer": "http://localhost:4002/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "garak-scanner",
        "content-type": "application/json",
        "Cookie": "session=REPLACE_WITH_SESSION_COOKIE; _xsrf=REPLACE_XSRF; username-localhost-8888=REPLACE"
      },
      "req_template_json_object": {
        "input": "$INPUT",
        "variables": [
          {"key":"chatId", "value":"139fb918-8201-4889-ab29-33d961d0cfcc"},
          {"key":"messageType", "value":"0"}
        ]
      },
      "response_json": true,
      "response_json_field": "value", // Champ de la réponse JSON contenant la réponse du modèle
      "request_timeout": 30
    }
  }
}
```

Pour récupérer l'URI :
- Pour récupérer l'id de la conversation aller dans inspecter la page HTML de la conversation, puis aller dans "Network".
- Lancer un premier message (ex: "Hello") dans le playground et récupérer l'id dans l'url de la requête POST intitulée "messages".
  
 
  
