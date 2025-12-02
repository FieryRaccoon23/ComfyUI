[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Load Image (as Mask)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load Image (as Mask)
![comfyUI节点-Load Image\(as Mask\)|加载图像遮罩](https://comfyui-wiki.com/mask/Load_Image\(as_Mask\).jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/load-image-mask#documentation)
  * Class name: `LoadImageMask`
  * Category: `mask`
  * Output node: `False`


The LoadImageMask node is designed to load images and their associated masks from a specified path, processing them to ensure compatibility with further image manipulation or analysis tasks. It focuses on handling various image formats and conditions, such as presence of an alpha channel for masks, and prepares the images and masks for downstream processing by converting them to a standardized format.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/load-image-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `COMBO[STRING]` | The ‘image’ parameter specifies the image file to be loaded and processed. It plays a crucial role in determining the output by providing the source image for mask extraction and format conversion.  
`channel` | `COMBO[STRING]` | The ‘channel’ parameter specifies the color channel of the image that will be used to generate the mask. This allows for flexibility in mask creation based on different color channels, enhancing the node’s utility in various image processing scenarios.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/load-image-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | `MASK` | This node outputs the mask generated from the specified image and channel, prepared in a standardized format suitable for further processing in image manipulation tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/invert-mask "Invert Mask")[Mask Composite](https://comfyui-wiki.com/en/comfyui-nodes/mask/mask-composite "Mask Composite")
Discover more
Wiki
Stable Diffusion
ComfyUI
Stable diffusion
Artificial intelligence
FLUX.1
user interface
Interface
FLUX
stable diffusion
