import { app } from "../../scripts/app.js";
import { api } from "../../scripts/api.js";

const EXT = "agent_menu_ext";
const ROUTE_ASK = "/agent_menu_ext/ask";

// --------- UI State (persist across tab re-renders) ----------
const AgentUI = {
  root: null,
  msgs: null,
  input: null,
  sendBtn: null,
  thinkingEl: null,
  busy: false,
};

// --------- Styles ----------
function ensureChatStylesOnce() {
  if (document.getElementById("agent_chat_styles")) return;

  const style = document.createElement("style");
  style.id = "agent_chat_styles";
  style.textContent = `
    .agent-chat {
      height: 100%;
      min-height: 0;              /* IMPORTANT for flex scrolling */
      display: flex;
      flex-direction: column;
      padding: 10px;
      gap: 10px;
      box-sizing: border-box;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
    }

    .agent-chat__msgs {
      flex: 1 1 auto;
      min-height: 0;              /* IMPORTANT for flex scrolling */
      overflow-y: auto;           /* vertical scroll */
      overflow-x: hidden;
      display:flex;
      flex-direction: column;
      gap: 8px;
      padding: 10px;
      border-radius: 12px;
      border: 1px solid var(--border-color, #4e4e4e);
      background: rgba(0,0,0,0.12);
    }

    .agent-msg {
      padding: 8px 10px;
      border-radius: 12px;
      line-height: 1.25;
      max-width: 95%;
      white-space: pre-wrap;
      overflow-wrap: anywhere;
    }

    .agent-msg--user {
      align-self: flex-end;
      background: rgba(255,255,255,.08);
      border: 1px solid rgba(255,255,255,.10);
    }

    .agent-msg--bot {
      align-self: flex-start;
      background: rgba(0,0,0,.18);
      border: 1px solid rgba(255,255,255,.08);
    }

    .agent-msg--thinking::after {
      content: " …";
      animation: agentDots 1.2s steps(4, end) infinite;
      opacity: 0.9;
    }
    @keyframes agentDots {
      0%   { content: ""; }
      25%  { content: "."; }
      50%  { content: ".."; }
      75%  { content: "..."; }
      100% { content: ""; }
    }

    .agent-chat__footer {
      display:flex;
      gap: 8px;
      align-items:flex-end;
    }

    .agent-input {
      flex: 1;
      resize: vertical;
      min-height: 44px;
      max-height: 160px;
      border-radius: 12px;
      border: 1px solid var(--border-color, #4e4e4e);
      background: var(--comfy-input-bg, #222);
      color: var(--input-text, #ddd);
      padding: 10px;
      outline: none;
      box-sizing: border-box;
    }

    .agent-btn {
      border-radius: 12px;
      padding: 10px 14px;
      cursor: pointer;
      border: 1px solid var(--border-color, #4e4e4e);
      background: var(--comfy-menu-secondary-bg, #303030);
      color: var(--fg-color, #fff);
      height: 44px;
      box-sizing: border-box;
    }

    .agent-btn:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
  `;
  document.head.appendChild(style);
}

// --------- Backend call ----------
async function askPython(text) {
  const resp = await api.fetchApi(ROUTE_ASK, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  // If Python returns {"error": "..."} with 500, show that nicely
  if (!resp.ok) {
    const bodyText = await resp.text().catch(() => "");
    throw new Error(`HTTP ${resp.status} ${resp.statusText}${bodyText ? `: ${bodyText}` : ""}`);
  }

  const data = await resp.json();
  return data.answer ?? "";
}

// --------- Helpers ----------
function scrollToBottom() {
  if (!AgentUI.msgs) return;
  AgentUI.msgs.scrollTop = AgentUI.msgs.scrollHeight;
}

function addMessage(role, text) {
  const el = document.createElement("div");
  el.className = `agent-msg ${role === "user" ? "agent-msg--user" : "agent-msg--bot"}`;
  el.textContent = text;
  AgentUI.msgs.appendChild(el);
  scrollToBottom();
}

function addThinking() {
  // Remove existing one if present
  removeThinking();

  const el = document.createElement("div");
  el.className = "agent-msg agent-msg--bot agent-msg--thinking";
  el.textContent = "Thinking";
  el.dataset.thinking = "1";

  AgentUI.msgs.appendChild(el);
  AgentUI.thinkingEl = el;
  scrollToBottom();
}

function removeThinking() {
  if (AgentUI.thinkingEl && AgentUI.thinkingEl.parentNode) {
    AgentUI.thinkingEl.parentNode.removeChild(AgentUI.thinkingEl);
  }
  AgentUI.thinkingEl = null;
}

function setBusy(isBusy) {
  AgentUI.busy = isBusy;

  if (AgentUI.input) {
    AgentUI.input.disabled = isBusy;
    AgentUI.input.placeholder = isBusy
      ? "Thinking…"
      : "Type… (Enter to send, Shift+Enter for newline)";
  }
  if (AgentUI.sendBtn) {
    AgentUI.sendBtn.disabled = isBusy;
    AgentUI.sendBtn.textContent = isBusy ? "…" : "Send";
  }
}

// --------- Build + Mount ----------
function ensureUI(el) {
  ensureChatStylesOnce();

  // Make sure the container can constrain height for scrolling
  el.style.height = "100%";
  el.style.minHeight = "0";

  // Reuse existing UI so you keep chat history when tab rerenders
  if (AgentUI.root && el.contains(AgentUI.root)) return;

  if (!AgentUI.root) {
    const root = document.createElement("div");
    root.className = "agent-chat";

    const msgs = document.createElement("div");
    msgs.className = "agent-chat__msgs";

    const footer = document.createElement("div");
    footer.className = "agent-chat__footer";

    const input = document.createElement("textarea");
    input.className = "agent-input";
    input.placeholder = "Type… (Enter to send, Shift+Enter for newline)";

    const sendBtn = document.createElement("button");
    sendBtn.className = "agent-btn";
    sendBtn.textContent = "Send";

    async function send() {
      if (AgentUI.busy) return; // prevent sending while thinking

      const text = input.value.trim();
      if (!text) return;

      input.value = "";
      addMessage("user", text);

      setBusy(true);
      addThinking();

      try {
        const answer = await askPython(text);
        removeThinking();
        addMessage("bot", answer || "(empty reply)");
      } catch (e) {
        console.error(e);
        removeThinking();
        addMessage("bot", `Error: ${e?.message || e}`);
      } finally {
        setBusy(false);
        input.focus();
      }
    }

    sendBtn.onclick = send;

    input.addEventListener("keydown", (ev) => {
      if (AgentUI.busy) return; // block typing? (disabled does this anyway)
      if (ev.key === "Enter" && !ev.shiftKey) {
        ev.preventDefault();
        send();
      }
    });

    footer.appendChild(input);
    footer.appendChild(sendBtn);

    root.appendChild(msgs);
    root.appendChild(footer);

    AgentUI.root = root;
    AgentUI.msgs = msgs;
    AgentUI.input = input;
    AgentUI.sendBtn = sendBtn;

    addMessage("bot", "Agent ready. (Waiting for your message.)");
  }

  el.innerHTML = "";
  el.appendChild(AgentUI.root);
  scrollToBottom();
}

// --------- Register extension ----------
app.registerExtension({
  name: EXT,

  bottomPanelTabs: [
    {
      id: `${EXT}.chat`,
      title: "Agent",
      type: "custom",
      render: (el) => ensureUI(el),
    },
  ],

  commands: [
    {
      id: `${EXT}.open`,
      label: "Open Agent (Bottom Tab)",
      function: () => {
        app.extensionManager?.toast?.add?.({
          severity: "info",
          summary: "Agent",
          detail: "Open the bottom panel tab named “Agent”.",
          life: 2500,
        });
      },
    },
  ],

  menuCommands: [
    { path: ["Extensions", "Agent"], commands: [`${EXT}.open`] },
  ],
});
