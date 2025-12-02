[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")Image Composite Masked
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Composite Masked
![comfyUI节点-ImageCompositeMasked|图像遮罩复合](https://comfyui-wiki.com/image/ImageCompositeMasked.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-composite-masked#documentation)
  * Class name: `ImageCompositeMasked`
  * Category: `image`
  * Output node: `False` The ImageCompositeMasked node is designed for compositing images, allowing for the overlay of a source image onto a destination image at specified coordinates, with optional resizing and masking.


## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-composite-masked#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`destination` | `IMAGE` | The destination image onto which the source image will be composited. It serves as the background for the composite operation.  
`source` | `IMAGE` | The source image to be composited onto the destination image. This image can optionally be resized to fit the destination image’s dimensions.  
`x` | `INT` | The x-coordinate in the destination image where the top-left corner of the source image will be placed.  
`y` | `INT` | The y-coordinate in the destination image where the top-left corner of the source image will be placed.  
`resize_source` | `BOOLEAN` | A boolean flag indicating whether the source image should be resized to match the destination image’s dimensions.  
`mask` | `MASK` | An optional mask that specifies which parts of the source image should be composited onto the destination image. This allows for more complex compositing operations, such as blending or partial overlays.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-composite-masked#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The resulting image after the compositing operation, which combines elements of both t  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-batch "Image Batch")[Invert Image](https://comfyui-wiki.com/en/comfyui-nodes/image/image-invert "Invert Image")
Discover more
Stable Diffusion
Stable diffusion
Wiki
ComfyUI
Black Forest Labs
Comfy
SDXL
stable diffusion
AI
FLUX.1
