cd
sudo find . -type f -printf "%s\t%p\n" | sort -n | tail -10 > text
cd ~/Downloads
