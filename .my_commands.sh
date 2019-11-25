#!/bin/zsh

function create(){
	cd
	python3 create.py $1
	cd /your_code_directory/$1
	echo "creating repo"
	git init
	git remote add origin https://github.com/your_github_username/$1.git
	touch README.md
	git add .
	git commit -am "initial commit"
	git push -u origin master
}