#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  17 09:27:59 2019

@author: stephaneblondellarougery
"""

import os
path = os.path.abspath(__file__)

characteristic = {
	"subject" : { "data_path" : path + "/characteristics/subject.csv", "refer_as" : "id_sujet"},
	"destination_is" : { "data_path" : path + "/characteristics/destination.csv", "refer_as" : "id_destination"},
	"destination_to" : { "data_path" : path + "/characteristics/destination.csv", "refer_as" : "id_destination"},
	"destination_from" : { "data_path" : path + "/characteristics/destination.csv", "refer_as" : "id_destination"}, 
}