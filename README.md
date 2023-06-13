# nipolib-python
Nipo library for python


## sample

```python
import nipo 

#Create initial config 
nipo.create_config("TOKEN", "IP", PORT)

#call ping function 
#result must be Pong 
nipo.ping()

#set key and value in database 
nipo.set("KEY" , "VALUE")

#get value of specefic key 
nipo.get("KEY")

```
