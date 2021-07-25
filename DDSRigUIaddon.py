bl_info = {
    "name": "DDS Rigging UI",
    "author": "Dwayne Savage",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D View->Properties Region",
    "description": "Rigging UI.",
    "warning": "",
    "wiki_url": "https://blenderclassroom.com",
    "category": "3D View",
    }


import bpy

rig_id = "Temp"

class DDSRigUI(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "DDS"
    bl_label = rig_id+" Rig UI"
    bl_idname = "VIEW3D_PT_DDS_"+rig_id
    
    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.type == "ARMATURE")
        except(AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        od = context.active_object.data
        col = self.layout.column(align=True)
        row = col.row(align=True)
        row.prop(od, "show_bone_custom_shapes", toggle=True, text="Shape")
        row.prop(od, "display_type", text="")
        row = col.row(align=True)
        row.prop(context.active_object, "show_in_front", toggle=True, text="In Front")
        if hasattr(od, "axes_position"):
            row.prop(od, "show_group_colors", toggle=True, text="Color")
            row = col.row(align=True)
            row.prop(od, "show_axes", toggle=True, text="Axis")
            row.prop(od, "axes_position", toggle=True, text="")
        else:
            row.prop(od, "show_axes", toggle=True, text="Axis")
            row.prop(od, "show_group_colors", toggle=True, text="Color")
    #hidden            
        row = col.row(align=True)
        row.separator(factor=0.5)
        row = col.row(align=True)        
        row.prop(od, "layers", text="")
        row = col.row(align=True)        
        row.prop(od, "layers", toggle=True, index=31, text="Deform")
        row = col.row(align=True)
        row.prop(od, "layers", toggle=True, index=30, text="Mechanism")
        row = col.row(align=True)
        row.prop(od, "layers", toggle=True, index=15, text="Motion Capture")
    #None Hidden    
        row = col.row(align=True)
        row.separator(factor=0.5)
        row = col.row(align=True)
        row.prop(od, "layers", toggle=True, index=0, text="Root")
        
        
def register():
    bpy.utils.register_class(DDSRigUI)

def unregister():
    bpy.utils.unregister_class(DDSRigUI)
    
if __name__=="__main__":
    register()
