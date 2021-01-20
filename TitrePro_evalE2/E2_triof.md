# Amélioration grâce à l'IA d'une application existante

Il s'agit du cas pratique 1 (évaluation E2) du titre professionnel de "Développeur en intelligence artificielle".

## Contexte

Triof est une start-up de tri et de recyclage des déchets spécialisée dans le traitement des déchets plastiques. Elle a développé une machine qu'elle loue aux entreprise : grâce à cette dernière les salariés peuvent déposer leurs déchets plastiques afin qu'ils soient recyclés en fil d'impression 3D.

Il est important de trier les déchêts plastiques avant de les recycler car le point de fusion de chaque plastique est différent. L'entreprise a donc conçu une interface où l'utilisateur sélectionne le type de dêchet qu'il entre dans la machine. 

Malheureusement on a remarqué que les personnes n'indiquaient pas toujours bien quel déchet ils inséraient or cela a un impact négatif sur la qualité du filament.

Triof vous sollicite pour proposer une solution intégrant de l'IA afin de pallier ce problème.

## Questions préliminaires

### Compréhension du problème

Après avoir analysé le fonctionnement de l'application de Triof et expliqué votre compréhension du problème, proposer une solution basée sur de l'IA.

### Généralités sur l'intégration d'une IA dans une application existante
1. Expliquer en un paragraphe ce qu'est l'architecture client/serveur et quels sont ses avantages. Vous accompagnerez vos explications d'un schéma fait sur https://draw.io. Veiller à la clarté du propos.
2. Expliquer ce qu'est un web service et son utilité dans le développement d'applications.
3. Expliquer en quoi un modèle packagé dans un web service permet de l'utiliser en production et pourquoi c'est une bonne idée par rapport à utiliser un script python.

## Première approche : une solution IA Cloud

Mise en place d'une solution utilisant Custom Vision de Azure Cognitive Services. 

### Choix d'une solution Cloud

Décrire en quelques ligne le fonctionnement, le mode de tarification et le coût de ce service.

Quels autres services clouds fournis par différents providers (azure, google, amazon, ovh, etc) permettraient de répondre à la problématique exposée ? Comparer ces différents services notamment en termes de coût, de rapidité. Vous pouvez synthétiser tout ça dans un tableau

### Mise en place de la solution

En pratique, indications :
1. Créer sur Azure un groupe de ressource ainsi qu'une ressource Cognitive Services
2. Sur le portail Custom Vision (https://www.customvision.ai/), initier un projet en le reliant à votre ressource tout juste créée.
3. Entraîner un modèle de reconnaissance d'image permettant d'identifier les 3 types de déchets plastiques distingués par l'application.
4. Publier votre modèle afin de pouvoir le mobiliser via API
5. Intégrer un appel API dans l'application mettant en place la solution qui vous parait le plus mieux : précocher le type de déchet plastique, suggérer le type de déchet, etc...

## Deuxième approche : une amélioration via une solution locale

Un autre problème auquel la machine de Triof fait face est l'insertion par les salariés de déchets plastiques **sales** ce qui entraîne là encore, un fil d'impression de moindre qualité.

Proposer cette fois une solution sans recourir aux services IA Cloud pour résoudre ce problème.

Indications:
- Vous êtes relativement libres sur cette partie mais l'idée est de construire un modèle permettant de classifier, en plus du type de déchet, la propreté du déchet.
- Vous pourrez soit construire votre propre modèle soit utiliser du *transfer learning* à partir de modèles de computer vision pré-implémentés.
- Une étape cruciale va être la constitution de votre jeu de données d'entraînement. Plusieurs solutions sont possibles notamment le scraping. Quoi qu'il en soit, n'oubliez pas l'existence de la *data augmentation*...

## Les livrables

Voir les infos sur le passage du titre pro :
https://github.com/louiskuhn/PromoIA/blob/master/Admin/Titre%20Professionnel%20Simplon/Developpeurse_en_intelligence_artificielle_Mode_demploi_passage_du_titre_1.pdf

- le code de l'application finale
- 1 rapport écrit de 5 à 10 pages sur les réalisations produites (n'oubliez pas d'intégrer dans votre rapport les réponses apportées aux différentes questions)
- 1 présentation orale de 5 min (pour la soutenance)

