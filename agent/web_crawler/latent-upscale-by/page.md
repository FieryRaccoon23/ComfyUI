[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")Latent Upscale By
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Upscale Latent By
![comfyUI节点- Upscale latent by｜Latent按系数缩放](https://comfyui-wiki.com/latent/Upscale_latent_by.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale-by#documentation)
  * Class name: `LatentUpscaleBy`
  * Category: `latent`
  * Output node: `False`


The LatentUpscaleBy node is designed for upscaling latent representations of images. It allows for the adjustment of the scale factor and the method of upscaling, providing flexibility in enhancing the resolution of latent samples.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale-by#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The latent representation of images to be upscaled. This parameter is crucial for determining the input data that will undergo the upscaling process.  
`upscale_method` | `COMBO[STRING]` | Specifies the method used for upscaling the latent samples. The choice of method can significantly affect the quality and characteristics of the upscaled output.  
`scale_by` | `FLOAT` | Determines the factor by which the latent samples are scaled. This parameter directly influences the resolution of the output, allowing for precise control over the upscaling process.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale-by#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The upscaled latent representation, ready for further processing or generation tasks. This output is essential for enhancing the resolution of generated images or for subsequent model operations.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/empty-latent-image "Empty Latent Image")[Latent Composite](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-composite "Latent Composite")
