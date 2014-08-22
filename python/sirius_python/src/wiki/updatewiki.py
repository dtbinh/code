#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import pywikibot
import storage_ring
import booster
import linac
import linac_to_booster_transport_line
import booster_to_storage_ring_transport_line


sort_flag = False
bot_default_comment = ('Automatically generated by ' + os.path.basename(__file__))


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
    #return
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
    
def generate_parameter_flat_list_page(label, parameters):
    wiki = []
    for parameter in parameters:
        name = parameter.name.replace(label+' ', '')
        name_capitalized = name[0].upper() + name[1:]
        wiki.append('=[[Parameter:'+parameter.name+'|'+name_capitalized+']]=')
        wiki.append("'''Data'''")
        wiki.append('{{#lst:Parameter:'+parameter.name+'|data}}')
        wiki.append("'''Observations'''")
        wiki.append('')
        wiki.append('{{#lst:Parameter:'+parameter.name+'|obs}}')
    site = pywikibot.Site('en', 'siriuswiki')
    page = pywikibot.Page(site, 'Machine:' + label + ' parameter flat list')
    page.text = '\n'.join(wiki)
    page.save(bot_default_comment)
    #print(page.text)
        
    
    
def generate_parameter_pages(parameters):
    #return
    site = pywikibot.Site('en', 'siriuswiki')  
    for parameter in parameters:
        page = pywikibot.Page(site, 'Parameter:'+parameter.name)
        page.text = parameter.create_wiki_page()
        page.save(bot_default_comment)
        #print(page.text)

def update_submachine(submachine, parameters_list = None):
    if sort_flag:
        submachine.parameter_list.sort()
    if parameters_list is None:
        generate_parameter_pages(submachine.parameter_list)
        generate_parameter_name_list_page(submachine.label, submachine.parameter_list)
        generate_parameter_flat_list_page(submachine.label, submachine.parameter_list)
        return
    if len(parameters_list) == 0:
        return
    print('<'+submachine.label+'>')
    parm_names = [p.name for p in submachine.parameter_list]
    parameter_updated = False
    parameters_list.sort()
    for parameter in parameters_list:
        try:
            parameter_full_name = submachine.label + ' ' + parameter
            idx = parm_names.index(parameter_full_name)
            parm = submachine.parameter_list[idx]
            generate_parameter_pages([parm])
            #print(parm.name + ' updated.')
            parameter_updated = True
        except ValueError:
            print(parameter + ' not defined!')
    if parameter_updated:
        generate_parameter_name_list_page(submachine.label, submachine.parameter_list)
        generate_parameter_flat_list_page(submachine.label, submachine.parameter_list)
        #print('"Machine:'+submachine.label+' parameter name list" page updated.')
    

    
def update_all():
    update_submachine(submachine = storage_ring)
    update_submachine(submachine = booster)
    update_submachine(submachine = linac)
    update_submachine(submachine = linac_to_booster_transport_line)
    update_submachine(submachine = booster_to_storage_ring_transport_line)
    
def lists_all_parameters():
    submachine = storage_ring
    if sort_flag:
        submachine.parameter_list.sort()
    print('<'+submachine.label+'>')
    for i in range(len(submachine.parameter_list)):
        print('{0:03d}. {1}'.format(i+1, submachine.parameter_list[i].name))
    submachine = booster
    if sort_flag:
        submachine.parameter_list.sort()
    print('<'+submachine.label+'>')
    for i in range(len(submachine.parameter_list)):
        print('{0:03d}. {1}'.format(i+1, submachine.parameter_list[i].name))
    submachine = linac
    if sort_flag:
        submachine.parameter_list.sort()
    print('<'+submachine.label+'>')
    for i in range(len(submachine.parameter_list)):
        print('{0:03d}. {1}'.format(i+1, submachine.parameter_list[i].name))
    submachine = linac_to_booster_transport_line
    if sort_flag:
        submachine.parameter_list.sort()
    print('<'+submachine.label+'>')
    for i in range(len(submachine.parameter_list)):
        print('{0:03d}. {1}'.format(i+1, submachine.parameter_list[i].name))
    submachine = booster_to_storage_ring_transport_line
    if sort_flag:
        submachine.parameter_list.sort()
    print('<'+submachine.label+'>')
    for i in range(len(submachine.parameter_list)):
        print('{0:03d}. {1}'.format(i+1, submachine.parameter_list[i].name))
   

def print_help(argv):
    print('NAME')
    print('      ' + argv[0] + ' - updates Sirius wiki pages' )
    print('')
    print('SYNOPSIS')
    print('      ' + argv[0] + ' [STRING1] [STRING2] [STRING3]...')
    print('')
    print('EXAMPLES')
    print('      ' + '01. updates all parameters in Sirius wiki:')
    print('      ' + argv[0])
    print('')
    print('      ' + '02. updates all parameters but sorting first:')
    print('      ' + argv[0] + ' sort')
    print('')
    print('      ' + '03. updates all storage ring parameters:')
    print('      ' + argv[0] + ' si')
    print('')
    print('      ' + '04. updates all booster parameters:')
    print('      ' + argv[0] + ' bo')
    print('')
    print('      ' + '05. updates all linac parameters:')
    print('      ' + argv[0] + ' li')
    print('')
    print('      ' + '06. updates all linac to booster transport line parameters:')
    print('      ' + argv[0] + ' tb')
    print('')
    print('      ' + '07. updates all booster to storage ring transport line parameters:')
    print('      ' + argv[0] + ' ts')
    print('')
    print('      ' + '08. updates two storage ring parameters and one booster parameter:')
    print('      ' + argv[0] + ' si "beam energy" circumference booster "horizontal tune"')
    print('')
    print('      ' + '09. lists all defined parameters.')
    print('      ' + argv[0] + ' parameters')
    print('')
    
    
def process_arguments(argv):
    
    global sort_flag
    
    if len(argv) < 2:
        update_all()
    else:
        submachine  = None
        parms_lists = {'si':[], 'bo':[], 'li':[], 'tb':[], 'ts':[]}
        subma_flags = {'si':False, 'bo':False, 'li':False, 'tb':False, 'ts':False}
        all_parms   = {'si':storage_ring, 'bo':booster, 'li':linac, 'tb': linac_to_booster_transport_line, 'ts': booster_to_storage_ring_transport_line}
        '''builds lists with parameters'''
        for arg in argv[1:]:
            if arg == 'help':
                print_help()
            elif arg == 'parameters':
                lists_all_parameters()
            elif arg == 'si':
                submachine = 'si'
                subma_flags[submachine] = True
            elif arg == 'bo':
                submachine = 'bo'
                subma_flags[submachine] = True
            elif arg == 'li':
                submachine = 'li'
                subma_flags[submachine] = True
            elif arg == 'tb':
                submachine = 'tb'
                subma_flags[submachine] = True
            elif arg == 'ts':
                submachine = 'ts'
                subma_flags[submachine] = True
            elif arg == 'sort':
                sort_flag = True
            else:
                if submachine is None:
                    print_help()
                else:
                    parms_lists[submachine].append(arg)
                
        ''' calls updating functions '''    
        for sub in parms_lists.keys():
            if subma_flags[sub]:
                if parms_lists[sub]:
                    update_submachine(all_parms[sub], parms_lists[sub])
                else:
                    update_submachine(submachine = all_parms[sub])
                    
                    
                
if __name__ == "__main__":
    
    argv = sys.argv
    #argv = ['updatewiki.py', 'sort', 'parameters']
    process_arguments(argv)