from fileread import FileRead

def main():
  print("This Worked");
  f = FileRead("iris.data");
  f.getFileContents();
  
  datapointHolder = f.convertContents();
  




if __name__ == "__main__":
  main();



