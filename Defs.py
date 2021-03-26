from winsound import Beep
# module for functions used in layers project

import winsound

from system_setup import error_msn


def sound_error():
	sd1 = [1500, 200]  # frequency, time mseg.
	sd2 = [2500, 200]
	winsound.Beep(sd1[0],sd1[1])
	winsound.Beep(sd2[0],sd2[1])
	return

def exit_app(msn):
	sound_error()
	print('\n' + msn + '\n')
	print('\n ' + error_msn['abort_app'])
	exit()