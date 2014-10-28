
def buildlat(elist):
    """builds flat list of elements"""
    the_ring = []
    try:
        for e in elist:
            the_ring += buildlat(e)
    except TypeError:
        the_ring += [elist]
    return the_ring

def findspos(lattice, indices = None):
    """returns longitudinal position of the entrance for all lattice elements"""
    
    ''' process input '''
    is_number = False
    if indices is None:
        indices = range(len(lattice))
    else:
        try:
            indices[0]
        except:
            is_number = True
            indices = [indices]
                    
    pos = (len(lattice)+1) * [0.0]
    for i in range(1,len(lattice)+1):
        pos[i] = pos[i-1] + lattice[i-1].length
    pos[-1] = pos[-2] + lattice[-1].length
    if is_number:
        return pos[i]
    else:
        return [pos[i] for i in indices]
    
def findcells(lattice, attribute_name, value=None):
    """returns a list with indices of elements that match criteria 'attribute_name=value'"""
    indices = []
    for i in range(len(lattice)):
        if hasattr(lattice[i], attribute_name):    
            if value == None:
                if getattr(lattice[i], attribute_name) != None:
                    indices.append(i)
            else:
                if getattr(lattice[i], attribute_name) == value:
                    indices.append(i)
    return indices

def getcellstruct(lattice, attribute_name, indices = None):
    """ returns a list with requested lattice data """
    if indices is None:
        indices = range(len(lattice))
    else:
        try:
            indices[0]
        except:
            indices = [indices]
    
    data = []
    for idx in indices:
        tdata = getattr(lattice[idx], attribute_name)
        data.append(tdata)
    return data

def setcellstruct(lattice, attribute_name, indices, values):    
    """ sets elements data and returns a new updated lattice """
    for idx in range(len(indices)):
        try:
            setattr(lattice[indices[idx]], attribute_name, values[idx])
        except:
            setattr(lattice[indices[idx]], attribute_name, values)
    return lattice

def finddict(lattice, attribute_name):
    """ returns a dict which correlates values of 'attribute_name' and a list of indices corresponding to matching elements """
    latt_dict = {}  
    for i in range(len(lattice)):
        if hasattr(lattice[i], attribute_name):
            att_value = getattr(lattice[i], attribute_name)
            if att_value in latt_dict:
                latt_dict[att_value].append(i)
            else:
                latt_dict[att_value] = [i]
    return latt_dict