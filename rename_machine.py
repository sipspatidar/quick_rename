#Author : Sips
#Date : 28/01/2018

import os,re
import argparse

def get_title(filename):
	try:
		song = taglib.File(filename)
		newname = str(song.tags["TITLE"][0])+".mp3"
	except:
		print("cant read")
		newname = filename
	finally:
		song.close()
	return newname

def rem_brackets(filename):
	filename = re.sub(r'^(\[?\D*\]\s*)', "", filename)
	filename = re.sub(r'^(\[?\D*\]\s*)', "", filename)
	return filename

def rem_digit(filename):
	filename = re.sub(r'^\d*\s*', "", filename)
	return filename

def rem_spchr(filename):
	filename = re.sub(r'^\W*\s*', "", filename)
	return filename

def ren(oldname,filename):
	if filename == "":
		filename = oldname
	filename = filename.capitalize()
	try:
		os.rename(oldname, filename)
	except FileExistsError:
		print("[error]file already exist : ",oldname)
	except:
		print("Can't able to remane file : ",oldname)

def Main():
	parser =  argparse.ArgumentParser()
	parser.add_argument("path",help="The path of directory where the files are exists",type=str)
	parser.add_argument("-b","--brackets",help="To remove brackets from starting of filename",action="store_true")
	parser.add_argument("-d","--digits",help="To remove digits from starting of filename",action="store_true")
	parser.add_argument("-s","--spchr",help="To remove special character from starting of filename",action="store_true")
	args = parser.parse_args()
	os.chdir(args.path)
	filenames = os.listdir(args.path)
	if not any([args.brackets,args.digits,args.spchr]):
		for filename in filenames:
			oldname = filename
			filename = get_title(filename)
			filename = rem_brackets(filename)
			filename = rem_digit(filename)
			filename = rem_spchr(filename)
			ren(oldname,filename)
	if args.brackets:
		for filename in filenames:
			oldname = filename
			filename = get_title(filename)
			filename = rem_brackets(filename)
			ren(oldname,filename)
	if args.digits:
		for filename in filenames:
			oldname = filename
			filename = get_title(filename)
			filename = rem_digit(filename)
			ren(oldname,filename)
	if args.spchr:
		for filename in filenames:
			oldname = filename
			filename = get_title(filename)
			filename = rem_spchr(filename)
			ren(oldname,filename)
	
if __name__ == "__main__":
	Main()
	
	
	
	
	
