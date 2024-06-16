#!/bin/sh
setxkbmap -layout es &
# /home/ansgair/display_conf1.sh &
pgrep -x picom > /dev/null || picom  --config $HOME/.config/qtile/script/picom/picom.conf &

#feh --bg-fill $HOME/.config/qtile/wallpaper/calavera.jpg -Z $HOME/.config/qtile/wallpaper/command.png &
nitrogen --restore &
#   Iconos de sistema.
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 &
#screenout.sh &

if [ -f $HOME/.screenlayout/screenlayout.sh ]
then
  $HOME/.screenlayout/screenlayout.sh &
fi

#xrandr --output Virtual1  --mode 1920x1080+0+0 &
#xrandr --output Virtual2  --mode 1920x1080 --rotate left &
#conky &
(conky -c $HOME/.config/qtile/script/conky/conky.conf) &
