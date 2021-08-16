# Have_a_peek
To run the above code you need to first meet the requirements mentioned in requirements.txt i.e.basically you need to install scrapy module for this project to work.

Just to let u know before hand this code here parses and crawls the final links of all topics from the website "Learnawesome.org" and u can use these kinds of tricks for other websites as well.

After downloading the code unzip it to a location u prefer.
Open command propmt of that file location
Now move inside test1 directory using "cd test1" command in the command prompt.
Now enter the following command to parse and retreive all the final links of Learnawesome.org website:

scrapy crawl topic

Here topic is the name of our spider and worry not this will take some time to retreive all the links.
To retreive all the links and to store in a csv file or other, use the below line.

scrapy crawl topic -o file_name.csv

This will create a csv file where all the links their names and topics they are related to are present.
