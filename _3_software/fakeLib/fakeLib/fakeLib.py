#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Infos
=====

   :Nom du fichier:     fakeLib.py
   :Autheur:            `Poltergeist42 <https://github.com/poltergeist42>`_
   :Version:            20180131

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
    - devchk
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

import logging
from logging.handlers import RotatingFileHandler

try :

    from devchk_pac.devchk import C_DebugMsg as dbg
    from devchk_pac.devchk import C_Benchmark as tm
    from devchk_pac.devchk import C_GitChk as gitChk

    v_dbgChk = True

except ModuleNotFoundError:
    print( "devChk n'a pas été trouvé" )
    v_dbgChk = False
    
import argparse

####

__all__ = ['C_FakeLib']

####

#################
#               #
# Snipet logger #
#               #
#################
v_chkDir = False
for _, t_dir, _ in os.walk( '.' ) :
    for i in t_dir :
        if "_log" in t_dir :
            v_chkDir = True
        
if not v_chkDir : 
    os.makedirs(os.path.normpath("./_log"), mode=0o777, exist_ok=True)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
## dbg_handler
dbg_formatter = logging.Formatter('%(asctime)s::%(levelname)s:: %(message)s')
dbg_handler = RotatingFileHandler('./_log/activity.log', 'a', 1000000, 1)
dbg_handler.setLevel(logging.DEBUG)
dbg_handler.setFormatter(dbg_formatter)

## info_handler
info_formatter = logging.Formatter('\n%(asctime)s::%(levelname)s::%(funcName)s')
info_handler = RotatingFileHandler('./_log/activity.log', 'a', 1000000, 1)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(info_formatter)

logger.addHandler(dbg_handler)
logger.addHandler(info_handler)

class C_FakeLib( object ) :
    """ Class fictive permettant de faire des tests pour les autres lib
        en cours de développement.
    """
    
    def __init__( self ) :
        """ **__init__()**
        
            Création et initialisation des variables globales de cette Class
        """
        
        
    @dbg()
    @tm("time")
    def f_daleks( self ) :
        logger.info("")
        try :
            raise Exception("EX-TER-MI-NA-TE")
        except Exception as e :
            logger.warning( e )
            print( e )

        
    @dbg() 
    @tm("time")
    def f_jeSappelGroot( self) :
        logger.info("")
        return "Je s'appel Groot !"

        
    @dbg() 
    @tm("time")
    def f_knocPeny( self, v_value ) :
        logger.info("")
        for i in range( v_value ) :
            logger.debug(f"i - {i}")
            print( "Toc ! toc ! toc ! Peny" )
        return "doue chaton"

        
    @dbg() 
    @tm("time")
    def f_42( self, v_value ) :
        logger.info("")
        logger.debug(f"v_value - {v_value}")
        if v_value == 42 :
            return 42, "la réponse à la vie, l'univers et tout le reste"
        
####

@dbg() 
@tm("time")
@gitChk(1, 'f')
def main() :
    """ Fonction principale """
    
    parser = argparse.ArgumentParser()
    parser.add_argument( "-d", "--debug", action='store_true', help="activation du mode debug")
                        
    args = parser.parse_args()
    
    if args.debug :
        if v_dbgChk :
            print( "Mode Debug activer" )
            dbg(1)
            tm(1)
        else :
            print( "Le mode Debug ne peut pas être active car le module n'est pas pressent")

    i_ist = C_FakeLib()
    
    i_ist.f_daleks()
    i_ist.f_jeSappelGroot()
    i_ist.f_knocPeny(3)
    i_ist.f_42(42)
    
    
    
if __name__ == '__main__':
    main()

        