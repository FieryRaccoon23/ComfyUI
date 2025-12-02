[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")upscale-diffusionSD_4X Upscale Conditioning
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# SD_4X Upscale Conditioning
![comfyUI节点-SD_4XUpscale_Conditioning|SD4X放大条件](https://comfyui-wiki.com/conditioning/upscale_diffusion/SD_4XUpscale_Conditioning.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/upscale-diffusion/sd-4xupscale-conditioning#documentation)
  * Class name: `SD_4XUpscale_Conditioning`
  * Category: `conditioning/upscale_diffusion`
  * Output node: `False`


This node specializes in enhancing the resolution of images through a 4x upscale process, incorporating conditioning elements to refine the output. It leverages diffusion techniques to upscale images while allowing for the adjustment of scale ratio and noise augmentation to fine-tune the enhancement process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/upscale-diffusion/sd-4xupscale-conditioning#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`images` | `IMAGE` | The input images to be upscaled. This parameter is crucial as it directly influences the quality and resolution of the output images.  
`positive` | `CONDITIONING` | Positive conditioning elements that guide the upscale process towards desired attributes or features in the output images.  
`negative` | `CONDITIONING` | Negative conditioning elements that the upscale process should avoid, helping to steer the output away from undesired attributes or features.  
`scale_ratio` | `FLOAT` | Determines the factor by which the image resolution is increased. A higher scale ratio results in a larger output image, allowing for greater detail and clarity.  
`noise_augmentation` | `FLOAT` | Controls the level of noise augmentation applied during the upscale process. This can be used to introduce variability and improve the robustness of the output images.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/upscale-diffusion/sd-4xupscale-conditioning#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | The refined positive conditioning elements resulting from the upscale process.  
`negative` | `CONDITIONING` | The refined negative conditioning elements resulting from the upscale process.  
`latent` | `LATENT` | A latent representation generated during the upscale process, which can be utilized in further processing or model training.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/unclip-conditioning "unCLIP Conditioning")[SVD img2vid Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/video-models/svd-img2vid-conditioning "SVD img2vid Conditioning")
Discover more
ComfyUI
Stable Diffusion
Stable diffusion
Workflow
Wiki
User interface
Sdxl
SDXL
Flux.1
user interface
