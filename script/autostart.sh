#!/bin/sh
setxkbmap -layout es &
# /home/ansgair/display_conf1.sh &
picom & #--config $HOME/.config/qtile/scripts/picom/picom.comf &
nitrogen --restore &
#   Iconos de sistema.
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 &
#screenout.sh &
#xrandr --output Virtual1  --mode 1920x1080+0+0 &
#xrandr --output Virtual2  --mode 1920x1080 --rotate left &
conky &
#(conky -c $HOME/.config/qtile/script/system-overwiew) &