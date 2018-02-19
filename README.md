# ABOUT:

Desktop cleaner and n largest and n smallest files locator.


# DEPENDENCIES: 

- python3 
- python3 os library



# INSTALLING DEPENDENCIES:

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```


# RUNNING THE CODE:
code can be run from linux terminal with command. The file can be run from any directory in linux.
```
$ python3 cleaning.py 
```
# FEATURES:
It takes input from the uesr whether the user wants n largest files or n smallest filein their pc and handles wrong input given by the user.<br />
Stores all the files in Documents directory in Home directory. If Documents directory is not present then creates it.<br />
Handles the escape character like white spaces and paranthesis in the path. Also handles removing of escape characters.<br />
Handles both folders in the Desktop and files in the folder separately.<br />
Find extensions for all the files and files without extensions are classified into unknown_type and create their respective folders along with a folder where all the directories from the Desktop will be moved.<br />
In directories as well as file both known extension and unknown extension, duplicate files and directories will be handled. They will be numbered ( say a duplicate file with a.txt then say t duplicate entries of it will be a0.txt a1.txt and so on and also with directories say it has directory name A with k duplicate directories so it will be numbered A0 A1 and so on)<br />

# AUTHOR:
	Anurag Ramteke
	CSE Undergraduate at IIT Guwahati

	