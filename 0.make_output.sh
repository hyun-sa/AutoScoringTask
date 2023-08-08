#!/bin/bash
for file_path in ./input/*
do
  if [ -f "$file_path" ]
  then
    file_name=$(basename "$file_path")
    mkdir -p "./output/${file_name%.*}"
    gcc -o "./output/${file_name%.*}/${file_name%.*}" "$file_path"
    for i in {1..50}
    do
      echo $i | "./output/${file_name%.*}/${file_name%.*}" > "./output/${file_name%.*}/$i.txt"
    done
  fi
done
