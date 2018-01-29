import os,re

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
	filename = rem_brackets(filename)
	filename = rem_digit(filename)
	filename = rem_spchr(filename)
	if filename == "":
		filename = oldname
	filename = filename.capitalize()
	try:
		os.rename(oldname, filename)
	except FileExistsError:
		print("[error]file already exist : ",oldname)
	except:
		print("Can't able to remane file : ",oldname)
		
		

