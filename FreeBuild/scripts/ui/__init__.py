print "Importing %s..."%(__name__),
import os.path
from main import determine_package
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
__all__=determine_package(dir_path)

def configure_ui(width,height):
	print "Executing configure_ui(%d,%d)" % (width,height)
	from _rocketcore import CreateContext, Vector2i
	import Drivers
	driver = Drivers.getMainDriver()
	if driver == None or width <= 0 or height <= 0:
		ret = False
	else:
		driver.uiHandle = CreateContext("primary_ui_context",Vector2i(width,height))
		print " Importing standard keymap...",
		from scripts.prefs.keymaps import getKeyMap
		Drivers.clearKeyMap()
		for g,r in getKeyMap().iteritems():
			Drivers.mapKey(g,r)
		import main_menu
		main_menu.init(driver.uiHandle)
		print "Done"
		ret = True
	return ret


print "Success!"
print " Contains these submodules: %s"%(", ".join(__all__))