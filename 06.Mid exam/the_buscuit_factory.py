from math import floor
buscuit_per_worker_per_day = int(input())
number_of_workers = int(input())
competitors_buscuits = int(input())

produced_buscuits = 0


for day in range(1,31):

    if day % 3 == 0:
        produced_buscuits += floor(number_of_workers * buscuit_per_worker_per_day * 0.75)

    else:
        produced_buscuits += number_of_workers * buscuit_per_worker_per_day

production_difference = abs(produced_buscuits - competitors_buscuits)

print(f"You have produced {produced_buscuits} biscuits for the past month.")

if produced_buscuits > competitors_buscuits:
    print(f"You produce {production_difference /competitors_buscuits *100:.2f} percent more biscuits." )
else:
    print(f"You produce {production_difference / competitors_buscuits*100:.2f} percent less biscuits.")
