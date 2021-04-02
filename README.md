# nipolib-python
Nipo library for python


## sample

import nipo 
#Create initial config 
nipo.CreateConfig("061b30a7-1a12-4280-8e3c-6bc9a19b1683", "0.0.0.0", 2323)

# call ping function 
# result must be Pong 
nipo.Ping()

#set key and value in database 
nipo.Set("key" , "value")

# get value of specefic key 
nipo.Get("key")

