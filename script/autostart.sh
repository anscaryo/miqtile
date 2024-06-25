#!/bin/sh
setxkbmap -layout es &
# /home/ansgair/display_conf1.sh &
#   Iconos de sistema.
udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 -p &
#screenout.sh &
blueberry-tray &

# --->  Configuracion del escritorio  <---

if [ -f $HOME/.screenlayout/screenlayout.sh ]
then
  $HOME/.screenlayout/screenlayout.sh &
fi
pgrep -x picom > /dev/null || picom  --config $HOME/.config/qtile/script/picom/picom.conf &
nitrogen --restore &
#feh --bg-fill $HOME/.config/qtile/wallpaper/calavera.jpg -Z $HOME/.config/qtile/wallpaper/command.png &

pgrep -x conky || (conky -c $HOME/.config/qtile/script/conky/conky.conf) &


# --->  Configuracion de sistema  <---

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
