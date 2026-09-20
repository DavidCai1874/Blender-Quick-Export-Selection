import bpy
from bpy.props import EnumProperty




# ------------ Format setup
# distionary, key:value, doing this for easier adding of new formats in the future
EXPORT_FORMATS = {
    'FBX': {
        'label': "FBX",
        'operator': "export_scene.fbx",
        'options': {
            'use_selection': True,
        },
    },

    'OBJ': {
        'label': "OBJ",
        'operator': "wm.obj_export",
        'options': {
            'export_selected_objects': True,
        },
    },

    'ABC': {
        'label': "Alembic (.abc)",
        'operator': "wm.alembic_export",
        'options': {
            'selected': True,
        },
    },
}
# setup ends






# --------------------- Panel
class VIEW3D_PT_quick_export_selection(bpy.types.Panel):
    bl_label = "Export Selection As"
    bl_idname = "VIEW3D_PT_quick_export_selection"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"

    def draw(self, context):
        column = self.layout.column(align=True)

        # create a button for each export format defined in EXPORT_FORMATS
        for format_id, format_data in EXPORT_FORMATS.items():
            button = column.operator("quick_export.export_selected", text=format_data["label"], icon="EXPORT")
            button.export_format = format_id # Set the export format for the button from the dictionary key to the EnumProperty of the operator
# panel ends




# --------------------- Operator
class QUICKEXPORT_OT_export_selected(bpy.types.Operator):
    bl_idname = "quick_export.export_selected"
    bl_label = "Export Selection"

    # Define an EnumProperty to hold the export format, with items selected from the panel
    export_format: EnumProperty(
        name="Export Format",
        items=[(format_name, format_data["label"], "") for format_name, format_data in EXPORT_FORMATS.items()])

    def execute(self, context):
        # based on the selected export format, retrieve data from the EXPORT_FORMATS dictionary
        format_data = EXPORT_FORMATS[self.export_format]

        # get the operator command and options from the dictionary
        operator_path = format_data["operator"]
        options = format_data["options"]

        # split the operator path, then retrieve the operator function from bpy.ops
        operator_group, operator_name = operator_path.split(".")
        operator_group = getattr(bpy.ops, operator_group)
        operator = getattr(operator_group, operator_name)

        # call the window, unpack the options as selected only
        operator('INVOKE_DEFAULT', **options)

        return {'FINISHED'}
# operator ends







# -------------------- register
classes = (
    QUICKEXPORT_OT_export_selected,
    VIEW3D_PT_quick_export_selection,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
# -------------------- register ends