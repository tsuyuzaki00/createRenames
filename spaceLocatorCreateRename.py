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
        
    num = '1'.zfill(2)
    locator = pm.spaceLocator( n = '_'.join( ['lct','help',scene,num]) )
    grpGuide = '_'.join( ['grp','guide',scene] )
    if pm.objExists(grpGuide):
        pm.parent(locator, grpGuide)