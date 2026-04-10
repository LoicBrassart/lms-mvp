## Introduction aux prototypes

Le prototypage a pour vocation simuler le produit final. Il va permettre de mettre en scène la maquette de façon fonctionnelle.

![](https://cdn.dribbble.com/users/27547/screenshots/4013027/video-reveal.gif)

_Source : [dribble.com](https://dribbble.com/shots/4013027-Video-Reveal)_

## 🤓 À la fin de cette quête, tu sauras

✅ Quels sont les principes du prototypage sur Figma
✅ Créer des interactions entre différents éléments
✅ Associer des pages entre elles

---

## En quoi consiste un prototype ?

Il s’agit d’une projection en situation réelle. Le site ou l’application répondront de la même façon que s'ils étaient déployés sur support physique (ordinateur, téléphone, …etc).

On peut y retrouver les différentes interactions entre les pages comme le parcours d’achat d’un produit ou des effets visuels tels que des animations au survol des boutons.

![](https://cdn.dribbble.com/users/977026/screenshots/4719197/shot-final.gif)

_Source : [dribble.com](https://dribbble.com/shots/4719197-Tariff-Cards-Landing-Page/attachments/4719197-Tariff-Cards-Landing-Page?mode=media)_

## Avantages

Au delà de présenter le produit fini, le prototype permet à l’intégrateur de visualiser quelles seront les fonctionnalités attendues durant la phase de développement web.

Il offre également au client la possibilité de valider une maquette opérationnelle en aval de la phase d’intégration.

---

## Éléments d’un prototype

Avant de commencer dans le vif du sujet, reprenons quelques éléments de vocabulaire importants qui te permettront de comprendre au mieux les différentes parties prenantes d’un prototype.

### Flow

En design d'interface (ou **UI/UX design**), un **flow** (ou **user flow**) désigne le parcours que suit un utilisateur pour accomplir une tâche spécifique à travers une interface numérique, comme une application ou un site web. Il représente l'ensemble des étapes, des actions et des interactions entre l'utilisateur et le système pour atteindre un objectif donné.

![flow-career-foundry](https://storage.googleapis.com/quest_editor_uploads/pmFeiHmVXiQMUP5iK2WlGYfjyRHbvSBC.png)_Exemple d’un flow. Source : CareerFoundry_

### Interactions

En prototypage et en UX/UI Design, une **interaction** désigne l’ensemble des actions ou comportements qui se produisent lorsque l’utilisateur _interagit_ avec un élément de l'interface d'une application ou d'un site web. Cela peut inclure des _clics_, des _taps_, des gestes ou d'autres formes d'intervention qui déclenchent une réaction ou un changement visible ou invisible dans l'interface.

![https://media.giphy.com/media/l2JHTEfCi5FZHpAic/giphy.gif?cid=790b7611a6ct61q680wshys5edd42wgkytlpt7kv2s6bxara&ep=v1_gifs_search&rid=giphy.gif&ct=g](https://media.giphy.com/media/3oFzmp2N5Moog2IbFC/giphy.gif?cid=790b7611a6ct61q680wshys5edd42wgkytlpt7kv2s6bxara&ep=v1_gifs_search&rid=giphy.gif&ct=g) _Source: Giphy_

---

## Prototyper une maquette

Pour commencer, rends-toi dans la section _Prototype_ de ton espace de travail sur Figma :

![accès prototype](https://storage.googleapis.com/quest_editor_uploads/DByqLR0GZXOh24O5wBQcE7T5wGinZSaJ.png)

Nous remarquons plusieurs choses :

L’icône de player, en haut à droite, pour le lancement du prototype.
(Il faudra lancer cette dernière pour constater le bon fonctionnement de ce dernier).

![player](https://storage.googleapis.com/quest_editor_uploads/6koRYCTCaUHnWanza72KcaffKsAqcJrD.png)

Le bouton de partage, pour partager le document auprès de collaborateurs ou de clients :

![share](https://storage.googleapis.com/quest_editor_uploads/wVqTXzA5AS3sP4M2rpZBhN0qOXpX7fyD.png)

Les paramètres de l’appareil (prototype settings) pour définir sur quel type de support le prototype s’articulera (mobile, tablette, ordinateur portable et bien plus encore) :

![prototype settings](https://storage.googleapis.com/quest_editor_uploads/olYyH5O7KAEJ9NYpDKth4xOEBtrnzL1Z.png)

Le ou les flows :

![flow](https://storage.googleapis.com/quest_editor_uploads/JepatqcLgOBExKfIeheVIiB7Hp3zEJv6.png)_Exemple de flow qui a pour but d'effectuer une redirection._

```alert info
L'espace dédié aux flows permet d'avoir un flow unique tout comme plusieurs flows.
Cela permettra d\'envisager plusieurs parcours utilisateurs, comme par exemple un flow dédié à la connexion/création de compte, tout comme celle d'un ajout à un panier, qui nécessiteront aussi bien des parcours que des actions différentes.
```

Il te sera par conséquent important de renommer tes flows de manière claire et compréhensible. Cela comporte plusieurs avantages :

- une meilleure compréhension et une meilleure pro-activité pour du travail en équipe
- une meilleure compréhension par le client des fonctionnalités proposées
- mieux s’y retrouver lors d’une présentation et pouvoir effectuer un changement rapide entre deux flows distincts sans avoir à rafraichir la page de prototype présentée

### Créer un _flow_

Pour rappel, ton _flow_ constituera un ensemble de connexions entre les _frames_.
La création de _flows_ distincts va permettre d’organiser les chemins utilisateurs les uns des autres (on pourra donc avoir un flow dédié au parcours d’achat, un à une création de compte, un autre pour l’accès à une page, …etc).

![](https://storage.googleapis.com/quest_editor_uploads/oZjfrQHePCXbwHkKdLFycX8U231d6drB.png)

_Source : [uiprep.com](https://www.uiprep.com/blog/ultimate-guide-to-prototyping-in-figma)_

Lorsque l’onglet « Prototype » est actif et qu’une _frame_ est sélectionnée, il est possible de créer un flow en cliquant sur le « + » de « Flow starting point » depuis l’onglet « Prototype ». Un encart bleu adjacent à la _frame_ apparait et définit le point de départ du _flow_.

```alert info
Un flow starting point peut-être littéralement traduit par un point d'entrée de flux.
Il s'agit de l\'endroit où tu souhaites faire démarrer le flow dans ta maquette.Si ton prototype évolue, il sera possible de bouger le point d'entrée pour l\'adapter
à ce dernier.
```

Dès que tu as défini à quel endroit tu souhaites faire démarrer ton flow, renommes-le en suivant pour facilement t’y retrouver ultérieurement. Il faudra choisir une frame globale pour définir ton flow starting point.

Dans l’exemple ci-dessous, nous avons une page d’ajout au panier. Nous allons donc renommer notre flow en conséquence pour que celui-ci soit clair.

![add-to-cart-frame](https://storage.googleapis.com/quest_editor_uploads/nTs9NuWLNiXUrh0C28RuVh2vHHHP8pXW.png)
![add-to-cart barre latérale](https://storage.googleapis.com/quest_editor_uploads/LPhCn4OAlV5s16qVpdR1NmUmkvG9IFjr.png)

```alert info
Il est généralement conseillé de nommer les flows en anglais pour faciliter le travail d’équipe, en particulier si les différentes parties prenantes du projet ne sont pas toutes francophones.
```

Dès lors que ton flow starting point est lancé, il te sera possible de créer des interactions.

### Créer des _interactions_

Comme indiqué en introduction, les _interactions_ permettent une visualisation globale de l’arborescence du site ou de l’application. Elles vont notamment définir la façon dont les éléments interagissent entre eux. De façon générale, on peut voir quelles pages mènent vers quelles pages et inversement.

![](https://storage.googleapis.com/quest_editor_uploads/33PKkw5Xmv6jUJ94XD9f2ezMLRKOH9lC.jpg)

_Source : [help.figma.com](https://www.notion.so/wild-code-school/help.figma.com)_

Il sera également possible de créer des interactions sur des éléments plus petits que les frames globales, comme des interactions sur des boutons, des éléments de menu…

Lorsque l’onglet « Prototype » est actif et qu’un élément ou une _frame_ est sélectionné, un cercle aux contours bleu apparait sur l’une des tranches. En le reliant (via un _drag & drop_) vers un élément de destination, un chemin unilatéral (symbolisé par une flèche) sera formé. Les deux éléments sont connectés et une _interaction_ est créée, elle permet de définir une action de laquelle dépendra une réaction.

```alert info
Il est également possible de créer une _interaction_ en sélectionnant un élément puis en cliquant sur le « + » de « Interactions » depuis l’onglet « Prototype », ou directement sur l'élément concerné.
```

![interactions](https://storage.googleapis.com/quest_editor_uploads/Vzl5lcWwZEtqlyak3cv1pa4HSBawEDmr.png)
![interaction sur un bouton](https://storage.googleapis.com/quest_editor_uploads/ayyVKdMwXIjMIzmsHhcLVb811jXv6aMf.png)_Exemple d'interaction sur un bouton_

Ta partie des interactions comporte deux éléments :

- le _trigger_, que l’on peut traduire par “déclenchement”. Il consiste à indiquer quel type de comportement de l’utilisateur est attendu.
- _l’action_, qui indiquera le type d’action qui s’effectuera après l’interaction provoquée par l’utilisateur.

![trigger](https://storage.googleapis.com/quest_editor_uploads/KWRmNdIAJdguYAgSX51WtxATetVzlTzq.png)

```alert info
alert info
Dans certains car, il sera possible que cette fenêtre évolue en fonction du type d'action attendu.
C'est par exemple le cas de l'action _"Navigate to"_ qui prendra un paramètre supplémentaire, la **destination** (une frame de début, et une frame suivante, voire une frame de fin).
```

![navigate to](https://storage.googleapis.com/quest_editor_uploads/7DMS85QFCfyyGLzhqulQVPVBsrrFU5Ss.png)

Dans les types de déclenchement qui peuvent être appliqués, tu retrouveras :

- **On click** : Lorsque l’élément est cliqué
- **On drag** : Lorsque l’élément est tiré
- **While hovering** : Pendant que l’élément est survolé
- **While pressing** : Pendant que l’élément est pressé
- **Key/Gamepad** : Lorsqu’une touche est pressée

- **Mouse enter** : Lorsque le pointeur entre dans la zone de l’élément
- **Mouse leave** : Lorsque le pointeur sort de la zone de l’élément
- **Mouse down** : Lorsque le pointeur descend
- **Mouse up** : Lorsque le pointeur monte

```alert info
À noter qu’il est possible d’attribuer une latence à l’action via le pictogramme symbolisant un chronomètre « Trigger after delay ».
```

Ces déclenchements peuvent entraîner les actions suivantes :

- **Navigate to** : Diriger vers l’élément de destination
- **Change to** : Permuter par l’élément de destination
- **Open overlay** : Ouvrir l’élément de destination en _pop-up_
- **Swap overlay** : Changer l’élément de destination en _pop-up_
- **Close overlay** : Fermer l’élément de destination en _pop-up_
- **Back** : Revenir à la page précédente
- **Scroll to** : Scroller jusqu’à l’élément de destination
- **Open link** : Ouvrir un lien URL

> Ainsi en affectant les valeurs « On click » puis « Navigate to » vers une page, le clic sur cet élément dirigera vers la page concernée.

_Des options supplémentaires peuvent apparaître selon les actions choisies, le positionnement d’une fenêtre pop-up par exemple._

![](https://storage.googleapis.com/quest_editor_uploads/95IipmlSJojvJU4qV8tKYtdfsAMsW17M.jpg)

_Source : [youtube.com](https://www.youtube.com/watch?v=B9mhOBAbsuo)_

---

## Visualiser le prototype

Si aucun élément n’est sélectionné, il est possible de paramétrer les options de visualisation depuis l’onglet latéral droit « Prototype ». Il est respectivement possible de :

- Définir un mockup (support physique dans lequel sera affiché la maquette) via « Device »
- Choisir la couleur de fond via « Background »

![](https://storage.googleapis.com/quest_editor_uploads/XFtKhXITpvDfXXUOVhh4b8OIqygwBGbK.jpg)

_Source : [behance.com](https://www.behance.net/gallery/56854245/Creative-Studio)_

Il est ensuite possible de visualiser le prototype en cliquant sur le bouton « Present » présent dans le menu supérieur et symbolisé par un triangle. La maquette s’ouvre dans un nouvel onglet.

```youtube
https://www.youtube.com/watch?v=X5qiBwqptek
```

---

## ☝️ Résumé

- La fonction Prototype offre une visualisation globale du projet à travers les différentes interactions possibles. Il va permettre de déterminer le chemin utilisateur (_User Flow_) à travers le site ou l’application.
- Le mode présentation met en scène la maquette en situation réelle et donne un aperçu fonctionnel en amont de la phase de développement.
- Il est important de penser l’expérience utilisateur au préalable pour offrir la meilleure navigation possible.

![](https://storage.googleapis.com/quest_editor_uploads/2hclNracfglIJXB4jmy17LbZBH84f4t8.png)

## 💪 Challenge

Un nouveau site de mode en ligne fait appel à vos services pour réaliser la mise en page de leur site e-commerce.

En reprenant les notions vues précédemment, réalisez l’ensemble des pages suivantes :

- La **homepage** contient 2 boutons :
  - Le premier "Découvrir" - situé sur le carrousel en haut de page - renvoie vers le second via un scroll
  - Le second « Voir les articles » renvoie vers la page d'articles
- La **page d'articles** contient une galerie d’articles (avec une miniature, un titre et un bouton « Voir l'article »)

Partagez votre solution via un lien Figma accessible à tous.

## 🧐 Critères d'acceptation

- Création d’interactions
- Navigation d’un élément à un autre
- Paramétrage des options d’interactions
  Solution

```youtube
https://youtu.be/Fw_1q3ilvec
```
