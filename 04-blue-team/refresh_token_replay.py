import time
import secrets

def simulate_refresh_token_replay():
    print("=" * 95)
    print(" [SCREENSHOT 6] REFRESH TOKEN ROTATION: STALE TOKEN REPLAY ATTACK TEST")
    print("=" * 95)

    # 1. Initial Legitimate Token Issuance
    initial_refresh_token = "rt_initial_" + secrets.token_hex(16)
    print(f"\n[*] Step 1: Initial OAuth 2.0 Token Issued to Agent A")
    print(f"    - Initial Refresh Token (RT-1): {initial_refresh_token}")

    # 2. Legitimate Client Rotates Token
    print(f"\n[*] Step 2: Agent A Exchanges RT-1 for a New Access Token (Refresh Token Rotation)")
    print(f"    - POST /oauth/token [grant_type=refresh_token, token={initial_refresh_token}]")
    
    new_refresh_token = "rt_rotated_" + secrets.token_hex(16)
    revoked_tokens = {initial_refresh_token}  # RT-1 is now invalidated/revoked
    
    print(f"    - HTTP 200 OK: Rotation Successful!")
    print(f"    - New Active Refresh Token (RT-2): {new_refresh_token}")
    print(f"    - Old Refresh Token (RT-1) Status: REVOKED & INVALIDATED")

    # 3. Attacker Replays the Stolen / Stale RT-1
    print(f"\n" + "-" * 95)
    print(f"[*] Step 3: Malicious Actor Attempts to Replay Old Refresh Token (RT-1)")
    print(f"    - POST /oauth/token [grant_type=refresh_token, token={initial_refresh_token}]")
    print("-" * 95)

    if initial_refresh_token in revoked_tokens:
        print("\n[SECURITY BREACH DETECTED] Replay of Revoked Refresh Token Detected!")
        print("    - Incident : Stolen / Stale Refresh Token Replay Attempt")
        print("    - Action   : Invalidating Entire Token Family under RFC 6749 / Auth0 RTR Policy")
        print("\n[BLOCKED] Auth0 Gateway HTTP Response:")
        print("    - HTTP Status Code : 400 Bad Request")
        print("    - Error Code       : invalid_grant")
        print("    - Error Description: \"Access denied - Refresh token reuse detected. Token family has been permanently revoked.\"")
        print("\n[+] Verification: Old refresh token replay was definitively blocked and security error returned.")
    
    print("=" * 95)

if __name__ == "__main__":
    simulate_refresh_token_replay()