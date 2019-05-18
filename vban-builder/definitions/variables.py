#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:27:59 2019

@author: stephaneblondellarougery
"""

import axp.update

general_parameters = {
    "clientKeyPath" : "/Users/stephaneblondellarougery/Desktop/client_secret/all_in_debug.txt",
    "worksheetFormat" : {
        "inputStartingRow" : 2,               # using python convention
        "inputStartingColumn" : 1,            # using python convention
        "jl_condition_row" : 0,               # using python convention
        "field_name_row" : 1,                 # using python convention
        "missing_character" : "#"
    }
}


# Get the list of axps

f = open('variables.txt','r')
variables_all = f.read()
f.close()

variables = variables_all.split("\n")



# Rebuild the meta-parameters

meta_parameters = []

for var_id in variables :

    if len(var_id) != 6 : pass    # to do properly someday
    else : 
    
        spreadsheet_name = "axp-" + var_id.replace(".", "")
        
        meta_parameter = general_parameters
        meta_parameter["variableId"] = var_id
        meta_parameter["spreadsheetName"] = spreadsheet_name
        
        meta_parameters.append(meta_parameter)




# Update

for meta_parameter in meta_parameters : 
    
    axp.update.update_axp(meta_parameter)
    
    print("Transfered : " + str(meta_parameter["variableId"]))