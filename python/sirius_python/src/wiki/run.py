#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pywikibot
import storage_ring
import booster


bot_default_comment = 'Automatically generated by ' + os.path.basename(__file__)


def check_deps(parameters):
    names = [parameter.name for parameter in parameters]
    for parameter in parameters:
        msg = ''
        deps = parameter.deps
        for dep in deps:
            if dep not in names:
                if msg is '':
                    msg = str(parameter.name) + ': ' + str(dep)
                else:
                    msg += ', ' + str(dep)

        if msg is not '':
            print(msg)


def generate_parameter_name_list_page(label, parameters):
    wiki = []
    for parameter in parameters:
        name = parameter.name.replace(label+' ', '')
        name_capitalized = name[0].upper() + name[1:]
        line = '#[[Parameter:' + parameter.name + '|' + name_capitalized + ']]'
        wiki.append(line)
    
    site = pywikibot.Site('en', 'siriuswiki')
    page = pywikibot.Page(site, 'Machine:' + label + ' parameter name list')
    page.text = '\n'.join(wiki)
    page.save(bot_default_comment)
    
    
def generate_parameter_pages(parameters):
    site = pywikibot.Site('en', 'siriuswiki')  
    for parameter in parameters:
        page = pywikibot.Page(site, 'Parameter:'+parameter.name)
        page.text = parameter.create_wiki_page()
        #page.save(bot_default_comment)
        print(page.text)


#check_deps(sirius_sr)
storage_ring.parameter_list.sort()
generate_parameter_pages(storage_ring.parameter_list)
#generate_parameter_name_list_page(storage_ring.label, storage_ring.parameter_list)
