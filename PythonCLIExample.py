import json
import requests
import time

# Required values
apiKey = ""
universeId = ""
placeId = ""

# Mutable Constants
maximumRetryAttempts = 10
retryPollingCadence = 1

class Commands():
    GetInstance = "get"
    ListInstanceChildren = "lst"
    UpdateInstance = "upd"
    Help = "help"

# Immutable Constants
apiKeyHeaderKey = "x-api-key"
contentTypeHeaderKey = "Content-type"
contentTypeValue = "application/json"

apiBaseURL = "https://apis.roblox.com/cloud/v2/"
instanceResourceUrl = apiBaseURL + "universes/%s/places/%s/instances/%s"
listChildrenUrlPostfix = ":listChildren"

kEngineInstanceKey = "engineInstance"
kDetailsKey = "Details"
kPathKey = "path"
kDoneKey = "done"

# HTTP Requests
def Request_GetInstance(instanceId):
    url = instanceResourceUrl % (universeId, placeId, instanceId)
    headerData = {apiKeyHeaderKey: apiKey}
    return requests.get(url, headers = headerData)

def Request_ListChildren(instanceId):
    url = (instanceResourceUrl % (universeId, placeId, instanceId)) + listChildrenUrlPostfix
    headerData = {apiKeyHeaderKey: apiKey}
    return requests.get(url, headers = headerData)

def Request_UpdateInstance(instanceId, instanceType, propertyName, propertyValue):
    url = instanceResourceUrl % (universeId, placeId, instanceId)
    postBody = json.dumps({kEngineInstanceKey: {kDetailsKey: {instanceType: {propertyName: propertyValue}}}})
    headerData = {apiKeyHeaderKey: apiKey, contentTypeHeaderKey: contentTypeValue}
    return requests.patch(url, headers = headerData, data = postBody)

def Request_GetOperation(operationId):
    url = apiBaseURL + operationId
    headerData = {apiKeyHeaderKey: apiKey}
    return requests.get(url, headers = headerData)

def PollForOperationResults(operationId):
    currentNumberOfRetries = 0
    while (currentNumberOfRetries < maximumRetryAttempts):
        results = Request_GetOperation(operationId)
        if (results.status_code != 200 or results.json()[kDoneKey]):
            print("\n")
            return results
        time.sleep(retryPollingCadence)
        currentNumberOfRetries += 1
        print(".",  end="")
        
        
    print("\nMaximum retries attempted")

# Commands
def ExecuteRequestCommand(func, args):
    reqResults = func(args)
    if (not reqResults):
        print(reqResults.content)
        return
    
    if (reqResults.status_code != 200):
        print(func.__name__, " - Error: ", reqResults.status_code)
        return

    operationId = reqResults.json()["path"]
    results = PollForOperationResults(operationId)

    if (results is None):
        print("No Results")
        return
    
    if (results.status_code == 429):
        print("Too many requests: Please wait before trying again")
        return

    if (results.status_code != 200):
        print("Error:", results.status_code, " - ", results.text)
        return
    
    PrettyPrint(results.json())

def Command_GetInstance(args):
    if (len(args) != 1):
        print("Command_GetInstance: Incorrect number of args. 1 expected")
        return
    return Request_GetInstance(args[0])

def Command_ListChildren(args):
    if (len(args) != 1):
        print("Command_ListChildren: Incorrect number of args. 1 expected")
        return
    return Request_ListChildren(args[0])

def Command_UpdateInstance(args):
    if (len(args) < 4):
        print("Command_UpdateInstance: Incorrect number of args. 4 expected")
        return
    valueData = args[3:]
    valueString = " ".join(valueData)
    return Request_UpdateInstance(args[0], args[1], args[2], valueString)

def ExecuteCommand(commandData):
    cmd = commandData[0].lower()
    if (cmd == Commands.GetInstance):
        ExecuteRequestCommand(Command_GetInstance, commandData[1:])
    elif (cmd == Commands.ListInstanceChildren):
        ExecuteRequestCommand(Command_ListChildren, commandData[1:])
    elif (cmd == Commands.UpdateInstance):
        ExecuteRequestCommand(Command_UpdateInstance, commandData[1:])
    elif (cmd == Commands.Help):
        Print_Help()
    else:
        print("Unknown command:", cmd)

def getNextCommand():
    print(">> ", end="")
    commandInput = input()
    commandData = commandInput.split(" ")
    if len(commandData) > 0:
        return commandData
    
    print("no commands passed")
    return getNextCommand()

# Output
def PrettyPrint(jsonDict):
    if 'response' not in jsonDict:
        print(jsonDict, "\n")
        return
    response = jsonDict['response']
    if 'instances' in response:
        instanceList = response["instances"]
        if (len(instanceList) == 0):
            print ("No children present")
        for i in instanceList:
            print(i) 
    elif 'engineInstance' in response:
        print(response)
    else:
        print("Unknown formatting error occurred: ", jsonDict)
    print("")

def Print_Help():
    print("=====================================")
    print("===Engine Open Cloud API V0.1 Test===")
    print("=====================================\n")
    print("AVAILABLE COMMANDS:\n")
    print("GET <instanceId>")
    print("   Gets information about the provided instance")
    print("   <instanceId> : 128-bit condensed format 32 char hex id to identify the instance\n")
    print("LST <instanceId>")
    print("   Lists the children of an instance")
    print("   <instanceId> : 128-bit condensed format 32 char hex id to identify the instance\n")
    print("UPD <instanceId> <instanceType> <propertyName> <propertyValue>")
    print("   Updates the properties of an instance and gets that instance data")
    print("   <instanceId> : 128-bit condensed format 32 char hex id to identify the instance")
    print("   <instanceType> : The camelCase name of the class you are attempting to edit")
    print("   <propertyName> : The camelCase name of the property you are attempting to edit")
    print("   <propertyValue> : The value of the property you are attempting to edit\n")
    print("Note: For all commands, root is an alias of the DataModel and can be passed instead of instanceId")
    print("\n=====================================\n")

# Command List Interface
def startCLI():
    print("===========================================")
    print("== Engine Open Cloud API V0.1 Bug Bash 1 ==")
    print("===========================================")

    global apiKey
    global universeId
    global placeId

    if (not apiKey):
        print("No API Key found. Please enter a valid API Key:")
        apiKey = getNextCommand()[0]

    if (not universeId):
        print("No UniverseId found. Please enter a valid UniverseId:")
        universeId = getNextCommand()[0]

    if (not placeId):
        print("No PlaceId found. Please enter a valid PlaceId:")
        placeId = getNextCommand()[0]

    print("Please Enter Command (Enter HELP to get started)")
    while True:
        commandData = getNextCommand()
        ExecuteCommand(commandData)

startCLI()