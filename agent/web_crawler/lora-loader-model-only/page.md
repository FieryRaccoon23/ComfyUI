[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")Lora Loader Model Only
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Lora Loader Model Only
![comfyUI节点-LoraLoaderModelOnly｜Lora加载器（仅模型](https://comfyui-wiki.com/loaders/LoraLoaderModelOnly.jpg)
This node will detect models located in the `ComfyUI/models/loras` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.
## Documentation - Lora Loader Model Only[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only#documentation---lora-loader-model-only)
  * Class name: `LoraLoaderModelOnly`
  * Category: `loaders`
  * Output node: `False`


This node specializes in loading a LoRA model without requiring a CLIP model, focusing on enhancing or modifying a given model based on LoRA parameters. It allows for the dynamic adjustment of the model’s strength through LoRA parameters, facilitating fine-tuned control over the model’s behavior.
## Prerequisites[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only#prerequisites)
Before using this node, please ensure that you have installed the relevant model files in your ComfyUI model directory and that the `Lora Loader Model Only` node can read the model files correctly.
If you are unsure where to download LoRA models, here are some resources I recommend:
[Lora Models Resource](https://comfyui-wiki.com/en/resource/lora-models)
If you are unsure how to install, here is a tutorial on installing LoRA models:
[Install LoRA Models Guide](https://comfyui-wiki.com/en/install/install-models/install-lora)
## Input types - Lora Loader Model Only[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only#input-types---lora-loader-model-only)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The base model for modifications, to which LoRA adjustments will be applied.  
`lora_name` | `COMBO[STRING]` | The name of the LoRA file to be loaded, specifying the adjustments to apply to the model.  
`strength_model` | `FLOAT` | Determines the intensity of the LoRA adjustments, with higher values indicating stronger modifications.  
## Output types - Lora Loader Model Only[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only#output-types---lora-loader-model-only)
Field | Comfy dtype | Description  
---|---|---  
`model` | `MODEL` | The modified model with LoRA adjustments applied, reflecting changes in model behavior or capabilities.  
## Lora Loader Model Only Workflow Example[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only#lora-loader-model-only-workflow-example)
LoRA LOader Model Only Toy you workflow
From 
## What is LoRA?[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only#what-is-lora)
Imagine that the Stable Diffusion AI image generator model is like an experienced chef, who has a set of basic cooking techniques and recipes that allow them to create delicious dishes based on given ingredients and instructions. However, different customers may have different tastes and preferences, and this is where adjustments to the basic cooking methods come into play.
LoRA models can be compared to a set of advanced spices and seasonings that can be added to a dish in small amounts to change its flavor, making it more appealing to specific customers. These spices and seasonings may not add much in quantity, but their impact on the dish is significant.
  1. Basic Recipe (Stable Diffusion): This is like the chef’s basic recipe, which provides a general method for generating images.
  2. Personalized Adjustments (LoRA Models): This is like the chef adding specific spices to the dish based on the customer’s taste, which fine-tunes the AI model parameters to generate images with specific styles or characteristics.
  3. Low-Rank Matrix (Technology in LoRA): This can be compared to a carefully selected combination of spices, which are added to the dish in small amounts but can significantly change the taste.
  4. Final Dish (Generated Images): This is like the final dish that is served, which is more appealing to the user due to the personalized adjustments made by the LoRA model.


By fine-tuning with LoRA models, the Stable Diffusion AI image generator model can create “delicious dishes” that are both aesthetically pleasing and tailored to individual preferences, just like a chef can create dishes that satisfy different customers.
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader "Lora Loader - ComfyUI Node Documentation")[Style Model Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/style-model-loader "Style Model Loader")
Discover more
Wiki
workflow
Stable Diffusion
Stable diffusion
ComfyUI
Workflow
workflows
AI
Interface
FLUX.1
