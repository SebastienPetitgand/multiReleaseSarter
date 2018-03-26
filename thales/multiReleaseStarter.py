import sys, string, time
import com.xhaus.jyson.JysonCodec as json
from com.xebialabs.xlrelease.domain import Task
from com.xebialabs.deployit.plugin.api.reflect import Type
from java.text import SimpleDateFormat
 
 #code récupéré
def createSimpleTask(phaseId, taskTypeValue, title, propertyMap):
    parenttaskType = Type.valueOf(taskTypeValue)
    parentTask = parenttaskType.descriptor.newInstance("nonamerequired")
    parentTask.setTitle(title)
    sdf = SimpleDateFormat("yyyy-MM-dd hh:mm:ss")
    for item in propertyMap:
        if item.lower().find("date") > -1:
            if propertyMap[item] is not None and len(propertyMap[item]) != 0:
                parentTask.setProperty(item,sdf.parse(propertyMap[item]))
        else:
            parentTask.setProperty(item,propertyMap[item])
    taskApi.addTask(phaseId,parentTask)




task = getCurrentTask()
release = getCurrentRelease()
ReleaseVariables = releaseApi.getVariables(release.id)
paramVariable = ReleaseVariables[0].value
listeVariable = ReleaseVariables[1].value


#print listeVariable
#print paramVariable

for i in listeVariable:
	createSimpleTask(phase.id,"xlrelease.CreateReleaseTask", "New release", 
	{"newReleaseTitle":i, "templateId" :"Applications/Folder242423627/Folder631136719/Release894680951"})
	
	
#"templateVariables":{'git_url':'test'},
#createSimpleTask(phase.id,"xlrelease.CreateReleaseTask", "New release", 
#{"description":"coolio","newReleaseTitle":"toto", "templateId" :"Applications/Folder242423627/Folder882369723/Release894680951"})