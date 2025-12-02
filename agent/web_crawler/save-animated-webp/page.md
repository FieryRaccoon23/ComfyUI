[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Image[animation](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-png "animation")Save Animated WEBP
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Save Animated WEBP
![comfyUI节点-SaveAnimatedWEBP|保存WEBP](https://comfyui-wiki.com/image/animation/SaveAnimatedWEBP.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-webp#documentation)
  * Class name: `SaveAnimatedWEBP`
  * Category: `image/animation`
  * Output node: `True`


This node is designed for saving a sequence of images as an animated WEBP file. It handles the aggregation of individual frames into a cohesive animation, applying specified metadata, and optimizing the output based on quality and compression settings.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-webp#input-types)
Field | Comfy dtype | Description  
---|---|---  
`images` | `IMAGE` | A list of images to be saved as frames in the animated WEBP. This parameter is essential for defining the visual content of the animation.  
`filename_prefix` | `STRING` | Specifies the base name for the output file, which will be appended with a counter and the ‘.webp’ extension. This parameter is crucial for identifying and organizing the saved files.  
`fps` | `FLOAT` | The frames per second rate for the animation, influencing the playback speed.  
`lossless` | `BOOLEAN` | A boolean indicating whether to use lossless compression, affecting the file size and quality of the animation.  
`quality` | `INT` | A value between 0 and 100 that sets the compression quality level, with higher values resulting in better image quality but larger file sizes.  
`method` | `COMBO[STRING]` | Specifies the compression method to use, which can impact the encoding speed and file size.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-webp#output-types)
Field | Comfy dtype | Description  
---|---|---  
`ui` | N/A | Provides a UI component displaying the saved animated WEBP images along with their metadata, and indicates whether the animation is enabled.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-png "Save Animated PNG")[Image From Batch](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch "Image From Batch")
Discover more
Stable Diffusion
SDXL
Animate
animated
Flux
animation
compression
ComfyUI
Animated
Flux.1
