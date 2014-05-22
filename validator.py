import urllib 
import time 
  
student_id = raw_input("Student ID: ") 
page = urllib.urlopen("http://rtgkom.dk/~" + student_id) 
source = page.readlines() 
source = str(source) 
  
#Check if page has "the requested url could not be found", if yes, terminate program 
if source.find("<p>The requested URL /~" + student_id + " was not found on this server.</p>") == -1: 
    print("Code parsed") 
    time.sleep(0.5) 
    print("Validating source code") 
    validated = urllib.urlopen("http://validator.w3.org/check?uri=http://rtgkom.dk/~" + student_id) 
    validated_source = validated.readlines() 
    validated_source = str(validated_source) 
    print("Code validated") 
    if validated_source.find("[Invalid]") == -1: 
        print("Source code for " + student_id + " was valid!") 
    elif validated_source.find("[Valid]") == -1: 
        print("Source code for " + student_id + " was invalid!") 
else: 
    print("Code not found!") 
    time.sleep(.5) 
    print("Terminating script") 
