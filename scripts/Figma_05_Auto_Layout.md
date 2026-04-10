# Les contraintes et l'auto-layout

Les contraintes et l’auto-layout, deux outils de mise en page automatique, font partie des clés du succès de Figma. En les maîtrisant, tu pourras créer des maquettes responsive et obtenir des gains de temps significatifs.

#### 🤓 À la fin de cette quête, tu sauras :

✅ Ce que sont les contraintes et l'auto-layout
✅ En quoi ils permettent de gagner en productivité
✅ Comment les utiliser

![](https://storage.googleapis.com/quest_editor_uploads/Sz6KfHl5kHU279CVJ77EAfeDsldW5Bjs.gif)
_Source Image : UXPlanet_

---

## Les contraintes

Les contraintes sont utilisées pour rendre la conception **plus flexible et adaptable à différentes tailles d'écran**. Celles-ci ont deux dimensions — verticale et horizontale. Elles permettent d'indiquer à quel distance des bords (haut, bas, gauche, droite) doit être placé un élément vis à vis de la frame qui le contient.

Imaginons que nous souhaitons avoir un bouton qui se trouve toujours en haut à gauche de l'écran, même lorsque ce dernier est rétréci ou agrandi. Pour ce faire, nous utiliserions les contraintes : sur l'axe horizontal, nous définirions la contrainte sur le bord droit, et sur l'axe vertical, la contrainte sur le bord haut. Sur l'exemple ci-dessous, il s'agirait donc de la second option, "Right, Top".

![](https://miro.medium.com/v2/resize:fit:640/0*Vy6BbtmHonEV60Ik.gif)

### Ajouter des contraintes

```tabs ui
!--- UI 3 (2024)
Sur la version 3 de l'interface utilisateur de Figma, les contraintes sont accessibles depuis le panneau "Design" en cliquant sur l'icône "Constraints".
![Contraintes](https://storage.googleapis.com/quest_editor_uploads/1CGmmZ6uxS71YCuGBz39UkeawxhX4GnN.jpg)
!--- UI 2 (ancienne version)
Sur la version 2 de l'interface utilisateur de Figma, les contraintes sont visible depuis le panneau "Design" dans la section dédiée.
![Contraintes](https://storage.googleapis.com/quest_editor_uploads/D6mCTJbWCIOFtUPKDJ8TQRsUoiBq1jKN.jpg)

```

#### Horizontales

Les contraintes horizontales définissent le comportement d'un élément lorsque l’on redimensionne en largeur la frame qui le contient.

```tabs ui
!--- UI 3 (2024)
![contraintes horizontales](https://storage.googleapis.com/quest_editor_uploads/GjaxfjbnTuYElDYEs2t5PvSL3aFANbUP.jpg)
!--- UI 2 (ancienne version)
![Contraintes horizontales](https://storage.googleapis.com/quest_editor_uploads/T1PJcos4mdPBIvqrGF7CCGLIZmQyAc8U.jpg)
```

- **Gauche** : l’élément gardera toujours la même distance avec le bord gauche de la frame. Il s'agit de la valeur appliquée par défaut.
- **Droite** : l’élément gardera toujours la même distance avec le bord droit de la frame
- **Gauche et Droite** : l’élément gardera toujours la même distance avec le bord gauche ET droit de la frame. Pour maintenir les espacements, cela implique que l’élément sera redimensionné en même temps que la frame.
- **Centre** : l’élément restera centré horizontalement dans la frame.
- **Échelle** : l’élément sera redimensionné “classiquement” à l’horizontale en même temps que la frame. Les distances aux bords droits et gauche garderont le même ratio.

#### Verticales

```tabs ui
!--- UI 3 (2024)
![Contraintes verticales](https://storage.googleapis.com/quest_editor_uploads/LnHd4Y0B8p13kqb8e6ZYJpixloWCEh91.jpg)
!--- UI 2 (ancienne version)
![Contraintes verticales](https://storage.googleapis.com/quest_editor_uploads/MI0HPb8VIo5465O79Qv1ffDwiz0QwK91.jpg)
```

- **Haut** : l’élément gardera toujours la même distance avec le bord haut de la frame. Il s'agit de la valeur appliquée par défaut.
- **Bas** : l’élément gardera toujours la même distance avec le bord bas de la frame
- **Haut et Bas** : l’élément gardera toujours la même distance avec le bord haut ET bas de la frame. Pour - maintenir les espacements, cela implique que l’élément sera redimensionné en même temps que la frame.
- **Centre** : l’élément restera centré verticalement dans la frame.
- **Échelle** : l’élément sera redimensionné “classiquement” à la verticale en même temps que la frame. Les distances aux bords haut et bas garderont le même ratio.

### Exemples de contraintes

Lorsque l’on crée un champ de texte multiligne (“textarea”) redimensionnable, on peut définir une contrainte pour toujours positionner l’icône en bas à droite, et les infos complémentaires en bas à gauche. Pour ce faire, nous mettons une contrainte **Droite, Bas** à l’icône et **Gauche, Bas** aux infos. Voyons le résultat :

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*Vlqwgq5xiJFwmd3p.png)

![](https://miro.medium.com/v2/resize:fit:720/0*wfVDDqp8IiPt7pBU.gif)

Voici un exemple de contraintes sur un design d’écran complet :

![](https://miro.medium.com/v2/resize:fit:720/format:webp/0*Ppch_PMtQba8LW21.png)

![](https://miro.medium.com/v2/resize:fit:720/0*r6WXim4ADTz0elK8.gif)

---

## L’auto-layout

L’auto-layout permet de créer des **mise en page réactives, qui s'agrandissent pour remplir, rétrécissent pour s'adapter et redistribuent le contenu**. Il peut par exemple être appliqué sur un bouton pour qu'il s'agrandisse ou rétrécisse à mesure que l'on change son texte, mais aussi être appliqué à plus grande échelle sur une frame qui engloberait plusieurs éléments afin de les aligner et de les distribuer au sein de celle-ci.

![](https://miro.medium.com/v2/resize:fit:720/0*T_F3srrxeHZpBhA-.gif)
![Exemples d'usages de l'auto-layout](https://storage.googleapis.com/quest_editor_uploads/HgYBciHEhzOFHJPsJ99jSBuftVIdsVfi.png)

Sur l'exemple ci-dessus, nous pouvons observer les différents cas d'usage de l'auto-layout. Sur un bouton, il permettra de gérer l'alignement du texte et les espacements internes, aussi appelés "paddings". Sur un ensemble de deux boutons, il permettra de les distribuer sur un axe horizontal tout en gérant l'espacement entre eux. Au sein d'une carte, il permettra également de distribuer l'ensemble des éléments qu'elle contient, mais cette fois-ci à la verticale. Idem pour l'ensemble des cartes qui se positionnent automatiquement les unes sous les autres à distance égale.

Ces exemples montrent un aspect essentiel de cette fonctionnalité : **il est possible d'imbriquer des auto-layout** pour créer un système complètement adaptatif.

```alert info
L’auto-layout est une excellente manière de se familiariser avec le concept des “flexbox” et plusieurs autres propriétés CSS que nous verrons plus tard !
```

Un peu de mal avec tous ces auto-layout ? 🤯 Pas d'inquiétudes, nous allons commencer avec un cas plus simple. Regardons maintenant comment l'appliquer, quels sont ses paramètres et comment l'utiliser sur un élément tel qu'un bouton 👇

### Appliquer l'auto-layout

L'auto-layout peut être ajouté à **une frame ou à une sélection d'objets**. Il peut s'agir de frames vides, avec des éléments à l'intérieur, mais aussi d'une sélection de calques ou de composants.

On peut rapidement définir un auto-layout avec le raccourci clavier :key[SHIFT]+ :key[A] (après avoir sélectionné tous les éléments à inclure) ou en faisant un clic droit > "Add Auto-layout". Il est également possible de l'appliquer directement depuis le panneau "Design", d'où nous gérerons également ses paramètres.

```tabs ui
!--- UI 3 (2024)
![Auto-layout](https://storage.googleapis.com/quest_editor_uploads/3mblpXmKBqHjVcyQM7NYAFZfHY4NmPM6.jpg)
!--- UI 2 (ancienne version)
![Auto-layout](https://storage.googleapis.com/quest_editor_uploads/GahyZmvIBebKz6pnegE8OUCsfPkjkmdw.jpg)
```

Il y a un ensemble de propriétés à connaître liées aux auto-layouts :

1. **Direction** — Permet de définir la direction dans laquelle les éléments vont être disposés de manière automatique : horizontalement ou verticalement.
2. **Espacement entre les éléments** — Contrôle l'espacement entre les objets dans le conteneur
3. **Paddings** - Détermine l'espacement interne (padding) horizontal et vertical entre les objets et le conteneur.
4. **Alignement & Position** — gère le positionnement des éléments dans le conteneur (centré, à gauche/droite, en haut/bas…), et leur alignement dans l’axe de la direction.
5. **Mode d'espacement** — Définit l'espace entre les éléments sur Packed (les éléments se “suivent”) ou sur Space between (les éléments se répartissent dans l’espace du conteneur)
6. **Strokes** - Définit si l’épaisseur des contours du conteneur sont pris en compte dans le padding ou non
7. **Canvas** stacking — Définit dans quel ordre apparaissent les éléments (le premier ou le dernier au-dessus)

### Redimensionnement automatique

Il est possible de définir le comportement de redimensionnement des frames pour qu’elles puissent s'adapter à toute modification apportée à leurs objets enfants (ceux qu'elle contient).
Les paramètres de redimensionnement peuvent aussi être appliqués individuellement aux objets sur les axes X et Y. Par exemple, nous pourrions vouloir qu'un bouton ait une hauteur fixe mais que sa largeur s'adapte selon le texte qu'il comprend.

```tabs ui
!--- UI 3 (2024)
Sur la version 3 de l'interface utilisateur de Figma, les options de redimensionnement de la largeur (width) et de la hauteur (height) sont visible directement depuis la section Auto-Layout du panneau Design.

![redimensionnement](https://storage.googleapis.com/quest_editor_uploads/O3f3jX3ng3h1fiH20gBpgNhYghhVZyTM.jpg)
!--- UI 2 (ancienne version)
Sur la version 2 de l'interface utilisateur de Figma, les options de redimensionnement de la largeur (width) et de la hauteur (height) ne sont pas associés à la section Auto-Layout du panneau Design mais celle plus haut.
![redimensionnement](https://storage.googleapis.com/quest_editor_uploads/YedaQ9NYahjUbwTV0giN3qjaASmIWkd8.jpg)


```

#### Largeur ou hauteur fixe

Lorsqu'un auto-layout est défini sur largeur ou hauteur fixe, les valeurs des dimensions de la frame restent les mêmes quel que soit le contenu qu'elle contient. La taille ne s’adapte pas aux modifications des objets qu'il contient.

#### Hug content

Un auto-layout défini sur hug content pour s’adaptera à la taille de ses objets enfants. La frame gardera les dimensions les plus petites possibles pour “entourer” les objets qu'elle contient.

#### Fill container

Les objets dans un auto-layout définis sur fill container remplissent la largeur et/ou hauteur de leur frame.
_Cette option n'est visible que si l'élément sélectionné est bien contenu dans une frame._

### Créer un bouton adaptatif avec l'auto-layout

Nous allons maintenant réaliser un bouton en utilisant l'auto-layout afin de permettre au texte de rester centré et de ne pas dépasser de son conteneur.
Pour ce faire, nous allons :

1. Créer un calque de texte
2. Appliquer de l'auto-layout à ce texte grâce au raccourci clavier :key[SHIFT]+ :key[A]
3. Appliquer un fond ainsi qu'un arrondi à la frame en auto-layout fraîchement créée pour qu'elle ait l'apparence d'un bouton
4. Définir des paddings horizontaux et verticaux pour que le texte ne soit pas collé aux bords de la frame
5. Aligner le contenu au centre pour que le texte reste centré peut importe la largeur du bouton
6. Définir le redimensionnement sur Hug Content pour que la taille de la frame s'adapte au contenu textuel

```youtube
https://youtu.be/zFNjji1sRuk?si=hoXYLBnRX2REZ-H4
```

---

# ☝️Résumé

- Les contraintes et l’auto-layout sont des outils puissants de Figma qui permettent **d'automatiser différents comportements de dimensionnement**.
- **Les contraintes** permettent de contrôler la façon dont les objets réagissent aux redimensionnements de la frame, notamment au niveau de leur position dans la frame,
- **L’auto-layout** permet de contrôler la façon dont les frames/composants réagissent aux changements d'objets, et inversement.

---

# 💪 Challenge

- Crée un bouton grâce à l'auto-layout afin que celui-ci soit flexible
- Place ce bouton au sein d'une frame représentant un écran d'ordinateur et ajoute lui une contrainte pour qu'il reste sur le bord droit en haut de l'écran, même si on le redimensionne

# 🧐 Critères d'acceptation

- Le contenu du bouton est centré et peut être modifié sans sortir de la frame
- Le bouton reste à distance égale du bord haut droit de l'écran
