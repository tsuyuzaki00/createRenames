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
    lightShape = pm.ambientLight( n = '_'.join( ['atl','cut',scene,'C',num]) )
    light = pm.listRelatives(lightShape, p = True)
    grp = '_'.join( ['grp','lit',scene] )
    if pm.objExists(grp):
        pm.parent(light, grp)