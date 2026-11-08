
import time
import spacy 
import urllib.request

nlp = spacy.load("en_core_web_md")
nlp.max_length = 2000000  # Increase the maximum length to handle larger documents


ruler = nlp.add_pipe("entity_ruler", before="ner")
# adding capital cities and organization patterns to the entity ruler
patterns = [{"label": "CAPITAL_CITY", "pattern": [{"LOWER":"paris"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"tokyo"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"rabat"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"london"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"washington"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"berlin"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"madrid"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"rome"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"beijing"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"moscow"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"ottawa"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"canberra"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"new"}, {"LOWER":"delhi"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"brasilia"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"cairo"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"abuja"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"nairobi"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"jakarta"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"bangkok"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"seoul"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"riyadh"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"tehran"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"baghdad"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"kabul"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"islamabad"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"athens"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"oslo"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"stockholm"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"helsinki"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"copenhagen"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"vienna"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"brussels"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"lisbon"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"dublin"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"warsaw"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"prague"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"budapest"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"belgrade"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"zagreb"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"ljubljana"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"sarajevo"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"skopje"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"podgorica"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"tirana"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"algiers"}]},
            {"label": "CAPITAL_CITY", "pattern": [{"LOWER":"tunis"}]},
            {"label": "ORG", "pattern": "OpenAI"},
            {"label": "ORG", "pattern": "Google"},
            {"label": "ORG", "pattern": "Microsoft"},
            {"label": "ORG", "pattern": "Apple"},
            {"label": "ORG", "pattern": "Amazon"},
            {"label": "ORG", "pattern": "Facebook"},
            {"label": "ORG", "pattern": "Twitter"},
            {"label": "ORG", "pattern": "Tesla"},
            {"label": "ORG", "pattern": "SpaceX"},
            {"label": "ORG", "pattern": "IBM"},
            {"label": "ORG", "pattern": "Intel"}]

ruler.add_patterns(patterns)

while True:
   

  print("\n" + "=" * 50)
  print("       NLP TEXT ANALYSIS TOOL       ")
  print("=" * 50)

  options= input("choose an option:\n file or web or exit \n").strip().lower()

  if options == "exit":
      print ("Exiting the program.")
      time.sleep(1)
      break      

  doc = None

  try:
    if options == "file":
     
     file_path= input("Enter the path of the text file (Ex: C:\\path\\to\\file.txt) :").strip().strip("'")
     print ("Loading file...")
     time.sleep(0.5)
     with open(file_path, "r", encoding = "utf-8" ) as file:
       doc = nlp(file.read())
   

    elif options == "web":
     import ssl
     from bs4 import BeautifulSoup

     url= input("Enter the link:").strip()
     print ("Fetching and processing the web page...")
     time.sleep(0.5)

     req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

     ssl_context = ssl._create_unverified_context()
   

     with urllib.request.urlopen(req, context=ssl_context) as response:
      
      
      html_content= response.read().decode("utf-8")
      soup = BeautifulSoup(html_content, "html.parser")
      for script in soup(["script", "style"]):
        script.decompose()
      clean_text = soup.get_text(separator = " ") 
      doc = nlp(clean_text)

    else:
         print("invalid option. Please choose either 'file' or 'web' or 'exit'.") 
         exit()
  except FileNotFoundError:
    print("File not found. Please check the file path.")
    continue
  except Exception as e:
   print(f"An error occurred: {e}")
   continue

  from spacy import displacy

  Diagram = input ("Do you want to visualize the diagram of the text ? (y/n)").lower().strip()

  if Diagram == "y":
   print("Copy the link in your browser to view the diagram. Press Ctrl+C to stop the visualization.")
   print ("Visualising the content...")
   time.sleep(1.5)
   try:
    displacy.serve(doc, style="dep", options = {"distance":220, "word_spacing":60},port=5001)
   except KeyboardInterrupt:
       print("Diagram visualization stopped.")
  else:
   print("Diagram visualization skipped.")



  options_2= input ("choose an option:\n labels or pos \n").strip().lower()

  if options_2 == "labels":
    print("Loading...")
    time.sleep(0.5)

    for token in doc.ents:
     
     print(f"TEXT: {token.text}, LABEL: {token.label_}")

  elif  options_2 == "pos":
   print("Loading...")
   time.sleep(0.5)

   for token in doc:
    print(f"TEXT: {token.text}, POS: {token.pos_}")

  options_3 = input ("choose an option: Do you want to check similarity? (y/n): ").strip().lower()

  if options_3 == "y":
   check= input ("Enter the word you want to check the similarity with the text:").strip().lower()
   check_token = nlp(check)
   if not check_token.has_vector:
       print(f"The word '{check}' does not have a vector representation in the model.") 
   else:
    print("Checking in process...")
    time.sleep(1)
    for token in doc:
     if token.is_punct or token.text.lower() == check:
            continue
     similarity = token.similarity(check_token)
     if similarity > 0.49:
        
        print(f"{token.text} is similar to {check} with a similarity score of {similarity:.2f}")

  Exiting = input("Do you want to exit the program? (y/n):").strip().lower()
  if Exiting == "y":
    print ("Exiting the program.")
    time.sleep(1)
    break
  else:
   print("Continuing the program...")
   time.sleep(1)
   continue






