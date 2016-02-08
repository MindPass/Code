#-*- coding: utf-8 -*-

from librairie import *


table= Table("mindpasstest_laposte")
table.add_mail(["12","un_autre","chocolaté","content","152124"])
table.save()
print(table.liste_id())
table.close()