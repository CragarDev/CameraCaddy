
# Camera Caddy 🎥

![Camera Caddy Logo](assets/03_fbm_port_cameraCaddy_med.png)

**A Python-powered Blender add-on for managing multiple cameras and simplifying 3D production workflows.**

Camera Caddy helps Blender users create, organize, switch, and configure cameras directly from a custom interface in the 3D Viewport.

I developed Camera Caddy using Python and Blender's API, combining my experience in animation and video production with software development to solve practical workflow problems.

**Technologies:** Python · Blender API · Custom UI Development · 3D Production Automation

<p align="left">
  <img
    src="https://github.com/user-attachments/assets/605fc5c2-2c50-4aea-8da0-7423fc4f4d4d"
    alt="Camera Caddy add-on panel in Blender"
    width="300"
  >
</p>

---

## 🎬 Video Demonstrations

- [Installation Tutorial](https://youtu.be/P4zxviWVIZ8)
- [Camera Caddy Walkthrough](https://youtu.be/WQvY06sDCAI)

## 🛒 Get Camera Caddy

Camera Caddy is available for **$12.99 USD** on Superhive (formerly Blender Market).

**[View Camera Caddy on Superhive](https://superhivemarket.com/products/camera-caddy)**

---

## ✨ Features

- **Camera management:** Create, select, organize, and remove cameras.
- **Camera switching:** Change the active scene camera from a dropdown.
- **Timeline integration:** Assign cameras to timeline frames using markers.
- **Transform controls:** Adjust camera position and rotation.
- **Camera configuration:** Set focal length, f-stop, and depth-of-field options.
- **Focus controls:** Select a focus object or configure focus distance.
- **Viewport integration:** Access Camera Caddy from Blender's N-panel.

---

## 🧩 Blender Compatibility

Camera Caddy includes two implementations:

| Camera Caddy Version | Blender Compatibility |
|---|---|
| v1.0.0 — Legacy Add-on | Blender 2.83–4.1.1 (documented) |
| v2.0.0 — Extension Format | Blender 4.2 minimum; personally confirmed working in 5.1.2 |

**Latest confirmed working Blender version: 5.1.2**

Camera Caddy v2.0.0 has been tested and confirmed working in Blender 5.1.2 without requiring changes to the add-on.

The minimum Blender version declared in the v2 extension manifest is 4.2.0. The table does not imply every intermediate Blender release has been individually tested.

**Source code:**

- [Camera Caddy v1](camera_caddy_v1/)
- [Camera Caddy v2](camera_caddy_v2/)

---

## 📦 Installation

Download the appropriate Camera Caddy package from your purchase on Superhive.

### Blender 2.83–4.1 (Legacy Add-on)

1. Open Blender.
2. Navigate to **Edit → Preferences → Add-ons**.
3. Select the option to install an add-on.
4. Choose the `camera_caddy_v1.zip` package.
5. Enable Camera Caddy in the add-on preferences.
6. Save your preferences.
7. Return to the 3D Viewport and press **N** to open the sidebar.

### Blender 4.2 and Newer (Extension Format)

1. Open Blender.
2. Navigate to **Edit → Preferences → Get Extensions** or the extension installation area for your Blender version.
3. Select **Install from Disk**.
4. Choose the `camera_caddy_v2.zip` package.
5. Enable Camera Caddy if necessary.
6. Save your preferences.
7. Open the 3D Viewport sidebar by pressing **N**.

The exact preferences layout may vary between Blender releases.

For a visual walkthrough, watch the [installation tutorial](https://youtu.be/P4zxviWVIZ8).

---

## 🚀 Getting Started

### Access Camera Caddy

Open Blender's 3D Viewport and press **N** to display the sidebar.

Select the **Camera Caddy** tab.

### Add a Camera

1. Position the viewport at your desired camera angle.
2. Click **Add Camera** in the Camera Caddy panel.
3. Enter a camera name, focal length, and f-stop.
4. Confirm the settings.

Camera Caddy adds the camera to a collection named `Cameras`, makes it active, and switches to camera view.

### Switch Cameras

Open the camera dropdown and select the camera you want to activate.

The active camera is identified by a green icon.

### Delete a Camera

Use the trash icon beside a non-active camera in the camera dropdown.

---

## 🎞️ Timeline Camera Management

Camera Caddy provides tools for organizing camera changes along Blender's timeline.

### Assign a Camera to a Frame

1. Select the camera you want to use.
2. Click the film icon beside that camera.
3. Choose a frame in the popup.
4. Confirm the selection.

A marker with the camera's name is added at the selected frame.

### Manage Camera Markers

- **Move a marker:** Select and drag it to another frame.
- **Delete a marker:** Select it, press **X**, and confirm.
- **Preview shots:** Arrange camera markers at specific frames to inspect different camera angles.

This workflow can simplify shot planning, scene previews, and multi-camera animation setups.

---

## 📷 Camera Controls

### Position and Rotation

Adjust camera location and rotation using the controls in the Camera Caddy panel.

### Lock Camera to View

Enable **Lock Camera to View** to reposition the active camera through viewport navigation.

The lock is automatically disabled when switching cameras.

### Depth of Field

Use Camera Caddy's depth-of-field controls to enable or disable depth of field.

Focus options include:

- Selecting an object to focus on
- Setting a specific focus distance

---

## 💡 Tips & Best Practices

- Use descriptive camera names when working with multiple shots.
- Arrange camera markers to organize scene timing.
- Use one-frame intervals to preview alternative camera angles.
- Save your Blender project before making substantial scene changes.

---

## ❓ Frequently Asked Questions

### What is Camera Caddy?

Camera Caddy is a Python add-on for Blender that provides tools for creating, switching, organizing, and configuring multiple cameras in a 3D scene.

### Where can I find the add-on after installation?

Open Blender's 3D Viewport and press **N**. Select the Camera Caddy tab in the sidebar.

### Can I delete cameras?

Yes. Camera Caddy allows you to delete non-active cameras through its camera dropdown.

### Can I assign cameras to timeline frames?

Yes. Use the film icon beside a camera to place a corresponding camera marker at a selected frame.

### Can I adjust depth of field?

Yes. Camera Caddy includes depth-of-field controls and focus settings.

### Does Camera Caddy work in Blender 5.1.2?

Yes. Camera Caddy v2.0.0 has been confirmed working in Blender 5.1.2.

### Where can I purchase Camera Caddy?

Camera Caddy is available on [Superhive](https://superhivemarket.com/products/camera-caddy).

---

## 🔧 Troubleshooting

### Camera Caddy does not appear in the sidebar

Check that the add-on is enabled under Blender's preferences.

If necessary, restart Blender and reopen the 3D Viewport.

### Camera markers are not appearing

Verify that the correct camera and frame are selected, then use the film icon to assign the camera to that frame.

### Installation fails

Confirm that the installation package corresponds to your Blender version and that the ZIP archive is valid.

Refer to the installation video for additional guidance.

---

## 📚 Documentation & Support

- [Camera Caddy on Superhive](https://superhivemarket.com/products/camera-caddy)
- [Camera Caddy Repository](https://github.com/CragarDev/CameraCaddy)
- [Installation Video](https://youtu.be/P4zxviWVIZ8)
- [Walkthrough Video](https://youtu.be/WQvY06sDCAI)

For development questions or project inquiries, contact:

**cragardev@gmail.com**

---

## 📋 Version Information

The repository contains two Camera Caddy implementations:

- **v1.0.0:** Original Blender add-on with a declared minimum Blender version of 2.83.
- **v2.0.0:** Updated Blender extension format with a declared minimum Blender version of 4.2.

Camera Caddy v2.0.0 has also been personally tested and confirmed working in Blender 5.1.2.

These version numbers come from the source metadata. A separate, verified GitHub release history has not been established.

---

## 👨‍💻 About the Developer

Camera Caddy was independently developed by Craig Burke, a software developer with a background in video production, motion graphics, animation, and creative technology.

The project demonstrates Python scripting, Blender API integration, interface development, and practical workflow automation.

[GitHub Profile](https://github.com/CragarDev) · [LinkedIn](https://www.linkedin.com/in/cragardev/) · [Developer Portfolio](https://craigburke-portfolio.netlify.app)

---

*Camera Caddy — Making multi-camera workflows simpler.*
