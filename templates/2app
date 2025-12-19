from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    emi = total_interest = total_payment = None
    schedule = []

    if request.method == "POST":
        P = float(request.form["principal"])
        R = float(request.form["rate"]) / 12 / 100
        N = int(request.form["years"]) * 12

        emi = round(P * R * (1 + R)**N / ((1 + R)**N - 1), 2)

        balance = P
        total_payment = round(emi * N, 2)
        total_interest = round(total_payment - P, 2)

        for m in range(1, N + 1):
            interest = round(balance * R, 2)
            principal = round(emi - interest, 2)
            balance = round(balance - principal, 2)

            schedule.append({
                "month": m,
                "emi": emi,
                "interest": interest,
                "principal": principal,
                "balance": max(balance, 0)
            })

    return render_template(
        "index.html",
        emi=emi,
        total_interest=total_interest,
        total_payment=total_payment,
        schedule=schedule
    )

if __name__ == "__main__":
    app.run(debug=True)
