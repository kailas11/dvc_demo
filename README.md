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

dvc dd data_given/winequality.scv