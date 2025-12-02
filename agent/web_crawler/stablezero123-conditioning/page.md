[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Conditioning3d-modelsStable Zero 123 Conditioning
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Stable Zero 123 Conditioning
![comfyUI节点-StableZero123_Conditioning|SZ123条件](https://comfyui-wiki.com/conditioning/3d_models/StableZero123_Conditioning.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning#documentation)
  * Class name: `StableZero123_Conditioning`
  * Category: `conditioning/3d_models`
  * Output node: `False`


This node is designed to process and condition data for use in StableZero123 models, focusing on preparing the input in a specific format that is compatible and optimized for these models.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_vision` | `CLIP_VISION` | Processes visual data to align with the model’s requirements, enhancing the model’s understanding of visual context.  
`init_image` | `IMAGE` | Serves as the initial image input for the model, setting the baseline for further image-based operations.  
`vae` | `VAE` | Integrates variational autoencoder outputs, facilitating the model’s ability to generate or modify images.  
`width` | `INT` | Specifies the width of the output image, allowing for dynamic resizing according to model needs.  
`height` | `INT` | Determines the height of the output image, enabling customization of the output dimensions.  
`batch_size` | `INT` | Controls the number of images processed in a single batch, optimizing computational efficiency.  
`elevation` | `FLOAT` | Adjusts the elevation angle for 3D model rendering, enhancing the model’s spatial understanding.  
`azimuth` | `FLOAT` | Modifies the azimuth angle for 3D model visualization, improving the model’s perception of orientation.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | Generates positive conditioning vectors, aiding in the model’s positive feature reinforcement.  
`negative` | `CONDITIONING` | Produces negative conditioning vectors, assisting in the model’s avoidance of certain features.  
`latent` | `LATENT` | Creates latent representations, facilitating deeper model insights into the data.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/model-merging/vae-save "VAE Save")[Stable Zero 123 Conditioning Batched](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning-batched "Stable Zero 123 Conditioning Batched")
Discover more
Wiki
Stable Diffusion
User interface
interface
Artificial intelligence
Flux
FLUX.1
Comfy
AI
Interface
