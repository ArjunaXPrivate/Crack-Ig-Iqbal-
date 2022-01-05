import os
h = ""
p = ""
try:

	os.system("git clone https://github.com/Dicky-XD/instadev")
	os.system("rm -rf instadev.py")
	os.system("cp -f instadev/instadev.py \\.")
	os.system("rm -rf instadev")
	os.system("chmod 777 *")
	print h+"\n Sukses Update Tool.."+p+">_<\n"
except:
	print "\n Perangkat Tidak Suport\n"