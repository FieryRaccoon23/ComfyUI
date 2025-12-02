[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[loaders](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "loaders")Load Checkpoint With Config (DEPRECATED)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load Checkpoint With Config (DEPRECATED)
![comfyUI节点-Load Checkpoint With Config\(DEPRECATED\)|Checkpoint加载器（已弃用）](https://comfyui-wiki.com/advanced/loaders/Load-Checkpoint-With-Config\(DEPRECATED\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-checkpoint-loader#documentation)
  * Class name: `CheckpointLoader`
  * Category: `advanced/loaders`
  * Output node: `False`


The CheckpointLoader node is designed for advanced loading operations, specifically to load model checkpoints along with their configurations. It facilitates the retrieval of model components necessary for initializing and running generative models, including configurations and checkpoints from specified directories.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-checkpoint-loader#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`config_name` | `COMBO[STRING]` | Specifies the name of the configuration file to be used. This is crucial for determining the model’s parameters and settings, affecting the model’s behavior and performance.  
`ckpt_name` | `COMBO[STRING]` | Indicates the name of the checkpoint file to be loaded. This directly influences the state of the model being initialized, impacting its initial weights and biases.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-checkpoint-loader#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | Represents the primary model loaded from the checkpoint, ready for further operations or inference.  
`clip` | `CLIP` | Provides the CLIP model component, if available and requested, loaded from the checkpoint.  
`vae` | `VAE` | Delivers the VAE model component, if available and requested, loaded from the checkpoint.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "CLIP Loader")[Diffusers Loader](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/deprecated-diffusers-loader "Diffusers Loader")
Discover more
ComfyUI
Wiki
Workflow
Stable diffusion
Stable Diffusion
Comfy
Interface
FLUX.1
Sdxl
user interface
