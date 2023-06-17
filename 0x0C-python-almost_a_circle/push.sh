#!/bin/bash

echo "Enter commit  Message"
read message

git add .
git commit -m "$message"
git push
