#!/bin/bash
filename='/Users/kveselov/fishes.txt'

nums=()

while read p; do 
    #name=$(echo "$p" | jq -sRr @uri)
    
    echo "$p"
    nums+=$(curl -v -s "http://gryaz.fish.lyceumctf.ru/$name" 2>&1 | grep number)
done < "$filename"

echo "$nums" | sort | uniq

