import math

class kNearestNeighbor:

   
    def __init__(self, dataPointHolder):
        
        self.dataPointHolder = dataPointHolder;
        

    


    def calculate(self,testValue, trainingSet):
        
        distanceList = [];
        nameList = [];
        for i in range(149):
            distanceList.append( math.sqrt( (testValue.slPosition - trainingSet[i].slPosition)**2 + (testValue.swPosition - trainingSet[i].swPosition)**2 + (testValue.plPosition - trainingSet[i].plPosition)**2 + (testValue.pwPosition - trainingSet[i].pwPosition)**2));
            nameList.append(trainingSet[i].flowerActual);
            
        return self.sort(distanceList, nameList);
        
         
    

    def sort(self,distanceList, nameList):

        for i in range( len(distanceList)):
            for j in range( len(distanceList) - 1):
                if distanceList[j] > distanceList[j+1]:
                    holder = distanceList[j];
                    distanceList[j] = distanceList[j+1];
                    distanceList[j+1] = holder; 
                    holder = nameList[j];
                    nameList[j] = nameList[j+1];
                    nameList[j+1] = holder;

        return nameList;
        



    def kNN(self):
        
       correctGuess = 0;
       wrongGuess = 0;

       for i in range(150):

            testValue = self.dataPointHolder[i];
            trainingSet = self.dataPointHolder[0:i] + self.dataPointHolder[i+1:];
            flowerType = { "setosa" : 0,
                           "versicolor" : 0,
                           "virginica" : 0 };
           
             
            sortedList = self.calculate(testValue,trainingSet);
          

            for k in range(5): 
                 
                
                if sortedList[k].lower() == "iris-setosa":
                    flowerType["setosa"] = flowerType["setosa"] + 1;

                elif sortedList[k].lower() == "iris-versicolor":
                    flowerType["versicolor"] = flowerType["versicolor"] + 1;

                else:
                    flowerType["virginica"] = flowerType["virginica"] + 1;

            
            if flowerType["setosa"] > flowerType["versicolor"] and flowerType["setosa"] > flowerType["virginica"]:
                  if "iris-setosa" == testValue.flowerActual.lower():
                      correctGuess = correctGuess + 1;
                  else: 
                      wrongGuess = wrongGuess + 1;

            elif flowerType["versicolor"] > flowerType["setosa"] and flowerType["versicolor"] > flowerType["virginica"]:
                  if "iris-versicolor" == testValue.flowerActual.lower():
                      correctGuess = correctGuess + 1;
                  else:
                      wrongGuess = wrongGuess + 1;

            else:
                  if "iris-virginica" == testValue.flowerActual.lower():
                      correctGuess = correctGuess + 1;
                  else: 
                      wrongGuess = wrongGuess + 1;


       print("Percentage of correctly guessed", correctGuess/(correctGuess + wrongGuess));

                 

              
            
                
                
             
        
  
        


     
     

    
        


     

        
             
            
     
        

    