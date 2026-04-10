```title book
Introduction
```

Les variables permettent de gérer et d'appliquer des valeurs réutilisables à divers éléments d'une conception. Elles participent à maintenir de la cohérence, à optimiser le flux de travail, et facilitent les modifications à grande échelle.

![variables](https://storage.googleapis.com/quest_editor_uploads/IvRoGTppIRMaHcmRIDJsey0ETGvIYuup.jpg)
_Source : [specifyapp.com](https://specifyapp.com/blog/introduction-to-design-tokens)_

## 🤓 À la fin de cette quête, vous saurez

✅ Comment créer & utiliser des _variables_
✅ Appliquer des thèmes
✅ C’est qu’est un _design token_

---

## À quoi servent les variables dans Figma ?

### Pourquoi utiliser des variables ?

Les variables permettent de créer, de stocker et d'utiliser des valeurs réutilisables dans tous nos projets Figma. Elles offrent donc de nombreux avantages 👇

- **Cohérence** : Les variables aident à maintenir une apparence cohérente à travers un Design System. En définissant des variables pour les couleurs, la typographie, les espacements et d'autres éléments de conception, le projet sera harmonieux et uniformisé.

- **Adaptabilité** : Les variables offrent de la felxibilité, permettant d'expérimenter avec différentes valeurs, comme des jeux de couleurs ou des tailles de police, en ajustant simplement les variables. Cette adaptabilité est également précieuse lors de la création de designs pour différentes plateformes ou appareils.

- **Efficacité** : Lorsqu'une variable est mise à jour, toutes les instances de cette variable dans le design se mettent à jour automatiquement. Cela permet de gagner du temps et des efforts, en éliminant le besoin de mettre à jour manuellement chaque instance d'un élément spécifique.

- **Évolutivité** : Les variables sont particulièrement utiles dans les grands projets ou les Design systems en raison de leur évolutivité et de leur facilité de maintenance.

- **Facilité de mise à jour** : Comme les projets grandissent et que les Design sytsems évoluent avec le temps, les variables peuvent être ajustées globalement pour répondre aux nouvelles exigences. Elles assurent que tous les éléments sont modifiés de manière cohérente.

- **Développement** : Les designers peuvent fournir aux développeurs des valeurs précises pour les éléments, réduisant les risques de mauvaise interprétation et simplifiant leur intégration.

### Les types de variables

![types de variables](https://storage.googleapis.com/quest_editor_uploads/uN6I3aEdJteOv1iqq5FvkdWDstqj0i34.png)
_Source image_

- **Color :** Les variables de couleur utilisent des valeurs de couleur unie, telles que #000000 ou #FFCD29.
  Elles peuvent être utilisée pour organiser la palette de couleur ou créer des modes clairs et sombres ("_dark mode_").

```tabs
!--- UI 2
![variables de couleur ](https://storage.googleapis.com/quest_editor_uploads/bUCWGUBWGsrXhjL6Ih3ql7WudCs3RWRn.png)
!--- UI 3
![variable de couleur](https://storage.googleapis.com/quest_editor_uploads/gFwkKhM4KEMU58brI3bDk4PK3x7JNDCl.png)
```

_Sur cet exemple, les couleurs qui constituent la palette utilisée sont renseignée en tant que variables._

- **Number :** Les variables de type Number vont être utilisées pour définir des valeurs numériques.
  Elles sont par exemple utilisées pour des espacements (margin, padding), des tailles ou des arrondis.

```tabs
!--- UI2
![variable numérique](https://storage.googleapis.com/quest_editor_uploads/xiXVxGLBGue8EUE4f1LSf9xA8ZS4UVA4.jpg)
!--- UI3
![variables de font](https://storage.googleapis.com/quest_editor_uploads/SnssI9MmpAFqI6vOiswWYy4YyhvYxTOu.png)
```

_Sur cet exemple, des variables de type nombre sont utilisées pour des attributs typographiques (taille du texte, espacements)_

- **String :** Ces variables de texte permettent de créer des chaînes de caractères spécifiques qui peuvent être intégrées dans n’importe quel texte, y compris les textes imbriqués dans les instances de composants.
  Elles sont par exemple utilisées pour créer une variante de mise en page dans une autre langue.
  ![variable de texte](https://storage.googleapis.com/quest_editor_uploads/mQvmc0D69zozUFXIGyjDxHJIpgpiARds.png)
  _Sur cet exemple, nous utilisons une variable de type String pour indiquer le texte contenu dans les boutons. Associé aux **modes**, que nous verrons un peu plus tard dans cette quête, il est possible d'avoir des variantes de ce texte dans différentes langues._

- **Boolean :** Les variables booléennes dans Figma prennent comme valeur "vrai" ou "faux" et permettent la création d'une logique conditionnelle, dans laquelle les éléments peuvent être affichés ou masqués en fonction de la saisie de l'utilisateur ou d'autres conditions.
  ![Prototypage avec variable booléenne ](https://storage.googleapis.com/quest_editor_uploads/dcE8pMQO3A6uDw4YRUyGyNpYRbUUGC1Y.gif)
  _Les variables peuvent aussi être utilisées lors du prototypage ! Sur cet exemple, une variable nommée CircleVisibility prend la valeur "faux" par défaut, mais lorsque l'on clique sur le composant interactif (nommé button), celui-ci est modifié et la valeur de la variable change également pour passer à "vrai"._

---

## Utilisation des variables

Pour commencer à te familiariser avec les variables dans Figma, regarde cette vidéo qui propose une vue d'ensemble de cette fonctionnalité 👇

```youtube
https://youtu.be/LhhMpKXhRmQ?si=B-4uRT8wTxmeyZYB
```

### Création de _variables_

La création de _variables_ est accessible depuis le panneau latéral droit `Local variables`. En cliquant sur `+ Create variable`, nous pouvons choisir le type de variable, puis renseigner la valeur souhaitée et nommer la variable d’après ses **propriétés intrinsèques**. Par exemple, nous créons une variable de type "color" et lui assignons la valeur hexadécimale « #ff0050 », elle pourrait être nommée « red » en référence à la teinte de cette couleur.

Il est ensuite possible de regrouper nos valeurs par sous-catégories avec une sélection multiple puis clic droit `New Group with selection`. Ces sous-catégories permettront de segmenter les valeurs de notre collection ; par exemple, dans une collection nommée « colors » nous retrouverons « brand » et « neutral » avec respectivement les couleurs de la marque et les tons neutres.

![Image Alt](https://help.figma.com/hc/article_attachments/15455006796823)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes)_

---

### Implémentation de _variables_

À l'instar des styles, pour appliquer une _variable_ de couleur à un élément, il suffit de la sélectionner via le pictogramme `Style` formé de 4 points. Les styles y seront représentés par des formes circulaires et les _variables_ par des formes carrées.

```tabs
!--- UI 2
![application d'une variable de couleur à un bouton](https://storage.googleapis.com/quest_editor_uploads/Iw7jL0A82Ga71mbDdRWVl8G5XoxmoG1l.jpg)
!--- UI 3
![ui3 ajout d'une couleur](https://storage.googleapis.com/quest_editor_uploads/uVyUFvjRaAjnmCe6yXpMk4JpdhdN7dJe.png)
```

Les _variables_ de valeurs seront quant à elles attribuables depuis le pictogramme hexagonal `Apply variable` en forme d'écrou et adjacent à un champ de saisie de valeur numérique.

````tabs
!--- UI 2
![Application d'une variable pour le padding horizontal ](https://storage.googleapis.com/quest_editor_uploads/vm1PDKhErSu9dSiQ3qPb2rzVIHkjw6eb.jpg)
!--- UI 3
![application de spacing](https://storage.googleapis.com/quest_editor_uploads/5HMDS7xBamoJvgetg5tlP3MoJjv454Xt.png)

```alert info
En marge des indicateurs visuels, il est important de faire preuve de vigilance quant à l'attribution des _variables_. Par exemple un texte prendrait la _variable_ « text-brand-primary » et non « surface-brand-primary », cela indépendamment de la valeur indexée.
````

---

## Les modes

Les modes vont permettre de créer des **thèmes** spécifiques englobant des _variables_ différentes. On pense notamment à un thème sombre dont les _tokens_ auraient leurs valeurs de couleur inversées (les fonds clairs deviennent foncés et inversement pour les textes).

```tabs
!--- UI 2
![Modes dans le panneau de _variables_ du logiciel Figma](https://storage.googleapis.com/quest_editor_uploads/zhRxlOQGTLpqnJhaBbpBb1jy51uxUlMk.jpg)_Source : [youtube.com](https://www.youtube.com/watch?v=1ONxxlJnvdM)_
!--- UI 3
![nouveau mode](https://storage.googleapis.com/quest_editor_uploads/Y575ta5iZz1rjBrOIE72G3pTFKtrZEL2.png)
```

Pour créer un mode, il suffit de cliquer sur le `+` (_New variables mode_) de la rangée `Name` d'une collection de _tokens_. Une seconde colonne adjacente nommée « Mode 2 » apparait.

Il est ensuite possible d'éditer le nom des _modes_ et d'affecter différentes valeurs à nos _tokens_ afin d'en faire un mode visuellement distinct.

La bascule entre les différents _modes_ se fait ensuite via le pictogramme hexagonal `Change variable mode` en double écrous du panneau `Layer` en ayant une _frame_ ou un élément comportant des _variables_ sélectionnés.

![Bascule entre deux modes dans le logiciel Figma](https://help.figma.com/hc/article_attachments/15462338954135)_Source : [figma.com](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes)_

---

## _Variables VS Styles_

Au contraire des _styles_, les _variables_ vont permettre une **imbrication multi-niveaux** et ainsi introduire l’utilisation de _design tokens_.

![Image Alt](https://miro.medium.com/v2/1*B2z6uNePbOQ3o3zSFhOxZg.png)_Source : [uxdesign.cc](https://uxdesign.cc/design-tokens-cheatsheet-927fc1404099)_

En outre — et contrairement aux _variables_ — les _styles_ vont permettre de contenir plusieurs valeurs (qu'elles soient définies ou non au sein de variables). Ainsi, ils resteront utiles pour l’utilisation de dégradés, de styles typographiques ou d’effets tels que des ombres portées par exemple.

---

## Les Design Tokens

### Définition

Un _design token_ est une valeur prédéfinie qui représente un **attribut visuel spécifique**, tel qu’une couleur, une taille de police ou une dimension. Il s’agit d’un élément clé utilisé dans la conception d’interfaces utilisateur.

A contrario d’affecter une valeur à notre élément, nous allons utiliser un _design token_ qui va référer à cette valeur. Cela offre une meilleure cohérence et facilite la maintenance et les modifications du design. En effet, la modification de la valeur de ce _token_ affectera ainsi tous les éléments auquel il a été attribué.

### Structure

Usuellement, nous allons trouver la hiérarchisation de _tokens_ suivante :

- **Token global** : valeur primitive du _Design System_, référencée par un nom décorrélé de son contexte d’utilisation (ex : « yellow » ou « brand-color »). Ces valeurs peuvent être ensuite utilisées par les autres types de jetons.

- **Token alias :** référence à l’usage spécifique du token global (ex : « cta-background-color »)

- **Token relatif :** référence à une variante d’utilisation, en fonction du contexte et de l’imbrication de l’élément concerné (ex : « card-cta-background-color »)

![Visuel d'une représentation hiérarchique des différents types de design token](https://storage.googleapis.com/quest_editor_uploads/UNk9VXGySbRXK9HjDoD42P3ii0e9P2cn.gif)

```alert info
Un _design token_ peut être une référence d’alias qui fait référence au _token global_, à partir d’un _token global_ (ex : « brand-color »).
```

D’autres _tokens_ peuvent être créés pour répondre à une récurrence d’utilisation (ex : « card-cta-primary-background »), ce qui permet une meilleure maintenance du _Design System_.

### Implémentation dans Figma

Afin de sur-imbriquer nos _variables_ pour leur donner une valeur d'usage et en faire des _tokens alias_, nous créerons une nouvelle collection dédiée à une utilisation concrète. L'option `Create collection` est accessible depuis la section déroulante supérieure gauche du panneau `Local variables`.

Une fois cette collection créée, nous pourrons **attribuer des alias** en indexant de nouvelles valeurs d'usage à nos valeurs primaires. Nous irons les affecter depuis l'onglet `Librairies` lorsque l'on souhaite sélectionner une valeur.

![alias](https://storage.googleapis.com/quest_editor_uploads/3mlG6CrEWzryu0cx5CLrplXIgCoRyJyo.gif)

```resource
https://bootcamp.uxdesign.cc/flexing-figma-variables-advanced-tips-335e31ee2301
# Article : Conseils avancés sur l'utilisation de variables dans Figma [anglais-optionnel]
Envie d'aller plus loin ? Consulte cette ressource pour obtenir différents conseils et astuces sur l'utilisation des variables dans Figma
```

### Maintenance

Par leur nature, les _tokens_ offrent une grande flexibilité en matière de modification grâce à la distinction entre **option** (_token global_) et **décision** (_tokens alias & relatif_).

Avec une **option de design « color-blue »** nous pouvons créer une **décision de design « header-background : color-blue** ». Dans ce cas, le token header-background pointe vers le token « color-blue ». Cependant, cette décision peut être amenée à changer. Il suffira alors de faire pointer le token « header-background » vers un nouveau token de couleur.

### Sémantique

La nomenclature des _tokens_ devra respecter les conventions de nommage des _variables_ CSS. On proscrit ainsi l’utilisation de majuscules, de caractères spéciaux tels que des accents ou des espaces que l’on remplacera par des tirets.

![Image Alt](https://miro.medium.com/v2/1*LA1KHk_o7Km0LU926l_0kw.png)_Source : [uxdesign.cc](https://uxdesign.cc/design-tokens-cheatsheet-927fc1404099)_

Dans sa forme la plus exhaustive, la sémantique sera structurée selon les valeurs d’usage en décomposant successivement la catégorie, la propriété, la surface, la variante et l’état.

---

## ☝️ Résumé

- Une **variable est un conteneur qui stocke des valeurs** et permet de les réutiliser.

- Un _design token_ est une **valeur prédéfinie** qui représente un **attribut visuel spécifique**, utilisé pour maintenir la cohérence et faciliter la gestion du design dans les interfaces utilisateur. En ces faits, les _variables_ de Figma favorisent leur utilisation à travers une imbrication multiniveaux des valeurs.
  Au-delà d'offrir une maintenance aisée du _Design System_, les _design tokens_ vont également rendre plus fluide le travail d'intégration en structurant la déclaration des _variables_ CSS.

## 💪 Challenge

Pratique les variables en dupliquant (via le bouton "Open in Figma") ce [Playground Figma](https://www.figma.com/community/file/1234936397107899445/variables-playground), qui te guide pas à pas dans la prise en main de cette fonctionnalité. Essaie d'aller au moins jusqu'à la partie "Apply Variables".

_Ce challenge est en auto-validation, tu n'auras pas besoin de soumettre une solution_
