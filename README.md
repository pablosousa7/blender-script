# Simple plugin to move between collections within blender

This first function moves all objects between collections, you have to pass 3 arguments

```python 
moveAllObjectsAnotherCollection(cFrom, cTo, stayObjs):
```

```python
moveJustOneObject(cFrom, obj, cTo, stayObjs = False):
```


***cFrom*** = collection from which objects will be extracted<br/><br/>
***cTo*** = collection where new objects will be stored<br/><br/>
***stayObjs*** = if you want to keep the objects in the original collection or remove them.<br/><br/>
**obj** = Specific object you want to extract to another collection<br/><br/>


the second function does the same thing, but you can only move one file at a time.<br/><br/><br/><br/>
	
***Author: Pablo Sousa***
