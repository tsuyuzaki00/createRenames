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
    camShape = pm.camera( n = '_'.join( ['cam','cut',scene,'C',num]) )
    cam = pm.listRelatives(camShape, p = True)
    pm.rename(cam, '_'.join( ['cam','cut',scene,'C',num] ))
    grp = '_'.join( ['grp','cam',scene] )
    if pm.objExists(grp):
        pm.parent(cam, grp)