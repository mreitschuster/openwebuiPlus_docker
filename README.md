 


 install
 https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

 curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list


sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

 -> needs nvidia driver, not cuda

 test if it worked
 docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
