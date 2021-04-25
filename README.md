create env

'''bash
conda create -n wineq python=3.8 -y
'''

activate env
''' bash
conda activate wineq
'''

created a req file

install the req 
''' bash
pip install -r requirement.txt
'''

git init

dvc init

dvc dd data_given/winequality.csv

git add.
git commit -m "initial commit"

git remote add origin https://github.com/kailas11/dvc_demo.git
git branch -M main
git push -u origin main