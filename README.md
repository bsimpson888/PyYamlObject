# PyYamlObject
Object based representation of a YAML file

# Basic usage:

imagine you got an yaml file with following content:

database:
    host: localhost
    user: dba
    passwd: secret
    dblist:
        - users
        - emails
        


```python
import YamlObject

obj = YamlObject.load("test.yaml")
dblist = obj.database.dblist
```



