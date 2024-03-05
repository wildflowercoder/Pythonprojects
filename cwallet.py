import pyfiglet
from block_io import BlockIo
version = 2 #API version
block_io = BlockIo('5cbc-42b0-7fe9-e590', '', version  )



ascii_banner = pyfiglet.figlet_format("HELLO")
print (ascii_banner)