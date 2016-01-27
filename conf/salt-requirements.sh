#salt-call --local -l debug state.template conf/requirements.sls
#sudo salt-call -l debug --local --pillar-root=joe --file-root=`pwd` state.template requirements.sls 

echo
echo Be sure to run $0 as the user you want the venv installed as, from the conf/ subdir!  
echo It will ask for your pw if you are set up that way for sudo
echo

me=`id -un`
cwd=`pwd`

echo Running salt-requirements as $me in $cwd
sudo salt-call --local --pillar-root=$me --file-root=$cwd state.template requirements.sls 

