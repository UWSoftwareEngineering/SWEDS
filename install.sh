#!/bin/bash
echo "Install atom"
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom
echo "Install miniconda"
curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh >miniconda_setup.sh
bash miniconda_setup.sh
rm miniconda_setup.sh
echo "Close this terminal session; open a new session; 'bash conda_installs.sh'"
