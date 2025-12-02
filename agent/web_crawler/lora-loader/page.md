[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Loaders](https://comfyui-wiki.com/en/comfyui-nodes/loaders/checkpoint-loader-simple "Loaders")Lora Loader - ComfyUI Node Documentation
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Load LoRA
![LoRA Loader Node](https://comfyui-wiki.com/_next/static/media/Load_LoRA.57b3d715.jpg)
This node automatically detects models located in the LoRA folder (including subfolders) with the corresponding model path being `ComfyUI\models\loras`. For more information, please refer to [Installing LoRA Models](https://comfyui-wiki.com/en/install/install-models/install-lora)
The LoRA Loader node is primarily used to load LoRA models. You can think of LoRA models as filters that can give your images specific styles, content, and details:
  * Apply specific artistic styles (like ink painting)
  * Add characteristics of certain characters (like game characters)
  * Add specific details to the image All of these can be achieved through LoRA.


If you need to load multiple LoRA models, you can directly chain multiple nodes together, as shown below: ![Loading Multiple Models](https://comfyui-wiki.com/_next/static/media/Load_LoRA-2.42e277fb.jpg)
## Input Types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader#input-types)
Parameter Name | Data Type | Function  
---|---|---  
`model` | MODEL | Typically used to connect to the base model  
`clip` | CLIP | Typically used to connect to the CLIP model  
`lora_name` | COMBO[STRING] | Select the name of the LoRA model to use  
`strength_model` | FLOAT | Value range from -100.0 to 100.0, typically used between 0~1 for daily image generation. Higher values result in more pronounced model adjustment effects  
`strength_clip` | FLOAT | Value range from -100.0 to 100.0, typically used between 0~1 for daily image generation. Higher values result in more pronounced model adjustment effects  
## Output Types[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader#output-types)
Parameter Name | Data Type | Function  
---|---|---  
`model` | MODEL | The model with LoRA adjustments applied  
`clip` | CLIP | The CLIP instance with LoRA adjustments applied  
## Additional LoRA Information[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader#additional-lora-information)
  1. **LoRA Flexibility:**
     * LoRA can quickly generate specific style images by fine-tuning existing models without retraining the entire model. It’s an “artist’s tool” that allows for more precise control over image effects.
  2. **Resource Efficiency:**
     * Using LoRA models requires fewer computational resources, avoiding the time cost of large-scale model training. It only needs to fine-tune for target effects, making it both efficient and resource-saving.
  3. **Diverse Applications:**
     * LoRA can not only change character appearances but also adjust backgrounds, color tones, lighting, weather, and other elements, adding rich details to your work.
  4. **Customization and Compatibility:**
     * LoRA models support personalized customization, allowing you to create custom LoRA models based on needs and combine multiple LoRA models to achieve more complex effects.
  5. **Adaptation to Different Domains:**
     * LoRA is not limited to artistic styles and character features; it can also be used to adjust mood atmosphere, change lighting environments, add specific object details, and more.


### Examples:[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader#examples)
  * **Ink Painting Style** : LoRA models can adjust color rendering and brush strokes to simulate the layered feel of ink paintings.
  * **Game Character Features** : LoRA can adjust character details like clothing and hairstyles to create game character styles.


## Usage Examples and Workflows[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader#usage-examples-and-workflows)
[SD1.5 Basic LoRA Workflow](https://comfyui-wiki.com/en/tutorial/basic/lora) [ComfyUI Basic LoRA Workflow](https://comfyui-wiki.com/en/workflows/lora)
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/loaders/hypernetwork-loader "Hypernetwork Loader")[Lora Loader Model Only](https://comfyui-wiki.com/en/comfyui-nodes/loaders/lora-loader-model-only "Lora Loader Model Only")
Discover more
Workflows
ComfyUI
Stable Diffusion
Stable diffusion
Wiki
Workflow
stable diffusion
AI
interface
Flux.1
