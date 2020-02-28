# CS 1XA3 Project01 - <bandukwn>
## Usage
### Since this script is already executable, enter the file path "home/bandukwn/private/CS1XA3/Project01". After this, enter the command "./project_analyze.sh" to run the file.



## **Feature01**
Description: This feature lists all the files in your repository from largest to smallest file size.
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "1" when the program prompts for an input feature.
Reference: This code was written with some help from the lab TA. 

## **Feature02**
Description: This feature prompts the user to enter a file extension and then outputs the number of files in your repository which contain that extension.
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "2" when prompted to. 
Reference: Some help was taken from: [https://stackoverflow.com/questions/1447625/list-files-with-certain-extensions-with-ls-and-grep/1447974] 

## **Feature03**
Description: This feature prompts the user to enter any word and then creates a log file with that name if it does not already exist. It then looks at all python files in your repository that contain a "#" and puts them in the log file that was just created.
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "3" when prompted to.
Reference: Some help was taken from classmates and lab TAs.


###Custom feature 1
Description: This feature prompts the user to enter a file name and checks whether the file contains any "/" symbols. If it does, the program will give an error message as Unix systems cannot contain "/" in file names. 
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "4" when promted to.
Reference: Some help was taken from: [https://linuxize.com/post/how-to-check-if-string-contains-substring-in-bash/]

### Custom feature 2
Description: This feature prompts the user to enter a file and checks if the file contains certain characters. It then outputs the number of times the character was found in the file. 
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "5" when promted to.

## **Feature 04**
Description: This feature will find all shell files in the repo. It then creates a file to store original permissions of the file. If the user selects Change the program will give executable permissions to those who have write permissions. If the user selects Restore the program will restore the files to their original permissions.
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "6" when prompted to.
Reference: Some help was taken from the lab lecture slides and the TA's. 

## **Feature 05**
Description: If the user selects "Backup" then this feature will find all temporary files in the repo and move them to another directory called backup. It then stores their filepaths in another file called restore.log. If the user selects Restore, the code will look at the original filepaths stored in restore.log and store them back to their original location.
Execution: This feature can be executed by running "./project_analyze.sh" and entering the number "7" when promted to.
Reference: Help was taken from classmates and lab TA's.    
