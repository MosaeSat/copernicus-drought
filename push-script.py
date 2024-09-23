import os

# Directory where the data is stored
data_dir = './drought_data'

# Git commands to add, commit, and push data
def git_push():
    os.system('git add .')
    os.system('git commit -m "Automated data upload"')
    os.system('git push origin main')

if __name__ == '__main__':
    git_push()
