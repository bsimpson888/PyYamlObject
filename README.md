# PyYamlObject
Object based representation of a YAML file

# Basic usage:

imagine you got an yaml file with following content:

```yaml
database:
    host: localhost
    user: dba
    passwd: secret
    dblist:
        - users
        - emails
``` 

Accessing the dblist would look like this:

```python
import YamlObject

obj = YamlObject.load("test.yaml")
dblist = obj.database.dblist
```



