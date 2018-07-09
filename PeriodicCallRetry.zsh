#!/usr/bin/env zsh

let counter=0
echo calling in 5
while true
do
	if [[ $(dc ${counter} 300 mod p) -eq 0 ]] ; then
		termux-telephony-call 6692120197
		date
		sleep 60s
	fi
	sleep 1s
	((counter += 1))
	printf "      %i \r " $counter 
done
