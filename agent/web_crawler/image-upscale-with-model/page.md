[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[upscaling](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale "upscaling")Image Upscale With Model
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Upscale Image (using Model)
![comfyUI node - Upscale Image\(using Model\)|Image Upscale with Model](https://comfyui-wiki.com/image/upscaling/Upscale_Image\(using_Model\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-upscale-with-model#documentation)
  * Class name: `ImageUpscaleWithModel`
  * Category: `image/upscaling`
  * Output node: `False`


This node is designed for upscaling images using a specified upscale model. It efficiently manages the upscaling process by adjusting the image to the appropriate device, optimizing memory usage, and applying the upscale model in a tiled manner to prevent potential out-of-memory errors.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-upscale-with-model#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`upscale_model` | `UPSCALE_MODEL` | The upscale model to be used for upscaling the image. It is crucial for defining the upscaling algorithm and its parameters.  
`image` | `IMAGE` | The image to be upscaled. This input is essential for determining the source content that will undergo the upscaling process.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-upscale-with-model#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The upscaled image, processed by the upscale model. This output is the result of the upscaling operation, showcasing the enhanced resolution or quality.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-to-total-pixels "Image Scale To Total Pixels")[Latent Upscale](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent Upscale")
