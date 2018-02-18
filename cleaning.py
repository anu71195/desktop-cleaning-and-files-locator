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
	for dir_name in directories:
		move_directory_command="mv -v "+dir_name+" "+location+"/"
		counter=0;
		while(os.path.exists(remove_escape(location)+"/"+remove_escape(dir_name))):
			dir_name=dir_name+str(counter);
			counter+=1;
		move_directory_command=move_directory_command+dir_name	
		os.system(move_directory_command)

def find_extensions(files):
	extensions=[]
	for file_name in files:
		file_name=file_name.split('.');
		if(len(file_name)>1):
			extensions.append(file_name[-1])
		else:
			extensions.append("unknown_type")
	return extensions

def create_all_folders(extensions,source,Documents_location):
	os.chdir(Documents_location)
	for extension_name in extensions:
		os.system("mkdir "+extension_name)
	os.chdir(source)

def move_files(files,source,location):
	os.chdir(source)
	for file_name in files:
		if(len(file_name.split('.')[-1])>1):
			move_file_command="mv -v "+file_name+" "+location+"/"+file_name.split('.')[-1]+"/"
			file_finaladdress=(remove_escape(location))+"/"+remove_escape(file_name.split('.')[-1])+"/"

		else:
			move_file_command="mv -v "+file_name+" "+location+"/"+"unknown_type"+"/"
			file_finaladdress=(remove_escape(location))+"/"+"unknown_type/"
		counter=0;
		while(os.path.exists(file_finaladdress+remove_escape(file_name.split('.')[0])+str(counter)+"."+remove_escape(file_name.split('.')[1]))):
			counter+=1;
		move_file_command+=file_name.split('.')[0]+str(counter)+"."+file_name.split('.')[1]

		print(move_file_command)
		os.system(move_file_command)



size_type_input=input("give input for whether the requirement is for 'largest' files or 'smallest' files\n>");
file_names=required_ranged_file(size_type_input[0]);#required output
print("Required files are as follows:-\n")
print(file_names)#printing the result for the n largest of n smallest files






#change afterwards Downloads to Desktop---------------------- note#
Desktop_location=escape_string(os.popen("cd && cd Desktop && pwd").read()[0:-1]," ");#by default os.popen return string ending with \n to remove \n 0:-1 is taken and spaces are escaped in it
Documents_location=escape_string(os.popen("cd && cd Documents && pwd").read()[0:-1]," ");
current_location=escape_string(os.popen("pwd").read()[0:-1]," ");
#error handling if there is no Desktop Directory
try :
	os.chdir(Desktop_location)
except:
	print("error no desktop found");
	exit();

#if Documents directory is not present then create it
if(os.path.isdir(Documents_location)!=True):
	print("Creating Documents Directory")
	make_doc_directory_command="cd && mkdir Documents"
	os.system(make_doc_directory_command)

directories,files=find_dir_files((os.popen("ls -X").read())[0:-1].split("\n"));#list all the files and directories by their type then differentiate between files and directories

move_directories(directories,Desktop_location,Documents_location);
extensions=find_extensions(files);
create_all_folders(extensions,Desktop_location,Documents_location)
move_files(files,Desktop_location,Documents_location)




