'''
class IdentityService:
    def register(username: str, password: str, properties: Dict[str, Any]):
        pass 
    def authenticate(username: str, password: str) -> bool:
        pass 
    def save_to_json(path: str, overwrite: bool = false):
        pass
'''

import json
from os import path


class IdentityService:
    def register(Username=str, Password=str):
                
        db = open("database.txt", "a")
        db.write(Username+", "+Password+"\n")

    def authenticate(Username=str, Password=str):
        if not len(Username or Password) < 1:

            if True:
                db = open("database.txt","r")
                d = []
                f = []
                for i in db:
                    a,b = i.split(",")
                    b = b.strip()
                    c = a,b
                    d.append(a)
                    f.append(b)
                data = dict(zip(d,f))

                try:
                    if data[Username]:
                        try:
                            if Password == data[Username]:
                                return True
                            else:
                                return False
                        except:
                            return False
                    else:
                        return False

                except:
                    return False
            else:
                return False
        else:
            return False            


    def save_to_json(path=str):
        # the file to be converted
        filename = 'database.txt'
        # resultant dictionary
        dict1 = {}
        # fields in the sample file 
        fields =['username', 'password']
  
        with open(filename) as fh:
            l = 1
            for line in fh:
          
                # reading line by line from the text file
                description = list( line.strip().split(None, 4))
          
                # for output see below
                print(description) 
          
                # for automatic creation of id for each employee
                sno ='user'+str(l)
      
                # loop variable
                i = 0
                # intermediate dictionary
                dict2 = {}
                while i<len(fields):
              
                    # creating dictionary for each employee
                    dict2[fields[i]]= description[i]
                    i = i + 1
                  
                # appending the record of each employee to
                # the main dictionary
                dict1[sno]= dict2
                l = l + 1



        # path = 'C:\\Users\\sneha\\datamole\\test3.json'
        out_file = open(path, "w")
        json.dump(dict1, out_file, indent = 4)
        out_file.close()

# IdentityService.register('sneha7','thakur7')

# print(IdentityService.authenticate('sneha7','thakur7'))

# IdentityService.save_to_json('C:\\Users\\sneha\\datamole\\test3.json')

			
# print(IdentityService.authenticate('sneha','thakur'))
        
