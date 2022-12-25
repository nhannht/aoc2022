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
  {
  echo "\`\`\`text"
  figlet "Advent of code 2022"
  echo "\`\`\`"
  echo "****************************"
  echo "![cloc](./tokei.png)"
  echo "****************************"
} >> README.md

  echo "\`\`\`text" >> README.md
  tokei -f *.py | tee -a README.md > /dev/null
  echo "\`\`\`" >> README.md
  echo "****************************" >> README.md
  echo "> This analytic is not accurate, I don't attempt to create it util the day 25. Previous day I use Pypercent file and doing thing in code block,
  so many problem can occur like code in block is conflict together, or I comment out some code, and it will not be counted." >> README.md
  tokei -f *.py -o json |tee  tokei.json > /dev/null
  for file in  *.py; do
    file=${file##*/}
    day_number=$(echo "$file" | sed 's/day\(.*\).py/\1/gm;t;d' )
    echo "#### Day ${day_number}: " >> README.md
    echo "[Day $day_number](day${day_number}.py)" >> README.md
  done
}

case $1 in
"--help" | "-h")
  help
  ;;
"--update_readme"|"-R")
  update_readme
  ;;
"--all" | "-a")
  for file in *.py; do
    jupytext --to notebook --from py:percent "$file"
  done
  for file in *.ipynb; do
    jupyter nbconvert --to markdown --execute "$file"
  done
  ;;
"--file" | "-f")
  jupytext --to notebook --from py:percent "$2"
  notebook_name=$(echo $2 | cut -d'.' -f1)
  jupyter nbconvert --to markdown --execute "$notebook_name".ipynb
  ;;
"--clear"|"-c")
  rm *.ipynb 2&>/dev/null
  rm *.md 2&>/dev/null
  ;;
"--publish"|"-p")
  for file in *.ipynb; do
    jupyter nbconvert --to html --execute --output-dir "public" "$file"
  done
  update_readme
  ;;
#other
*)
  echo "Invalid argument"
  ;;
esac