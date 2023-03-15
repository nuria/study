#!/usr/local/bin

"""
input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
"""


def flatten_dictionary(dictionary):
    # set of key/value pairs
    acumu = {}
  
    def flatten_value(key, item, acumu):
        # base case is item is a primitive type
        if isinstance(item,int) or isinstance(item,str):
            acumu[key] = item
            return    

        for k in item.keys():
            # we need to flatten each of the keys 
            if key== "":
                prefix =''
            else:
                prefix = key +"."

            compound_key = prefix + k
            value = item[k]
            if value!="":
                flatten_value(compound_key, value,acumu)
          


    flatten_value('', dictionary, acumu)
  
    print  acumu

if __name__=="__main__":
    dictionary = {
                "Key1" : "1",
                "Key2" : {
                        "a" : "2",
                        "b" : "3",
                        "c" : {
                        "d" : "3",
                        "e" : {
                        "" : "1"
                        }
                    }
                }
    }
    flatten_dictionary(dictionary)

