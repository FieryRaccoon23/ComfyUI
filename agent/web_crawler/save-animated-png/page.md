[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")ImageanimationSave Animated PNG
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Save Animated PNG
![comfyUI节点-SaveAnimatedPNG|保存APNG](https://comfyui-wiki.com/image/animation/SaveAnimatedPNG.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-png#documentation)
  * Class name: `SaveAnimatedPNG`
  * Category: `image/animation`
  * Output node: `True`


The SaveAnimatedPNG node is designed for creating and saving animated PNG images from a sequence of frames. It handles the assembly of individual image frames into a cohesive animation, allowing for customization of frame duration, looping, and metadata inclusion.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-png#input-types)
Field | Comfy dtype | Description  
---|---|---  
`images` | `IMAGE` | A list of images to be processed and saved as an animated PNG. Each image in the list represents a frame in the animation.  
`filename_prefix` | `STRING` | Specifies the base name for the output file, which will be used as a prefix for the generated animated PNG files.  
`fps` | `FLOAT` | The frames per second rate for the animation, controlling how quickly the frames are displayed.  
`compress_level` | `INT` | The level of compression applied to the animated PNG files, affecting file size and image clarity.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-png#output-types)
Field | Comfy dtype | Description  
---|---|---  
`ui` | N/A | Provides a UI component displaying the generated animated PNG images and indicating whether the animation is single-frame or multi-frame.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/video-models/wan-fun-control-to-video "WanFunControlToVideo")[Save Animated WEBP](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-webp "Save Animated WEBP")
Discover more
stable diffusion
Flux.1
interface
Interface
ComfyUI
FLUX
AI
Stable diffusion
Flux
Wiki
