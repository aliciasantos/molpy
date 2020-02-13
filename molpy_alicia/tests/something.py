#Add imports here
from .molpy import *
from . import util
+from . import data

#Handle versioneer
from ._verion import get_versions
diff --git a/molpy/data/__init__.py b/molpy/data/__init__.py
new file mode 100644
index 0000000..9c4fb56
--- /dev/null
+++ b/molpy/data/reader.py
@@ -0,0 +1,8 @@
+import os
+
+dirname = os.path.dirname(os.path.abspath(__file__))
+filename = os.path.join(dirname, "look_and_say.dat")
+
+with open(filename,"r") as handle:
+   look_and_say=handle.read()

#from .reader import look_and_say
