[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")unCLIP Conditioning
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# unCLIP Conditioning
![comfyUI节点-unCLIPConditioning｜unCLIP条件](https://comfyui-wiki.com/conditioning/unCLIPConditioning.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/unclip-conditioning#documentation)
  * Class name: `unCLIPConditioning`
  * Category: `conditioning`
  * Output node: `False`


This node is designed to integrate CLIP vision outputs into the conditioning process, adjusting the influence of these outputs based on specified strength and noise augmentation parameters. It enriches the conditioning with visual context, enhancing the generation process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/unclip-conditioning#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The base conditioning data to which the CLIP vision outputs are to be added, serving as the foundation for further modifications.  
`clip_vision_output` | `CLIP_VISION_OUTPUT` | The output from a CLIP vision model, providing visual context that is integrated into the conditioning.  
`strength` | `FLOAT` | Determines the intensity of the CLIP vision output’s influence on the conditioning.  
`noise_augmentation` | `FLOAT` | Specifies the level of noise augmentation to apply to the CLIP vision output before integrating it into the conditioning.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/unclip-conditioning#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The enriched conditioning data, now containing integrated CLIP vision outputs with applied strength and noise augmentation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/style-model/style-model-apply "Apply Style Model")[SD_4X Upscale Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/upscale-diffusion/sd-4xupscale-conditioning "SD_4X Upscale Conditioning")
