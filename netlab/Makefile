.PHONY: setup stop destroy restart status

setup:
	netlab up

stop:
	netlab down

destroy:
	netlab down --cleanup

connect:
	netlab connect $(host)

restart:
	netlab restart

status:
	netlab status
