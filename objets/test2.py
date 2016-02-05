#-*- coding: utf-8 -*-

from librairie import *


table= Table("mindpasstest_laposte")
table.addMail(["12","un_autre","chocolaté","content","152124"])
print(table.getId())
table.saveAndClose()