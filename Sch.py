bl_info = {
    "name": "Sch",
    "author": "Stivan Chardakov",
    "version": (1, 0),
    "blender": (2, 92, 0),
    "category": "Object",
    "location": "Operator Search",
    "description": "Prepares a mesh for high poly"
}

import bpy



class SCH_PT_Panel(bpy.types.Panel):
    bl_label = "Sch"
    bl_idname = "PT_Sch"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Sch'
    

    def draw(self, context):
        layout = self.layout
        


        row = layout.row()
        row.operator("wm.schop")
 
        



class WM_OT_SchOp(bpy.types.Operator):
    bl_label = "Sch Operator"
    bl_idname = "wm.schop"
    bl_options = {'REGISTER', 'UNDO'}
    
    duplicate = bpy.props.BoolProperty(name= "Duplicate", default= True)
    shade = bpy.props.BoolProperty(name= "Shade Smooth", default= True)
    subdiv = bpy.props.BoolProperty(name= "SubDiv", default= True)
    newcol = bpy.props.BoolProperty(name= "New Collection", default= True)
    hide = bpy.props.BoolProperty(name= "Hide Unselected", default= True)


    def execute(self, context):
        
        d = self.duplicate
        s = self.shade
        sd = self.subdiv
        c = self.newcol
        h = self.hide
        
        
        if d == True:
            bpy.ops.object.duplicate()
            
        if s == True:
            bpy.ops.object.shade_smooth()
            
        if sd == True:
            bpy.ops.object.subdivision_set(level= 3)
            
        if c == True:
            bpy.ops.object.move_to_collection(
            collection_index = 0,
            is_new = True,
            new_collection_name = "_HIGH")
            
        if  h == True:
            bpy.ops.object.hide_view_set(unselected = True)
        
        
        bpy.ops.object.editmode_toggle()
        
        return {'FINISHED'}
        
    
    def invoke(self,context, event):
        return context.window_manager.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(SCH_PT_Panel)
    bpy.utils.register_class(WM_OT_SchOp)

def unregister():
    bpy.utils.unregister_class(SCH_PT_Panel)
    bpy.utils.unregister_class(WM_OT_SchOp)

if __name__ == "__main__":
    register()
