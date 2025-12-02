[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")batchImage From Batch
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image From Batch
![ImageFromBatch-comfyui node](https://comfyui-wiki.com/image/batch/ImageFromBatch.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch#documentation)
  * Class name: `ImageFromBatch`
  * Category: `image/batch`
  * Output node: `False`


The ImageFromBatch node is designed for extracting a specific segment of images from a batch based on the provided index and length. It allows for more granular control over the batched images, enabling operations on individual or subsets of images within a larger batch.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch#input-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The batch of images from which a segment will be extracted. This parameter is crucial for specifying the source batch.  
`batch_index` | `INT` | The starting index within the batch from which the extraction begins. It determines the initial position of the segment to be extracted from the batch.  
`length` | `INT` | The number of images to extract from the batch starting from the batch_index. This parameter defines the size of the segment to be extracted.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The extracted segment of images from the specified batch. This output represents a subset of the original batch, determined by the batch_index and length parameters.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/animation/save-animated-webp "Save Animated WEBP")[Rebatch Images](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/rebatch-images "Rebatch Images")
Discover more
ComfyUI
Stable diffusion
Stable Diffusion
Workflow
Wiki
user interface
FLUX.1
Sdxl
Flux
Black Forest Labs
