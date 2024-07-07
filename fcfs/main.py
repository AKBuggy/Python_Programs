def fcfs(processes):
    processes.sort(key=lambda i: i[0])
    print("Process\tAT\tBT\tCT\tTAT\tWT")

    def find_ct():
        ct = processes[0][0] + processes[0][1]
        ct_list = [ct]

        for at, bt, p in processes[1:]:
            if at >= ct:
                ct = at + bt
            else:
                ct += bt
            ct_list.append(ct)
        return ct_list

    ct_list = find_ct()

    def find_tat():
        tat_list = []
        for i in range(len(processes)):
            tat = ct_list[i] - processes[i][0]
            tat_list.append(tat)
        return tat_list

    tat_list = find_tat()

    def find_wt():
        wt_list = []
        for i in range(len(processes)):
            wt = tat_list[i] - processes[i][1]
            wt_list.append(wt)
        return wt_list


    wt_list = find_wt()

    for i, (at, bt, p) in enumerate(processes):
        print(f"{p}\t\t{at}\t{bt}\t{ct_list[i]}\t{tat_list[i]}\t{wt_list[i]}")

    # Calculate and print average turnaround time and average waiting time
    avg_turnaround_time = sum(tat_list) / len(processes)
    avg_waiting_time = sum(wt_list) / len(processes)

    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")


if __name__ == "__main__":
    processes = [(4, 5, "P1"), (6, 4, "P2"), (0, 3, "P3"), (6, 2, "P4"), (5, 4, "P5")]  # Process IDs

    fcfs(processes)
