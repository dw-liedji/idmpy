import subprocess

# import idm from the idm system location
idm = "C:\\Program Files (x86)\\Internet Download Manager\\IDman.exe"

# location for saving the downloaded files
local_path = "D:\\programming\\android\\ecommerce"

# This is the link of file we want to download
link = "http://www.wordtolatex.com/file/word-to-latex-2.56.zip"

# start downloading....
subprocess.call([idm, '/d', link, '/p', local_path])

# Have fun !
