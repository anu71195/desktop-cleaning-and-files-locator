import os

##10 largest files codes...... 
#upgraes---- generalize it to  n....... upgrade to also take smallest...... take the range....
largest_file_command='cd && sudo find . -type f -printf "%s\t%p\n" | sort -n | tail -10'
n_largest_files=os.popen(largest_file_command).read();

Desktop_location=os.popen("cd && cd Downloads").read();
