#
# random-bin.py
# Set a unique firmware name based on current date and time plus commit hash
#
import pioutil
if pioutil.is_pio_build():
	from datetime import datetime
	from subprocess import Popen, PIPE
	Import("env")

	# determine commit hash (which isn't sortable, so we append it after the tiemstamp)
	cmd = Popen(['git', 'rev-parse', '--short', 'HEAD'], shell=True, stdout=PIPE)
	for line in cmd.stdout:
		commit = line.decode().rstrip()

	env['PROGNAME'] = datetime.now().strftime("firmware-%Y%m%d-%H%M%S-" + commit)
