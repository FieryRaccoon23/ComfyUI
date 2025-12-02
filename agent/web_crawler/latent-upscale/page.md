[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")LatentLatent Upscale
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Upscale Latent
![comfyUI节点-Upscale latent｜Latent缩放](https://comfyui-wiki.com/latent/Upscale_latent.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale#documentation)
  * Class name: `LatentUpscale`
  * Category: `latent`
  * Output node: `False`


The LatentUpscale node is designed for upscaling latent representations of images. It allows for the adjustment of the output image’s dimensions and the method of upscaling, providing flexibility in enhancing the resolution of latent images.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The latent representation of an image to be upscaled. This parameter is crucial for determining the starting point of the upscaling process.  
`upscale_method` | `COMBO[STRING]` | Specifies the method used for upscaling the latent image. Different methods can affect the quality and characteristics of the upscaled image.  
`width` | `INT` | The desired width of the upscaled image. If set to 0, it will be calculated based on the height to maintain the aspect ratio.  
`height` | `INT` | The desired height of the upscaled image. If set to 0, it will be calculated based on the width to maintain the aspect ratio.  
`crop` | `COMBO[STRING]` | Determines how the upscaled image should be cropped, affecting the final appearance and dimensions of the output.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The upscaled latent representation of the image, ready for further processing or generation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-upscale-with-model "Image Upscale With Model")[Empty Latent Image](https://comfyui-wiki.com/en/comfyui-nodes/latent/empty-latent-image "Empty Latent Image")
Discover more
Stable Diffusion
Workflow
ComfyUI
Wiki
Stable diffusion
Sdxl
SDXL
Comfy
stable diffusion
Black Forest Labs
