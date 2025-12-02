[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Advanced](https://comfyui-wiki.com/en/comfyui-nodes/advanced/conditioning "Advanced")[loaders](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/clip-loader "loaders")QuadrupleCLIPLoader
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# ComfyUI QuadrupleCLIPLoader Node
![ComfyUI QuadrupleCLIPLoader](https://comfyui-wiki.com/_next/static/media/QuadrupleCLIPLoader.4526569f.jpg)
The Quadruple CLIP Loader, QuadrupleCLIPLoader, is one of the core nodes of ComfyUI, first added to support the HiDream I1 version model. If you find this node missing, try updating ComfyUI to the latest version to ensure node support.
It requires 4 CLIP models, corresponding to the parameters `clip_name1`, `clip_name2`, `clip_name3`, and `clip_name4`, and will provide a CLIP model output for subsequent nodes.
This node will detect models located in the `ComfyUI/models/text_encoders` folder, and it will also read models from additional paths configured in the [extra_model_paths.yaml](https://comfyui-wiki.com/en/tutorial/basic/link-models-between-comfyui-and-a1111) file. Sometimes, after adding models, you may need to **reload the ComfyUI interface** to allow it to read the model files in the corresponding folder.
## QuadrupleCLIPLoader Node Source Code[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/quadruple-clip-loader#quadruplecliploader-node-source-code)
Code version 
```
class QuadrupleCLIPLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "clip_name1": (folder_paths.get_filename_list("text_encoders"), ),
                              "clip_name2": (folder_paths.get_filename_list("text_encoders"), ),
                              "clip_name3": (folder_paths.get_filename_list("text_encoders"), ),
                              "clip_name4": (folder_paths.get_filename_list("text_encoders"), )
                             }}
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "load_clip"
    CATEGORY = "advanced/loaders"
    DESCRIPTION = "[Recipes]\n\nhidream: long clip-l, long clip-g, t5xxl, llama_8b_3.1_instruct"
    def load_clip(self, clip_name1, clip_name2, clip_name3, clip_name4):
        clip_path1 = folder_paths.get_full_path_or_raise("text_encoders", clip_name1)
        clip_path2 = folder_paths.get_full_path_or_raise("text_encoders", clip_name2)
        clip_path3 = folder_paths.get_full_path_or_raise("text_encoders", clip_name3)
        clip_path4 = folder_paths.get_full_path_or_raise("text_encoders", clip_name4)
        clip = comfy.sd.load_clip(ckpt_paths=[clip_path1, clip_path2, clip_path3, clip_path4], embedding_directory=folder_paths.get_folder_paths("embeddings"))
        return (clip,)
NODE_CLASS_MAPPINGS = {
    "QuadrupleCLIPLoader": QuadrupleCLIPLoader,
}
```

## QuadrupleCLIPLoader Node Example Workflow[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/quadruple-clip-loader#quadruplecliploader-node-example-workflow)
Please visit the tutorial below to see examples of using the QuadrupleCLIPLoader node [ComfyUI HiDream-I1 Text-to-Image Workflow Example](https://comfyui-wiki.com/en/tutorial/advanced/image/hidream/i1-t2i)
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/dual-clip-loader "Dual CLIP Loader - How it work and how to use it.")[UNET Loader Guide | Load Diffusion Model - Documentation & Example](https://comfyui-wiki.com/en/comfyui-nodes/advanced/loaders/unet-loader "UNET Loader Guide | Load Diffusion Model - Documentation & Example")
Discover more
Stable Diffusion
Workflow
Stable diffusion
ComfyUI
stable diffusion
FLUX
AI
Flux.1
Artificial intelligence
User interface
