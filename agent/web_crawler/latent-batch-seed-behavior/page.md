[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[advanced](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add "advanced")Latent Batch Seed Behavior
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent Batch Seed Behavior
![LatentBatchSeedBehavior-Latent批次随机种操作](https://comfyui-wiki.com/latent/advanced/LatentBatchSeedBehavior.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-batch-seed-behavior#documentation)
  * Class name: `LatentBatchSeedBehavior`
  * Category: `latent/advanced`
  * Output node: `False`


The LatentBatchSeedBehavior node is designed to modify the seed behavior of a batch of latent samples. It allows for either randomizing or fixing the seed across the batch, thereby influencing the generation process by either introducing variability or maintaining consistency in the generated outputs.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-batch-seed-behavior#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The ‘samples’ parameter represents the batch of latent samples to be processed. Its modification depends on the seed behavior chosen, affecting the consistency or variability of the generated outputs.  
`seed_behavior` | `COMBO[STRING]` | The ‘seed_behavior’ parameter dictates whether the seed for the batch of latent samples should be randomized or fixed. This choice significantly impacts the generation process by either introducing variability or ensuring consistency across the batch.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-batch-seed-behavior#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The output is a modified version of the input latent samples, with adjustments made based on the specified seed behavior. It either maintains or alters the batch index to reflect the chosen seed behavior.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-add "Latent Add")[Latent Interpolate](https://comfyui-wiki.com/en/comfyui-nodes/latent/advanced/latent-interpolate "Latent Interpolate")
Discover more
Stable diffusion
Wiki
ComfyUI
Workflow
Stable Diffusion
User interface
Interface
Flux.1
AI
Comfy
