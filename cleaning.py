import os

##n largest and smallest code
def required_ranged_file(input_type):
	if(input_type=='s' or input_type=='S'):#n smallest
		n=int(input("give n for which n smallest files will be generated\n>"));
		command='cd && sudo find . -type f -printf "%s\t%p\n" | sort -n | head -'+str(n)

	elif(input_type=='l' or input_type=='L'):#n largest
		n=int(input("give n for which n largest files will be generated\n>"));
		command='cd && sudo find . -type f -printf "%s\t%p\n" | sort -n | tail -'+str(n)
	else:
		print("Invalid input\nType smallest or the largest");#wrong input
		return required_ranged_file(input("give input for whether the requirement is for 'largest' files or 'smallest' files\n>")[0])	
	return os.popen(command).read();#required output


def escape_string(input_string,e_str): #input_string is the string where escape of characters to be done and e_str is the character or string to be escaped
	input_string=input_string.split(e_str);
	e_str="\\"+e_str
	return e_str.join(input_string)
def remove_escape(input_string):
	input_string=input_string.split("\\")
	return "".join(input_string)


def find_dir_files(ls):#find all the files and directories separately 
	directories=[];
	files=[];
	for fod in ls: #fod =files or directories
		escaped_fod=escape_string(escape_string(escape_string(fod," "),"("),")");
		if(os.path.isdir(fod)):
			directories.append(escaped_fod);
		else:
			files.append(escaped_fod)
	return directories , files;

def move_directories(directories,source,location):#move directories to the folder named directories in the desired location
	os.chdir(location);
	location=location+"/directories"#location updated to the directory where directories from desktop are to be moved
	if os.path.exists(location):
		pass;
	else :
		os.system("mkdir directories")
		print("directories directory created")
	os.chdir(source)
	for dir_name in directories:#creating commands to move the directory from desktop to documents
		move_directory_command="mv -v "+dir_name+" "+location+"/"#verbose move
		counter=0;#counter to name the duplicate files

		if(os.path.exists(remove_escape(location)+"/"+remove_escape(dir_name))):
			while(os.path.exists(remove_escape(location)+"/"+remove_escape(dir_name+str(counter)))):#handling the duplicate file names by numbering them
				counter+=1;
			dir_name=dir_name+str(counter);	
		move_directory_command=move_directory_command+dir_name	
		os.system(move_directory_command)#implementing those commands

def find_extensions(files):#finding all the extensions
	extensions=[]
	for file_name in files:
		file_name=file_name.split('.');
		if(len(file_name)>1):
			extensions.append(file_name[-1])
		else:
			extensions.append("unknown_type")
	return extensions

def create_all_folders(extensions,source,Documents_location):#creating folders for all the extensions
	os.chdir(Documents_location)
	for extension_name in extensions:
		os.system("mkdir "+extension_name)
	os.chdir(source)

def move_files(files,source,location):#moving all the files corresponding to their extensions
	os.chdir(source)
	for file_name in files:
		if(len(file_name.split('.'))>1):#checking whether the file has extension or not... this statement tells it has 
			move_file_command="mv -v "+file_name+" "+location+"/"+file_name.split('.')[-1]+"/"
			file_finaladdress=(remove_escape(location))+"/"+remove_escape(file_name.split('.')[-1])+"/"
		else:
			move_file_command="mv -v "+file_name+" "+location+"/"+"unknown_type"+"/"
			file_finaladdress=(remove_escape(location))+"/"+"unknown_type/"
			file_name=file_name+".unknown_type"
		counter=0;
		if(os.path.exists(file_finaladdress+remove_escape(file_name.split('.')[0])+"."+remove_escape(file_name.split('.')[1]))):
			while(os.path.exists(file_finaladdress+remove_escape(file_name.split('.')[0])+str(counter)+"."+remove_escape(file_name.split('.')[1]))):
				counter+=1;
			move_file_command+=file_name.split('.')[0]+str(counter);#file command creation to move a single file in case of duplicatoin
		elif(os.path.exists(file_finaladdress+remove_escape(file_name.split('.')[0])) and file_name.split('.')[1]=="unknown_type"):
			while(os.path.exists(file_finaladdress+remove_escape(file_name.split('.')[0])+str(counter))):
				counter+=1;
			move_file_command+=file_name.split('.')[0]+str(counter);#file command creation to move a single file in case of duplicatoin
		else:
			move_file_command+=file_name.split('.')[0]#file command creation to move a single filein case of no duplication
		if file_name.split('.')[1]!="unknown_type":
				move_file_command+="."+file_name.split('.')[1]
		os.system(move_file_command)#moving file



size_type_input=input("give input for whether the requirement is for 'largest' files or 'smallest' files\n>");
file_names=required_ranged_file(size_type_input[0]);#required output

#error handling if there is no Desktop directory
try:
	Desktop_location=escape_string(os.popen("cd && cd Desktop && pwd").read()[0:-1]," ");#by default os.popen return string ending with \n to remove \n 0:-1 is taken and spaces as well as parenthesis are escaped in it
except:
	print("Error - Desktop is not found in the operating system")
	print("Exiting...")
	exit();

#error handling if docments directory is not present then create it
try:
	os.system("cd && mkdir Documents")
	Documents_location=escape_string(os.popen("cd && cd Documents && pwd").read()[0:-1]," ");
	print("Done")
except:
	print("Documents folder not found")
	print("Creating Documents folder in home directory")
	os.system("cd && mkdir Documents")
	Documents_location=escape_string(os.popen("cd && cd Documents && pwd").read()[0:-1]," ");

current_location=escape_string(os.popen("pwd").read()[0:-1]," ");
os.chdir(Desktop_location)
print("Finding all the files and folders....",end='\r');
print("                                                    ",end='\r')
print("Dividing them into files and folders...",end='\r')
print("                                                    ",end='\r')
directories,files=find_dir_files((os.popen("ls -X").read())[0:-1].split("\n"));#list all the files and directories by their type then differentiate between files and directories
print("                                                    ",end='\r')
print("Finding all the extensions...",end='\r')
print("                                                    ",end='\r')
extensions=find_extensions(files);
print("Creating folders for all the extensions...",end='\b')
print("                                                    ",end='\r')
create_all_folders(extensions,Desktop_location,Documents_location)
os.system("clear")
print("Required files are as follows:-\n")
print(file_names)#printing the result for the n largest of n smallest files
print()
print("Moving directories....",end='\r')
print()
move_directories(directories,Desktop_location,Documents_location);#moves all directories from home to Directories directory in Documents
print()
print("Moving all the files",end='\b')
print()
move_files(files,Desktop_location,Documents_location)





