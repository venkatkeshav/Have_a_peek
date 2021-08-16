# Have_a_peek
To run the above code you need to first meet the requirements mentioned in requirements.txt
Just to let u know before hand this code here parses and crawls the final links of all topics from the website "Learnawesome.org" and u can use these kinds of tricks for other websites as well.
after downloading the code unzip it to a location u prefer.
open command propmt of that file location
now move to test1 directory using "cd test1" command in the command prompt.
now enter the following command to parse and retreive all the final links of Learnawesome.org website:
scrapy crawl topic
here topic is the name of our spider and worry not this will take some time to retreive all the links.
to retreive all the links and to store in a csv file or other, use the below line.
scrapy crawl topic -o file_name.csv
This will create a csv file where all the links their names and topics they are related to are present.
