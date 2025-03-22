from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
    }
    total = 0.0
    depot_a_faire=0.0

    if request.method == "POST":
        data = request.POST
        if data["vendre_adjuste"]:
            context["vendre_adjuste"] = data["vendre_adjuste"]
        if data["vendre_par_cartes"]:
            context["vendre_par_cartes"] = data["vendre_par_cartes"]
        if data["debourse"]:
            context["debourse"] = data["debourse"]
        if data["depot"]:
            context["depot"] = data["depot"]
        if data["vendre_adjuste"] and data["vendre_par_cartes"]:
            if not data["depot"]:
                context["depot"] = 0
            if not data["debourse"]:
                context["debourse"] = 0
            depot_a_faire = float(data["vendre_adjuste"]) - float(data["vendre_par_cartes"]) - float(
                context["debourse"]) - float(context["depot"])
            context["depot_a_faire"] = f"{depot_a_faire:.2f}"
        if data["d005"]:
            context["d005"] = data["d005"]
            res_d005 = int(data["d005"]) * 0.05
            total  += res_d005
            context["res_d005"] = f"{res_d005:.2f}"
        if data["d01"]:
            context["d01"] = data["d01"]
            res_d01= int(data["d01"]) * 0.1
            total += res_d01
            context["res_d01"] = f"{res_d01:.2f}"
        if data["d025"]:
            context["d025"] = data["d025"]
            res_d025 = int(data["d025"]) * 0.25
            total += res_d025
            context["res_d025"] = f"{res_d025:.2f}"
        if data["d1"]:
            context["d1"] = data["d1"]
            res_d1 = int(data["d1"])
            total += res_d1
            context["res_d1"] = f"{res_d1:.2f}"
        if data["d2"]:
            context["d2"] = data["d2"]
            res_d2= int(data["d2"])*2
            total += res_d2
            context["res_d2"] = f"{res_d2:.2f}"
        if data["d5"]:
            context["d5"] = data["d5"]
            res_d5 = int(data["d5"])*5
            total += res_d5
            context["res_d5"] = f"{res_d5:.2f}"
        if data["d10"]:
            context["d10"] = data["d10"]
            res_d10 = int(data["d10"]) * 10
            total += res_d10
            context["res_d10"] = f"{res_d10:.2f}"
        if data["d20"]:
            context["d20"] = data["d20"]
            res_d20 = int(data["d20"])*20
            total += res_d20
            context["res_d20"] = f"{res_d20:.2f}"
        if data["d50"]:
            context["d50"] = data["d50"]
            res_d50 = int(data["d50"])*50
            total += res_d50
            context["res_d50"] = f"{res_d50:.2f}"
        if data["d100"]:
            context["d100"] = data["d100"]
            res_d100 = int(data["d100"])*100
            total += res_d100
            context["res_d100"] = f"{res_d100:.2f}"
        if total:
            context["total"] = f"{total:.2f}"
        if "total" in context and "depot_a_faire" in context:
            over_short = total  - 200  - depot_a_faire
            if over_short > 0:
                context["over"] = f"{over_short:.2f}"
            elif over_short < 0:
                context["short"] = f"{abs(over_short):.2f}"
            else:
                context["over_short"] = f"{over_short:.2f}"

    return render(request, 'subway/index.html', context)
