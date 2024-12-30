# CSS Administration System

## Overview

The CSS Administration System is a platform designed to manage the various roles and responsibilities within the CSS Department. It is organized into sections corresponding to different levels of access, ensuring proper permissions are granted to each role. The system allows the President, or the Admin (acting as a proxy when the President is unavailable), to manage these permissions and all aspects of the system effectively.

## Executives Admin Control System
(Controls the site from news, blogs, events to educational resources which are regulated by the right executive in charge)
(An Executive assign to a Group only views, edit or create entities the group has permissions base on rules set by the system admin(President or Proxy); more about this in the permissions section)
![Image Description](./.readme_assets/admin_home.png)

## Department Site
![frontend view](./.readme_assets/frontend.png)
## Sections

The system is divided into the following sections from the admin to the frontend:

- **Accounts and Permissions Management**
- **Academics and Resources**
- **Exam Allocation System**
- **Events and News**
- **Timeline and Executive Position History (Achievements)**
- **Advertisements**
- **And More**

![Image Description](./.readme_assets/admin_home_2.png)

---
- Please Note: The Backend Sytem Admin(President) controls permissions and resources the frontend⬇️  has access to 

## Accounts and Permissions Management

Every CSS Executive or appointee is provided with an Administrator account by the elected President. During account creation, permissions are set according to the user's role. The account details, such as email, phone number, and a custom password, are provided, and the user can change their password later.

### **Account Activation:**

- Once the account is created, an email is sent with login credentials, allowing the user to log in, change their password, and start working right away.

### **Account Misuse:**

- If an account or position is misused, the President can deactivate the account (not delete it). The account can be reactivated after careful consideration.

---

### Managing Executive Groups and Permissions

In the CSS System, **Executive Groups** and **Permissions** are used to control the level of access different users have within the system. This section explains how to manage these groups and permissions for the members of your society.

#### Understanding Executive Groups

**Executive Groups** are used to categorize users based on their roles. Each group has different levels of access (permissions), which are inherited by the users in that group.

Common groups may include:

- **Executive Board**: Full control over the system, including managing users and content.
- **General Members**: Can view and create content but cannot delete or modify existing content.
- **Visitors**: Can only view content, with no interaction or modification rights.

#### Managing Executive Groups

To create or manage **Executive Groups**:

1. Navigate to the **Groups** section of the CSS System.
2. You will see a list of existing groups (e.g., **Executive Board**, **General Members**, **Visitors**).
3. To **create a new group**:
   - Click on the **Add Group** button.
   - Enter a name for the new group (e.g., "Event Coordinators").
   - Click **Save** to create the group.
4. To **edit an existing group**:
   - Click on the group name.
   - Add or remove users as needed.
   - Modify the **permissions** associated with the group (explained below).
   - Click **Save** to confirm changes.

#### Managing Permissions for Executive Groups

Permissions define the actions that users within a group can perform. These actions may include:

- **View content**: The ability to see specific pages or data.
- **Add content**: The ability to create new content or records.
- **Edit content**: Modify existing content or settings.
- **Delete content**: Remove data or content.

#### Assigning Permissions to Groups

To assign or modify permissions for a group:

1. In the **Groups** section, click on the desired group.
2. You will see a section called **Permissions**.
3. Use the checkboxes to assign permissions like "Can view content," "Can add content," etc.
4. Click **Save** to apply the changes.

To remove a permission, simply uncheck the relevant box and save the changes.

#### Assigning Users to Executive Groups

After creating or editing an **Executive Group** and its permissions, you can assign users to that group:

1. Go to the **Users** section in the CSS System.
2. Select the user you want to modify.
3. In the **Groups** section of the user's profile, select the appropriate group (e.g., **Executive Board**, **General Members**, **Visitors**).
4. Click **Save** to apply the changes.

#### Best Practices for Managing Executive Groups and Permissions

- **Keep it simple**: Use clear and straightforward group names (e.g., **Executive Board**, **Members**, **Visitors**).
- **Limit high-level permissions**: Only assign **Add**, **Edit**, and **Delete** permissions to users who require those capabilities. Most users should only need **View** or **Add** permissions.
- **Review groups regularly**: Periodically check and update groups and their permissions to reflect changes in roles or responsibilities.

#### Example Group and Permission Setup

Here’s a common setup for **Executive Groups** and permissions:

- **Executive Board**:
  - Permissions: **Add**, **Edit**, **Delete**, **View**
  - Users: Admins or key executives who manage content, users, and system settings.

- **General Members**:
  - Permissions: **Add**, **View**
  - Users: Members who can contribute content (e.g., articles) but cannot delete or modify others' content.

- **Visitors**:
  - Permissions: **View** only
  - Users: Guests who can browse the content but cannot interact with it.

#### Summary

- **Executive Groups** organize users by role and determine the actions they can perform.
- **Permissions** define the scope of each group’s actions (view, add, edit, delete).
- You can manage groups and permissions easily through the **Groups** and **Users** sections of the CSS System.
- Regularly review your groups and permissions to ensure users have the appropriate level of access.

Every CSS Executive or appointee is provided with an Administrator account by the elected President. During account creation, permissions are set according to the user's role. The account details, such as email, phone number, and a custom password, are provided, and the user can change their password later.

### **Account Activation:**

- Once the account is created, an email is sent with login credentials, allowing the user to log in, change their password, and start working right away.

### **Account Misuse:**

- If an account or position is misused, the President can deactivate the account (not delete it). The account can be reactivated after careful consideration.

---

## Academics and Resources
![frontend view](./.readme_assets/aca.png)
This section allows the President or the executive in charge of academics to create courses and add resources that students need. Resources such as YouTube videos, articles, and files (e.g., slides, PDFs) can be added to these courses after the President's or academics administrators approval.
![courses view](./.readme_assets/courses.png)
- Please note that Courses are created first before academic resourcre can be assign to them
- Resources inlcude the following you see below
![resources](./.readme_assets/resoursces.png)
- Once approved, resources will be made available on the front-end for students to browse and use.

- Files will remain in the system until manually deleted, and they may be available for years unless removed.

### **Note:**

- The President or the Academic Board must approve resources before they are displayed, as only trusted content is shared with students.

---


### **Exam Allocation and Management**

The **Exam Allocation Section** is a comprehensive platform built to manage the allocation of examination locations to students. It ensures that students receive timely information about their assigned exam venues, the corresponding exam times, and relevant details such as maps and coordinates. Administrators can efficiently control and manage exam allocations, making the entire process smooth and transparent. The system also ensures that all notifications, including exam details and location data, are automatically sent to students.

![exam scheduled](./.readme_assets/exam_schedule.png)

- **Exam Location Assignment**: Admin assigns a specific location to each student (e.g., Room 101, Building A).
- **Exam Time**: The admin can set specific exam start and end times for each student.
- **Google Maps Integration**

### **Note:**

- Only authorized personnel (admin or designated executives) are permitted to modify or update the allocations to avoid errors or conflicts.

---

### **Admin Dashboard and Controls**

The Admin Dashboard is the control center of the Exam Allocation System, providing administrators with an easy-to-use interface to manage all aspects of exam assignments.

- **Examination Overview**: The admin can view all current and upcoming exam allocations for students, including their locations and times.
- **Search and Filter Options**: The dashboard allows the admin to filter students by exam location, status (allocated, pending, etc.), and exam time.
- **Modification and Reallocation**: The admin can reassign students to different locations or update exam times as necessary.
- **Bulk Allocation**: The admin can assign exam locations to multiple students simultaneously (for example, for a particular department or course).

### **Note:**

- All changes made through the admin dashboard are automatically updated in the system and notified to the affected students.

---

### **Notifications and Communication**

The system automatically sends out notifications to students once their exam locations and times are confirmed. The notifications contain all necessary details, such as:

- **Exam Location**: Coordinates of the exam venue and its address.
- **Exam Time**: The scheduled start and end time of the exam.
- **Map Link**: A link to the location on Google Maps, making it easy for students to find their exam venue.

The notification can be sent via:

- **Email**: Automatically sent to each student with all relevant details.
- **SMS** (if configured): A text message containing the basic details of the exam (location, time, and map link).

### **Note:**

- Students receive a single notification upon allocation, but the admin can manually resend notifications if any updates or changes are made to the exam details.

---

### **Google Maps Integration**

This section allows students to access the exact location of their exam venue through an integrated Google Maps link.

- The admin inputs the coordinates (latitude and longitude) for each exam location.
- The system generates a Google Maps link that students can click to view the exam venue and plan their route accordingly.

### **Note:**

- Accurate coordinates are critical for proper map functionality. The admin must double-check location data before finalizing allocations.

---

### **System Logs**

The system maintains a detailed log of all activities within the admin dashboard, including:
![Image Description](./.readme_assets/logs.png)
- **Exam Allocation Changes**: Who made the changes and when.
- **Notifications Sent**: Tracks which students were sent notifications and when.
- **Student Status Updates**: Logs updates to student allocation status (e.g., reallocation, new times).

### **Note:**

- The logs serve as an important audit trail for administrators to track changes and maintain transparency.

---

## Upcoming Events
![pic](./.readme_assets/events.png)
The Events and Programs section grants permissions to those in charge to write about upcoming events in the department, along with pictures and videos. This allows the department to keep students informed about upcoming activities.

---

## Timeline and Executive Position History (Achievements)

The Timeline is a historical record of events and programs within the department. After each event, pictures and videos are uploaded to the platform with student names tagged. If approved by the President, these are displayed publicly.

The goal of this feature is to preserve memories of department activities. Even years later, students can search for their names and view the events they participated in, along with related photos.

- Pictures can be removed from the timeline through a special request from the user, along with an explanation. If approved, the pictures will be removed.

---

## Executive Positions and Info (github, linkdin, twitter etc)
![execs](./.readme_assets/execs.png)

This information is controlled and provided by the administrators which is managed and changed in every change in executives
Executives account and changed to inactive after thier time in office and new roles are given after the neccessary permissions are assign

---

## News And Blogs
![Image Description](./.readme_assets/news_read.png)
![Image Description](./.readme_assets/news_read2.png)

## News and Blogs Feed
![Image](./.readme_assets/news.png)
Similar to events, this section is where news related to the department and blogs about Tech are written on the admin dashboard by individuals who permissions assign to them by the P.R.O Commitee. The news and blogs are published dynamically, so it doesn't need to be hardcoded each time. News and blog updates are automatically displayed for students to read.

---

## Advertisements

On the business side, the system allows ads to be displayed in order to generate sponsorship for the department. These ads are controlled by the department and can appear on the news site, event announcements, and other sections once approved.

---

## History

The system logs all activity within the admin dashboard for feedback purposes, as well as tracking the most recent logins. Accounts are arranged by the latest login, with the most recent user appearing at the top.

---

## The Plan

The frontend of the system will be open-source, allowing students to contribute. The backend will be maintained by core students for academic purposes, providing hands-on experience and the opportunity to work on a live project. This initiative aims to boost students' confidence in tackling real-world systems.

---

**Note:** For any questions or further clarification on specific features, please feel free to reach out. Some features are explained in more detail practically.

