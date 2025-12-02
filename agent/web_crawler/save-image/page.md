[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")Save Image - Save Images to Local in ComfyUI
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Save Image - Save Images to Local in ComfyUI
![comfyUI node-Save Image](https://comfyui-wiki.com/_next/static/media/Save_Image.1b62716a.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/save-image#documentation)
  * Class name: `SaveImage`
  * Category: `image`
  * Output node: `True`


**Node Function:** The `Save Image` node is mainly used to save images to the **output** folder in ComfyUI. If you only want to preview the image during the intermediate process rather than saving it, you can use the `Preview Image` node. Default save location: `ComfyUI/output/`
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/save-image#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`images` | `IMAGE` | The images to be saved. This parameter is crucial as it directly contains the image data that will be processed and saved to disk.  
`filename_prefix` | `STRING` | The filename prefix for images saved to the `ComfyUI/output/` folder. The default is `ComfyUI`, but you can customize it.  
## Right-click Menu Options[](https://comfyui-wiki.com/en/comfyui-nodes/image/save-image#right-click-menu-options)
After the image generation is complete, right-clicking on the corresponding menu provides the following node-specific options and functions:
Option Name | Function  
---|---  
`Save Image` | Save the image locally  
`Copy Image` | Copy the image to clipboard  
`Open Image` | Open the image in a new browser tab  
The saved images are generally in PNG format and include all the image generation data. If you want to use the corresponding workflow for regeneration, you can simply load the corresponding image into ComfyUI to load the workflow.
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/preview-image "Preview Image")[Image Crop](https://comfyui-wiki.com/en/comfyui-nodes/image/transform/image-crop "Image Crop")
Discover more
ComfyUI
Stable diffusion
Wiki
Stable Diffusion
AI
SDXL
Flux.1
Interface
stable diffusion
Flux
