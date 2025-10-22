String[] loadFromFile(){
  String[] rawResultArray, resultArray;
  rawResultArray = loadStrings("data.txt"); // loads in ALL data from the text file

  /* Data structure (for reference)
  {"uniqueId": 28922, "logo": "https://bookface-images.s3.amazonaws.com/small_logos/392ff7d64717e95c1b8ca23af91934ffec643fbf.png", "description": "Automated revenue cycle management, starting with dentists", "industry": "Healthcare", "batch": "Winter 2025"} */
  for( String dataPoint : rawResultArray ){
    // Clean datapoint from {}
    dataPoint = dataPoint.replace("{","");
    dataPoint = dataPoint.replace("}","");




  } 

  return resultArray;
}

// load file from sketch/data/data.txt


void setup(){
  pixelDensity(1);
  size(400,400);
  println("Hello world!");
}
