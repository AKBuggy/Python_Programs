def count_valid_pairs(SKILL):
    N = len(SKILL)
    count = 0
    skill_counts = {}  # Dictionary to store skill level counts

    for i in range(N):
        # Update skill level count
        skill_counts[SKILL[i]] = skill_counts.get(SKILL[i], 0) + 1

        # Calculate valid pairs
        for j in range(i + 1, N):
            if SKILL[i] > 2 * SKILL[j]:
                count += skill_counts.get(SKILL[j], 0)

    return count

# Example usage
N = 5
SKILL = [4, 1, 2, 3, 1]
result = count_valid_pairs(SKILL)
print(f"Output: {result}")
