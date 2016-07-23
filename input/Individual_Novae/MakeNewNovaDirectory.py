import sys
import string
import os
from pylab import *
import datetime as dt
import math as m 





NewNovaName = sys.argv[1]
CurrentWorkingDirectory = os.getcwd()

NewDirectoryRoot = CurrentWorkingDirectory+'/'+NewNovaName
NewDirectoryTicketDirectory = NewDirectoryRoot+'/Tickets'
NewDirectoryDataDirectory = NewDirectoryRoot+'/Data'
NewDirectoryPendingTicketSubDirectory = NewDirectoryTicketDirectory+'/PendingTickets'
NewDirectoryCompletedTicketSubDirectory = NewDirectoryTicketDirectory+'/CompletedTickets'
directoryList = [NewDirectoryRoot, NewDirectoryTicketDirectory, NewDirectoryDataDirectory, NewDirectoryPendingTicketSubDirectory, NewDirectoryCompletedTicketSubDirectory]
BlankFile = "blankreadme.txt"

for directory in directoryList:
	if not os.path.exists(directory):
		os.makedirs(directory)
		f = open(directory+"/"+BlankFile, "w")
		f.write("")
		f.close()













