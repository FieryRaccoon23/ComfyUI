[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Crop Mask
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Crop Mask
![comfyUI节点-CropMask|遮罩裁剪](https://comfyui-wiki.com/mask/CropMask.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/crop-mask#documentation)
  * Class name: `CropMask`
  * Category: `mask`
  * Output node: `False`


The CropMask node is designed for cropping a specified area from a given mask. It allows users to define the region of interest by specifying coordinates and dimensions, effectively extracting a portion of the mask for further processing or analysis.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/crop-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The mask input represents the mask image to be cropped. It is essential for defining the area to be extracted based on the specified coordinates and dimensions.  
`x` | INT | The x coordinate specifies the starting point on the horizontal axis from which the cropping should begin.  
`y` | INT | The y coordinate determines the starting point on the vertical axis for the cropping operation.  
`width` | INT | Width defines the horizontal extent of the crop area from the starting point.  
`height` | INT | Height specifies the vertical extent of the crop area from the starting point.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/crop-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | MASK | The output is a cropped mask, which is a portion of the original mask defined by the specified coordinates and dimensions.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/split-image-with-alpha "Split Image with Alpha")[Feather Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/feather-mask "Feather Mask")
Discover more
Workflow
ComfyUI
Stable diffusion
Wiki
Stable Diffusion
User interface
FLUX
Sdxl
Interface
interface
