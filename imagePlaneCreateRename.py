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
    
    test = '1'
    num = test.zfill(2)
    imageShape = pm.imagePlane()
    imageFile = pm.listRelatives(imageShape, p = True)
    pm.rename(imageFile, '_'.join( ['image','file',scene,num]))
    grp = '_'.join( ['grp','gud',scene] )
    if pm.objExists(grp):
        pm.parent(imageFile[0], grp)