#Script to list all the movies and export it to a text file
#here we can use the script to any kind of applications where we want to extract the names all the directories specified in the path
#here we have taken example of extracting the names of the movies in a specified path
import os,re
ret=os.listdir('f:\\collection\\movies\\English\\')#the parameter is the path from which the names of the movies is to be extracted
os.chdir('f:\\collection\\movies\\English\\')#this changes the current working directory to path which is passed as a paramter
for i in ret:
    path1=os.path.join(os.getcwd(),i)
        if os.path.isdir(path1):#checking if the folder is a directory,cause we only want the name of the directory and not the name of the files in it
        file=open("Movie list.txt",'a')#here movie list.txt can be any file to which the list of movie names is to be exported
        file.write(i)#writing to the file
        file.write('\n')

