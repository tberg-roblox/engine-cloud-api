# Engine Cloud API V0.1 Alpha Quick Start Guide



1. Choose a place to get set up
    1. Choose a place that has Script(s), LocalScript(s), and/or ModuleScript(s) that you want to edit through Cloud API
    2. Fill out the form provided on the Guilded Server to get your place added to the allowed places
    3. We will let you know when the place is ready to use
2. Generate an API Key
    1. Go to [https://create.roblox.com/dashboard/credentials](https://create.roblox.com/dashboard/credentials)
    2. Click the ‘**CREATE API KEY**’ button
    3. Type a name for your key
    4. Select and add ‘Engine’ from the API System list
        1. If this system is not available, let us know
    5. Click the ‘**ADD API SYSTEM**’ button
    6. Find the experience that includes the place(s) you filed to add in Step 1
    7. Click the ‘**ADD EXPERIENCE**’ button
    8. In the Operations dropdown, add both ‘Read’ and ‘Write’
    9. Enter the IP address you will be using the key from
        1. Enter 0.0.0.0/0 if you want to allow access from all addresses
    10. Click the ‘**ADD IP ADDRESS**’ button
    11. Click the ‘**SAVE & GENERATE KEY**’ button
    12. Copy the API Key that was generated

* NOTE: At this point you should have:
    * API Key with Engine permissions
    * PlaceId for a whitelisted place
    * Corresponding UniverseId \

3. Install Python
    1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
    2. Click the ‘Download Python’ button
    3. Follow the installation instructions
4. Clone the git repo
    1. Clone or download the git repo - [https://github.com/tberg-roblox/engine-cloud-api](https://github.com/tberg-roblox/engine-cloud-api)
5. Run the Quick Start Python Script
    1. Open your command shell
        1. CMD on Windows
        2. Terminal on MacOS
    2. Navigate to the location the python script was downloaded to
        1. cd &lt;location>
    3. Execute the following command
        1. python .\PythonCLIExample.py


### Using Python.CLIExample.py

For ease of use, feel free to edit the script to add **apiKey**, **universeId**, and **placeId **directly to the code under the section Required Values, otherwise, these values will be prompted on every run of the script \


When you have entered the previous data, try entering the following command

\>> help

```
=====================================
===Engine Open Cloud API V0.1 Test===
=====================================

AVAILABLE COMMANDS:

GET <instanceId>
   Gets information about the provided instance
   <instanceId> : 128-bit condensed format 32 char hex Id to identify the instance

LST <instanceId>
   Lists the children of an instance
   <instanceId> : 128-bit condensed format 32 char hex Id to identify the instance

UPD <instanceId> <instanceType> <propertyName> <propertyValue>
   Updates the properties of an instance and gets that instance data
   <instanceId> : 128-bit condensed format 32 char hex Id to identify the instance
   <instanceType> : The PascalCase Name of the class you are attempting to edit
   <propertyName> : The PascalCase Name of the property you are attempting to edit
   <propertyValue> : The value of the property you are attempting to edit

Note: For all commands, root is an alias of the DataModel and can be passed instead of instanceId

=====================================
```

As you can see, we have three other commands at our disposal. Let’s try out the get command. root is an alias for the datamodel root. Let's use that to get more data

\>> get root

```
{'@type': 'type.googleapis.com/roblox.open_cloud.cloud.v2.Instance', 'path': 'universes/5173123139/places/15022282565/instances/33bfdd7f-81e8-faa5-0551-8b8300000001', 'hasChildren': True, 'engineInstance': {'Id': '33bfdd7f-81e8-faa5-0551-8b8300000001', 'Parent': '', 'Name': 'Game', 'Details': {}}}
```

It worked! If for some reason it didn’t, let us know in the channel. There are a few items of note here, so lets break it down. ‘`hasChildren' `lets us know if this instance has children in the datamodel. `'Id'` provides a unique identifier for referring to a specific instance. root is the only current alias, and all other instances will need to be referred to by their Id. Let’s use this now to get information about its children

\>> lst 33bfdd7f-81e8-faa5-0551-8b8300000001

```
{'path': 'universes/5173123139/places/15022282565/instances/44b188da-ce63-2b47-02e9-c68d004815fc', 'hasChildren': True, 'engineInstance': {'Id': '44b188da-ce63-2b47-02e9-c68d004815fc', 'Parent': '33bfdd7f-81e8-faa5-0551-8b8300000001', 'Name': 'Workspace', 'Details': {}}}
{'path': 'universes/5173123139/places/15022282565/instances/33bfdd7f-81e8-faa5-0551-8b8300000004', 'hasChildren': False, 'engineInstance': {'Id': '33bfdd7f-81e8-faa5-0551-8b8300000004', 'Parent': '33bfdd7f-81e8-faa5-0551-8b8300000001', 'Name': 'Run Service', 'Details': {}}}
{'path': 'universes/5173123139/places/15022282565/instances/33bfdd7f-81e8-faa5-0551-8b8300000005', 'hasChildren': True, 'engineInstance': {'Id': '33bfdd7f-81e8-faa5-0551-8b8300000005', 'Parent': '33bfdd7f-81e8-faa5-0551-8b8300000001', 'Name': 'GuiService', 'Details': {}}}
...

```

lst will return a list of children. As you can see, the first instance returned was Workspace and has the Id `44b188da-ce63-2b47-02e9-c68d004815fc`. Let’s use this to dive deeper into the instance hierarchy.

\>> lst 44b188da-ce63-2b47-02e9-c68d004815fc

```
{'path': 'universes/5173123139/places/15022282565/instances/44b188da-ce63-2b47-02e9-c68d004831f8', 'hasChildren': False, 'engineInstance': {'Id': '44b188da-ce63-2b47-02e9-c68d004831f8', 'Parent': '44b188da-ce63-2b47-02e9-c68d004815fc', 'Name': 'Camera', 'Details': {}}}
{'path': 'universes/5173123139/places/15022282565/instances/44b188da-ce63-2b47-02e9-c68d00483205', 'hasChildren': False, 'engineInstance': {'Id': '44b188da-ce63-2b47-02e9-c68d00483205', 'Parent': '44b188da-ce63-2b47-02e9-c68d004815fc', 'Name': 'Terrain', 'Details': {}}}
{'path': 'universes/5173123139/places/15022282565/instances/1ccbbed0-ea2a-a9b8-0539-e4a200003d79', 'hasChildren': False, 'engineInstance': {'Id': '1ccbbed0-ea2a-a9b8-0539-e4a200003d79', 'Parent': '44b188da-ce63-2b47-02e9-c68d004815fc', 'Name': 'ModuleScript', 'Details': {'ModuleScript': {'Source': 'asdfkjasl;fkjasdldk;f'}}}}
```

Here we’ve listed the children of Workspace. There are three children, Camera, Terrain, and ModuleScript. We can see that ModuleScript  has more details than the other instances. That's because this alpha is focused on script-type instances (Script, LocalScript, ModuleScript) and their Source property. Lets try editing the contents of ModuleScript. The Id for ModuleScript is `1ccbbed0-ea2a-a9b8-0539-e4a200003d79`

\>> upd 1ccbbed0-ea2a-a9b8-0539-e4a200003d79 ModuleScript Source --newValue

```
{'@type': 'type.googleapis.com/roblox.open_cloud.cloud.v2.Instance', 'path': 'universes/5173123139/places/15022282565/instances/1ccbbed0-ea2a-a9b8-0539-e4a200003d79', 'hasChildren': False, 'engineInstance': {'Id': '1ccbbed0-ea2a-a9b8-0539-e4a200003d79', 'Parent': '44b188da-ce63-2b47-02e9-c68d004815fc', 'Name': 'ModuleScript', 'Details': {'ModuleScript': {'Source': '--newValue'}}}}
```

The Source value for ModuleScript has been changed to --newValue.

Congratulations! You know how to use all the commands in the quick start python script!
