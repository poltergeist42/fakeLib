infos générales
===============

   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Projet:             fakeLib
   :dépôt GitHub:       https://github.com/poltergeist42/fakeLib
   :documentation:      https://poltergeist42.github.io/fakeLib/
   :Licence:            CC BY-NC-SA 4.0
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/ 

------------------------------------------------------------------------------------------

Déscription
===========

    Cette Librairie ne fait rien. Elle n'existe que pour pouvoir tester certain
    éléments des autres lib en cours de développement.

    La class est fictive, mais elle doit tout de même être commenter pour pourvoir générer
    la documentation de façon automatique avec Sphinx et ainsi pouvoir tester des éléments
    de traitement de la documentation.

    
Arborescence du projet
======================

Pour aider à la compréhension de mon organisation, voici un bref déscrptif de l'arborescence de se projet. Cette arborescence est à reproduire si vous récupérez ce dépôt depuis GitHub. ::

    FAKELIB                 # Dossier racine du projet (non versionner)
    |
    +--project              # (branch master) contient l'ensemble du projet en lui même
    |   |
    |   +--_1_userDoc       # Contien toute la documentation relative au projet
    |   |   |
    |   |   \--source       # Dossier réunissant les sources utilisées par Sphinx
    |   |
    |   \--_3_software      # Contien toute la partie programmation du projet
    |
    \--webDoc               # Dossier racine de la documentation qui doit être publiée
        |
        \--html             # (branch gh-pages) C'est dans se dosier que Sphinx vat 
                            # générer la documentation à publié sur internet