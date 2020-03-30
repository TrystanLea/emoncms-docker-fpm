#!/bin/bash
# Disable bluetooth device and restores UART0/ttyAMA0
# once the device tree overlay setting is added to the /boot/config.txt the host must reboot

set -e

python2 ${EMONHUB_DIR}/src/emonhub.py

exec "$@"
