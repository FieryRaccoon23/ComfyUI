[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[batch](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch "batch")Repeat Image Batch
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Repeat Image Batch
![comfyUI节点-RepeatImageBatch|复制图像批次](https://comfyui-wiki.com/image/batch/RepeatImageBatch.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/repeat-image-batch#documentation)
  * Class name: `RepeatImageBatch`
  * Category: `image/batch`
  * Output node: `False`


The RepeatImageBatch node is designed to replicate a given image a specified number of times, creating a batch of identical images. This functionality is useful for operations that require multiple instances of the same image, such as batch processing or data augmentation.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/repeat-image-batch#input-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The ‘image’ parameter represents the image to be replicated. It is crucial for defining the content that will be duplicated across the batch.  
`amount` | `INT` | The ‘amount’ parameter specifies the number of times the input image should be replicated. It directly influences the size of the output batch, allowing for flexible batch creation.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/repeat-image-batch#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output is a batch of images, each identical to the input image, replicated according to the specified ‘amount’.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/rebatch-images "Rebatch Images")[Empty Image](https://comfyui-wiki.com/en/comfyui-nodes/image/empty-image "Empty Image")
Discover more
Stable diffusion
Batch processing
Wiki
Stable Diffusion
batch processing
ComfyUI
Flux
stable diffusion
Black Forest Labs
Sdxl
