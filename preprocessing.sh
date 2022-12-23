#!/bin/bash
# This script is used to preprocess the data
function help() {
  echo "Usage: $0 [options]"
  echo "Options:"
  echo "  -h, --help: show this help message and exit"
  echo " -a|--all : convert all py file to ipynb , run then and convert to markdown"
}
function update_readme(){
  rm README.md
  echo "\`\`\`markdown" >> README.md
  figlet "Advent of code 2022" >> README.md
  echo "\`\`\`" >> README.md
  echo "****************************" >> README.md
  for file in  public/*.html; do
    file=${file##*/}
    day_number=$(echo $file | sed 's/day\(.*\).html/\1/g' )
    echo "#### Day $day_number: " >> README.md
    echo "[Day $day_number](day${day_number}.py)" >> README.md
  done
}

case $1 in
"--help" | "-h")
  help
  ;;
"--all" | "-a")
  for file in *.py; do
    jupytext --to notebook --from py:percent $file
  done
  for file in *.ipynb; do
    jupyter nbconvert --to markdown --execute $file
  done
  ;;
"--file" | "-f")
  jupytext --to notebook --from py:percent $2
  notebook_name=$(echo $2 | cut -d'.' -f1)
  jupyter nbconvert --to markdown --execute $notebook_name.ipynb
  ;;
"--clear"|"-c")
  rm *.ipynb 2&>/dev/null
  rm *.md 2&>/dev/null
  ;;
"--publish"|"-p")
  for file in *.ipynb; do
    jupyter nbconvert --to html --execute --output-dir "public" $file
  done
  update_readme
  ;;
#other
*)
  echo "Invalid argument"
  ;;
esac

print()
