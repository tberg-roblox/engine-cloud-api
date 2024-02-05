# Instance Cloud Resource Schema
This schema has been adapted from the internal protobuf definitions but has been slightly altered for easier readability.

#### InstanceResource
Cloud representation of an instance.
```
{
  // The resource path of the instance.
  // Format: universes/{universe}/places/{place}/instances/{instance}
  string path;

  // True if the instance has children in the instance tree
  bool hasChildren;

  // Instance specific information that can also be found in engine
  EngineInstance engineInstance;
}
```

#### EngineInstance
Representation of an instance in a place
```
{
  // The unique identifier for an instance
  // In format: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  string Id;

  // The unique identifier for the parent instance
  // In format: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  string Parent;

  // Name of the instance
  optional string Name;

  // Type and property information
  optional InstanceDetails Details;
}
```

#### InstanceDetails
Data specific to the type of the instance
```
{
  // Property data for an instance. If the instance type is not present, this will be empty
  oneof kind {
    Folder Folder;
    LocalScript LocalScript;
    ModuleScript ModuleScript;
    Script Script;
  }
}
```

#### Folder
Data specific to instance with the Folder type
```
{
  // No properties exposed
}

#### LocalScript
Data specific to instance with the LocalScript type
```
{
  // Value of LocalScript.Disabled in engine (Not currently editable through API)
  optional bool Disabled;
  // Value of LocalScript.Source in engine
  optional string Source;
}
```

#### ModuleScript
Data specific to instance with the ModuleScript type
```
{
  // Value of ModuleScript.Source in engine
  optional string Source;
}
```

#### Script
Data specific to instance with the Script type
```
{
  // Value of Script.Disabled in engine (Not currently editable through API)
  optional bool Disabled;
  // Value of Script.RunContext in engine (Not currently editable through API)
  optional RunContext RunContext;
  // Value of Script.Source in engine
  optional string Source;
}
```
