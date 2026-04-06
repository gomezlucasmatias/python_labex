!#/bin/bash

# Get user age 
echo "Tell me, how old are you?"
read old

# Filter respond based user's input
if [ $old -lt 2 ]; then
    echo "You are a baby"
elif [[ $old -ge 2 && $old -lt 4 ]]; then
      echo "You are a toddler"
elif [[ $old -ge 4 && $old -lt 13 ]]; then
      echo "You are a kid"
elif [[ $old -ge 13 && $old -lt 20 ]]; then
      echo "You are a teenager"
elif [[ $old -ge 20 && $old -lt 65 ]]; then
      echo "You are an adult"
else
      echo "You are an elder"
fi
