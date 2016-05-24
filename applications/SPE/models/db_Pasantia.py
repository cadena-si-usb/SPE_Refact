# -*- coding: utf-8 -*-

db.define_table('Pasantia',
    Field('titulo',
           requires=[IS_NOT_EMPTY
                        (error_message='Es necesario un Titutlo.')],
           label='Titulo'),
    Field('periodo',##referencia a tabla Periodo
           label ='Periodo'),
    Field('area_proyecto','string',
          requires=[IS_NOT_EMPTY
                        (error_message='Adicione Area del Proyecto.')],
          label = 'Area del Proyecto'),
    Field('resumen_proyecto','text',
          requires=[IS_NOT_EMPTY
                        (error_message='Coloque resumen del proyecto ')],
          label ='Resumen del Proyecto'),
    Field('Materia',##refenrecia a tabla Materia
          label ='Materia'),
    Field('obejtivo',
          requires=[IS_NOT_EMPTY
                (error_message='Adicione Area del Proyecto.')],
          label ='Objetivo General'),
    Field('confidencialidad',
          requires=[IS_NOT_EMPTY
                        (error_message='Adicione Area del Proyecto.')],
          label ='Detalles de Confidencialidad'),
    Field('plan_trabajo',##referencia a plan de trabajo
          label = 'Plan de Trabajo')
)