[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[upscaling](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale "upscaling")Image Scale To Total Pixels
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Scale To Total Pixels
![comfyUI节点-ImageScaleToTotalPixels|图像按像素缩放](https://comfyui-wiki.com/image/upscaling/ImageScaleToTotalPixels.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-to-total-pixels#documentation)
  * Class name: `ImageScaleToTotalPixels`
  * Category: `image/upscaling`
  * Output node: `False`


The ImageScaleToTotalPixels node is designed for resizing images to a specified total number of pixels while maintaining the aspect ratio. It provides various methods for upscaling the image to achieve the desired pixel count.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-to-total-pixels#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The input image to be upscaled to the specified total number of pixels.  
`upscale_method` | `COMBO[STRING]` | The method used for upscaling the image. It affects the quality and characteristics of the upscaled image.  
`megapixels` | `FLOAT` | The target size of the image in megapixels. This determines the total number of pixels in the upscaled image.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-to-total-pixels#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The upscaled image with the specified total number of pixels, maintaining the original aspect ratio.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-scale-by "Image Scale By Node")[Image Upscale With Model](https://comfyui-wiki.com/en/comfyui-nodes/image/upscaling/image-upscale-with-model "Image Upscale With Model")
