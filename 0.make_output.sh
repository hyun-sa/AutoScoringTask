#!/bin/bash

if [[ $1 == "C" ]]; then
  compile_extension=".c"
  compile_command="gcc -o"
elif [[ $1 == "Python" ]]; then
  compile_extension=".py"
  compile_command="python3 -m py_compile"
else
  echo "Please Type "C" or "Python"" >&2
  exit 1
fi

for file_path in ./input/*
do
  if [[ "${file_path}" != *"${compile_extension}" ]]; then
    continue
  fi
  if [ -f "$file_path" ]
  then
    file_name=$(basename "$file_path")
    rm -rf "./output/${file_name%.*}.txt"
    mkdir -p "./output"
    
    if [[ $1 == "C" ]]; then
      $compile_command "./output/${file_name%.*}" "$file_path"
    fi
    
    for i in {1..2000}
    do
      if [[ $1 == "C" ]]; then
        echo "<<< $i case >>>" >> "./output/${file_name%.*}.txt"
        echo "$i" | "./output/${file_name%.*}" >> "./output/${file_name%.*}.txt"        
      elif [[ $1 == "Python" ]]; then
        echo "<<< $i case >>>" >> "./output/${file_name%.*}.txt"
        echo "$i" | python3 "$file_path" >> "./output/${file_name%.*}.txt"
      fi
    done
  fi
done

