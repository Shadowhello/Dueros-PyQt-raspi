cp dist.tar ~/
cd ~/
tar -xvf dist.tar
rm dist.tar
cd -
cp 智能语音控制系统.sh ~/Desktop
cd ~/Desktop
echo "raspberry" | sudo -S chmod 777 智能语音控制系统.sh
