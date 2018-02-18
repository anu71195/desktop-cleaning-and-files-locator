import os

##10 largest files codes...... 
#upgraes---- generalize it to  n....... upgrade to also take smallest...... take the range....-----------------------note
largest_file_command='cd && sudo find . -type f -printf "%s\t%p\n" | sort -n | tail -10'
n_largest_files=os.popen(largest_file_command).read();


def escape_string(input_string,e_str): #input_string is the string where escape of characters to be done and e_str is the character or string to be escaped
	input_string=input_string.split(e_str);
	e_str="\\"+e_str
	return e_str.join(input_string)
def remove_escape(input_string):
	print("string here")
	print(input_string)
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
		print("yes exist")
	else :
		os.system("mkdir directories")
		print("directories directory created")
	os.chdir(source)
	for dir_name in directories:
		print(dir_name)
		move_directory_command="mv -v "+dir_name+" "+location+"/"
		counter=0;
		print(location+"/"+dir_name)
		while(os.path.exists(remove_escape(location)+"/"+remove_escape(dir_name))):
			print("exist")
			dir_name=dir_name+str(counter);
			counter+=1;
		move_directory_command=move_directory_command+dir_name	
		print(move_directory_command)
		os.system(move_directory_command)






#change afterwards Downloads to Desktop---------------------- note#
Desktop_location=escape_string(os.popen("cd && cd Desktop && pwd").read()[0:-1]," ");#by default os.popen return string ending with \n to remove \n 0:-1 is taken and spaces are escaped in it
Documents_location=escape_string(os.popen("cd && cd Documents && pwd").read()[0:-1]," ");
current_location=escape_string(os.popen("pwd").read()[0:-1]," ");
	# print("here")
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

move_directories(directories,Desktop_location,Documents_location)




