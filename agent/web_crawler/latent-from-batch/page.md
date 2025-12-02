[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Latent](https://comfyui-wiki.com/en/comfyui-nodes/latent/latent-upscale "Latent")[batch](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch "batch")Latent From Batch
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Latent From Batch
![comfyUI节点-Latent From Batch｜从批次获取Latent](https://comfyui-wiki.com/latent/batch/Latent_From_Batch.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-from-batch#documentation)
  * Class name: `LatentFromBatch`
  * Category: `latent/batch`
  * Output node: `False`


This node is designed to extract a specific subset of latent samples from a given batch based on the specified batch index and length. It allows for selective processing of latent samples, facilitating operations on smaller segments of the batch for efficiency or targeted manipulation.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-from-batch#input-types)
Parameter | Comfy dtype | Description  
---|---|---  
`samples` | `LATENT` | The collection of latent samples from which a subset will be extracted. This parameter is crucial for determining the source batch of samples to be processed.  
`batch_index` | `INT` | Specifies the starting index within the batch from which the subset of samples will begin. This parameter enables targeted extraction of samples from specific positions in the batch.  
`length` | `INT` | Defines the number of samples to be extracted from the specified starting index. This parameter controls the size of the subset to be processed, allowing for flexible manipulation of batch segments.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-from-batch#output-types)
Parameter | Comfy dtype | Description  
---|---|---  
`latent` | `LATENT` | The extracted subset of latent samples, now available for further processing or analysis.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/latent-batch "Latent Batch")[Rebatch Latents](https://comfyui-wiki.com/en/comfyui-nodes/latent/batch/rebatch-latents "Rebatch Latents")
