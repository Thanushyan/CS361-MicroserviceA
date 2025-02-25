# CS361-MicroserviceA

This is the microservice I have created for my groupmate. 
To use this microservice, have funFact.py running and through your web application program, write to a text file called Food.txt with the word "run".
For the test program I have implemented request.py that does just that by writing the word "run" to the Food.txt file. 

<img width="358" alt="image" src="https://github.com/user-attachments/assets/c19cf4c0-df02-4ba9-8831-f5cc68f206fa" />

The funFact.py will generate a random number once it reads the word "run" from Food.txt and ensures that there will be no duplicate random numbers for every 100 requests.
For example, if the user requests a fun fact 106 times, only 6 random numbers are used twice. This will ensure that all 100 numbers are given before repeating any prior generated numbers.
When the funFact.py writes to the text file, it will replace the "run written in it with the pseudo-random number.
This allows for the program to handle as many requests the user makes.

<img width="353" alt="image" src="https://github.com/user-attachments/assets/bbf14dc7-c803-4c1c-bfdd-7d3d35839ca7" />


Things you will need to do to adapt this to work with your project, write to the text file similarly to how request.py does with the word "run" when you want to receive a random number. Note that the number in the text file is written as a string as well.

UML DIAGRAM:

![Screenshot 2025-02-24 193930](https://github.com/user-attachments/assets/5073b72c-8b90-49a4-a5cd-52a4df84c4bb)


