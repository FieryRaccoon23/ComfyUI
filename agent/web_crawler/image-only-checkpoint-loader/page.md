[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")video-modelsImage Only Checkpoint Loader (img2vid model)
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Image Only Checkpoint Loader (img2vid model)
![comfyUI节点-Image Only Checkpoint Loader\(img2vid model\)｜Checkpoint加载器（仅图像](https://comfyui-wiki.com/loaders/video_models/Image_Only_Checkpoint_Loader\(img2vid_model\).jpg)
This node will detect models located in the `ComfyUI/models/checkpoints` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/video-models/image-only-checkpoint-loader#documentation)
  * Class name: `ImageOnlyCheckpointLoader`
  * Category: `loaders/video_models`
  * Output node: `False`


This node specializes in loading checkpoints specifically for image-based models within video generation workflows. It efficiently retrieves and configures the necessary components from a given checkpoint, focusing on image-related aspects of the model.
## Input types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/video-models/image-only-checkpoint-loader#input-types)
Field | Comfy dtype | Description  
---|---|---  
`ckpt_name` | `COMBO[STRING]` | Specifies the name of the checkpoint to load, crucial for identifying and retrieving the correct checkpoint file from a predefined list.  
## Output types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/video-models/image-only-checkpoint-loader#output-types)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | Returns the main model loaded from the checkpoint, configured for image processing within video generation contexts.  
`clip_vision` | `CLIP_VISION` | Provides the CLIP vision component from the checkpoint, tailored for image understanding and feature extraction.  
`vae` | `VAE` | Delivers the Variational Autoencoder (VAE) component, essential for image manipulation and generation tasks.  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/vae-loader "VAE Loader")[Join Image with Alpha](https://comfyui-wiki.com/en/comfyui-nodes/mask/compositing/join-image-with-alpha "Join Image with Alpha")
Discover more
Workflow
Wiki
Video
video
workflows
ComfyUI
Stable diffusion
stable diffusion
AI
Artificial intelligence
