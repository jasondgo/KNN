import datapoint

class FileRead:
    
   
   def __init__(self, path):
       self.path = path;
       self.holder = [];


   def getFileContents(self):
       file = open(self.path,"r");

       for line in file:
           self.holder.append(line);
           print(line);

       file.close();
       