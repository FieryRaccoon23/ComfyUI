[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Sampling](https://comfyui-wiki.com/en/comfyui-nodes/sampling/custom-sampling "Sampling")video-modelsVideo Linear CFG Guidance
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Video Linear CFG Guidance
![comfyUI节点-VideoLinearCFGGUidance 线性CFG引导](https://comfyui-wiki.com/sampling/video_models/01.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/video-models/video-linear-cfg-guidance#documentation)
  * Class name: `VideoLinearCFGGuidance`
  * Category: `sampling/video_models`
  * Output node: `False`


The VideoLinearCFGGuidance node applies a linear conditioning guidance scale to a video model, adjusting the influence of conditioned and unconditioned components over a specified range. This enables dynamic control over the generation process, allowing for fine-tuning of the model’s output based on the desired level of conditioning.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/video-models/video-linear-cfg-guidance#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The model parameter represents the video model to which the linear CFG guidance will be applied. It is crucial for defining the base model that will be modified with the guidance scale.  
`min_cfg` | `FLOAT` | The min_cfg parameter specifies the minimum conditioning guidance scale to be applied, serving as the starting point for the linear scale adjustment. It plays a key role in determining the lower bound of the guidance scale, influencing the model’s output.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/video-models/video-linear-cfg-guidance#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The output is a modified version of the input model, with the linear CFG guidance scale applied. This adjusted model is capable of generating outputs with varying degrees of conditioning, based on the specified guidance scale.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/sampling/sampler "Sampler")[Note](https://comfyui-wiki.com/en/comfyui-nodes/utils/note "Note")
Discover more
Wiki
Video
Stable diffusion
ComfyUI
video
Stable Diffusion
interface
Comfy
SDXL
FLUX
