#!/bin/bash
# Simple number guessing game

SECRET=$((RANDOM % 10 + 1))
ATTEMPTS=0

echo "Guess a number between 1 and 10"

while true; do
    read -p "Your guess: " GUESS
    ((ATTEMPTS++))
    
    if [ $GUESS -eq $SECRET ]; then
        echo "🎉 Correct! You guessed it in $ATTEMPTS attempts"
        break
    elif [ $GUESS -lt $SECRET ]; then
        echo "📈 Too low, try again"
    else
        echo "📉 Too high, try again"
    fi
done
