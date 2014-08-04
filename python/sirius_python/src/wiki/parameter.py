
class Parameter:
    def __init__(self, 
        name, 
        value,
        group    = 'LNLS',
        symbol   = '', 
        units    = '', 
        deps     = '', 
        obs      = '', 
        revision = ''):
        self.name     = name
        self.group    = group
        self.symbol   = symbol
        self.value    = value 
        self.units    = units
        self.deps     = deps
        self.obs      = obs
        self.revision = revision

    def __str__(self):
        r = self.name + ': ' + str(self.value) + ' ' + self.units + ' [' + self.revision + ']'
        return r

    def create_wiki_deps(self):
        deps = ''
        for dep in self.deps:
            if deps is not '': 
                deps = deps + ', '
            deps = deps + '[[Parameter:' + str(dep) + '|' + str(dep) + ']]'
        return deps

    def create_wiki_page(self):
        wiki = []
        wiki.append('=Data=')
        wiki.append('<section begin=data/>')
        wiki.append('* Group: <section begin=group/>' + str(self.group) + '<section end=group/>')
        wiki.append('* Revision: <section begin=revision/>' + str(self.revision) + '<section end=revision/>')
        wiki.append('* Symbol: <section begin=symbol/>' + str(self.symbol) + '<section end=symbol/>')
        wiki.append('* Value: <section begin=value/>' + str(self.value) + '<section end=value/>')
        wiki.append('* Units: <section begin=units/>' + str(self.units) + '<section end=units/>')
        wiki.append('* Deps: <section begin=deps/>' + self.create_wiki_deps() + '<section end=deps/>')
        wiki.append('<section end=data/>')
        wiki.append('=Observations=')
        wiki.append('<section begin=obs/>' + str(self.obs) + '<section begin=obs/>')
        return '\n'.join(wiki)