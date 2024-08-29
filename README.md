 


 # install
 
[nvidia install guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

```
 curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list


sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```
This needs nvidia driver drivers to be installed, not cuda. Go and test if it worked with: 
``` 
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```


# first usage

## add models
admin panel -> settings -> model

search for models [on the ollama webpage](https://ollama.com/search?c=code)

add some models, eg
- llama3.1
- mistral:7b
- deepseek-coder-v2
- codellama 
- llava-llama3 
- brxce/stable-diffusion-prompt-generator 


## image generation
works for me. the trick is to click the samll icon below the response that states "generate image"
- set engine to automatic1111
- check url (should be prefilled) 
- enable
- set a model

## documents
? model engine -> ollama

install embedding model

?enable hybrid search

?install reranking model: baai/bge-reranker-v2-m3


## web search

## pipelines


# voice
