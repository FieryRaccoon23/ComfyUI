[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Apply ControlNet (Advanced)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Apply ControlNet (Advanced)
💡
This node has been renamed to Apply ControlNet in the new version of ComfyUI, replacing the old version named Apply ControlNet (OLD). Since the previous Apply ControlNet (OLD) is currently somewhat similar to an enabled state, the latest documentation for this node has been moved to [Apply ControlNet](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply) for clarification.
![Apply ControlNet advance](https://comfyui-wiki.com/_next/static/media/Apply_ControlNet-advance.43a99f02.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply-advanced#documentation)
  * Class name: `ControlNetApplyAdvanced`
  * Category: `conditioning`
  * Output node: `False`


This node applies advanced control net transformations to conditioning data based on an image and a control net model. It allows for fine-tuned adjustments of the control net’s influence over the generated content, enabling more precise and varied modifications to the conditioning.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply-advanced#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | The positive conditioning data to which the control net transformations will be applied. It represents the desired attributes or features to enhance or maintain in the generated content.  
`negative` | `CONDITIONING` | The negative conditioning data, representing attributes or features to diminish or remove from the generated content. The control net transformations are applied to this data as well, allowing for a balanced adjustment of the content’s characteristics.  
`control_net` | `CONTROL_NET` | The control net model is crucial for defining the specific adjustments and enhancements to the conditioning data. It interprets the reference image and strength parameters to apply transformations, significantly influencing the final output by modifying attributes in both positive and negative conditioning data.  
`image` | `IMAGE` | The image serving as a reference for the control net transformations. It influences the adjustments made by the control net to the conditioning data, guiding the enhancement or suppression of specific features.  
`strength` | `FLOAT` | A scalar value determining the intensity of the control net’s influence on the conditioning data. Higher values result in more pronounced adjustments.  
`start_percent` | `FLOAT` | The starting percentage of the control net’s effect, allowing for gradual application of transformations over a specified range.  
`end_percent` | `FLOAT` | The ending percentage of the control net’s effect, defining the range over which the transformations are applied. This enables more nuanced control over the adjustment process.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply-advanced#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | The modified positive conditioning data after the application of control net transformations, reflecting the enhancements made based on the input parameters.  
`negative` | `CONDITIONING` | The modified negative conditioning data after the application of control net transformations, reflecting the suppression or removal of specific features based on the input parameters.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply "Apply ControlNet")[GLIGEN Text Box Apply](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/gligen/gligen-text-box-apply "GLIGEN Text Box Apply")
Discover more
ComfyUI
Wiki
Stable Diffusion
Workflow
Stable diffusion
AI
FLUX
SDXL
Artificial intelligence
Flux
