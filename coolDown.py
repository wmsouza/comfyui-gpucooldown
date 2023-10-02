import time
import GPUtil
 
class CoolDown:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { "latent": ("LATENT",),
                              "maxTemperature": ("INT", {"default": 70, "min": 50, "max": 90}),
                              }}
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "CoolDown"

    CATEGORY = "utils"
 
    def CoolDown(self, latent, maxTemperature):
        while True:
            tooHot = False
            for gpu in GPUtil.getGPUs():
                if gpu.temperature > maxTemperature:
                    tooHot = True
                    print("Waiting... GPU is too hot!", gpu.temperature, "C")

            if tooHot:
                time.sleep(2)
            else:
                break

        return (latent,)