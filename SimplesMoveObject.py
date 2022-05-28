import bpy

"""

	Simple plugin to move between collections within blender

	This first function moves all objects between collections, you have to pass 3 arguments
	moveAllObjectsAnotherCollection(cFrom, cTo, stayObjs)

	cFrom = collection from which objects will be extracted
	cTo = collection where new objects will be stored
	stayObjs = if you want to keep the objects in the original collection or remove them.


	the second function does the same thing, but you can only move one file at a time.
	
	Author: Pablo Sousa
"""

def moveAllObjectsAnotherCollection(cFrom, cTo, stayObjs = False):
    
    # Get the collection "from"
    coll_from = bpy.data.collections[cFrom]
    
    # Get the collection "to"
    coll_to = bpy.data.collections[cTo]
    
    # clear all object 'from' collection
    obj_unlink = []
    
    for obj in coll_from.objects:
        # try link objects to the new collections
        try:
            coll_to.objects.link(obj)
        except RuntimeError:
            pass
        
        # Add all object to link unlink / delete
        obj_unlink.append(obj)
        
    
    # Here all objects inside list are deleted
    if stayObjs == False:
        for obj_del in obj_unlink:
            coll_from.objects.unlink(obj_del)
        

def moveJustOneObject(cFrom, obj, cTo, stayObjt = False):
    
    # If collection is not empty then true or false
    hasObj = len(list(bpy.data.collections[cFrom].all_objects)) > 0
     
    # Here get the object specific in the collection 'from'
    if hasObj:
        coll_from_obj = bpy.data.collections[cFrom].all_objects[obj]
        
        # add the object for delete
        obj_unlink = coll_from_obj
    else:
        print("This object not found in this collection!")
        
    
    if hasObj:
        # add object the another collection
        coll_to = bpy.data.collections[cTo].objects.link(coll_from_obj)
    else:
        print("This object not found in this collection!")
        
    # remove object of the current view
    if stayObjt == False:
        bpy.data.collections[cFrom].objects.unlink(obj_unlink)

        
moveAllObjectsAnotherCollection('DEMO.001', 'Collection', False)
#moveJustOneObject('DEMO.001', 'Cube', 'Collection')
