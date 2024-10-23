import bpy
import math

def selectobj(objn):
	obj = bpy.data.objects[objn]
	bpy.context.view_layer.objects.active = obj
	obj.select_set(True)

def unselectobj(objn):
    obj = bpy.data.objects[objn]
    bpy.context.view_layer.objects.active = obj
    obj.select_set(False)

def hex_to_blender_rgb(hex_color):
    # 去除可能的'#'字符
    hex_color = hex_color.lstrip('#')
    
    # 将十六进制颜色值转换为RGB
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    # 将RGB值从0-255转换为0-1
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    
    # 应用Gamma校正（sRGB到线性RGB的转换）
    gamma = 2.2
    def srgb_to_linear(c):
        if c < 0: return 0
        elif c < 0.04045: return c / 12.92
        else: return ((c + 0.055) / 1.055) ** gamma
    r_linear = srgb_to_linear(r)
    g_linear = srgb_to_linear(g)
    b_linear = srgb_to_linear(b)
    return (r_linear, g_linear, b_linear)

def colored(bhex_value):
	hex_to_blender_rgb(bhex_value)
	selectobj(objn)
	r_value, g_value, b_value = hex_to_blender_rgb(bhex_value)
	bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (r_value, g_value, b_value,1)
	unselectobj(objn)

bhex_value=input("bhex_value:")
objn=input("objn:")
colored(bhex_value)
bpy.context.view_layer.update()
