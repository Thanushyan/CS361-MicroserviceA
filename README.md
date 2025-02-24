# CS361-MicroserviceA

This is the microservice I have created for my groupmate. 
To use this microservice, have funFact.py running and through your web application program, write to a text file called Food.txt with the word "run".
For the test program I have implemented request.py that does just that by writing the word "run" to the Food.txt file. 

The funFact.py will generate a random number once it reads the word "run" from Food.txt and ensures that there will be no duplicate random numbers for every 100 requests.
For example, if the user requests a fun fact 106 times, only 6 random numbers are used twice. This will ensure that all 100 numbers are given before repeating any prior generated numbers.
Before the funFact.py writes to the file with the number, it will go back to the beginning of the text file and write the number, then truncate to cut off the rest of what was there.
This gets rid of the "run" in the text file and allows for the program to handle as many requests the user makes.

Things you will need to do to adapt this to work with your project, write to the text file similarly to how request.py does with the word "run". Remember that the number in the text file is written as a string as well.

