import bpy
from bpy.props import *
from math import sin, cos, pi
from ... data_structures import Vector3DList
from ... base_types import AnimationNode

modeItems = [
    ("LINE", "Line", "Distribute Points on line", "", 0),
    ("CIRCLE", "Circle", "Distribute points on circle", "", 1)
]


class GeneratePointsNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_GeneratePointsNode"
    bl_label = "Ninja_Generate_Points"

    mode = EnumProperty(name = "Mode", default = "LINE",
        items = modeItems, update = AnimationNode.refresh)

    def create(self):
        self.newInput("Integer", "Amount", "amount")
        if self.mode == "LINE":
            self.newInput("Vector", "Start", "start")
            self.newInput("Vector", "Direction", "direction")
        elif self.mode == "CIRCLE":
            self.newInput("Float", "Radius", "radius")
        self.newOutput("Vector List", "Points", "points" )

    def draw(self, layout):
        layout.prop(self, "mode")

    def getExecutionFunctionName(self):
        if self.mode == "LINE":
            return "execute_Line"
        elif self.mode == "CIRCLE":
            return "execute_Circle"

    def execute_Line(self, amount, start, direction):
        points = Vector3DList()
        for i in range(amount):
            points.append(start + i * direction)
        return points

    def execute_Circle(self, amount, radius):
        points = Vector3DList()
        if amount <= 0: return points
        factor = 2 * pi / amount
        for i in range(amount):
            points.append((cos(i * factor) * radius, sin(i * factor) * radius, 0))
        return points
