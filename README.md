<div align="center">

# ⛔ WebView2 Hard Blocker
### by [Pascal Tweaks](https://github.com/pascaltweaks)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.x-orange?style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows-10%2F11-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Admin Required](https://img.shields.io/badge/Requires-Administrator-red?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A system-level tool to completely block, kill, or restore Microsoft WebView2 — built for gamers and power users who want full control over background processes.**

</div>

---

## 🧠 What is WebView2?

Microsoft Edge WebView2 (`msedgewebview2.exe`) is a runtime component embedded in Windows that allows applications to render web content inside native apps. While it serves legitimate purposes, it also runs silently in the background — consuming CPU, RAM, and disk — even during gaming sessions or when you simply don't need it.

**WebView2 Hard Blocker** gives you a one-click solution to shut it down completely and bring it back when you're done.

---

## ✨ Features

- **Hard Disable** — Renames the WebView2 executable, replaces it with a dummy block file, applies IFEO debugger traps, and disables the associated Windows service. WebView2 **cannot** run under any circumstance.
- **Re-Enable** — Fully restores the original executable, removes all blocks, and re-enables the service. Clean, reversible, no leftovers.
- **Kill Processes** — Instantly terminates all running `msedgewebview2.exe` and `MicrosoftEdgeUpdate.exe` processes without applying a permanent block.
- **Live Activity Log** — Every action is timestamped and logged in real time directly in the GUI.
- **Admin Auto-Elevation** — Automatically requests administrator privileges on launch. No manual UAC prompts needed.
- **Dark Terminal UI** — Built with CustomTkinter for a clean, modern dark interface.

---

## 📸 Preview

> *<img width="1512" height="808" alt="image" src="https://github.com/user-attachments/assets/0560a08d-1819-497a-b8ef-ebf729edb602" />
*

---

## 🚀 Getting Started

### Requirements

- Windows 10 or 11
- Python 3.8 or higher
- `customtkinter` library

### Installation

```bash
git clone https://github.com/pascaltweaks/webview2-hard-blocker.git
cd webview2-hard-blocker
pip install customtkinter
```

### Run

```bash
python WebView2Blocker.py
```

> The tool will automatically request Administrator privileges on launch. If UAC prompts you, click **Yes**.

---

## ⚙️ How It Works

### Hard Disable (Gaming Mode)

When you press **HARD DISABLE**, the tool applies the following in sequence:

| Step | Action |
|------|--------|
| 1 | Kills any running `msedgewebview2.exe` processes |
| 2 | Stops and disables `MicrosoftEdgeElevationService` |
| 3 | Takes ownership of the WebView2 executable and renames it to `.disabled` |
| 4 | Creates a dummy empty file in its place marked as read-only |
| 5 | Applies an **IFEO Debugger** registry trap (`cmd.exe`) so any launch attempt is intercepted |
| 6 | Sets AppLocker-level registry restrictions |

### Re-Enable (Normal Mode)

All changes are fully reversible. Re-Enable:

- Removes the IFEO debugger trap
- Deletes the dummy block file
- Renames `.disabled` back to the original executable
- Re-enables and starts the Windows service
- Clears the AppLocker registry restriction

---

## ⚠️ Disclaimer

> This tool makes **system-level changes** including registry modifications, file ownership transfers, and Windows service control. It is intended for advanced users who understand the implications.
>
> Some applications (Widgets, Teams, certain Microsoft 365 apps) rely on WebView2 and **may crash or fail to open** while the hard block is active. Always re-enable WebView2 when you are done gaming or no longer need the block.
>
> **Pascal Tweaks is not responsible for any system instability caused by improper use of this tool.**

---

## 📁 Files

```
webview2-hard-blocker/
├── WebView2Blocker.py     # Main GUI application
├── Webview.bat            # Original batch script (legacy)
└── README.md
```

---

## 🛠️ Built With

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — Modern Python UI framework
- Python `subprocess`, `ctypes`, `threading`, `os` — System control
- Windows Registry & Service APIs via native CLI tools

---

## 📜 License

This project is licensed under the **MIT License** — feel free to fork, modify, and distribute with credit.

---

<div align="center">

Made with ☕ by **Pascal Tweaks**

*If this helped you, drop a ⭐ on the repo!*

</div>
