import os,re
import taglib

path = input("Enter the path : ")
os.chdir(path)
filenames = os.listdir(path)


def rem_brackets(filename):
	filename = re.sub(r'^(\[\D*\]\s*)', "", filename)
	filename = re.sub(r'^(\[\D*\]\s*)', "", filename)
	return filename

def rem_digit(filename):
	filename = re.sub(r'^\d*\s*', "", filename)
	return filename

def rem_spchr(filename):
	filename = re.sub(r'^\W*\s*', "", filename)
	return filename


for filename in filenames:
	oldname = filename
	try:
		song = taglib.File(filename)
		newname = str(song.tags["TITLE"][0])+".mp3"
	except:
		print("cant read")
		newname = filename
	finally:
		song.close()
	
	
	newname = rem_brackets(newname)
	newname = rem_digit(newname)
	newname = rem_spchr(newname)
	if newname == "":
		newname = oldname
	newname = newname.capitalize()
	try:
		os.rename(oldname, newname)
	except FileExistsError:
		print("[error]file already exist : ",oldname)
		os.rename(oldname, newname+'[1]')
	except:
		print("Can't able to remane file : ",oldname)
		
		

