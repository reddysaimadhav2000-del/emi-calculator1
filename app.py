from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    emi = total = interest = None
    schedule = []

    if request.method == "POST":
        loan = float(request.form["loan"])
        annual_rate = float(request.form["rate"])
        years = int(request.form["years"])

        rate = annual_rate / 100 / 12
        months = years * 12

        emi = loan * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)
        balance = loan

        for m in range(1, months + 1):
            interest_amt = balance * rate
            principal = emi - interest_amt
            balance -= principal

            schedule.append({
                "month": m,
                "emi": round(emi, 2),
                "principal": round(principal, 2),
                "interest": round(interest_amt, 2),
                "balance": round(max(balance, 0), 2)
            })

        total = emi * months
        interest = total - loan

        emi = round(emi, 2)
        total = round(total, 2)
        interest = round(interest, 2)

    return render_template(
        "index.html",
        emi=emi,
        total=total,
        interest=interest,
        schedule=schedule
    )

if __name__ == "__main__":
    app.run()
