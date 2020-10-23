import mainEdit.templateName as tpn
import pymel.core as pm

def main():
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        scene = part[0][:-3]
    elif part[0] == '':
        scene = 'scene'
    else:
        scene = part[0]
        
    num = '1'.zfill(3)
    model = pm.polyCube(n = '_'.join( ['C','model','geo',scene,num]) )
    grpGeo = '_'.join( ['grp','geo',scene] )
    if pm.objExists(grpGeo):
        pm.parent(model[0], grpGeo)

#tpn.name(obj = '', node = '', pos = '', num = '', scene = '')