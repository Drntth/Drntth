# Configuring Gnome Desktop Application Launchers

---

> :uk: English | [:hungary: Magyar](../hu/ubuntu/configuring-gnome-desktop-application-launchers.md)

---

## Purpose

This guide explains how to configure the launch parameters of application icons displayed on the left-hand side of the Ubuntu Gnome desktop. This involves editing `.desktop` files located in the `~/.local/share/applications` directory.

---

## Key Concepts

- **Desktop Files**: `.desktop` files define how an application is launched, including its name, icon, and execution parameters.
- **Custom Launchers**: User-created `.desktop` files for applications not installed system-wide.
- **File Location**: User-specific `.desktop` files are stored in `~/.local/share/applications`.

---

## Installation

No additional installation is required, as `.desktop` file handling is built into the Gnome desktop environment.

---

## Basic Usage

1. **Locate the `.desktop` File**: Navigate to `~/.local/share/applications` to find or create a `.desktop` file for the application.

2. **Edit the `.desktop` file**: Open the file with a text editor

  ```bash
  nano ~/.local/share/applications/example.desktop
  ```

3. **Modify the Exec line to include the desired parameters**: `Exec=/path/to/application --parameter1 --parameter2`

4. **Save and refresh**: Save the file and refresh the desktop menu:

  ```bash
  update-desktop-database ~/.local/share/applications/
  ```

5. **Test the configuration**: Click the icon on the desktop or in the application overview to verify the changes

---

## Shortcuts

- `Super + A`: Open the application overview.
- `Alt + F2`: Run a command.

---

## Best Practices

- Always back up `.desktop` files before making changes.
- Use absolute paths in the Exec field to avoid issues.
- Test changes immediately to ensure they work as expected.

---

## Common Pitfalls

- **Incorrect Paths**: Double-check file paths and parameters in the Exec field.
- **Caching Issues**: If changes don't appear, try restarting Gnome Shell: ```Alt + F2, then type `r` and press Enter.```

---

## Example Code

### Generic Example Launcher

The following is a generic example of a `.desktop` file, named [`example.desktop`](../../code/gnome-desktop/example.desktop), which can be used to create a custom application launcher.

To use this file copy it to the `~/.local/share/applications` directory, renaming it to match your desired application name:

```bash
cp /code/example.desktop ~/.local/share/applications/application_name.desktop
```

Then open the copied file and modify the parameters to suit your application:

- `Name`: The name of your application (e.g., "Custom Application").
- `Comment`: A short description of what the application does.
- `Exec`: The command to execute, including any required parameters (e.g., `/path/to/application --parameter1 --parameter2`).
- `Icon`: The path to the application's icon file.
- `Terminal`: Set to `false` if the application does not require a terminal.
- `Type`: Always set to `Application`.
- `Categories`: Specify the category (e.g., `Utility`).

### Terminator Launcher Example

Here is an example [`terminator.desktop`](../../code/gnome-desktop/terminator.desktop) file for launching the Terminator terminal emulator with a specific layout.

To use copy this file to your folder and change `--layout` name for your own config layout name.

```bash
cp /code/terminator.desktop ~/.local/share/applications/terminator.desktop
```

Then save the file and refresh the desktop menu:

```bash
update-desktop-database ~/.local/share/applications/
```

---

## Sources

- [Gnome Documentation](https://help.gnome.org/users/gnome-help/stable/index.html): Official Gnome help documentation.
- [Ubuntu Community Help Wiki](https://help.ubuntu.com/community): Community-driven help resources for Ubuntu users.
