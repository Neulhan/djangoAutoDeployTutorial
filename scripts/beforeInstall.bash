# beforeInstall.bash

#!/usr/bin/env bash
if [ -d /home/ubuntu/djangoAutoDeployTutorial ]; then
    sudo rm -rf /home/ubuntu/djangoAutoDeployTutorial
fi
sudo mkdir -vp /home/ubuntu/djangoAutoDeployTutorial