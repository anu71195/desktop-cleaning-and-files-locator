import os

##10 largest files codes...... 
#upgraes---- generalize it to  n....... upgrade to also take smallest...... take the range....-----------------------note
largest_file_command='cd && sudo find . -type f -printf "%s\t%p\n" | sort -n | tail -10'
n_largest_files=os.popen(largest_file_command).read();


def escape_string(input_string,e_str): #input_string is the string where escape of characters to be done and e_str is the character or string to be escaped
	input_string=input_string.split(e_str);
	e_str="\\"+e_str
	return e_str.join(input_string)

def find_dir_files(ls):#find all the files and directories separately 
	directories=[];
	files=[];
	for fod in ls: #fod =files or directories
		if(os.path.isdir(fod)):
			directories.append(fod);
		else:
			files.append(fod)
	return directories , files;


#change afterwards Downloads to Desktop---------------------- note
#
Desktop_location=escape_string(os.popen("cd && cd Downloads && pwd").read()," ");
os.chdir(Desktop_location[0:-1])#by default os.popen return string ending with \n to remove \n 0:-1 is taken
directories,files=find_dir_files((os.popen("ls -X").read())[0:-1].split("\n"));#list all the files and directories by their type



