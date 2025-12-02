[Nodes Manual](https://comfyui-wiki.com/en/comfyui-nodes "Nodes Manual")[Conditioning](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/3d-models "Conditioning")Apply ControlNet
### [Alibaba Cloud PAI Releases Z-Image-Turbo-Fun-Controlnet-Union - Multi-Condition ControlNet Model](https://comfyui-wiki.com/en/news/2025-12-02-z-image-turbo-controlnet-union)
12/01/2025
# Apply ControlNet
💡
This documentation is for the original `Apply ControlNet(Advanced)` node. The earliest `Apply ControlNet` node has been renamed to `Apply ControlNet(Old)`. While you may still see the `Apply ControlNet(Old)` node in many workflow folders you download from comfyui.org for compatibility reasons, you can no longer find the `Apply ControlNet(Old)` node through search or node list. Please use the `Apply ControlNet` node instead.
![Apply ControlNet](https://comfyui-wiki.com/_next/static/media/apply-controlnet.e906d535.jpg)
This node applies a ControlNet to a given image and conditioning, adjusting the image’s attributes based on the control network’s parameters and specified strength, such as Depth, OpenPose, Canny, HED, etc.
### Documentation[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#documentation)
  * Class name: `ControlNetApply`
  * Category: `conditioning`
  * Output node: `False`


Using controlNet requires preprocessing of input images. Since ComfyUI initial nodes do not come with preprocessors and controlNet models, please first install ContrlNet preprocessors 
### Input Types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#input-types)
Parameter | Data Type | Function  
---|---|---  
`positive` | `CONDITIONING` | Positive conditioning data, from [CLIP Text Encoder](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode) or other conditioning inputs  
`negative` | `CONDITIONING` | Negative conditioning data, from [CLIP Text Encoder](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode) or other conditioning inputs  
`control_net` | `CONTROL_NET` | The controlNet model to apply, typically input from [ControlNet Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader)  
`image` | `IMAGE` | Image for controlNet application, needs to be processed by preprocessor  
`vae` | `VAE` | Vae model input  
`strength` | `FLOAT` | Controls the strength of network adjustments, value range 0~~10. Recommended values between 0.5~~ 1.5 are reasonable. Lower values allow more model freedom, higher values impose stricter constraints. Too high values may result in strange images. You can test and adjust this value to fine-tune the control network’s influence.  
`start_percent` | `FLOAT` | Value 0.000~1.000, determines when to start applying controlNet as a percentage, e.g., 0.2 means ControlNet guidance will start influencing image generation at 20% of the diffusion process  
`end_percent` | `FLOAT` | Value 0.000~1.000, determines when to stop applying controlNet as a percentage, e.g., 0.8 means ControlNet guidance will stop influencing image generation at 80% of the diffusion process  
### Output Types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#output-types)
Parameter | Data Type | Function  
---|---|---  
`positive` | `CONDITIONING` | Positive conditioning data processed by ControlNet, can be output to next ControlNet or K Sampler nodes  
`negative` | `CONDITIONING` | Negative conditioning data processed by ControlNet, can be output to next ControlNet or K Sampler nodes  
💡
If you want to use **T2IAdaptor style models** , please use the `Apply Style Model` node instead
## ComfyUI ControlNet Usage Examples[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#comfyui-controlnet-usage-examples)
Visit the following pages for examples:
  * [ComfyUI OpenPose ControlNet Usage Example](https://comfyui-wiki.com/en/tutorial/advanced/how-to-use-openpose-controlnet-with-sd1.5)
  * [ComfyUI Depth ControlNet Usage Example](https://comfyui-wiki.com/en/tutorial/advanced/how-to-use-depth-controlnet-with-sd1.5)
  * [ComfyUI Canny ControlNet Usage Example](https://comfyui-wiki.com/en/tutorial/advanced/how-to-use-canny-controlnet-with-sd1.5)
  * [ComfyUI Multi ControlNet Usage Example](https://comfyui-wiki.com/en/tutorial/advanced/how-to-use-muti-contorlnet-in-comfyui)


## Related Resources[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#related-resources)
  * Model Resources: [controlNet Model Resources Download](https://comfyui-wiki.com/en/resource/controlnet-models)
  * Preprocessor Plugin: 


## Apply ControlNet (OLD) Node Description[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-node-description)
![Apply ControlNet](https://comfyui-wiki.com/_next/static/media/Apply_ControlNet.b992918d.jpg) This is an early version of the Apply ControlNet node. The node options have been updated, but for compatibility, if you download workflows using the old version node in ComfyUI, it will display as this node. You can switch to the new Apply ControlNet node.
### Apply ControlNet (OLD) Input Types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-input-types)
Parameter | Data Type | Function  
---|---|---  
`conditioning` | `CONDITIONING` | Conditioning data from [CLIP Text Encoder](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/clip-text-encode) or other conditioning inputs (such as input from another conditioning node)  
`control_net` | `CONTROL_NET` | The controlNet model to apply, typically input from [ControlNet Loader](https://comfyui-wiki.com/en/comfyui-nodes/loaders/controlnet-loader)  
`image` | `IMAGE` | Image for controlNet application, needs to be processed by preprocessor  
`strength` | `FLOAT` | Controls the strength of network adjustments, value range 0~~10. Recommended values between 0.5~~ 1.5 are reasonable. Lower values allow more model freedom, higher values impose stricter constraints. Too high values may result in strange images.  
### Apply ControlNet (OLD) Output Types[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply#apply-controlnet-old-output-types)
Parameter | Data Type | Function  
---|---|---  
`conditioning` | `CONDITIONING` | Conditioning data processed by ControlNet, can be output to next ControlNet or K Sampler nodes  
Last updated on August 10, 2025
[](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/conditioning-set-mask "Conditioning \(Set Mask\)")[Apply ControlNet (Advanced)](https://comfyui-wiki.com/en/comfyui-nodes/conditioning/controlnet-apply-advanced "Apply ControlNet \(Advanced\)")
Discover more
comfyui
Stable diffusion
ComfyUI
workflow
workflows
Workflow
Wiki
Stable Diffusion
stable diffusion
User interface
