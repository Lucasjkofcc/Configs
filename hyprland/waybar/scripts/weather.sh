#!/bin/bash

data=$(curl -sf --max-time 10 'https://wttr.in/Itaqui?format=%t|%C')

if [ -z "$data" ]; then
  echo '{"text":"󰖙","tooltip":"Clima indisponível"}'
  exit 0
fi

temp="${data%%|*}"
cond="${data#*|}"
cond="${cond#"${cond%%[![:space:]]*}"}"
cond="${cond%"${cond##*[![:space:]]}"}"
temp="${temp#+}"
temp="${temp//\"/\\\"}"

echo "{\"text\":\"󰖙\",\"alt\":\"󰖙 <span size='11pt'>${temp}</span>\",\"tooltip\":\": ${cond}, ${temp}\"}"
