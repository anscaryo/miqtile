# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import re
#import psutil
import subprocess
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.widget import Spacer
from libqtile.utils import guess_terminal


#-----------------------------------------------------------------------
#   Funciones
#-----------------------------------------------------------------------

def init_colors():
    return [["#ff9900", "#ff9900"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"], # color 9
            ["#5e81ac", "#5e81ac"], # color 10
            ["#4c566a", "#4c566a"], # color 11
            ["#5dade2", "#5dade2"], # color 12
            ["#4c566a", "#4c566a"], # color 13
            ["#f5b7b1", "#f5b7b1"], # color 14
            ]




def texto(texto):
    return widget.TextBox(
                    font="FontAwesome",
                    text=texto,
                    foreground=colors[3], #"fba922",
                    background=colors[1], #"#2f343f",
                    pading=0,
                    fontsize=16
                    )


def layout_actual():
    return widget.CurrentLayout(
                    foreground = f_ground,
                    background = b_ground,
                    fontsize = 16)


def init_layout_theme():

    return{
            "margin":5,
            "border_width":2,
            "border_focus":colors[10],
            "border_normal":colors[11]
            }


def window_name():
    return widget.WindowName(font="Noto Sans",
                                  foreground=colors[12],#"#5dade2",
                                  background=colors[1],
                                  fontsize=12)


def separador():
    return widget.Sep(
            linewidth = 0,
            padding = 10,
            foreground = colors[2],
            background = colors[1]
            )



#-----------------------------------------------------------------------
#   Asignación de teclas
#-----------------------------------------------------------------------

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.

   # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
   # Grow windows. If current window is on the edge of screen and direction
   # will be to screen edge - window would shrink.
# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        #lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        #lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        #lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        #lazy.layout.increase_nmaster(),
        ),
#    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
#    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
#    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
#    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    #Key(
    #    [mod, "shift"],
    #    "Return",
    #    lazy.layout.toggle_split(),
    #    desc="Toggle between split and unsplit sides of stack",
    #),
#   Aplicaciones:
    Key([mod, "shift"], "Return", lazy.spawn("thunar"), desc="Lanza el administrador de archivos"),
#    Key([mod], "x", lazy.cmd_spawn("/usr/bin/archlinux-logout"), desc="Lanza el menu para cerrar seison de arcolinux"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanza la terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "m", lazy.spawn("rofi -i -show drun -modi drun -show-icons"), desc="Abre el menu rofi"),
    Key([mod, "shift"], "f", lazy.spawn("firefox"), desc="Lanza el navegador firefox"),
    Key([mod], "b", lazy.spawn("brave"), desc="Lanza el navegador brave"),
    Key([mod, "shift"], "c", lazy.spawn("code"), desc="Lanza Visual Studio Code"),
    Key([mod, "shift"], "s", lazy.spawn("pavucontrol"), desc="Lanza aplicación para controlar el sonido")
    
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


#-----------------------------------------------------------------------
#   Grupos
#-----------------------------------------------------------------------

__groups = {
        1:Group("", layout="monadtall"),
        2:Group("", layout="monadwide"),
        3:Group("󰨞", layout="monadwide", matches=[Match(wm_class=re.compile(r"^(Code)$"))]),
        4:Group("", layout="monadwide", matches=[Match(wm_class=re.compile(r"^(firefox|brave)$"))], screen_affinity = 1),
        5:Group("", layout="monadtall"),
        0:Group("", layout="monadthreecol", screen_affinity = 0),
        }

groups = [__groups[i] for i in __groups]


def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]


for i in groups:
    keys.extend([
        # mod1 + leter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(), desc = "Cambia al grupo {}".format(i.name)),
        # mod1 + "shift" + lotter of group = mov a switch to group
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc = "Cambia y mueve el foco al grupo {}".format(i.name)),
        ])
#groups = [Group(i) for i in [
#  "","","󰨞","","","󰕼",#"","","󰣀",
#        ]
#    ]

#for i, group in enumerate(groups):
#    num = str(i+1)
#
#    keys.extend(
#        [
#            # mod1 + group number = switch to group
#            Key([mod], num, lazy.group[group.name].toscreen(),
#                desc="Switch to group {}".format(group.name),
#            ),
#            # mod1 + shift + group number = switch to & move focused window to group
#            Key([mod, "shift"], num, lazy.window.togroup(group.name, switch_group=True),
#                desc="Switch to & move focused window to group {}".format(group.name),
#            ),
#        ]
#    )


#-----------------------------------------------------------------------
#   Colores
#-----------------------------------------------------------------------
colors = init_colors()

f_ground = colors[0]
b_ground = colors[1]



#-----------------------------------------------------------------------
#   Layouts
#-----------------------------------------------------------------------

layout_theme =  init_layout_theme()

layouts = [
        #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
        #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadWide(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()



#-----------------------------------------------------------------------
#   Barra superior
#-----------------------------------------------------------------------

#widget_list = init_widgets_list()

screens = [

#-------------------------------------------------
#   Primera pantalla
#-------------------------------------------------
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(" 󰣇 ",
                               name= "Sistema", 
                               fontsize = 34,
                               foreground="#3ADE01", #colors[0],
                               margin_x=0,
                               margin_y=0,
                               padding_y=6,
                               padding_x=5,
                               background=b_ground),                
                widget.GroupBox(font="FontAwesome",
                                fontsize=14,
                                margin_x=0,
                                margin_y=0,
                                padding_y=6,
                                padding_x=5,
                                disable_drag = True,
                                active = colors[14], #"#f5b7b1",
                                inactive = colors[9], #"#a9a9a9",
                                rounded = False,
                                highlight_method = "text",
                                this_current_screen_border = colors[8], # "#6790eb",
                                foreground=f_ground,
                                background= colors[1],
                               ),
                separador(),
                layout_actual(),
                separador(),
                widget.Prompt(
                    foreground = colors[0],
                    background = colors[5]),
                separador(),
                #widget.Net(
                #    font="Noto Sanz",
                #    fontsize=12,
                #    interface="enp0s3",
                #    foreground="#c0c5ce",
                #    background="#2f343f"
                #    ),

                #widget.Prompt(),
                window_name(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                
                widget.NetGraph(
                        font="Noto Sans",
                        fontsize=12,
                        bandwidth="down",
                        interface="auto",
                        fill_color = colors[8],
                        foreground=colors[2],
                        background=colors[1],
                        graph_color = colors[0],
                        border_color = colors[1],
                        padding = 0,
                        line_width = 1,
                        ),
                widget.Systray(
                        foreground=colors[2],
                        background=colors[1],
                        icon_size=20
                ),
                separador(),
#                texto(" 󰚰 "),
#                                widget.CheckUpdates(
#                        distro = 'Arch',
#                        custom_command="checkupdates",
#                        background=colors[1],
#                        foreground=colors[2],
#                        update_interval=60,
#                        colour_have_updates="00ff00",
#                        colour_no_updates="ff5500",
#                        no_update_string='No Updates',
#                        display_format='Updates --> {updates}',
#                        padding=10,
#                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
#                        execute="st -e pacman -Syyu",
#                        ),
                separador(),
                texto(" 󰃰 "),
                widget.Clock(
                        foreground=colors[2],
                        background=colors[1],
                        format="%d/%m/%Y %A %H:%M "
                        ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                #widget.Systray(),
                #widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                # texto(" 󰩈 "),
                widget.QuickExit(
                        fontsize = 14,
                        default_text=' 󰩈 ',
                        foreground=colors[2],
                        background=colors[1]
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    
        ),

    
#-------------------------------------------------
#   Segunda pantalla
#-------------------------------------------------
    Screen(
        top=bar.Bar([
            widget.GroupBox(font="FontAwesome",
                                fontsize=14,
                                margin_x=0,
                                margin_y=0,
                                padding_y=6,
                                padding_x=5,
                                disable_drag = True,
                                active = colors[14], #"#f5b7b1",
                                inactive = colors[9],
                                rounded = False,
                                highlight_method = "text",
                                this_current_screen_border = colors[8],
                                foreground=f_ground,
                                background=b_ground,),
            window_name(),
            layout_actual(),
            widget.Clock(
                        foreground=colors[2],
                        background=colors[1],
                        format="%H:%M:%S "
                        ),
            widget.TextBox(
                         font="FontAwesome",
                         text="  ",
                         foreground=colors[2],
                         background=colors[1],
                         padding = 0,
                         fontsize=16
                        ),
            widget.CPUGraph(
                         border_color = colors[1],
                         fill_color = colors[8],
                         graph_color = colors[0],
                         background=colors[1],
                         border_width = 1,
                         line_width = 1,
                         core = "all",
                         type = "box"
                       ),
            ], 30),
        )
    ]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/script/autostart.sh")
    subprocess.run([script])

#cmd = [
#        fet
#        ]
