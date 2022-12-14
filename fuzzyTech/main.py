class SelectionCriteria:
    CGPA_9 = [0.9, 0.8, 0.97, 0.75, 0.6, 0.4, 0.2, 1.0, 0.0, 0.35]
    HSC_80 = [0.87, 0.75, 0.63, 0.19, 0.90, 0.40, 0.97, 0.1, 1.0, 0.0]
    SSC_85 = [0.54, 0.79, 0.68, 0.54, 0.78, 0.32, 0.91, 0.65, 0.20, 0.83]

    # Question no.1
    minValueQ1 = list(map(min, zip(CGPA_9, HSC_80)))
    ans = []
    for i in minValueQ1:
        if i > 0.5:
            ans.append(i)

    # Question no.2
    notSSC_85 = []
    for j in range(len(SSC_85)):
        res = 1 - SSC_85[j]
        notSSC_85.append(round(res, 2))

    minValueQ2 = list(map(min, zip(CGPA_9, notSSC_85)))
    res1 = []
    for k in minValueQ2:
        if k > 0.3:
            res1.append(k)

    # Question no.3
    ssc_85_or_hsc_80 = list(map(max, zip(SSC_85, HSC_80)))
    minValueQ3 = list(map(min, zip(CGPA_9, ssc_85_or_hsc_80)))
    res2 = []
    for j in minValueQ3:
        if j > 0.6:
            res2.append(j)


if __name__ == '__main__':
    SC = SelectionCriteria()
    print(SC.ans)
    print(SC.res1)
    print(SC.res2)
