# need to use . or source to run the bash script
path_to_add="/cygdrive/c/Program Files (x86)/Windows Kits/10/bin/10.0.17763.0/x64"

if [ -d "$path_to_add" ] && [[ ":$PATH:" != *":$path_to_add:"* ]]; then
  PATH="${PATH:+"$PATH:"}$path_to_add"
fi

alias cls='printf "\033c"'
