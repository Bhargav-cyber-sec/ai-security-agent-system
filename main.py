from guardrail import guardrail_check
from agents.root_agent import route_query

def get_multiline_input():
    print("\nPaste input (END to finish):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    print("Secure AI Security System Started")

    while True:
        mode = input("\nMode (single/multi/exit): ").strip().lower()

        if mode == "exit":
            break

        if mode == "multi":
            user_input = get_multiline_input()
        else:
            user_input = input("Enter query: ")

        # Guardrail
        guard = guardrail_check(user_input)

        if guard["status"] == "BLOCKED":
            print(f"\n🚫 BLOCKED | Score: {guard['risk_score']} | Reason: {guard['reason']}")
            continue

        result = route_query(user_input)

        print("\nResult:\n", result)


if __name__ == "__main__":
    main()
    