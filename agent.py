"""
Agentic AI Assistant (Phase I Prototype)
Implements a SUSPADR-based decision loop for safe automated email replies.
Author: Agasthya S, Kanishk Samurai G, Pavan B
Guide: Dr. M. Nirmala Devi
Thiagarajar College of Engineering, Dept. of CSE
"""

import random
import time

# -----------------------------
# STAGE 1: SENSE
# -----------------------------
def sense_incoming_mail():
    print("📥 Sensing incoming mail...")
    time.sleep(1)
    email = {
        "sender": "hr@example.com",
        "subject": "Interview Schedule Confirmation",
        "body": "Dear candidate, please confirm your availability for the interview tomorrow at 10 AM."
    }
    print("✅ Mail received from:", email["sender"])
    return email


# -----------------------------
# STAGE 2: UNDERSTAND
# -----------------------------
def understand_context(email):
    print("\n🧠 Understanding context...")
    time.sleep(1)
    intent = "confirmation"
    tone = "formal"
    print(f"Intent: {intent}, Tone: {tone}")
    return {"intent": intent, "tone": tone}


# -----------------------------
# STAGE 3: SIMULATE
# -----------------------------
def simulate_risks(email):
    print("\n⚙️ Simulating risks and safety checks...")
    time.sleep(1)
    contains_sensitive_data = any(word in email["body"].lower() for word in ["password", "account", "otp"])
    if contains_sensitive_data:
        risk_level = "High"
    else:
        risk_level = "Low"
    print("Risk level:", risk_level)
    return risk_level


# -----------------------------
# STAGE 4: PLAN
# -----------------------------
def plan_reply(intent):
    print("\n📝 Planning the reply template...")
    time.sleep(1)
    templates = {
        "confirmation": "Dear {sender},\n\nThank you for your message. I confirm my availability for the interview.\n\nBest regards,\nAgasthya",
        "thanks": "Dear {sender},\n\nThank you for your update.\n\nBest,\nAgasthya",
        "query": "Dear {sender},\n\nI have received your query and will get back to you shortly.\n\nRegards,\nAgasthya"
    }
    chosen_template = templates.get(intent, templates["thanks"])
    print("Template selected.")
    return chosen_template


# -----------------------------
# STAGE 5: ACT
# -----------------------------
def act_generate_reply(template, email):
    print("\n✉️ Generating draft reply...")
    reply = template.format(sender=email["sender"])
    print("Draft created.")
    return reply


# -----------------------------
# STAGE 6: DECIDE
# -----------------------------
def decide_action(risk_level):
    print("\n🤖 Deciding whether to send automatically...")
    time.sleep(1)
    confidence = random.uniform(0.6, 0.99) if risk_level == "Low" else random.uniform(0.3, 0.6)
    print(f"Confidence Score: {confidence:.2f}")
    if confidence > 0.75:
        action = "auto_send"
    else:
        action = "flag_review"
    print("Action:", action)
    return action, confidence


# -----------------------------
# STAGE 7: REFLECT
# -----------------------------
def reflect_update_logs(email, action, confidence):
    print("\n🪞 Reflecting and updating logs...")
    time.sleep(1)
    with open("decision_logs.txt", "a") as f:
        f.write(f"Email: {email['subject']} | Action: {action} | Confidence: {confidence:.2f}\n")
    print("Logs updated successfully.")


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():
    print("\n========== AGENTIC AI DECISION LOOP ==========\n")
    email = sense_incoming_mail()
    context = understand_context(email)
    risk = simulate_risks(email)
    template = plan_reply(context["intent"])
    reply = act_generate_reply(template, email)
    action, confidence = decide_action(risk)
    reflect_update_logs(email, action, confidence)

    print("\n--- Final Output ---")
    print("Suggested Reply:\n")
    print(reply)
    print("\nSystem Decision:", action.upper())

    if action == "flag_review":
        print("\n⚠️ Review required before sending.")
    else:
        print("\n✅ Reply ready to send automatically.")

    print("\n==============================================\n")


if __name__ == "__main__":
    main()
