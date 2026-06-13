"""
chatbot.py
ShopEase Customer Service Chatbot
Run: python chatbot.py
"""

import tkinter as tk
from tkinter import ttk
import datetime
import prompts_responses as pr


# ── Palette ──────────────────────────────────────────────────────────────────
BG_DARK      = "#0F1117"
BG_MID       = "#1A1D27"
BG_PANEL     = "#13151F"
BG_BUBBLE_US = "#1E6AFF"
BG_BUBBLE_BOT= "#1E2130"
ACCENT       = "#1E6AFF"
ACCENT_HOVER = "#3A7FFF"
TEXT_PRIMARY = "#E8EAF2"
TEXT_MUTED   = "#7880A0"
TEXT_BUBBLE  = "#FFFFFF"
CAT_COLORS   = {
    "Orders":           "#FF6B35",
    "Returns & Refunds":"#E040FB",
    "Payments":         "#00BCD4",
    "Shipping":         "#4CAF50",
    "Account":          "#FFC107",
    "Products":         "#FF4081",
    "Offers & Loyalty": "#69F0AE",
    "Contact Us":       "#1E6AFF",
}

FONT_FAMILY  = "Segoe UI"
FONT_TITLE   = (FONT_FAMILY, 13, "bold")
FONT_MSG     = (FONT_FAMILY, 11)
FONT_META    = (FONT_FAMILY, 9)
FONT_BTN     = (FONT_FAMILY, 9, "bold")
FONT_CAT     = (FONT_FAMILY, 8, "bold")


# ── Helpers ───────────────────────────────────────────────────────────────────
def now_time():
    return datetime.datetime.now().strftime("%I:%M %p")


def group_prompts():
    """Return OrderedDict: category → list of prompt dicts."""
    groups = {}
    for item in pr.PROMPTS_AND_RESPONSES:
        cat = item["category"]
        groups.setdefault(cat, []).append(item)
    return groups


# ── Main App ──────────────────────────────────────────────────────────────────
class ChatbotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{pr.COMPANY_NAME} · Customer Support")
        self.geometry("820x720")
        self.minsize(640, 560)
        self.configure(bg=BG_DARK)
        self._build_ui()
        self._post_welcome()

    # ── UI construction ────────────────────────────────────────────────────
    def _build_ui(self):
        self._build_header()

        # main pane: chat on top, prompt panel on bottom
        self.paned = tk.PanedWindow(
            self, orient=tk.VERTICAL,
            bg=BG_DARK, sashwidth=4, sashrelief="flat",
            sashpad=0
        )
        self.paned.pack(fill="both", expand=True, padx=0, pady=0)

        self._build_chat_area()
        self._build_prompt_panel()

        self.paned.add(self.chat_outer, minsize=180)
        self.paned.add(self.prompt_outer, minsize=140)
        self.paned.paneconfig(self.chat_outer,   stretch="always")
        self.paned.paneconfig(self.prompt_outer, stretch="never")

    def _build_header(self):
        hdr = tk.Frame(self, bg=BG_MID, height=56)
        hdr.pack(fill="x", side="top")
        hdr.pack_propagate(False)

        # Avatar circle
        canvas = tk.Canvas(hdr, width=36, height=36,
                            bg=BG_MID, highlightthickness=0)
        canvas.pack(side="left", padx=(16, 10), pady=10)
        canvas.create_oval(2, 2, 34, 34, fill=ACCENT, outline="")
        canvas.create_text(18, 18, text="SE", fill="white",
                            font=(FONT_FAMILY, 10, "bold"))

        info = tk.Frame(hdr, bg=BG_MID)
        info.pack(side="left", fill="y")
        tk.Label(info, text=f"{pr.COMPANY_NAME} Support",
                 bg=BG_MID, fg=TEXT_PRIMARY, font=FONT_TITLE).pack(anchor="w", pady=(8, 0))
        status_row = tk.Frame(info, bg=BG_MID)
        status_row.pack(anchor="w")
        dot = tk.Canvas(status_row, width=8, height=8,
                        bg=BG_MID, highlightthickness=0)
        dot.pack(side="left", pady=4)
        dot.create_oval(1, 1, 7, 7, fill="#4CAF50", outline="")
        tk.Label(status_row, text="Online · typically replies instantly",
                 bg=BG_MID, fg=TEXT_MUTED, font=FONT_META).pack(side="left", padx=4)

        # Clear button
        clear_btn = tk.Button(
            hdr, text="Clear Chat",
            bg=BG_PANEL, fg=TEXT_MUTED, font=FONT_META,
            relief="flat", cursor="hand2",
            activebackground=BG_MID, activeforeground=TEXT_PRIMARY,
            padx=10, pady=4, command=self._clear_chat
        )
        clear_btn.pack(side="right", padx=16)

    def _build_chat_area(self):
        self.chat_outer = tk.Frame(self, bg=BG_DARK)

        # Scrollable canvas for chat messages
        self.chat_canvas = tk.Canvas(
            self.chat_outer, bg=BG_DARK,
            highlightthickness=0, bd=0
        )
        self.chat_scroll = ttk.Scrollbar(
            self.chat_outer, orient="vertical",
            command=self.chat_canvas.yview
        )
        self.chat_canvas.configure(yscrollcommand=self.chat_scroll.set)

        self.chat_scroll.pack(side="right", fill="y")
        self.chat_canvas.pack(side="left", fill="both", expand=True)

        # Inner frame that holds all messages
        self.messages_frame = tk.Frame(self.chat_canvas, bg=BG_DARK)
        self.messages_window = self.chat_canvas.create_window(
            (0, 0), window=self.messages_frame, anchor="nw"
        )

        self.messages_frame.bind("<Configure>", self._on_frame_configure)
        self.chat_canvas.bind("<Configure>",    self._on_canvas_configure)
        self.chat_canvas.bind("<MouseWheel>",   self._on_mousewheel)
        self.messages_frame.bind("<MouseWheel>",self._on_mousewheel)

    def _build_prompt_panel(self):
        self.prompt_outer = tk.Frame(self, bg=BG_PANEL)

        # Fixed header bar
        panel_hdr = tk.Frame(self.prompt_outer, bg=BG_PANEL, height=32)
        panel_hdr.pack(fill="x", side="top")
        panel_hdr.pack_propagate(False)
        tk.Label(panel_hdr, text="  💬  Choose a topic",
                 bg=BG_PANEL, fg=TEXT_MUTED,
                 font=(FONT_FAMILY, 9, "bold")).pack(side="left", pady=4)

        sep = tk.Frame(self.prompt_outer, bg="#2A2D3E", height=1)
        sep.pack(fill="x")

        # Scrollable button area
        btn_canvas = tk.Canvas(
            self.prompt_outer, bg=BG_PANEL,
            highlightthickness=0, bd=0
        )
        btn_hscroll = ttk.Scrollbar(
            self.prompt_outer, orient="horizontal",
            command=btn_canvas.xview
        )
        btn_canvas.configure(xscrollcommand=btn_hscroll.set)

        btn_hscroll.pack(side="bottom", fill="x")
        btn_canvas.pack(fill="both", expand=True)

        self.btn_frame = tk.Frame(btn_canvas, bg=BG_PANEL)
        btn_canvas.create_window((0, 0), window=self.btn_frame, anchor="nw")

        self.btn_frame.bind(
            "<Configure>",
            lambda e: btn_canvas.configure(
                scrollregion=btn_canvas.bbox("all")
            )
        )
        btn_canvas.bind("<MouseWheel>", lambda e: btn_canvas.xview_scroll(-1 * (e.delta // 120), "units"))
        self.btn_frame.bind("<MouseWheel>", lambda e: btn_canvas.xview_scroll(-1 * (e.delta // 120), "units"))

        self._populate_prompt_buttons()

    def _populate_prompt_buttons(self):
        groups = group_prompts()
        col = 0
        for cat, items in groups.items():
            color = CAT_COLORS.get(cat, ACCENT)

            # Category label
            cat_lbl = tk.Label(
                self.btn_frame,
                text=f"  {cat.upper()}  ",
                bg=BG_PANEL, fg=color,
                font=FONT_CAT
            )
            cat_lbl.grid(row=0, column=col, columnspan=len(items),
                         sticky="w", padx=(10, 0), pady=(10, 2))

            for i, item in enumerate(items):
                btn = self._make_prompt_btn(item, color)
                btn.grid(row=1, column=col, padx=(10 if i == 0 else 4, 4),
                         pady=(0, 12), sticky="ns")
                col += 1

            # Thin divider between categories (visual column spacer)
            spacer = tk.Frame(self.btn_frame, bg="#2A2D3E", width=1)
            spacer.grid(row=0, column=col, rowspan=2, sticky="ns",
                        padx=(4, 0), pady=6)
            col += 1

    def _make_prompt_btn(self, item: dict, color: str) -> tk.Button:
        prompt_text = item["prompt"]

        def on_enter(e):
            btn.config(bg=color, fg="white")

        def on_leave(e):
            btn.config(bg=BG_MID, fg=color)

        def on_click():
            self._handle_prompt(item)

        btn = tk.Button(
            self.btn_frame,
            text=prompt_text,
            bg=BG_MID, fg=color,
            font=FONT_BTN,
            relief="flat",
            cursor="hand2",
            padx=12, pady=6,
            wraplength=130,
            justify="center",
            activebackground=color,
            activeforeground="white",
            command=on_click
        )
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # ── Message rendering ──────────────────────────────────────────────────
    def _post_welcome(self):
        self._add_bot_message(pr.WELCOME_MESSAGE)

    def _handle_prompt(self, item: dict):
        self._add_user_message(item["prompt"])
        self.after(350, lambda: self._add_bot_message(item["response"]))

    def _add_user_message(self, text: str):
        outer = tk.Frame(self.messages_frame, bg=BG_DARK)
        outer.pack(fill="x", pady=(4, 0), padx=12)

        row = tk.Frame(outer, bg=BG_DARK)
        row.pack(side="right")

        bubble = tk.Label(
            row, text=text,
            bg=BG_BUBBLE_US, fg=TEXT_BUBBLE,
            font=FONT_MSG,
            wraplength=460,
            justify="left",
            padx=14, pady=10,
            relief="flat",
        )
        bubble.pack(side="top", anchor="e")

        meta = tk.Label(
            row, text=now_time(),
            bg=BG_DARK, fg=TEXT_MUTED, font=FONT_META
        )
        meta.pack(anchor="e", pady=(2, 6))

        self._scroll_to_bottom()

    def _add_bot_message(self, text: str):
        outer = tk.Frame(self.messages_frame, bg=BG_DARK)
        outer.pack(fill="x", pady=(4, 0), padx=12)

        row = tk.Frame(outer, bg=BG_DARK)
        row.pack(side="left")

        # Small avatar
        av = tk.Canvas(row, width=28, height=28,
                       bg=BG_DARK, highlightthickness=0)
        av.pack(side="left", anchor="n", pady=(4, 0), padx=(0, 6))
        av.create_oval(2, 2, 26, 26, fill=ACCENT, outline="")
        av.create_text(14, 14, text="SE", fill="white",
                       font=(FONT_FAMILY, 7, "bold"))

        msg_col = tk.Frame(row, bg=BG_DARK)
        msg_col.pack(side="left", fill="x")

        bubble = tk.Label(
            msg_col, text=text,
            bg=BG_BUBBLE_BOT, fg=TEXT_PRIMARY,
            font=FONT_MSG,
            wraplength=460,
            justify="left",
            padx=14, pady=10,
            relief="flat",
        )
        bubble.pack(anchor="w")

        meta = tk.Label(
            msg_col, text=f"Support · {now_time()}",
            bg=BG_DARK, fg=TEXT_MUTED, font=FONT_META
        )
        meta.pack(anchor="w", pady=(2, 6))

        self._scroll_to_bottom()

    # ── Utility ────────────────────────────────────────────────────────────
    def _scroll_to_bottom(self):
        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)

    def _clear_chat(self):
        for widget in self.messages_frame.winfo_children():
            widget.destroy()
        self._post_welcome()

    def _on_frame_configure(self, event=None):
        self.chat_canvas.configure(
            scrollregion=self.chat_canvas.bbox("all")
        )

    def _on_canvas_configure(self, event):
        self.chat_canvas.itemconfig(
            self.messages_window, width=event.width
        )

    def _on_mousewheel(self, event):
        self.chat_canvas.yview_scroll(-1 * (event.delta // 120), "units")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    style = ttk.Style()
    try:
        style.theme_use("clam")
    except Exception:
        pass
    style.configure("Vertical.TScrollbar",
                    background=BG_MID,
                    troughcolor=BG_DARK,
                    arrowcolor=TEXT_MUTED,
                    bordercolor=BG_DARK,
                    lightcolor=BG_MID,
                    darkcolor=BG_MID)
    style.configure("Horizontal.TScrollbar",
                    background=BG_MID,
                    troughcolor=BG_PANEL,
                    arrowcolor=TEXT_MUTED,
                    bordercolor=BG_PANEL,
                    lightcolor=BG_MID,
                    darkcolor=BG_MID)

    app = ChatbotApp()
    app.mainloop()
