import time
import GPUtil
 
class CoolDown:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "latent": ("LATENT",),
                              "maxTemp": ("INT", {"default": 70, "min": 50, "max": 90}),
                              }}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "CoolDown"
 
    CATEGORY = "utils"
 
    def CoolDown(self, latent, maxTemp):
        while True:
            tooHot = False
            for gpu in GPUtil.getGPUs():
                if gpu.temperature > maxTemp:
                    tooHot = True
                    print("Waiting... GPU is too hot!", gpu.temperature, "C")

            if tooHot:
                time.sleep(2)
            else:
                break

        return (latent,)
 
NODE_CLASS_MAPPINGS = {
"CoolDown": CoolDown,
}
# Human readable names for the nodes
 
NODE_DISPLAY_NAME_MAPPINGS = {
"CoolDown": "CoolDown",
}