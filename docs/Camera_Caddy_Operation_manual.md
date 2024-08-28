### Camera Caddy User Manual

---

# **Camera Caddy User Manual**
### Works with Blender Versions 2.8 to 4.2

## **Overview**

Welcome to the Camera Caddy User Manual! This document provides comprehensive instructions on how to install, configure, and use Camera Caddy — a Blender addon designed to simplify camera management in your 3D projects.


## **Video Tutorials**

- [Installation Video](https://youtu.be/P4zxviWVIZ8) 
- [Walkthrough Video](https://youtu.be/WQvY06sDCAI)

## **Table of Contents**

1. [Installation](#installation)
2. [Accessing Camera Caddy](#accessing-camera-caddy)
3. [Adding a Camera](#adding-a-camera)
4. [Managing Cameras](#managing-cameras)
   - [Active Camera Overview](#active-camera-overview)
   - [Switching Between Cameras](#switching-between-cameras)
   - [Deleting Cameras](#deleting-cameras)
5. [Animating Cameras](#animating-cameras)
   - [Setting Up Animated Camera Transitions](#setting-up-animated-camera-transitions)
   - [Managing Camera Markers](#managing-camera-markers)
6. [Adjusting Camera Settings](#adjusting-camera-settings)
   - [Transform Controls](#transform-controls)
   - [Depth of Field](#depth-of-field)
7. [Tips & Best Practices](#tips--best-practices)
8. [Support](#support)
9. [Changelog](#changelog)


---

## **Installation**

1. **Download the Add-On:**
   - Purchase and download Camera Caddy from [link to purchase page](coming soon!).
   
2. **Install the Add-On: (select your Blender version)**
   ## Blender Version 2.8 to 4.1
   #### Video Installation Guide: [Installation Video](https://youtu.be/P4zxviWVIZ8)
   1. Download the camera_caddy_v1.zip file from the purchase link.
   2. Open Blender and go to **Edit** >>> **Preferences** >>> **Add-ons**.
   3. In the top right corner, click the  **Install an add-on** button.
   4. Navigate to the camera_caddy_v1.zip file that you downloaded, select it and click **Install Add-on**.
   5. Once installed, enable Camera Caddy by checking the **Enable add-on** box next to its name.
   6. Click **Save Preferences** to keep it enabled for future sessions.
   7. Access Camera Caddy from the N-Panel in the 3D Viewport.
  
   ## Blender Version 4.2
   #### Video Instillation Guide: [Link to video guide]
   1. Download the camera_caddy_v2.zip file from the purchase link.
   2. Open Blender and go to **Edit** >>> **Preferences** >>> **Get Extensions**.
   3. Click the dropdown menu in the top right hand corner and scroll down to select **Install from disk**.
   4. Navagate to the location of your camera_caddy_v2.zip file.
   5. Select it and click **Install from disk**. 
   6. Once installed, Camera Caddy should be enabled by default.
   7. If Camera Caddy is not enabled, go to the **Add-ons** section in your preferences and check the **Enable add-on** box next to its name to enable it.
   8. Click **Save Preferences** to keep it enabled for future sessions.
   9. Access Camera Caddy from the N-Panel in the 3D Viewport.



3. **Save Preferences:**
   - Click **Save Preferences** to ensure Camera Caddy is available every time you start Blender.

---

## **Accessing Camera Caddy**

1. Open Blender and go to the **3D Viewport**.
2. Press **N** to open the N-Panel on the right side of the viewport.
3. You will find **Camera Caddy** listed as a tab in the N-Panel.

---

## **Adding a Camera**

1. **Position the Viewport:**
   - Move your viewport to the desired angle where you want the camera to be placed.
   
2. **Add a New Camera:**
   - In the Camera Caddy panel, click the **Add Camera** button.
   - A pop-up menu will appear, allowing you to:
     - **Name your camera**
     - **Set the Focal Length**
     - **Set the F-Stop**
   - After setting your preferences, the camera will be added to a collection called "Cameras", set as the active camera and camera view will be toggled on.

---

## **Managing Cameras**

### **Active Camera Overview**

- The active camera is automatically displayed in the Camera Caddy panel.
- This overview allows you to quickly see and manage which camera is currently active.

### **Switching Between Cameras**

1. **Open the Camera Switching Dropdown:**
   - In the Camera Caddy panel, click the **Camera Switching Dropdown**.
   - You’ll see a list of all available cameras in your scene.
   
2. **Switch Cameras:**
   - Click on any camera in the list to make it the active camera.
   - The active camera is highlighted with a green icon.

### **Deleting Cameras**

1. **Delete a Non-Active Camera:**
   - In the Camera Switching Dropdown, click the **Trashcan icon** next to any non-active camera to delete it from your scene.

---

## **Animating Cameras**

### **Setting Up Animated Camera Transitions**

1. **Bind a Camera to the Timeline:**
   - In the Camera Switching Dropdown, click the **Film icon** next to the active camera.
   - A pop-up menu will appear, allowing you to select a frame on the timeline, by default the current frame will be selected.
   - Once selected, a marker with the camera's name will be placed on the timeline at that frame.

### **Managing Camera Markers**

1. **Move Camera Markers:**
   - Select the marker on the timeline and drag it to the desired frame.

2. **Delete Camera Markers:**
   - Select the marker, press **X**, and confirm the deletion.

3. **Preview Shots:**
   - Set up markers at specific intervals to preview different camera angles efficiently, this can make for quick camera view renders by setting each camera at 1 frame inervals, then render animation for only those frames.

---

## **Adjusting Camera Settings**

### **Transform Controls**

1. **Adjust Location and Rotation:**
   - Use the **Transform controls** in the Camera Caddy panel to adjust the camera’s XYZ location and rotation.

2. **Lock Camera to View:**
   - Click the **Lock Camera to View** button to dynamically reposition your camera as you move in the viewport.
   - This option is automatically disabled when you switch cameras.

### **Depth of Field**

1. **Toggle Depth of Field:**
   - Click the **Depth of Field** button to turn depth of field on or off.

2. **Focus Settings:**
   - Choose a specific object to focus on or set an exact focus distance.

---

## **Tips & Best Practices**

- **Descriptive Camera Names:** Always name your cameras descriptively to easily manage them in complex scenes.
- **Use Markers:** When animating, use timeline markers to keep track of camera transitions.
- **Preview Before Rendering:** Set up preview shots using one-frame intervals to quickly assess different angles.


---

## **Support**

If you encounter any issues or need further assistance, please refer to the following resources:

- **Support Email:** [support@fishblade.com](support@fishblade.com)
- **Documentation: User Manual:** [[User Manual - Online](http://192.168.1.113:5501/inner-page_cameraCaddyDocs_userManual.html)]
- **Documentation: Online FAQ:** [[Frequently Asked Questions - Online](http://192.168.1.113:5501/inner-page_cameraCaddyDocs_faq.html)]
- **Video:** [[Installation Video](https://youtu.be/P4zxviWVIZ8)]
- **Video:** [[Walkthrough Video](https://youtu.be/WQvY06sDCAI)]

---

## **Changelog**

### Version 1.2.0

- Converted to work with Blender version 4.2.0.

### Version 1.1.0

- Initial release, works with Blender versions 2.8 - 4.1.

Thank you for choosing Camera Caddy! We hope it enhances your Blender experience.

---

This manual is structured to provide clear, step-by-step instructions on using Camera Caddy, ensuring that users can easily access and utilize all of its features.


