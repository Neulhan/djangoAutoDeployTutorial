# djangoAutoDeployTutorial/scripts/afterInstall.py

print("after")
import os

os.system('sudo chmod -R gu+rwx /home/ubuntu/djangoAutoDeployTutorial')

os.system('python3 -m venv /home/ubuntu/djangoAutoDeployTutorial/venv')
os.system('sudo chown -R ubuntu.ubuntu /home/ubuntu/djangoAutoDeployTutorial')
os.system('sudo chmod -R gu+rwx /home/ubuntu/djangoAutoDeployTutorial')
os.system(
    '. /home/ubuntu/djangoAutoDeployTutorial/venv/bin/activate && pip install --upgrade pip && pip install -r /home/ubuntu/djangoAutoDeployTutorial/requirements.txt && python /home/ubuntu/djangoAutoDeployTutorial/manage.py migrate')
