# quick_rename
You can remove the unwanted and annoying stuff(brackets,webstites names,indexing digits,special characters) from the starting of the multiple songs filename(You can use it for otheer purpose also) in a single click.
This repository contain two files 
i)quick_rename.py
ii)rename_machine.py

Both perform the same operation but in the "quick rename.py" file you don't have the the options to perform seperate removing of brackets,digits and special characters.In the "rename_machine.py" file you can perform seperate operation using arguments.

# Steps to Use : (i) quick_rename.py

1)Run "quick_rename.py" file using the following command(you must have python instlled on your device) and hit enter
>>>python quick_rename.py

2)It ask for the folder name where the music files are store so just type or copy paste the folder path and hit enter
>>>Enter the path : E://my_music

3)Booommmm! All the brackets,webstites names,indexing digits,special characters from the starting of music filename removed.

youtube video link : https://youtu.be/gNXyUMWLYmM


# Steps to Use : (ii) rename_machine.py

This is argument based python script. You can use different options to perform seperate task.

usage: rename_machine.py [-h] [-b] [-d] [-s] path

positional arguments:
  path            The path of directory where the files are exists

optional arguments:
  -h, --help      show this help message and exit
  -b, --brackets  To remove brackets from starting of filename
  -d, --digits    To remove digits from starting of filename
  -s, --spchr     To remove special character from starting of filename


1)Run "rename_machine.py" file with the path of music folder using the following command(you must have python instlled on your device) and hit enter
>>>python rename_machine.py "E://my_music"
'or'
>>>python rename_machine.py -b "E://my_music"
'or'
>>>python rename_machine.py -d "E://my_music"
'or'
>>>python rename_machine.py -s "E://my_music"

2)Booommmm! All the brackets,webstites names,indexing digits,special characters from the starting of music filename removed.

youtube video link : https://youtu.be/yiN7pqfk3EI

Do you have any queries or want to add some more functionallity So feel free to contact me -

Facebook : https://www.facebook.com/sumit.patidar.77
Gmail : patidar.sumit1110@gmail.com

