[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing "Mask")Image To Mask
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Convert Image to Mask
![comfyUI节点-Convert Image to Mask|图像到遮罩](https://comfyui-wiki.com/mask/Convert_Image_to_Mask.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-to-mask#documentation)
  * Class name: `ImageToMask`
  * Category: `mask`
  * Output node: `False`


The ImageToMask node is designed to convert an image into a mask based on a specified color channel. It allows for the extraction of mask layers corresponding to the red, green, blue, or alpha channels of an image, facilitating operations that require channel-specific masking or processing.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-to-mask#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The ‘image’ parameter represents the input image from which a mask will be generated based on the specified color channel. It plays a crucial role in determining the content and characteristics of the resulting mask.  
`channel` | `COMBO[STRING]` | The ‘channel’ parameter specifies which color channel (red, green, blue, or alpha) of the input image should be used to generate the mask. This choice directly influences the mask’s appearance and which parts of the image are highlighted or masked out.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-to-mask#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`mask` | `MASK` | The output ‘mask’ is a binary or grayscale representation of the specified color channel from the input image, useful for further image processing or masking operations.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/mask/image-color-to-mask "Image Color To Mask")[Invert Mask](https://comfyui-wiki.com/en/comfyui-nodes/mask/invert-mask "Invert Mask")
Discover more
Mask
Stable diffusion
MASK
ComfyUI
Workflow
Wiki
Stable Diffusion
Artificial intelligence
Interface
Comfy
