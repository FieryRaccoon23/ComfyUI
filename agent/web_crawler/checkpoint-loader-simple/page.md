[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")LoadersCheckpoint Loader (Simple)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load Checkpoint
![comfyUI节点-Load Checkpoint｜Checkpoint加载器（简易](https://comfyui-wiki.com/loaders/Load_Checkpoint.jpg)
This node will detect models located in the `ComfyUI/models/checkpoints` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple#documentation)
  * Class name: `CheckpointLoaderSimple`
  * Category: `loaders`
  * Output node: `False`


The CheckpointLoaderSimple node is designed for loading model checkpoints without the need for specifying a configuration. It simplifies the process of checkpoint loading by requiring only the checkpoint name, making it more accessible for users who may not be familiar with the configuration details.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple#input-types)
Field | Comfy dtype | Description  
---|---|---  
`ckpt_name` | `COMBO[STRING]` | Specifies the name of the checkpoint to be loaded, determining which checkpoint file the node will attempt to load and affecting the node’s execution and the model that is loaded.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple#output-types)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | Returns the loaded model, allowing it to be used for further processing or inference.  
`clip` | `CLIP` | Returns the CLIP model associated with the loaded checkpoint, if available.  
`vae` | `VAE` | Returns the VAE model associated with the loaded checkpoint, if available.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/video/empty-hunyuan-latent-video "Empty Hunyuan Latent Video Node Tutorial")[CLIP Vision Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/clip-vision-loader "CLIP Vision Loader")
Discover more
Workflow
ComfyUI
Wiki
Stable diffusion
Stable Diffusion
AI
stable diffusion
Interface
User interface
Flux.1
