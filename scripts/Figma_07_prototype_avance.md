Les options de prototypage avec Figma permettent certaines fonctions avancées afin de rendre votre maquette encore plus interactive et dynamique.

Note : Cette quête fait suite à la quête [Introduction aux prototypes](https://login.wildcodeschool.com/admin/quests/2731) et en reprend l'exercice de validation, il est nécessaire de l'avoir completé au préalable.

![Image Alt](https://cdn.dribbble.com/users/501822/screenshots/4000231/media/1e3870348d84f78c8e0288560b684e69.gif)_Source : [dribbble.com](https://dribbble.com/shots/4000231-M-OSS-Industrial-Designer-Promo-Website-Work-Contacts-Pages)_

## 🤓 À la fin de cette quête, vous saurez

✅ Animer des éléments de façon fluide
✅ Régler les options de défilement
✅ Créer des fenêtres modales
✅ Optimiser le nombre d'interactions

---

## L'animation

### Les animations de prototype

Les animations vont permettre de définir les différentes transitions entre les éléments. Elles vont également régir le comportement d'actions telles que l'ouverture d'un menu, la navigation d'inter-pages ou l'apparition d'une galerie d'image par exemple.

Il est possible de choisir une animation depuis le panneau « Transitions » lors de la phase de prototypage.

Les animations disponibles sont les suivantes :

- **Instant** : Apparition immédiate
- **Dissolve** : Apparition progressive
- **Move In / Move Out** : Recouvrement latéral
- **Push** : Poussée latérale
- **Slide In / Slide Out** : Balayage latéral
- **Smart Animate** : Les éléments communs définissent la transition

Les paramètres vont permettre de définir la direction de l'animation, mais aussi la durée et l'accélération.

![Image Alt](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjViMjM0ZDgwMGYxNDYwNWQ3ZjNlNjkzMDZkOThlMjMzMWQ3NTdhNSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/bgMFxW9fdAGwQuRnC2/giphy.gif)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/360051748654/)_

Définie par l'attribut _ease_ l'accélération va permettre de contrôler la position dans le temps sous forme de fonction mathématique.

Détaillées dans le visuel ci-dessus, nous allons retrouver les propriétés _ease_ suivantes :

- **Linear**
- **Ease In**
- **Ease Out**
- **Ease In and Out**
- **Ease In Back**
- **Ease Out Back**
- **Ease In and Out Back**
- **Custom**

```alert info
À noter qu'il est possible de paramétrer manuellement les points d'inflexions de la courbe d'accélération depuis la propriété « Custom ».
```

### Utilisation de la propriété _Smart Animate_

![Image Alt](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d95307404286364bc8fe2d5/file-u0w1O0jCDW.gif)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/360039818874-Create-advanced-animations-with-smart-animate)_

La propriété _Smart Animate_ va créer une correspondance entre les éléments de départ et ceux d'arrivée.

Les possibilités sont nombreuses et _Smart Animate_ va notamment permettre de créer des animations avancées telles que :

- Des séquences de chargement
- Des effets de défilement en parallaxe
- Des interactions
- Des sliders ou des interupteurs
- D'actualiser du contenu

```alert info
L'échelle, la position, l'opacité, la rotation et le remplissage sont les différentes variables que cette propriété va permettre d'influencer.
```

Il est possible d'utiliser _Smart Animate_ de façon complémentaire à une transition classique, il suffit de cocher « Smart animate matching layers » depuis le panneau d'animation. Ainsi, les éléments avec une correspondance utiliseront _Smart Animate_ tandis que les autres seront régis par l'animation sélectionnée.

![Image Alt](https://d33v4339jhl8k0.cloudfront.net/docs/assets/5aa962fe2c7d3a2c4983093d/images/5d950b322c7d3a7e9ae1f7a2/file-aI3r9NOwPe.gif)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/360039818874-Create-advanced-animations-with-smart-animate)_

L'exemple ci-contre nous montre une transition de type _Push_ entre chaque page. L'activation de « Smart animate matching layers » va permettre d'assurer la continuité de la barre de navigation entre les _frames_.

Le nommage des éléments à son importance, la propriété _Smart Animate_ va associer les éléments de différentes _frames_ ayant le même nom. Pour les dissocier, il est donc important de les renommer distinctement.

---

## Le _scroll_

### _Scroll overflow_

De la même façon qu'il est possible de contrôler les différentes actions d'un prototype, le scrolling est entièrement paramétrable. Lorsque le contenu d'une _frame_ va dépasser de cette dernière, nous allons parler d'_overflow_.

![Image Alt](https://cdn.dribbble.com/users/256257/screenshots/1378010/animation.gif)_Source : [dribbble.com](https://dribbble.com/shots/1378010--GIF-Parallax-Building-animation)_

Les 4 modes d'overflow utilisables dans Figma sont les suivants :

- **No scrolling** : Le défilement est figé
- **Vertical** : Le défilement est vertical
- **Horizontal** : Le défilement est horizontal
- **Both directions** : Le défilement est vertical et horizontal

Pour définir une de ces options, il suffit de sélectionner une _frame_ dont au moins un élément sort du cadre et déninir le « Scroll behavior » depuis l'onglet « Prototype ».

```alert info
La _checkbox_ « Clip content » située dans la section « Frame » de l'onglet « Design » permets de masquer le contenu en excès. Il reste visionnable en mode _prototype_ si l'_overflow_ a été défini.
```

### _Scroll position_

La position du _scroll_ va définir le comportement d'un élément lorsque l'utilisateur défile sur la page. Il est possible d'en définir l'un des trois types possibles depuis la section « Scroll behaviour » du menu « Prototype » pour chaque élément d'une _frame_.

![Image Alt](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHRyajk1ejh5enFmMzlodnNyNnNlNzA1N3Nqd3R2eXFzeHpyaW51ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0o9p24ZXZjovlcg5hV/giphy.gif)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/360039818734-Prototype-scroll-and-overflow-behavior)_

#### • _Scroll with parent_

La propriété « Scroll with parent » va rendre l'élément dépendant du _scroll_ et ainsi le déplacer selon la position de la page.

#### • _Fixed_

L'élément sera figé sur la _frame_ grâce à la propriété « Fixed » et ne sera ainsi pas dépendant du _scroll_. Cet attribut est notamment utile dans le cadre de la création d'un _header_ ou d'un _footer_.

#### • _Sticky_

À l'instar de la propriété « Scroll with parent », la propriété « Sticky » va tout d'abord être dépendante du _scroll_ ; lorsque l'élément va atteindre le haut de la _frame_, il va ensuite prendre les attributs de la propriété « Fixed ».

Il n'est pas possible de fixer un objet « Sticky » ) d'autres bords de l'image, ainsi cette propriété n'est compatible qu'avec un _scroll_ vertical

---

## Les fenêtres modales

### Open Overlay

Également désignées boîtes de dialogue, les fenêtres modales sont générées via l'action _overlay_ dans Figma. Ils vont ainsi se superposer à la _frame_ sans qu'il n'y ait de changement de page.

![Image Alt](https://htmlburger.com/blog/wp-content/uploads/2022/11/Modal-UI-Design-Concepts-Company-Settings-Modal-by-Vishnu-Prasad.png)_Source : [htmlburger.com](https://htmlburger.com/blog/modal-ui-design/)_

Lors de la création d'interaction entre deux _frames_ il est possible de sélectionner « Open overlay » depuis les _actions_.

Il y a ensuite possibilité de personnaliser l'_overlay_ en choisissant par exemple sa position par rapport à la _frame_ de départ.

![Image Alt](https://help.figma.com/hc/article_attachments/360084141453/Overlay_section_of_Interaction_details_menu.png)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/360039818254-Create-overlays-in-your-prototypes)_

```alert info
Les _frames_ en _overlay_ sont identifiables grâce à un icône dédié représentant deux rectangles superposés. Le clic sur ce pictogramme va permettre de modifier les attributs de l'_overlay_ ou de le supprimer.
```

### Swap Overlay

La fonction « Swap overlay » permet de passer d'un _overlay_ à un autre. Cette fonction est utile lorsqu'une fenêtre modale en amène à une autre ou qu'elle contient plusieurs pages.

Lorsque une _frame_ de destination a déjà une transition « Open overlay » d'attribuée, l'option « Swap overlay » est sélectionnable lors la création d'une transtion vers une autre _frame_.

---

## Les sections

Les sections sont accessibles depuis le menu _frame_ et vont permettre de mieux structurer le projet. En Prototypage, elles vont permette de simplifier le nombre d'interactions entre les éléments.

![Image Alt](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HB9Cv67ehklaN5Kbmx0C2w.png)

![Image Alt](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*CrW0U3Q5GRRgYqsIUHW0xw.png)

Ainsi, dans le cadre d'un ensemble distinct, les différentes _frames_ vont être regroupées dans une section qui pourra être liée grâce à un nombre réduit d'interactions.

Cette fonction peut être utile dans le cadre de formulaires de connections ou de fenêtres contextuelles.

![Image Alt](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*h3o-s2ao4kvNE_6bETmpKQ.png)_Source : [uxdesign.cc](https://uxdesign.cc/advanced-figma-prototyping-tips-tricks-ccef9db99f24)_

---

## ☝️ Résumé

Il existe de nombreuses fonctionnalités permettant d'améliorer et de valoriser le prototypage d'une maquette avec Figma. Utilisées à l'unison, elle vont permettre de rendre le prototype plus vrai que nature et proche du résultat final.

> L'outil _Smart Animate_ est un réglage performant qui va permettre de simlifier les transitions en les rendant plus naturelles et _user friendly_. En parallèle, les courbes d'animation vont quant à elle rendre les mouvements plus fluides.

> Fonction essentielle à la navigation d'une page, le _scroll_ est entiérement paramétrable, qu'il s'agisse d'une frame entière ou des éléments qui la compose.

> Enfin les _overlay_ vont offrir une couche d'interaction supplémentaire en offrant la possibilité de superposer une _frame_ à une autre.

![Image Alt](https://cdn.dribbble.com/users/50529/screenshots/4011092/800x600.gif)_Source : [dribbble.com](https://dribbble.com/shots/4011092-Whisky-shop-redesign-concept)_
