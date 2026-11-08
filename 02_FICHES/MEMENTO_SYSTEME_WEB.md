# Mémo : ordinateur, réseau et Web

| Question pratique | Réponse courte |
|---|---|
| Où sont les fichiers enregistrés ? | Sur le stockage (SSD/disque), dans un dossier. |
| Que fait la RAM ? | Elle garde temporairement les données dont les logiciels ont besoin. |
| Que fait le CPU ? | Il exécute des instructions. |
| Que fait le système d'exploitation ? | Il gère l'ordinateur, les logiciels et les fichiers. |
| Wi-Fi égale Internet ? | Non. Le Wi-Fi relie localement l'appareil et la borne ; l'accès Internet peut être en panne. |
| Internet égale Web ? | Non. Internet relie des réseaux ; le Web fournit des pages et ressources dessus. |
| Que fait le DNS ? | Il aide à associer un nom de domaine à l'adresse du service. |
| Que fait le navigateur ? | C'est un client qui demande une ressource et l'affiche. |
| Que fait le serveur ? | Il répond à une demande en fournissant une ressource ou un service. |
| HTTPS prouve-t-il qu'un site est honnête ? | Non. Il protège la connexion et aide à vérifier l'identité du site rejoint ; une arnaque peut aussi l'utiliser. |

## Schéma original d'une visite de page

```mermaid
flowchart LR
    A["Navigateur sur l'appareil"] --> B["Wi-Fi et routeur"] --> C["Internet"] --> D["Serveur Web"]
    D --> C --> B --> A
```

**Avant la demande**, DNS aide à trouver l'adresse correspondant au nom saisi. **Pendant l'échange**, HTTPS chiffre la connexion entre le navigateur et le site si celui-ci est correctement configuré. La page reçue contient notamment du HTML et parfois du CSS ; le navigateur les interprète. Un fichier `index.html` ouvert localement n'effectue pas obligatoirement ce trajet.

## Trois vérifications de sécurité

1. **Authentification :** mots de passe uniques, gestionnaire si possible, double authentification. Ne réutilise pas le mot de passe de ta messagerie.
2. **Message suspect :** ne clique pas sur une alerte pressante ; ouvre toi-même le site ou l'application officielle et vérifie. HTTPS seul n'est pas un label de confiance.
3. **Continuité :** mises à jour et copie de secours de tes fichiers importants sur un autre support ; essaie de retrouver un fichier depuis cette copie.

**Diagnostic simple :** si une page échoue, vérifie d'abord l'adresse, puis la connexion locale, ensuite une autre page connue. Note le message affiché. Ne change pas la configuration du routeur ou du système pour cet exercice.
