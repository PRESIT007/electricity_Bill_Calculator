import gradio as gr

def calculate_bill(name, units):
    units = float(units)

    if units <= 100:
        energy_charge = units * 5
    elif units <= 200:
        energy_charge = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        energy_charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        energy_charge = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

    fixed_charge = 100
    total_bill = energy_charge + fixed_charge

    return f"""
Customer Name : {name}

Units Consumed : {units}

Energy Charge : ₹{energy_charge:.2f}

Fixed Charge : ₹{fixed_charge:.2f}

Total Bill : ₹{total_bill:.2f}
"""

demo = gr.Interface(
    fn=calculate_bill,
    inputs=[
        gr.Textbox(label="Customer Name"),
        gr.Number(label="Units Consumed (kWh)")
    ],
    outputs=gr.Textbox(label="Electricity Bill"),
    title="Electricity Bill Calculator",
    description="Calculate the electricity bill based on slab rates."
)

demo.launch()
