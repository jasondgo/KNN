from fileread import FileRead
from KNN import kNearestNeighbor

def main():
  print("This Worked");
  f = FileRead("iris.data");
  f.getFileContents();
  
  datapointHolder = f.convertContents();
  k = kNearestNeighbor(datapointHolder);
  k.kNN();
  




if __name__ == "__main__":
  main();

 
        
