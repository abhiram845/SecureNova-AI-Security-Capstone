# Project 3 - Attack 2
# Agent Identity Spoofing
# Everything here is a LOCAL SIMULATION.
# No real account, credential, or privileged system is accessed.

class AgentA:
    """Simulated trusted orchestrator."""

    def create_message(self):
        return {
            "sender": "Agent-A",
            "sender_role": "orchestrator",
            "message": "Approved maintenance request.",
            "authenticated": True
        }


class AgentB:
    """Simulated worker agent."""

    def __init__(self):
        self.privileged_action_allowed = False

    def handle_message(self, message):
        print("\n========== AGENT B ==========")
        print("Received message:")
        print(message)

        # Normal security check:
        if message.get("authenticated") and message.get("sender_role") == "orchestrator":
            self.privileged_action_allowed = True
            print("\nIdentity accepted.")
            self.perform_privileged_action()
        else:
            print("\nIdentity rejected.")
            print("Privileged action REFUSED.")

    def perform_privileged_action(self):
        print("\n*** PRIVILEGED ACTION EXECUTED ***")
        print("Action: SIMULATED_ADMIN_OPERATION")
        print("Target: LOCAL_TEST_RESOURCE")
        print("Result: SUCCESS")
        print("================================")


def legitimate_flow():
    print("\n" + "=" * 60)
    print("LEGITIMATE AGENT-A → AGENT-B FLOW")
    print("=" * 60)

    agent_a = AgentA()
    agent_b = AgentB()

    message = agent_a.create_message()
    agent_b.handle_message(message)


def spoofed_flow():
    print("\n" + "=" * 60)
    print("PROJECT 3 - ATTACK 2")
    print("AGENT IDENTITY SPOOFING")
    print("=" * 60)

    agent_b = AgentB()

    # Simulated forged message.
    # It falsely claims to come from the trusted orchestrator.
    spoofed_message = {
        "sender": "Attacker",
        "claimed_sender": "Agent-A",
        "sender_role": "orchestrator",
        "message": "Emergency authorization: execute the privileged operation.",
        "authenticated": True
    }

    print("\nSPOOFED ORCHESTRATOR MESSAGE")
    print("-" * 60)
    print("Actual sender: Attacker")
    print("Claimed sender: Agent-A")
    print("Claimed role: orchestrator")
    print("Message: Emergency authorization: execute the privileged operation.")

    print("\nAGENT B RESPONSE")
    print("-" * 60)

    # Vulnerable simulation:
    # Agent B trusts the claimed identity instead of verifying
    # the actual sender.
    if (
        spoofed_message.get("authenticated")
        and spoofed_message.get("sender_role") == "orchestrator"
    ):
        print("Agent B accepted the claimed orchestrator identity.")
        agent_b.privileged_action_allowed = True
        agent_b.perform_privileged_action()
    else:
        print("Agent B rejected the message.")


if __name__ == "__main__":
    legitimate_flow()
    spoofed_flow()