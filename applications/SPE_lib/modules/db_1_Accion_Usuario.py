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
        Field('accion','reference Accion'),
        Field('contexto',requires=IS_IN_SET(['Usuarios','Catálogos', 'Pasantias', 'Configuración','Otros'],zero=None)),
        Field('rol','reference auth_group',
              requires=IS_IN_DB(db,'auth_group.id','%(role)s',zero=None),
              label='Roles (*)')
       )

    if db(db.Accion_Usuario.id > 0).count() == 0:


        db.Accion_Usuario.insert(
            accion=1,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=2,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=3,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=4,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=5,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=6,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=7,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=8,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=9,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=10,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=11,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=12,
            contexto='Usuarios',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=13,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=14,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=15,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=16,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=17,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=18,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=19,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=20,
            contexto='Pasantias',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=21,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=22,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=23,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=24,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=25,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=26,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=27,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=28,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=29,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=30,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=31,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=32,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=33,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=34,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=35,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=36,
            contexto='Catálogos',
            rol='6'
        )
        db.Accion_Usuario.insert(
            accion=37,
            contexto='Configuración',
            rol='6'
        )
        # Acciones Comunes
        for i in range(1,7):
            db.Accion_Usuario.insert(
                accion=38,
                contexto='Configuración',
                rol=i
            )
        db.Accion_Usuario.insert(
            accion=39,
            contexto='Configuración',
            rol='1'
        )
        db.Accion_Usuario.insert(
            accion=41,
            contexto='Configuración',
            rol='1'
        )
        db.Accion_Usuario.insert(
            accion=42,
            contexto='Pasantias',
            rol='1'
        )
        db.Accion_Usuario.insert(
            accion=40,
            contexto='Pasantias',
            rol='3'
        )

        db.commit()

#------------------------------------------------------------------------------#

################################################################################
#                          FIN DECLARACION BASE DE DATOS                       #
################################################################################
