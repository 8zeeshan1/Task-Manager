# Task Management Application
#### Video Demo: [https://youtu.be/1s03HoffjO4?si=M26OOOTzDj12wLpR](#)
#### Description:

This project is a web-based **Task Management Application** built using the Flask framework. It enables users to efficiently manage their tasks by adding, amending, and deleting tasks, all while providing a simple and intuitive user interface.

### Features:
- **Add Tasks**: Users can add a subject and description for their tasks using a form on the main page.
- **Amend Tasks**: Tasks can be modified, allowing users to update the subject or description when needed.
- **Delete Tasks**: Completed tasks can be marked as "done" and removed from the list.
- **Timestamp Management**: Each task is automatically assigned a date and time (based on IST) when added, providing better tracking of task creation.
- **Real-time Flash Messages**: Feedback is displayed for user actions such as invalid input, ensuring a smooth user experience.
- **Responsive UI**: The interface is styled with CSS to ensure accessibility and aesthetic appeal, working seamlessly on both desktop and mobile devices.

---

### File Descriptions:
#### 1. **`app.py`**
This is the main Flask application file containing:
- **Route Handlers**:
  - `/`: Displays the homepage with options to add tasks, view the task list, and displays the date and time for each task.
  - `/amend`: Handles retrieving and displaying task data for amendments.
  - `/amendt`: Updates a specific task in the database.
  - `/done`: Deletes a task from the database.
- **Logic for Validation**: Includes form validation logic to ensure tasks cannot be added or amended with missing fields.
- **Database Operations**: Interacts with the SQLite database to execute CRUD (Create, Read, Update, Delete) operations.
- **Timestamp Integration**: Automatically records the current date and time for tasks, displayed on the main page with date and time on separate lines.

#### 2. **Templates Folder**:
Contains HTML files for rendering the web application:
- **`layout.html`**: The base layout that all pages extend, ensuring consistency in design and structure.
- **`index.html`**: The main page where users can add tasks, view the list of existing tasks, and see the date and time each task was added.
- **`amend.html`**: A form page for amending existing tasks, pre-filled with current task data.

#### 3. **Static Folder**:
Contains static files:
- **`styles.css`**: Defines the styling for all pages, including form elements, tables, buttons, and the responsive layout.
- **Background Image**: Adds a subtle background image to enhance the visual appeal of the main page.

#### 4. **Database File (`task.db`)**:
- SQLite database that stores all tasks with the following schema:
  - `id`: A unique identifier for each task.
  - `name`: The subject of the task.
  - `task`: A detailed description of the task.
  - `timestamp`: The date and time (IST) when the task was created.

---

### Design Choices:
1. **Framework**: Flask was chosen for its simplicity and ability to quickly build web applications.
2. **Database**: SQLite was selected for its lightweight nature, making it ideal for small-scale projects.
3. **UI Styling**: CSS was used to create a clean and modern interface. A background image was added to enhance visual appeal, with adjustments for responsiveness.
4. **Timestamp Management**: Adding a timestamp helps track when tasks are created, providing more detailed task tracking.

---

### Installation Instructions:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/8zeeshan1/Task-Manager
   cd Task-Manager
