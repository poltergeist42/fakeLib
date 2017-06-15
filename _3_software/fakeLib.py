#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Nom du fichier:     fakeLib.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170520

####

   :Licence:            CC-BY-NC-SA
   :Liens:              https://creativecommons.org/licenses/by-nc-sa/4.0/

####

    :dev language:      Python 3.4
    
####

lexique
=======

   :**v_**:                 variable
   :**l_**:                 list
   :**t_**:                 tuple
   :**d_**:                 dictionnaire
   :**f_**:                 fonction
   :**C_**:                 Class
   :**i_**:                 Instance
   :**m_**:                 Matrice
   
####

Liste des libs
==============

    - os
    - sys
    - devChk
    - argparse
    
####
   
objectif
========

    Cette Librairie ne fait rien. Elle n'existe que pour pouvoir tester certains
    éléments des autres lib en cours de développement.

    La class est fictive, mais elle doit tout de même être commenter pour pourvoir générer
    la documentation de façon automatique avec Sphinx et ainsi pouvoir tester des éléments
    de traitement de la documentation.
    
"""

import os, sys
sys.path.insert(0,'..')        # ajouter le répertoire précédent au path (non définitif)
                                # pour pouvoir importer les modules et paquets parent

import argparse

####

class C_FakeLib( object ) :
    """ Class fictive permettant de faire des tests pour les autres lib
        en cours de développement.
    """
    
    def __init__( self ) :
        """ **__init__()**
        
            Création et initialisation des variables globales de cette Class
        """
        
        ## Création de l'instance pour les message de debug
        # self.i_dbg = C_DebugMsg(v_debug)
        
####
        
    def __del__(self) :
        """ **__del__()**
        
            Permet de terminer proprement l'instance de la Class courante
        
            il faut utilise : ::
            
                del [nom_de_l'_instance]
                
            *N.B :* Si l'instance n'est plus utilisée, cette méthode est appelée 
            automatiquement.
        """
        ## dbg
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "__del__", self.__del__)
        
        ## Action
        v_className = self.__class__.__name__

        ## dbg
        f_dbg( v_dbg, v_className, v_tittle = False  )
        
####
        
    def f_doNothing( self ) :
        """ Cette fonction ne fait rien d'autre que de retourner 'True' """
        
        v_dbg = 1
        v_dbg2 = 1
        f_dbg(v_dbg2, "f_doNothing", self.f_doNothing)
        
        print( "\neuh ... non, non, rien !\n" )
        return True
        
####

def main() :
    """ Fonction principale """
    
    parser = argparse.ArgumentParser()
    parser.add_argument( "-d", "--debug", action='store_true', help="activation du mode debug")
                        
    args = parser.parse_args()
    
    if args.debug :
        if v_dbgChk :
            i_dbg.f_setAffichage( True )
            print( "Mode Debug activer" )
        else :
            print( "Le mode Debug ne peut pas être active car le module n'est pas pressent")

    i_ist = C_FakeLib()
    
    i_ist.f_doNothing()
    
if __name__ == '__main__':
    main()

        