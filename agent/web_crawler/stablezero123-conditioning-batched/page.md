[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")Conditioning[3d-models](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning "3d-models")Stable Zero 123 Conditioning Batched
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Stable Zero 123 Conditioning Batched
![comfyUI节点-StableZero123_Conditioning_Batched|SZ123条件\(批次\)](https://comfyui-wiki.com/conditioning/3d_models/StableZero123_Conditioning_Batched.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning-batched#documentation)
  * Class name: `StableZero123_Conditioning_Batched`
  * Category: `conditioning/3d_models`
  * Output node: `False`


This node is designed to process conditioning information in a batched manner specifically tailored for the StableZero123 model. It focuses on efficiently handling multiple sets of conditioning data simultaneously, optimizing the workflow for scenarios where batch processing is crucial.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning-batched#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`clip_vision` | `CLIP_VISION` | The CLIP vision embeddings that provide visual context for the conditioning process.  
`init_image` | `IMAGE` | The initial image to be conditioned upon, serving as a starting point for the generation process.  
`vae` | `VAE` | The variational autoencoder used for encoding and decoding images in the conditioning process.  
`width` | `INT` | The width of the output image.  
`height` | `INT` | The height of the output image.  
`batch_size` | `INT` | The number of conditioning sets to be processed in a single batch.  
`elevation` | `FLOAT` | The elevation angle for 3D model conditioning, affecting the perspective of the generated image.  
`azimuth` | `FLOAT` | The azimuth angle for 3D model conditioning, affecting the orientation of the generated image.  
`elevation_batch_increment` | `FLOAT` | The incremental change in elevation angle across the batch, allowing for varied perspectives.  
`azimuth_batch_increment` | `FLOAT` | The incremental change in azimuth angle across the batch, allowing for varied orientations.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning-batched#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`positive` | `CONDITIONING` | The positive conditioning output, tailored for promoting certain features or aspects in the generated content.  
`negative` | `CONDITIONING` | The negative conditioning output, tailored for demoting certain features or aspects in the generated content.  
`latent` | `LATENT` | The latent representation derived from the conditioning process, ready for further processing or generation steps.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models/stablezero123-conditioning "Stable Zero 123 Conditioning")[CLIP Set Last Layer](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-set-last-layer "CLIP Set Last Layer")
Discover more
Stable Diffusion
Workflow
ComfyUI
Stable diffusion
workflow
SDXL
Flux.1
stable diffusion
User interface
user interface
