# Auto Project creator
---
Creates repository folder and initializes github repository
---
## Requirements
* Selenium

---
Installation
1. Change line 6 of .my_commands.sh to point to your project directory
2. Change line 9 of .my_commands.sh to include your github username
3. Change lines 5, 14, and 16 of create.py to your project directory, github username, and github password
4. Move both files to home directory and create pointer to .my_commands.sh
```shell
mv .my_commands.sh ~/
mv create.py ~/
cd ~/
chmod +x .my_commands.sh
```
5. add ~/.my_commands.sh to .bashrc or .zshrc
