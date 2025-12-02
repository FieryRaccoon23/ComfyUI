[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[upscaling](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale "upscaling")Image Scale By Node
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Upscale Image By
![comfyUI节点-Upscale Image By|图像按系数缩放](https://comfyui-wiki.com/image/upscaling/Upscale_Image_By.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-by#documentation)
  * Class name: `ImageScaleBy`
  * Category: `image/upscaling`
  * Output node: `False`


The ImageScaleBy node is designed for upscaling images by a specified scale factor using various interpolation methods. It allows for the adjustment of the image size in a flexible manner, catering to different upscaling needs.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-by#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be upscaled. This parameter is crucial as it provides the base image that will undergo the upscaling process.  
`upscale_method` | `COMBO[STRING]` | Specifies the interpolation method to be used for upscaling. The choice of method can affect the quality and characteristics of the upscaled image.  
`scale_by` | `FLOAT` | The factor by which the image will be upscaled. This determines the increase in size of the output image relative to the input image.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-by#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The upscaled image, which is larger than the input image according to the specified scale factor and interpolation method.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale "Image Scale")[Image Scale To Total Pixels](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-to-total-pixels "Image Scale To Total Pixels")
Discover more
Wiki
Stable Diffusion
ComfyUI
Stable diffusion
AI
stable diffusion
Sdxl
FLUX.1
Artificial intelligence
Black Forest Labs
