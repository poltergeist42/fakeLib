#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Nom du fichier:     fakeLib.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20170829

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

import os, sys, time
l_path = [ 
            "../../../../../devChk/project/_3_software"
         ]
for p in l_path :
    if os.path.isdir( p ) :
        sys.path.insert(0, p)
    else :
        print( "\n\t ***attention ***, le chemin : \n{}\n n'est pas valide !".format(p))
   
try :
    from devChk import C_Benchmark as execTime
    
except ModuleNotFoundError:
    print( "devChk n'a pas été trouvé" )
    v_dbgChk = False
    
try :
    from devChk import C_DebugMsg
    v_dbgChk = True
    i_dbg = C_DebugMsg()
   
except ImportError :
    print( "module devChk non present" )
    v_dbgChk = False

import argparse

####

__all__ = ['C_FakeLib']

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
        
    def f_daleks( self ) :
        return "EX-TER-MI-NA-TE"
        
    def f_jeSappelGroot( self) :
        return "Je s'appel Groot !"
        
    def f_knocPeny( self, v_value ) :
        for i in range( v_value ) :
            print( "Toc ! toc ! toc ! Peny" )
        return "doue chaton"
        
    def f_42( self, v_value ) :
        if v_value == 42 :
            return 42, "la réponse à la vie, l'univers et tout le reste"
        
####

def f_dbg( v_bool, v_data, v_tittle = False  ) :
    """ Fonction de traitemant du debug """
    if v_dbgChk and v_tittle :
        i_dbg.dbgPrint( v_bool, v_tittle, v_data )
        
    elif v_dbgChk and not v_tittle :
        i_dbg.dbgDel( v_bool, v_data)

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
    
    i_ist.f_daleks()
    i_ist.f_jeSappelGroot()
    i_ist.f_knocPeny(3)
    i_ist.f_42(42)
    
    
    
if __name__ == '__main__':
    main()

        