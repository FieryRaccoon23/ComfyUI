[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")VAE Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load VAE
![comfyUI节点-Load VAE｜VAE加载器](https://comfyui-wiki.com/loaders/Load_VAE.jpg)
This node will detect models located in the `ComfyUI/models/vae` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/vae-loader#documentation)
  * Class name: `VAELoader`
  * Category: `loaders`
  * Output node: `False`


The VAELoader node is designed for loading Variational Autoencoder (VAE) models, specifically tailored to handle both standard and approximate VAEs. It supports loading VAEs by name, including specialized handling for ‘taesd’ and ‘taesdxl’ models, and dynamically adjusts based on the VAE’s specific configuration.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/vae-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`vae_name` | `COMBO[STRING]` | Specifies the name of the VAE to be loaded, determining which VAE model is fetched and loaded, with support for a range of predefined VAE names including ‘taesd’ and ‘taesdxl’.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/vae-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`vae` | `VAE` | Returns the loaded VAE model, ready for further operations such as encoding or decoding. The output is a model object encapsulating the loaded model’s state.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/upscale-model-loader "Upscale Model Loader")[Image Only Checkpoint Loader (img2vid model)](https://comfyui-wiki.com/en/comfyui-nodes/loaders/video-models/image-only-checkpoint-loader "Image Only Checkpoint Loader \(img2vid model\)")
Discover more
Stable Diffusion
ComfyUI
Workflow
Stable diffusion
SDXL
AI
Wiki
User interface
Comfy
Flux
