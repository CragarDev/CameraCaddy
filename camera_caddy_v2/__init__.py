"""
Copyright (C) 2024 Fishblade Media
info@fishblade.com

Created by Fishblade Media

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

"""
bl_info = {
    "name": "Camera Caddy",
    "description": "Simple Camera management with controls and options for using multiple cameras.",
    "author": "Fishblade Media",
    "version": (2, 0, 0),
    "blender": (4, 2, 0),
    "location": "View3D",
    "warning": "",
    "wiki_url": "https://www.fishblademedia.com/portfolio-details_cameraCaddy.html",
    "category": "3D View",
}
"""

import bpy
import os
from bpy.types import Panel, Operator  # type: ignore
from bpy.utils import register_class, unregister_class, previews  # type: ignore
from bpy.props import (  # type: ignore
    FloatProperty,
    StringProperty,
    IntProperty,
)


# global variable to store icons in
custom_icons = None


# Main Panel
class CAMERACADDY_PT_MainPanel(Panel):
    bl_label = ""
    bl_idname = "CAMERACADDY_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CameraCaddy"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="CAMERA CADDY")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        box = layout.box()

        box.operator(
            "wm.cameracaddy_ot_add_new_camera_popup_operator",
            icon="OUTLINER_DATA_CAMERA",
            text="Add Camera",
        )

        layout = self.layout
        row = layout.row(align=True)
        if bpy.data.cameras:
            cameras_data = list(bpy.data.cameras)

            # check to see if there is a camera in the scene
            if scene.camera == None:
                row.label(text="No Camera in Scene")
                row = layout.row()
            else:
                row.label(text=f"Active Camera:")
                row = layout.row(align=True)
                row.label(text=f"{scene.camera.name}", icon="CAMERA_DATA")
                row = layout.row()
        else:
            row.label(text="No Camera in Scene")
            row = layout.row()


# Camera switching Panel
class CAMERACADDY_PT_CameraSwitchingPanel(Panel):
    bl_label = "--- Camera Switching ---"
    bl_idname = "CAMERACADDY_PT_camera_switching_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CameraCaddy"
    bl_parent_id = "CAMERACADDY_PT_main_panel"
    # bl_options = {"DEFAULT_CLOSED"}
    bl_ui_units_x = 10

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        scene = context.scene

        # if no camera in the scene, then label "no camera in scene"
        if scene.camera == None:
            row.label(text="No Camera in Scene")
            row = layout.row()
        else:

            for obj in context.scene.objects:
                if obj.type == "CAMERA":
                    row = layout.row()

                    # if the camera is the active camera then use a different icon
                    if obj == scene.camera:
                        row.operator(
                            "wm.cameracaddy_ot_list_of_cameras_operator",
                            text=obj.name,
                            icon_value=custom_icons["greenCamera_icon"].icon_id,
                        ).name = obj.name
                    else:
                        row.operator(
                            "wm.cameracaddy_ot_list_of_cameras_operator",
                            text=obj.name,
                            icon="OUTLINER_OB_CAMERA",
                        ).name = obj.name

                    # if camera is active camera then show the Add camera to the timeline button
                    if obj == scene.camera:
                        anim_cam = row.operator(
                            "wm.cameracaddy_ot_camera_switch_operator",
                            icon="RENDER_ANIMATION",
                            text="",
                        )
                        anim_cam.name = obj.name
                        anim_cam.frame = scene.frame_current

                    # Delete button for each camera in the scene but not the active camera
                    if obj != scene.camera:
                        del_op = row.operator(
                            "wm.cameracaddy_ot_delete_camera_operator",
                            text="",
                            icon="TRASH",
                        )
                        del_op.name = obj.name


# Transform Camera Panel
class CAMERACADDY_PT_TransformCameraPanel(Panel):
    bl_label = "--- Transform Camera ---"
    bl_idname = "CAMERACADDY_PT_transform_camera_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "cameracaddy"
    bl_parent_id = "CAMERACADDY_PT_main_panel"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        scene = context.scene

        # check to see if there is an active object
        if bpy.context.scene.camera:
            cam = bpy.context.scene.camera

            col = box.column(align=True)

            if cam.type == "CAMERA":

                # add a switch for "Lock Camera to View"
                row = layout.row()
                col.prop(
                    bpy.context.space_data,
                    "lock_camera",
                    text="Lock Camera to View",
                    icon="LOCKED",
                )
                row = layout.row()

                col.prop(
                    cam,
                    "location",
                    text="location",
                )
                row = box.row()
                col.prop(
                    cam,
                    "rotation_euler",
                    text="rotation",
                )

                row = box.row(align=True)
                # add a setting for the Focal Length
                row.label(text="focal length:")
                row.prop(cam.data, "lens", icon_only=True)

                # add a setting for the f-stop
                row = box.row(align=True)
                row.label(text="f-stop:")
                row.prop(cam.data.dof, "aperture_fstop", icon_only=True)

                # Add settings for the Depth of Field
                split = box.split()
                col = split.column()
                col.label(text="")
                col.prop(
                    cam.data.dof,
                    "use_dof",
                )

                # if the depth of field is enabled then show the settings
                if cam.data.dof.use_dof:

                    split = box.split()

                    col = split.column()
                    col.label(text="focus object:")
                    col = split.column(align=True)
                    col.prop(cam.data.dof, "focus_object", icon_only=True)

                    if not cam.data.dof.focus_object:
                        split = box.split()
                        col = split.column()
                        col.label(text="focus distance:")
                        col = split.column(align=True)
                        col.prop(
                            cam.data.dof,
                            "focus_distance",
                            icon_only=True,
                        )
                    row = box.row()
                    row.separator()

            else:
                row = box.row()
                row.label(text="No Camera Selected")
                row = box.row()


class CAMERACADDY_OT_LIST_OF_CAMERAS(Operator):
    bl_label = "Select Camera"
    bl_idname = "wm.cameracaddy_ot_list_of_cameras_operator"
    bl_options = {"REGISTER", "UNDO"}

    # name: str
    name: StringProperty()  # type: ignore

    def execute(self, context):

        scene = context.scene

        # make sure the "lock camera to view" is off
        bpy.context.space_data.lock_camera = False

        scene.camera = bpy.data.objects[self.name]

        # Deselect all
        bpy.ops.object.select_all(action="DESELECT")
        camera = bpy.data.objects[self.name]
        camera.select_set(True)
        context.view_layer.objects.active = camera

        return {"FINISHED"}


class CAMERACADDY_WM_OT_CAMERA_SWITCH_POPUP(Operator):
    """Settings for setting an active camera at a specific frame"""

    bl_idname = "wm.cameracaddy_ot_camera_switch_operator"
    bl_label = "Set Camera at Frame"
    bl_options = {"REGISTER", "UNDO"}

    # frame: int
    frame: IntProperty(name="Frame", default=(1))  # type: ignore

    # name: str
    name: StringProperty(options={"HIDDEN"})  # type: ignore

    def execute(self, context):

        scene = context.scene

        if scene.camera == None:
            return {"CANCELLED"}

        if self.name in context.scene.objects:
            cam = context.scene.objects[self.name]
            scene.camera = cam  # Set the selected camera as the active camera

            fr = self.frame
            scene = bpy.data.scenes["Scene"]

            cam_name = cam.name

            # get a list of all the markers in the timeline
            mk_count = len(scene.timeline_markers)

            # check fr to see if it has a marker already
            # if it does then delete it
            for marker in scene.timeline_markers:
                if marker.frame == fr:
                    scene.timeline_markers.remove(marker)

            new_marker_name = f"mk_{mk_count + 1}_{cam_name}"

            # move to the frame selected
            scene.frame_set(fr)

            # Get the current area
            original_area = context.area.type

            # Override the context to be in the timeline area
            context.area.type = "DOPESHEET_EDITOR"

            # bind the camera to the marker
            bpy.ops.marker.camera_bind()

            # Assume the marker you want to rename is the last one added
            marker = scene.timeline_markers[-1]

            # Change the name of the marker
            marker.name = new_marker_name

            # Restore the original area
            context.area.type = original_area

        return {"FINISHED"}

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)


class CAMERACADDY_WM_OT_ADD_NEW_CAMERA_POPUP(Operator):
    """Adds a new camera to the scene at the current viewing angle and position and then sets it as the active camera."""

    bl_idname = "wm.cameracaddy_ot_add_new_camera_popup_operator"
    bl_label = "Add New Camera"
    bl_options = {"REGISTER", "UNDO"}

    # camera_name: str
    camera_name: StringProperty(name="Camera Name", default="Camera")  # type: ignore
    # focal_length: float
    focal_length: FloatProperty(name="Focal Length", default=50)  # type: ignore
    # f_stop: float
    f_stop: FloatProperty(name="F-Stop", default=2.8)  # type: ignore

    def toggle_camera_perspective(self, context):
        for area in bpy.context.screen.areas:
            if area.type == "VIEW_3D":
                for space in area.spaces:
                    if space.type == "VIEW_3D":
                        rv3d = space.region_3d
                        if rv3d.view_perspective == "CAMERA":
                            return True
                        else:
                            print("The viewport is not in camera perspective.")
                            return False

        print("No 3D Viewport found.")
        return True

    def execute(self, context):

        scene = context.scene
        message = "Add a new camera to the scene."

        # check the view to see if it is in camera view
        cam_persp = self.toggle_camera_perspective(context)

        if cam_persp:
            message = "Must be in user perspective, not camera perspective!"
            # Display the message
            self.report({"ERROR"}, message)
            return {"CANCELLED"}

        cameras_data = list(bpy.data.cameras)

        # get the name of the new camera from the user input above
        cam_name = self.camera_name

        # get the focal length from the user input above
        focal_length = self.focal_length

        # get the f-stop from the user input above
        f_stop = self.f_stop

        # check to see if the camera name already exists
        for cam in cameras_data:
            if cam_name == cam.name:
                message = f"Camera name {cam_name} already exists!"
                # Display the message
                self.report({"ERROR"}, message)
                print(message)
                return {"CANCELLED"}

        # deselect all objects
        bpy.ops.object.select_all(action="DESELECT")

        # add a new camera data block
        camera_data = bpy.data.cameras.new(name=cam_name)

        # create a new camera object
        camera_object = bpy.data.objects.new(cam_name, camera_data)

        # set the focal length and f-stop of the new camera
        camera_object.data.lens = focal_length
        camera_object.data.dof.aperture_fstop = f_stop

        if "Cameras" in bpy.data.collections:
            bpy.data.collections["Cameras"].objects.link(bpy.data.objects[cam_name])

            # unlink from the collection called "Collection"
            if cam_name in bpy.context.scene.collection.objects:
                bpy.context.scene.collection.objects.unlink(bpy.data.objects[cam_name])

        else:
            # if there is no collection called "Cameras" then create one and link the object to it
            # create a new collection in the main scene and call it "Cameras"
            camera_collection = bpy.data.collections.new("Cameras")

            # link the collection to the scene
            scene.collection.children.link(camera_collection)

            # link the object to the scene into the new collection
            camera_collection.objects.link(bpy.data.objects[cam_name])

            # unlink from the collection called "Collection"
            if cam_name in scene.collection.objects:
                scene.collection.objects.unlink(bpy.data.objects[cam_name])

        # set the camera as the active camera in the scene
        scene.camera = bpy.data.objects[cam_name]

        # set the camera as the active object
        bpy.context.view_layer.objects.active = camera_object

        # set the location of the new camera
        camera_object.location = (7.5, 7.5, 1.3)

        # set the rotation of the new camera
        camera_object.rotation_euler = (1.48353, 0, 2.33874)

        # set the new camera to the current view
        bpy.ops.view3d.camera_to_view()

        # deselect all objects
        bpy.ops.object.select_all(action="DESELECT")

        return {"FINISHED"}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


# Operator to delete a camera
class CAMERACADDY_OT_DELETE_CAMERA(Operator):
    bl_idname = "wm.cameracaddy_ot_delete_camera_operator"
    bl_label = "Delete Camera"
    bl_options = {"REGISTER", "UNDO"}

    # name: str
    name: StringProperty()  # type: ignore

    def execute(self, context):
        # Find the camera and delete it
        if self.name in context.scene.objects:
            cam = context.scene.objects[self.name]

            # Store a reference to the camera's data block before removing the object
            cam_data = cam.data

            # Remove the camera object from the scene
            bpy.data.objects.remove(cam, do_unlink=True)

            # Now, try to remove the camera data block if it's no longer used
            if cam_data and cam_data.users == 0:
                bpy.data.cameras.remove(cam_data)

        # Tagging the area for redraw
        for area in context.screen.areas:
            if area.type == "VIEW_3D":
                area.tag_redraw()

        return {"FINISHED"}


# Operator to confirm a selection
class CAMERACADDY_WM_OT_CONFIRM_SELECTION(Operator):
    bl_idname = "wm.confirm_selection"
    bl_label = "Confirm Selection"

    def execute(self, context):
        return {"FINISHED"}


_classes = [
    CAMERACADDY_PT_MainPanel,
    CAMERACADDY_PT_CameraSwitchingPanel,
    CAMERACADDY_PT_TransformCameraPanel,
    CAMERACADDY_OT_LIST_OF_CAMERAS,
    CAMERACADDY_WM_OT_CAMERA_SWITCH_POPUP,
    CAMERACADDY_WM_OT_ADD_NEW_CAMERA_POPUP,
    CAMERACADDY_OT_DELETE_CAMERA,
]


def register():
    for cls in _classes:
        register_class(cls)

    # for custom green camera icon
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    addon_path = os.path.dirname(__file__)
    icons_dir = os.path.join(addon_path, "icons")
    custom_icons.load(
        "greenCamera_icon", os.path.join(icons_dir, "GreenCameraIcon.png"), "IMAGE"
    )


def unregister():
    for cls in _classes:
        unregister_class(cls)

    global custom_icons
    bpy.utils.previews.remove(custom_icons)


if __name__ == "__main__":
    register()
