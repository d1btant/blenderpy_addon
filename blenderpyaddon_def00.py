import bpy
import math

#定义选择活动物体函数
def selectobj(objn):
	obj = bpy.data.objects[objn]
	bpy.context.view_layer.objects.active = obj
	obj.select_set(True)

#定义取消选择物体函数
def unselectobj(objn):
    obj = bpy.data.objects[objn]
    bpy.context.view_layer.objects.active = obj
    obj.select_set(False)

#定义移除物体函数
def removeobj(objn):
	objn = bpy.data.meshes[objn]
	bpy.data.meshes.remove(objn)

#定义刷新视图函数
def vision_update():
	bpy.context.view_layer.update()

#定义物体移动函数
def moveobj(objn,x_value,y_value,z_value):
	selectobj(objn)
	bpy.ops.transform.translate(value=(x_value, y_value, z_value))
	unselectobj(objn)

#定义复制并移动物体函数
def duplobj(objn,x_value,y_value,z_value):
	selectobj(objn)
	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={ "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(x_value, y_value, z_value), })
	unselectobj(objn)

#定义hex转线性rgb函数
def hex_to_blender_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    gamma = 2.2
    def srgb_to_linear(c):
        if c < 0: return 0
        elif c < 0.04045: return c / 12.92
        else: return ((c + 0.055) / 1.055) ** gamma
    r_linear = srgb_to_linear(r)
    g_linear = srgb_to_linear(g)
    b_linear = srgb_to_linear(b)
    return (r_linear, g_linear, b_linear)

#定义材质颜色函数
def coloredobj(objn,bhex_value):
	hex_to_blender_rgb(bhex_value)
	selectobj(objn)
	r_value, g_value, b_value = hex_to_blender_rgb(bhex_value)
	bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (r_value, g_value, b_value,1)
	unselectobj(objn)

#定义新建材质函数
def newmaterial(objn,matn):
    selectobj(objn)
    obj = bpy.context.object
    obj.data.materials.append(bpy.data.materials.new(name=matn))
    obj.active_material.name=matn
    unselectobj(objn)
    