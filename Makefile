.PHONY: setup stop destroy help restart status

setup:
	$(MAKE) -C netlab setup

stop:
	$(MAKE) -C netlab stop

destroy:
	$(MAKE) -C netlab destroy

connect:
	$(MAKE) -C netlab connect host=$(host)

restart:
	$(MAKE) -C netlab restart

status:
	$(MAKE) -C netlab status

help:
	@echo "Available commands:"
	@echo "  make setup     - Start the network lab"
	@echo "  make stop      - Stop the network lab"
	@echo "  make destroy   - Tear down the network lab"
	@echo "  make connect host=<host> - Connect to a specific host (e.g., R1)"
	@echo "  make restart   - Restart the network lab"
	@echo "  make status    - Check the status of the network lab"
