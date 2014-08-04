#!/usr/bin/python

import os
import pywikibot
import storage_ring


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


def generate_pages(parameters):
    site = pywikibot.Site('en', 'siriuswiki')  
    for parameter in parameters:
        page = pywikibot.Page(site, 'Parameter:'+parameter.name)
        page.text = parameter.create_wiki_page()
        page.save('Automatically generated by '+os.path.basename(__file__))

    
#check_deps(sirius_sr)
generate_pages(storage_ring.parameter_list)