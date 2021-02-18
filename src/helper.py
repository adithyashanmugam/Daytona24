def get_risk_score(x):
    alpha = 4
    beta = 1.3
    MEAN1 = 0
    MEAN2 = 45.25483333333322
    STD1 = 15.610617771584481
    STD2 = 9.909181352955741
    return (alpha*norm.pdf(x, MEAN1, STD1) + beta*norm.pdf(x, MEAN2, STD2))*10