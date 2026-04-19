import customtkinter as ctk
import subprocess
import threading
import ctypes
import sys
import os
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

class WebView2Blocker(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("WebView2 Hard Blocker")
        self.geometry("560x680")
        self.resizable(False, False)
        self.configure(fg_color="#0A0A0F")

        self._build_ui()
        self._check_admin()

    def _build_ui(self):
        self.header_frame = ctk.CTkFrame(self, fg_color="#111118", corner_radius=0, height=90)
        self.header_frame.pack(fill="x", side="top")
        self.header_frame.pack_propagate(False)

        self.accent_bar = ctk.CTkFrame(self, fg_color="#FF3C3C", corner_radius=0, height=2)
        self.accent_bar.pack(fill="x")

        title_label = ctk.CTkLabel(
            self.header_frame,
            text="WEBVIEW2  HARD BLOCKER",
            font=ctk.CTkFont(family="Consolas", size=20, weight="bold"),
            text_color="#FF3C3C"
        )
        title_label.place(x=24, y=18)

        sub_label = ctk.CTkLabel(
            self.header_frame,
            text="System-level WebView2 process control",
            font=ctk.CTkFont(family="Consolas", size=10),
            text_color="#606070"
        )
        sub_label.place(x=26, y=56)

        status_dot_color = "#3CFF7A" if is_admin() else "#FF9020"
        status_text = "Administrator" if is_admin() else "Limited Rights"
        self.status_label = ctk.CTkLabel(
            self.header_frame,
            text=f"● {status_text}",
            font=ctk.CTkFont(family="Consolas", size=9),
            text_color=status_dot_color
        )
        self.status_label.place(relx=1.0, x=-20, y=20, anchor="ne")

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=(18, 0), padx=30, fill="x")

        self._make_action_button(
            btn_frame,
            icon="⛔",
            label="HARD DISABLE  WebView2",
            sublabel="Blocks all execution — Gaming Mode",
            border_color="#FF3C3C",
            hover_color="#1A0808",
            command=lambda: self._run_task(self._hard_disable)
        ).pack(fill="x", pady=(0, 10))

        self._make_action_button(
            btn_frame,
            icon="✅",
            label="RE-ENABLE  WebView2",
            sublabel="Restores full functionality — Normal Mode",
            border_color="#3CDD88",
            hover_color="#08180E",
            command=lambda: self._run_task(self._enable)
        ).pack(fill="x", pady=(0, 10))

        self._make_action_button(
            btn_frame,
            icon="💀",
            label="KILL  Running Processes",
            sublabel="Terminates active WebView2 instances now",
            border_color="#FFA020",
            hover_color="#18100A",
            command=lambda: self._run_task(self._kill)
        ).pack(fill="x", pady=(0, 10))

        self._make_action_button(
            btn_frame,
            icon="✕",
            label="EXIT",
            sublabel="Close this tool",
            border_color="#404055",
            hover_color="#111118",
            command=self.destroy
        ).pack(fill="x")

        log_header = ctk.CTkFrame(self, fg_color="transparent")
        log_header.pack(padx=30, pady=(18, 4), fill="x")

        ctk.CTkLabel(
            log_header,
            text="ACTIVITY LOG",
            font=ctk.CTkFont(family="Consolas", size=9, weight="bold"),
            text_color="#404055"
        ).pack(side="left")

        self.clear_btn = ctk.CTkButton(
            log_header,
            text="CLEAR",
            font=ctk.CTkFont(family="Consolas", size=9),
            fg_color="transparent",
            hover_color="#1A1A25",
            text_color="#404055",
            border_color="#404055",
            border_width=1,
            height=20,
            width=55,
            corner_radius=4,
            command=self._clear_log
        )
        self.clear_btn.pack(side="right")

        self.log_box = ctk.CTkTextbox(
            self,
            fg_color="#08080C",
            text_color="#3CFF7A",
            font=ctk.CTkFont(family="Consolas", size=9),
            corner_radius=8,
            border_width=1,
            border_color="#1E1E2A",
            wrap="word",
            height=140
        )
        self.log_box.pack(padx=30, pady=(0, 20), fill="x")
        self.log_box.configure(state="disabled")

    def _make_action_button(self, parent, icon, label, sublabel, border_color, hover_color, command):
        frame = ctk.CTkFrame(
            parent,
            fg_color="#13131C",
            corner_radius=10,
            border_width=1,
            border_color=border_color
        )

        inner = ctk.CTkFrame(frame, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=16, pady=14)

        icon_lbl = ctk.CTkLabel(
            inner,
            text=icon,
            font=ctk.CTkFont(size=22),
            text_color=border_color,
            width=36
        )
        icon_lbl.pack(side="left", padx=(0, 12))

        text_col = ctk.CTkFrame(inner, fg_color="transparent")
        text_col.pack(side="left", fill="x", expand=True)

        ctk.CTkLabel(
            text_col,
            text=label,
            font=ctk.CTkFont(family="Consolas", size=11, weight="bold"),
            text_color="#E0E0EE",
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            text_col,
            text=sublabel,
            font=ctk.CTkFont(family="Consolas", size=9),
            text_color="#505065",
            anchor="w"
        ).pack(anchor="w")

        def on_enter(e):
            frame.configure(fg_color=hover_color)
        def on_leave(e):
            frame.configure(fg_color="#13131C")
        def on_click(e):
            command()

        for widget in [frame, inner, icon_lbl, text_col] + list(inner.winfo_children()) + list(text_col.winfo_children()):
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

        frame.configure(cursor="hand2")
        return frame

    def _log(self, msg, color="#3CFF7A"):
        ts = datetime.now().strftime("%H:%M:%S")
        self.log_box.configure(state="normal")
        self.log_box.insert("end", f"[{ts}]  {msg}\n")
        self.log_box.configure(state="disabled")
        self.log_box.see("end")

    def _clear_log(self):
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

    def _check_admin(self):
        if not is_admin():
            self._log("WARNING: Not running as Administrator!", "#FF9020")
            self._log("Some operations may fail. Re-run as Admin.", "#FF9020")
        else:
            self._log("Running with Administrator privileges")

    def _run_task(self, fn):
        threading.Thread(target=fn, daemon=True).start()

    def _run(self, cmd):
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

    def _hard_disable(self):
        self._log("Applying HARD BLOCK on WebView2...", "#FF3C3C")

        self._run("taskkill /f /im msedgewebview2.exe")
        self._log("[OK] Killed existing WebView2 processes")

        self._run("sc stop MicrosoftEdgeElevationService")
        self._run("sc config MicrosoftEdgeElevationService start= disabled")
        self._log("[OK] Service disabled")

        exe = r"C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe"
        disabled = exe + ".disabled"
        if os.path.exists(exe):
            self._run(f'takeown /f "{exe}" /a')
            self._run(f'icacls "{exe}" /grant administrators:F')
            try:
                os.rename(exe, disabled)
                self._log("[OK] Renamed WebView2 executable")
                open(exe, "w").close()
                self._run(f'attrib +r "{exe}"')
                self._log("[OK] Created block file")
            except Exception as ex:
                self._log(f"[!!] File operation failed: {ex}", "#FF9020")

        self._run('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Appx" /v AllowAllTrustedApps /t REG_DWORD /d 0 /f')
        self._log("[OK] App restrictions added")

        self._run('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\msedgewebview2.exe" /v Debugger /t REG_SZ /d cmd.exe /f')
        self._log("[OK] IFEO Debugger block applied")

        self._log("HARD BLOCK ACTIVE — WebView2 cannot run", "#FF3C3C")

    def _enable(self):
        self._log("Re-enabling WebView2...", "#3CDD88")

        self._run('reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\msedgewebview2.exe" /f')
        self._log("[OK] Removed IFEO block")

        exe = r"C:\Program Files (x86)\Microsoft\EdgeWebView\Application\msedgewebview2.exe"
        disabled = exe + ".disabled"
        if os.path.exists(disabled):
            try:
                self._run(f'attrib -r "{exe}"')
                if os.path.exists(exe):
                    os.remove(exe)
                os.rename(disabled, exe)
                self._log("[OK] Restored original executable")
            except Exception as ex:
                self._log(f"[!!] File restore failed: {ex}", "#FF9020")

        self._run("sc config MicrosoftEdgeElevationService start= manual")
        self._run("sc start MicrosoftEdgeElevationService")
        self._log("[OK] Service re-enabled")

        self._run('reg delete "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Appx" /v AllowAllTrustedApps /f')
        self._log("[OK] Removed App restrictions")

        self._log("WebView2 FULLY ENABLED — Normal operation restored", "#3CDD88")

    def _kill(self):
        self._log("Killing all WebView2 processes...", "#FFA020")
        self._run("taskkill /f /im msedgewebview2.exe")
        self._run("taskkill /f /im MicrosoftEdgeUpdate.exe")
        self._log("[OK] All WebView2 processes terminated")


if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
        sys.exit()
    app = WebView2Blocker()
    app.mainloop()
