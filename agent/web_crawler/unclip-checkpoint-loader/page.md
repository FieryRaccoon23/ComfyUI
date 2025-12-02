[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")unCLIP Checkpoint Loader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# unCLIPCheckpointLoader
![comfyUI节点-unClipCheckpointLoader｜unClipCheckpoint加载器](https://comfyui-wiki.com/loaders/unClipCheckpointLoader.jpg)
This node will detect models located in the `ComfyUI/models/checkpoints` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/unclip-checkpoint-loader#documentation)
  * Class name: `unCLIPCheckpointLoader`
  * Category: `loaders`
  * Output node: `False`


The unCLIPCheckpointLoader node is designed for loading checkpoints specifically tailored for unCLIP models. It facilitates the retrieval and initialization of models, CLIP vision modules, and VAEs from a specified checkpoint, streamlining the setup process for further operations or analyses.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/unclip-checkpoint-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`ckpt_name` | `COMBO[STRING]` | Specifies the name of the checkpoint to be loaded, identifying and retrieving the correct checkpoint file from a predefined directory, determining the initialization of models and configurations.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/unclip-checkpoint-loader#output-types)
Field | Comfy dtype | Description | Python dtype  
---|---|---|---  
`model` | `MODEL` | Represents the primary model loaded from the checkpoint. | `torch.nn.Module`  
`clip` | `CLIP` | Represents the CLIP module loaded from the checkpoint, if available. | `torch.nn.Module`  
`vae` | `VAE` | Represents the VAE module loaded from the checkpoint, if available. | `torch.nn.Module`  
`clip_vision` | `CLIP_VISION` | Represents the CLIP vision module loaded from the checkpoint, if available. | `torch.nn.Module`  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/style-model-loader "Style Model Loader")[Upscale Model Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/upscale-model-loader "Upscale Model Loader")
Discover more
Black Forest Labs
Sdxl
FLUX
Stable Diffusion
FLUX.1
ComfyUI
User interface
Stable diffusion
Flux
Wiki
