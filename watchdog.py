# file: watchdog.py

import signal

class wdTimer(Exception):
# usage wdTimer(timeout_in_seconds) or Watchdog() >> defaults to 2 seconds
	def __init__(self, timeout=2):
		self.time = timeout

	def __enter__(self):
		signal.signal(signal.SIGALRM, self.handler)
		signal.alarm(self.time)

	def __exit__(self, type, value, traceback):
		signal.alarm(0)

	def handler(self, signum, frame):
		raise self