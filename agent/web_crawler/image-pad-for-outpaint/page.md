[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")Image Pad For Outpainting
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Pad Image for Outpainting
![comfyUI节点-Pad Image for Outpainting|外补画板](https://comfyui-wiki.com/image/Pad_Image_for_Outpainting.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-pad-for-outpaint#documentation)
  * Class name: `ImagePadForOutpaint`
  * Category: `image`
  * Output node: `False`


This node is designed for preparing images for the outpainting process by adding padding around them. It adjusts the image dimensions to ensure compatibility with outpainting algorithms, facilitating the generation of extended image areas beyond the original boundaries.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-pad-for-outpaint#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The ‘image’ input is the primary image to be prepared for outpainting, serving as the base for padding operations.  
`left` | `INT` | Specifies the amount of padding to add to the left side of the image, influencing the expanded area for outpainting.  
`top` | `INT` | Determines the amount of padding to add to the top of the image, affecting the vertical expansion for outpainting.  
`right` | `INT` | Defines the amount of padding to add to the right side of the image, impacting the horizontal expansion for outpainting.  
`bottom` | `INT` | Indicates the amount of padding to add to the bottom of the image, contributing to the vertical expansion for outpainting.  
`feathering` | `INT` | Controls the smoothness of the transition between the original image and the added padding, enhancing the visual integration for outpainting.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-pad-for-outpaint#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output ‘image’ represents the padded image, ready for the outpainting process.  
`mask` | `MASK` | The output ‘mask’ indicates the areas of the original image and the added padding, useful for guiding the outpainting algorithms.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/image-invert "Invert Image")[Load Image](https://comfyui-wiki.com/en/comfyui-nodes/image/load-image "Load Image")
Discover more
Stable Diffusion
ComfyUI
Stable diffusion
Wiki
Workflow
Sdxl
AI
interface
Flux
Interface
