This is a project I am working on for fun at work in my spare time.
The purpose of this project is to automate and send out a text file to my coworkers and me that has the upcoming week's schedule.
There is a handful of us and it was hard to keep track of who is working what shift, so this project is providing that solution.

The project is using a very simple algorithm that grabs our names from a text file (list of people in order.txt), tosses them to a list, grabs the last person in the list and pops them to the top.
The script will then grab the shifts (from rotations.txt) and tosses them to a list as well. From there the script will merge everything together to a new list and writes it to a new file. 
The new file name is created by grabbing today's date and adding 3 days to it. This script is inteded to be ran on Friday's, so adding 3 days will get Monday's date. An example doc. currently in GitHub is "Schedule for the week of 14-06-2021.txt".
2 different files that are used for the rotation (list of people in order.txt and rotations.txt) makes this script dynamic to add/remove people to the rotations and add/adjust the rotation schedule order. 

Feel free to take a look to see what I am working on. Any open suggestions would be great! 
I do plan on cleaning on and remove any excess files currently used, but the main python file I am working on that is being used is performRotations.py.
test.py is being used to try out new things before making any changes or additions to performRotations.py. I do plan on making performRotations.py to be far more modular to keep things clean and dynamic. At the moment it is just one big ugly script.

Thank you for taking the time to read this document. Any questions let me know and I would be happy to answer.