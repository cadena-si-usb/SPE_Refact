# -*- coding: utf-8 -*-

################################################################################
#                         INICIO DECLARACION BASE DE DATOS                     #
################################################################################

#------------------------------------------------------------------------------#
#                            MODULO DE INVENTARIO                              #
#------------------------------------------------------------------------------#
from gluon import *
def Accion_Usuario_Table(db,T):
    db.define_table('Accion_Usuario',
        Field('first_name'),
        Field('destino'),
        Field('contexto'),
        Field('rol','reference auth_group',
              requires=IS_IN_DB(db,'auth_group.id','%(role)s',zero=None),
              label='Roles (*)')
       )

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
