# a-z-animals.com-parser allows you to get all the facts about animals in a convenient csv file

## The following steps to use the script

1) Git clone the project, and run "pip install -r requirements.txt"
2) Run the script 

## How it works, and what it does?

Here we are using requests, and BeautifulSoup4 libraries to retrieve information from the website.
It goes as follows:
1) Getting HTML text for the page of animals
2) After getting the HTML, we extract the links of all animals presented on it.
3) We have functions to extract information of animal page (title, facts)
4) Also, we have function which creates prototype Dictionary[] for the names of all attributes of specified animal.
4) As the animal pages were generated using the same pattern, we can combine clauses "3" and "4" and save all animals in the list of Dictionaries, as we have access to animal pages through clause "2".
5) Then we use this list to save it into CSV file.

## Example(Following csv file in Excel):
![image](https://user-images.githubusercontent.com/91605867/228304548-7215fd17-df36-4ac8-874b-9448c0c6a986.png)




