#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import DBhandler
from APIhandler import Model
import Encoder

class Curriculo(Model):
    #Building database object
    def __init__(self):
    	super(Curriculo,self).__init__(tableName="Curriculo")