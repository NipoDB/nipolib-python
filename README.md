# nipolib-python
Nipo library for python


## sample

```python
import nipo 

#Create initial config 
nipo.CreateConfig("TOKEN", "IP", PORT)

#call ping function 
#result must be Pong 
nipo.Ping()

#set key and value in database 
nipo.Set("KEY" , "VALUE")

#get value of specefic key 
nipo.Get("KEY")

```
