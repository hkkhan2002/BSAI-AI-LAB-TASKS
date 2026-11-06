def check(score, complete, fee_clear, form_signed):
    ok = complete and score >= 70 and fee_clear and form_signed
    if ok:
        return "Review"
    return "Hold"


def main():
    cases = [
        ("pass_all", 82, True, True, True, "Review", "all four conditions pass"),
        ("fee_not_clear", 85, True, False, True, "Hold", "fee clear condition fails"),
        ("form_not_signed", 88, True, True, False, "Hold", "form signed condition fails"),
        ("boundary_score", 70, True, True, True, "Review", "score is exactly on the threshold 70"),
    ]
    print("case | score | complete | fee_clear | form_signed | expected | actual | reason")
    for name, score, complete, fee_clear, form_signed, expected, reason in cases:
        ans = check(score, complete, fee_clear, form_signed)
        print(name, score, complete, fee_clear, form_signed, expected, ans, reason, sep=" | ")


if __name__ == "__main__":
    main()
