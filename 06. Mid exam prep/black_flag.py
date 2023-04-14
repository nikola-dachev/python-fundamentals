days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

plundered_sum = 0

for days in range(1, days_of_plunder + 1):
    plundered_sum += daily_plunder

    if days % 3 == 0:
        plundered_sum += daily_plunder / 2
    if days % 5 == 0:
        plundered_sum -= 0.3 * plundered_sum

if plundered_sum >= expected_plunder:
    print(f"Ahoy! {plundered_sum:.2f} plunder gained.")
else:
    percent = (plundered_sum / expected_plunder) * 100
    print(f"Collected only {percent:.2f}% of the plunder.")
