---

# [![MindPass](https://raw.githubusercontent.com/MindPass/Code/master/Interface%5Fgraphique/PyQt/ressources/MindPass-logoHQ.png)](http://www.mindpass.fr/)

---


## :two_men_holding_hands: Présentation

**MindPass** est un projet informatique, né en septembre 2015 et soutenu par **[Tetra Informatique](http://www.tetra-informatique.com/)**.

À son origine, 5 élèves de l'[École des Mines de Douai](http://www.mines-douai.fr/) :

Martial G. | Alexandre D. | Pierre L. | Yassine B. | Thibaut C.
------------ | ------------- | ------------- | ------------- | -------------
@martialgarchery | @alexandredomain | - | @boulmaneyassine | @aquathi

Nombre de ces membres sont *inspecteurs des travaux finis*, mais on les aime bien quand même (un peu).

Ce projet est rédigé exclusivement en [Python 3.4](https://docs.python.org/3.4/) : 

```python
def __init__(self):
  print("Hello World, Hello MindPass !")
```

Le livrable de ce projet est un exécutable, dont le premier déploiement sur Windows (version bêta) est prévu le 1er avril 2016 (non non, ce n'est pas une blague !).


## :interrobang: But du projet

De plus en plus d'internautes sont présents chaque jour sur Internet. Les internautes s'inscrivent sur de nombreux sites web et doivent donc gérer une pléiade d'identifiants et de mots de passe. Face à cette difficulté du quotidien, de nombreux utilisateurs d'internet négligent la sécurité : ils utilisent seulement quelques mots de passes pour tous ces sites sur lesquels ils ont créé un compte (newsletter, forum, suivi d'une discussion, compte mail, compte bancaire). Voire pire : ils n'utilisent qu'un unique mot de passe pour chaque compte créé. Ce manque de prise de conscience au profit d'un gain de temps et de practicité nous a choqués, et nous avons souhaité créer un logiciel pour aider à lutter contre ce comportement dangereux. Concrètement, il s'agit de :

> 1. Faire prendre conscience des risques que prend un internaute en utilisant de façon répétée des mots de passes identiques, l'avertir et l'inviter à changer son comportement.

> 2. Ne pas ennuyer l'internaute : il doit pouvoir gérer ses identifiants et ses mots de passe sans y passer des heures. C'est pour cette raison que l'un point-clé de MindPass est de rechercher lui-même dans une boîte mail, de façon automatique, les sites d'inscriptions, les identifiants et les mots de passe (s'ils sont présents).


## :wrench: Avancement du projet

- [x] Accéder à différentes boîtes webmail (Gmail, Outlook/Live, Yahoo, Laposte, Orange) grâce au protocole IMAP

- [x] Parcourir les mails reçus par l'utilisateur de façon honnête et sécurisée

- [ ] Reconnaître les mails d'inscriptions reçus par l'ensemble des mails

- [x] Avoir une interface claire, épurée et intuitive [en cours]

- [ ] Afficher des messages de prévention

- [ ] Créer un exécutable d'abord sur Windows, puis implémenter le logiciel en multi-plateformes.

- [ ] ...


## :floppy_disk: Dernière version

La sortie de la version bêta (v0.1-beta0) est planifiée le 1er avril 2016.

Stay tuned ! :computer:


---

Plus d'informations sur www.mindpass.fr