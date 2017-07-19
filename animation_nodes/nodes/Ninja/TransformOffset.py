import bpy
from ... base_types import AnimationNode

class NinjaTestNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_NinjaTestNode"
    bl_label = "Ninja Transform Test"

    def create(self):
        #inputs
        self.newInput("Object", "Source", "source")
        self.newInput("Object", "Target", "target")
        self.newInput("Vector", "Offset", "offset")
        self.newInput("Vector", "Scale_Offset", "scale_offset")


    def execute(self,source,target,offset, scale_offset):
        if source is None or target is None:
            return
        target.location = source.location + offset
        target.scale = source.scale + scale_offset
