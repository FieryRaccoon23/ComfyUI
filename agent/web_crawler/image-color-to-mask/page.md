[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Image Color To Mask
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Color To Mask
![comfyUI节点-ImageColorToMask|图像到遮罩](https://comfyui-wiki.com/mask/ImageColorToMask.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-color-to-mask#documentation)
  * Class name: `ImageColorToMask`
  * Category: `mask`
  * Output node: `False`


The ImageColorToMask node is designed to convert a specified color in an image to a mask. It processes an image and a target color, generating a mask where the specified color is highlighted, facilitating operations like color-based segmentation or object isolation.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-color-to-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The ‘image’ parameter represents the input image to be processed. It is crucial for determining the areas of the image that match the specified color to be converted into a mask.  
`color` | `INT` | The ‘color’ parameter specifies the target color in the image to be converted into a mask. It plays a key role in identifying the specific color areas to be highlighted in the resulting mask.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-color-to-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | `MASK` | The output is a mask highlighting the areas of the input image that match the specified color. This mask can be used for further image processing tasks, such as segmentation or object isolation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/grow-mask "Grow Mask")[Image To Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-to-mask "Image To Mask")
Discover more
Wiki
ComfyUI
Stable Diffusion
Stable diffusion
SDXL
Black Forest Labs
FLUX
Comfy
interface
stable diffusion
