print "Importing %s..."%(__name__),
import os.path
from main import determine_package
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
__all__=determine_package(dir_path)


# We want to make it so that we only have to
# import prefs.keymaps to get the right keymap

print "Success!"
print " Contains these submodules: %s"%(", ".join(__all__))