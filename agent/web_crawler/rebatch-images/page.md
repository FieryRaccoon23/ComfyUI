[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Image](https://comfyui-wiki.com/en/comfyui-nodes/image/animation "Image")[batch](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch "batch")Rebatch Images
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Rebatch Images
![comfyUI节点- Rebatch Images|重设图像批次](https://comfyui-wiki.com/image/batch/Rebatch_Images.jpg)
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/rebatch-images#documentation)
  * Class name: `RebatchImages`
  * Category: `image/batch`
  * Output node: `False`


The RebatchImages node is designed to reorganize a batch of images into a new batch configuration, adjusting the batch size as specified. This process is essential for managing and optimizing the processing of image data in batch operations, ensuring that images are grouped according to the desired batch size for efficient handling.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/rebatch-images#input-types)
Field | Comfy dtype | Description  
---|---|---  
`images` | `IMAGE` | A list of images to be rebatched. This parameter is crucial for determining the input data that will undergo the rebatching process.  
`batch_size` | `INT` | Specifies the desired size of the output batches. This parameter directly influences how the input images are grouped and processed, impacting the structure of the output.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/rebatch-images#output-types)
Field | Comfy dtype | Description  
---|---|---  
`image` | `IMAGE` | The output consists of a list of image batches, reorganized according to the specified batch size. This allows for flexible and efficient processing of image data in batch operations.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/image-from-batch "Image From Batch")[Repeat Image Batch](https://comfyui-wiki.com/en/comfyui-nodes/image/batch/repeat-image-batch "Repeat Image Batch")
Discover more
Wiki
Stable diffusion
Workflow
ComfyUI
Batch processing
batch operations
Stable Diffusion
Black Forest Labs
Comfy
stable diffusion
