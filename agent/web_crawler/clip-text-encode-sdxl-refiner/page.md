[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Advanced[conditioning](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl "conditioning")CLIP Text Encode SDXL Refiner
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# CLIP Text Encode SDXL Refiner
![comfyUI节点-ConditinoingSetTimstepRange|设置条件时间](https://comfyui-wiki.com/advanced/conditioning/CLIPTextEncodeSDXLRefiner.jpg)
## CLIPTextEncodeSDXLRefiner Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl-refiner#cliptextencodesdxlrefiner-documentation)
  * Class name: `CLIPTextEncodeSDXLRefiner`
  * Category: `advanced/conditioning`
  * Output node: `False`


This node specializes in refining the encoding of text inputs using CLIP models, enhancing the conditioning for generative tasks by incorporating aesthetic scores and dimensions.
## CLIPTextEncodeSDXLRefiner Input types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl-refiner#cliptextencodesdxlrefiner-input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip` | `CLIP` | A CLIP model instance used for text tokenization and encoding, central to generating the conditioning.  
`ascore` | `FLOAT` | The aesthetic score parameter influences the conditioning output by providing a measure of aesthetic quality.  
`width` | `INT` | Specifies the width of the output conditioning, affecting the dimensions of the generated content.  
`height` | `INT` | Determines the height of the output conditioning, influencing the dimensions of the generated content.  
`text` | `STRING` | The text input to be encoded, serving as the primary content descriptor for conditioning.  
## CLIPTextEncodeSDXLRefiner Output types[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl-refiner#cliptextencodesdxlrefiner-output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The refined conditioning output, enriched with aesthetic scores and dimensions for enhanced content generation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip-text-encode-sdxl "CLIP Text Encode SDXL")[CLIP Text Encode Hunyuan DiT](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning/clip_text_encode_hunyuan_dit "CLIP Text Encode Hunyuan DiT")
Discover more
SDXL
Stable diffusion
ComfyUI
Workflow
Stable Diffusion
Sdxl
interface
FLUX
Flux.1
stable diffusion
