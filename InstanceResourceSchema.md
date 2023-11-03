# Instance Cloud Resource Schema
This schema has been adapted from the internal alpha protobuf definitions but has been slightly altered for easier readability.

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
  string id;

  // The unique identifier for the parent instance
  // In format: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  string parent;

  // Name of the instance
  optional string name;

  // Type and property information
  optional InstanceDetails details;
}
```

#### InstanceDetails
Data specific to the type of the instance
```
{
  // Property data for an instance. If the instance type is not present, this will be empty
  oneof kind {
    LocalScript localScript;
    ModuleScript moduleScript;
    Script script;
  }
}
```

#### LocalScript
Data specific to instance with the LocalScript type
```
{
  // Value of LocalScript.Source in engine
  optional string source;
}
```

#### ModuleScript
Data specific to instance with the ModuleScript type
```
{
  // Value of ModuleScript.Source in engine
  optional string source;
}
```

#### Script
Data specific to instance with the Script type
```
{
  // Value of Script.Source in engine
  optional string source;
}
```
