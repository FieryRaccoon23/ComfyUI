[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")inpaintInpaint Model Conditioning
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Inpaint Model Conditioning
![comfyUI节点-inpaintModelConditioning｜内补模型条件](https://comfyui-wiki.com/conditioning/inpaint/inpaintModelConditioning.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/inpaint/inpaint-model-conditioning#documentation)
  * Class name: `InpaintModelConditioning`
  * Category: `conditioning/inpaint`
  * Output node: `False`


The InpaintModelConditioning node is designed to facilitate the conditioning process for inpainting models, enabling the integration and manipulation of various conditioning inputs to tailor the inpainting output. It encompasses a broad range of functionalities, from loading specific model checkpoints and applying style or control net models, to encoding and combining conditioning elements, thereby serving as a comprehensive tool for customizing inpainting tasks.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/inpaint/inpaint-model-conditioning#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | Represents the positive conditioning information or parameters that are to be applied to the inpainting model. This input is crucial for defining the context or constraints under which the inpainting operation should be performed, affecting the final output significantly.  
`negative` | `CONDITIONING` | Represents the negative conditioning information or parameters that are to be applied to the inpainting model. This input is essential for specifying the conditions or contexts to avoid during the inpainting process, thereby influencing the final output.  
`vae` | `VAE` | Specifies the VAE model to be used in the conditioning process. This input is crucial for determining the specific architecture and parameters of the VAE model that will be utilized.  
`pixels` | `IMAGE` | Represents the pixel data of the image to be inpainted. This input is essential for providing the visual context necessary for the inpainting task.  
`mask` | `MASK` | Specifies the mask to be applied to the image, indicating the areas to be inpainted. This input is crucial for defining the specific regions within the image that require inpainting.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/inpaint/inpaint-model-conditioning#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | The modified positive conditioning information after processing, ready to be applied to the inpainting model. This output is essential for guiding the inpainting process according to the specified positive conditions.  
`negative` | `CONDITIONING` | The modified negative conditioning information after processing, ready to be applied to the inpainting model. This output is essential for guiding the inpainting process according to the specified negative conditions.  
`latent` | `LATENT` | The latent representation derived from the conditioning process. This output is crucial for understanding the underlying features and characteristics of the image being inpainted.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/gligen/gligen-text-box-apply "GLIGEN Text Box Apply")[Apply Style Model](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/style-model/style-model-apply "Apply Style Model")
Discover more
ComfyUI
Stable diffusion
Workflow
Inpaint
Wiki
Stable Diffusion
Comfy
Interface
stable diffusion
user interface
