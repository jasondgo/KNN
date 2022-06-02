from datapoint import DataPoint

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
       
  
   def convertContents(self):
       
       dataHolder = [];
       for line in self.holder:
           lineList = line.strip().split(",");
           print(lineList);
           dataHolder.append( DataPoint( float(lineList[0]), float(lineList[1]), float(lineList[2]), float(lineList[3]), lineList[4] ));  
           
       return dataHolder;