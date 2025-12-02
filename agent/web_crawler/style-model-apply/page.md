[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")style-modelApply Style Model
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Apply Style Model
![comfyUI节点-Apply Style model | 风格模型应用](https://comfyui-wiki.com/conditioning/style_model/Apply_Style_model.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/style-model/style-model-apply#documentation)
  * Class name: `StyleModelApply`
  * Category: `conditioning/style_model`
  * Output node: `False`


This node applies a style model to a given conditioning, enhancing or altering its style based on the output of a CLIP vision model. It integrates the style model’s conditioning into the existing conditioning, allowing for a seamless blend of styles in the generation process.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/style-model/style-model-apply#input-types)
### Required[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/style-model/style-model-apply#required)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The original conditioning data to which the style model’s conditioning will be applied. It’s crucial for defining the base context or style that will be enhanced or altered.  
`style_model` | `STYLE_MODEL` | The style model used to generate new conditioning based on the CLIP vision model’s output. It plays a key role in defining the new style to be applied.  
`clip_vision_output` | `CLIP_VISION_OUTPUT` | The output from a CLIP vision model, which is used by the style model to generate new conditioning. It provides the visual context necessary for style application.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/style-model/style-model-apply#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`conditioning` | `CONDITIONING` | The enhanced or altered conditioning, incorporating the style model’s output. It represents the final, styled conditioning ready for further processing or generation.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/inpaint/inpaint-model-conditioning "Inpaint Model Conditioning")[unCLIP Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/unclip-conditioning "unCLIP Conditioning")
Discover more
ComfyUI
Wiki
Stable diffusion
Workflow
Stable Diffusion
User interface
Flux.1
FLUX
Flux
stable diffusion
