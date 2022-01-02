bl_info = {
    "name": "Stepped Loops Selection",
    "author": "Hannah Ümit <twitter.com/HannahUmit>",
    "version": (1,0),
    "blender": (2, 80, 0),
    "category": "Edit",
    "location": "3D Viewport",
    "description": "Select Loops with steps",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

import bpy


class SteppedLoopsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "select.steppedloops_operator"
    bl_label = "Stepped Loops Operator"
    bl_options = {'REGISTER', 'UNDO'}
    
    deselect: bpy.props.IntProperty(
        name="Deselect",
        description="Number of deselected elements in the repetitive sequence",
        default=1,
        min=1,
        )
    select: bpy.props.IntProperty(
        name="Select",
        description="Number of selected elements in the repetitive sequence",
        default=0,
        min=0,
        )
    offset: bpy.props.IntProperty(
        name="Offset",
        description="Offset from the starting point",
        default=0,
        min=0,
        )
    
    def execute(self, context):
        import bpy
        bpy.ops.mesh.loop_multi_select(ring=True)
        bpy.ops.mesh.select_nth(skip= self.deselect, nth= self.select, offset= self.offset)
        bpy.ops.mesh.loop_multi_select(ring=False)

        return {'FINISHED'}

class VIEW3D_PT_Steppedlooops_UI(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Edit"
    bl_context = "mesh_edit"
    bl_label = "Stepped loops"
    
    def draw(self, context):
        self.layout.operator('select.steppedloops_operator',
            text='Default Grid',
            icon='ALIGN_CENTER')
        pass

def select_edit_mesh_draw(self, context):
    self.layout.operator('select.steppedloops_operator')
    pass

# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access)
def register():
    bpy.utils.register_class(SteppedLoopsOperator)
    bpy.utils.register_class(VIEW3D_PT_Steppedlooops_UI)
    bpy.types.VIEW3D_MT_select_edit_mesh.append(select_edit_mesh_draw)

def unregister():
    bpy.utils.unregister_class(SteppedLoopsOperator)
    bpy.utils.unregister_class(VIEW3D_PT_Steppedlooops_UI)
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(select_edit_mesh_draw)


if __name__ == "__main__":
    register()