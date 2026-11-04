"""The Wigology Pricing Studio — imported by main.py inside owner dashboard."""
import streamlit as st


INDIAN_BUNDLES = {
    10: {"Straight / Wavy": 42},
    12: {"Straight / Wavy": 48},
    14: {"Straight / Wavy": 52},
    16: {"Straight / Wavy": 65},
    18: {"Straight / Wavy": 75},
    20: {"Straight / Wavy": 85},
    22: {"Straight / Wavy": 100},
    24: {"Straight / Wavy": 115},
    26: {"Straight / Wavy": 125},
    28: {"Straight / Wavy": 135},
    30: {"Straight / Wavy": 140},
    32: {"Straight / Wavy": 150},
    34: {"Straight / Wavy": 160},
    36: {"Straight / Wavy": 170},
}
FILIPINO_SAMPLE_BUNDLES = {18: 140, 20: 145, 22: 150, 24: 160, 26: 170}
INDIAN_CLOSURES = {
    10: {"2×6": 30, "4×4": 35, "5×5": 50, "6×6": 65, "7×7": 80},
    12: {"2×6": 35, "4×4": 40, "5×5": 55, "6×6": 70, "7×7": 85},
    14: {"2×6": 40, "4×4": 45, "5×5": 60, "6×6": 75, "7×7": 90},
    16: {"2×6": 45, "4×4": 50, "5×5": 65, "6×6": 80, "7×7": 95},
    18: {"2×6": 50, "4×4": 55, "5×5": 70, "6×6": 85, "7×7": 100},
    20: {"2×6": 55, "4×4": 60, "5×5": 75, "6×6": 90, "7×7": 105},
    22: {"2×6": 60, "4×4": 65, "5×5": 80, "6×6": 95, "7×7": 110},
    24: {"2×6": 65, "4×4": 70, "5×5": 85, "6×6": 100, "7×7": 115},
    26: {"2×6": 70, "4×4": 75, "5×5": 90, "6×6": 105, "7×7": 120},
}
FILIPINO_CLOSURES = {
    8: {"2×6": 57, "3×6": 67, "5×5": 70, "6×6": 90, "13×4": 127, "13×5": 137, "13×6": 147},
    10: {"2×6": 62, "3×6": 72, "5×5": 75, "6×6": 95, "13×4": 132, "13×5": 142, "13×6": 152},
    12: {"2×6": 67, "3×6": 77, "5×5": 80, "6×6": 98, "13×4": 137, "13×5": 147, "13×6": 157},
    14: {"2×6": 72, "3×6": 82, "5×5": 85, "6×6": 112, "13×4": 142, "13×5": 152, "13×6": 162},
    16: {"2×6": 77, "3×6": 87, "5×5": 90, "6×6": 115, "13×4": 147, "13×5": 157, "13×6": 167},
    18: {"2×6": 82, "3×6": 92, "5×5": 95, "6×6": 120, "13×4": 167, "13×5": 177, "13×6": 187},
    20: {"2×6": 87, "3×6": 97, "5×5": 100, "6×6": 130, "13×4": 177, "13×5": 187, "13×6": 197},
    22: {"2×6": 92, "3×6": 102, "5×5": 105, "6×6": 140, "13×4": 197, "13×5": 207, "13×6": 217},
    24: {"2×6": 97, "3×6": 107, "5×5": 110, "6×6": 150, "13×4": 207, "13×5": 217, "13×6": 227},
}

def zar(value):
    return f"R {value:,.2f}"

def show_pricing_studio():
    st.markdown("""
    <style>
    /* White luxury controls and taupe margin slider */
    [data-testid="stMain"] [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMain"] [data-testid="stNumberInput"] [data-baseweb="input"],
    [data-testid="stMain"] [data-testid="stNumberInput"] input {
      background:#FFFFFF !important; color:#25201C !important;
      -webkit-text-fill-color:#25201C !important;
      border-color:#D8CFC5 !important; border-radius:3px !important;
    }
    [data-testid="stMain"] [data-testid="stNumberInput"] button {
      background:#F3EEE8 !important; color:#25201C !important;
    }
    [data-testid="stMain"] [data-testid="stSlider"] {
      --primary-color:#8C7967 !important; accent-color:#8C7967 !important;
    }
    [data-testid="stMain"] [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"],
    [data-testid="stMain"] [data-testid="stSlider"] [role="slider"] {
      background-color:#8C7967 !important; border-color:#8C7967 !important;
      box-shadow:0 0 0 3px #FFFFFF !important;
    }
    [data-testid="stMain"] [data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stSliderTrackFill"],
    [data-testid="stMain"] [data-testid="stSlider"] [data-baseweb="slider"] [role="progressbar"] {
      background-color:#8C7967 !important;
    }
    [data-testid="stMain"] input[type="checkbox"] { accent-color:#8C7967 !important; }
    .profit-target-divider {border-top:1px solid #D8CFC5; margin:3.2rem 0 2rem;}
    .profit-target-heading {text-align:center; font-size:.78rem; letter-spacing:.2em; color:#786B60; margin-bottom:.6rem;}
    .profit-target-subheading {text-align:center; font:400 1.55rem Georgia,serif; color:#25201C; margin-bottom:1.1rem;}
    .profit-target-value {text-align:center; font:400 2.2rem Georgia,serif; color:#25201C; padding:.25rem 0; white-space:nowrap;}
    .profit-target-footnote {text-align:center; font-size:.78rem; color:#86786B; margin-top:.6rem;}
    [class*="st-key-pricing_margin_decrease"] button,
    [class*="st-key-pricing_margin_increase"] button {
      background:#FFFFFF!important; color:#25201C!important;
      border:1px solid #CBBEAF!important; border-radius:2px!important;
      min-height:3rem!important; font-size:1.4rem!important;
    }
    [class*="st-key-pricing_margin_decrease"] button:hover,
    [class*="st-key-pricing_margin_increase"] button:hover {
      background:#F2ECE5!important; border-color:#8C7967!important;
    }
    .pricing-section-title {font-family:Georgia,serif; font-size:1.8rem;
      font-weight:400; color:#1D1A17; margin:2.4rem 0 1.1rem; padding-bottom:.7rem;
      border-bottom:1px solid #D8CFC5;}
    .pricing-results-title {text-align:center; padding:2.6rem 0 .7rem;
      font:400 2.15rem Georgia,serif; color:#1D1A17;}
    .pricing-result-caption {text-align:center; color:#75695F;
      font-size:.78rem; letter-spacing:.13em; text-transform:uppercase;}
    .pricing-cost-row {display:flex; justify-content:space-between; gap:1rem;
      padding:.85rem .3rem; border-bottom:1px solid #E6DFD7; color:#302A25;}
    .pricing-cost-row span:last-child {font-variant-numeric:tabular-nums; text-align:right;}
    .pricing-metric {background:#F7F3EE; border:1px solid #E4DAD0;
      padding:1.4rem 1rem; text-align:center; min-height:125px;}
    .pricing-metric .label {font-size:.77rem; color:#766B61; letter-spacing:.07em;}
    .pricing-metric .value {font:400 clamp(1.3rem,2.4vw,2rem) Georgia,serif;
      color:#201C18; margin-top:.65rem; white-space:nowrap;}
    .pricing-note {font-size:.84rem; color:#75695F; text-align:center; line-height:1.7;}
    /* Improve widget spacing only within the owner pricing content */
    [data-testid="stMain"] [data-testid="stNumberInput"],
    [data-testid="stMain"] [data-testid="stSelectbox"] {margin-bottom:.65rem;}
    
    .pricing-hero {background:#F3EEE8; padding:2.6rem 1.2rem; text-align:center; margin-bottom:2rem;}
    .pricing-hero .eyebrow {font-size:.75rem; letter-spacing:.18em;}
    .pricing-hero h1 {font-family:Georgia,serif; font-size:clamp(2rem,4vw,3.3rem)!important; margin:.6rem 0;}
    .pricing-hero p {margin:0; font-size:.95rem;}
    [class*="st-key-pricing_tile_"] button {background:white!important; color:#161616!important;
        border:1px solid #BEB5AB!important; border-radius:2px!important; min-height:3.8rem!important;
        text-transform:none!important; letter-spacing:.025em!important;}
    [class*="st-key-pricing_tile_"] button[kind="primary"] {background:#F3EEE8!important;
        border:2px solid #8C7967!important; color:#111!important;}
    [class*="st-key-pricing_tile_"] button:hover {background:#EAE1D7!important;color:#111!important;}
    </style>
    <div class="pricing-hero">
      <div class="eyebrow">THE WIGOLOGY / OWNER TOOLS</div>
      <h1>Pricing Studio.</h1>
      <p>Made-to-Order Wig Pricing</p>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Private costing tool · Supplier quotes must be confirmed before selling.")

    def tiles(label, options, state_key, prefix):
        st.markdown(f"<p style='text-align:center;letter-spacing:.12em;font-size:.8rem;'>{label}</p>", unsafe_allow_html=True)
        if st.session_state.get(state_key) not in options:
            st.session_state[state_key] = options[0]
        cols = st.columns(len(options), gap="small")
        for col, option in zip(cols, options):
            with col:
                active = st.session_state[state_key] == option
                if st.button(("✓ " if active else "") + option,
                             key=f"pricing_tile_{prefix}_{option}",
                             type="primary" if active else "secondary", use_container_width=True):
                    st.session_state[state_key] = option
                    st.rerun()
        return st.session_state[state_key]

    origin = tiles("01 — SELECT YOUR HAIR ORIGIN", ["Indian", "Filipino"], "pricing_origin", "origin")
    texture = tiles("02 — SELECT YOUR HAIR TEXTURE", ["Straight", "Wavy"], "pricing_texture", "texture")
    if origin == "Indian":
        # Supplier lists straight and wavy together at the same price.
        bundle_prices = {length: options["Straight / Wavy"] for length, options in INDIAN_BUNDLES.items()}
        closure_prices = INDIAN_CLOSURES
    else:
        bundle_prices = FILIPINO_SAMPLE_BUNDLES
        closure_prices = FILIPINO_CLOSURES
        st.caption("Filipino prices are individual sample quotes; confirm the selected texture with the supplier.")

    st.markdown('<div class="pricing-section-title">01 &nbsp; Bundles</div>', unsafe_allow_html=True)
    number_of_lines = st.number_input("Different bundle lengths", min_value=1, max_value=8, value=2, step=1)
    lines = []
    for i in range(int(number_of_lines)):
        a, b = st.columns(2)
        with a:
            default_length = 20 if i % 2 == 0 else 22
            lengths = list(bundle_prices)
            length = st.selectbox(f"Bundle {i+1}: length (inches)", lengths, index=lengths.index(default_length) if default_length in lengths else 0, key=f"length_{i}")
        with b:
            quantity = st.number_input(f"Bundle {i+1}: quantity", min_value=1, max_value=20, value=2 if i == 0 else 1, step=1, key=f"qty_{i}")
        lines.append((length, int(quantity), bundle_prices[length]))
    bundle_usd = sum(qty * unit for _, qty, unit in lines)

    st.markdown('<div class="pricing-section-title">02 &nbsp; Closure</div>', unsafe_allow_html=True)
    include_closure = st.checkbox("Include a closure", value=True)
    closure_usd = 0.0
    closure_label = "None"
    unquoted_closure = False
    if include_closure:
        size = tiles("03 — SELECT YOUR CLOSURE SIZE", ["6x6", "7x7", "9x6"], "pricing_closure_size", "closure")
        price_key = size.replace("x", "×")
        available_lengths = list(closure_prices)
        closure_length = st.selectbox("Closure length (inches)", available_lengths,
            index=available_lengths.index(18) if 18 in available_lengths else 0)
        supplier_quote = closure_prices[closure_length].get(price_key)
        if supplier_quote is None:
            st.warning(f"The {size} closure has no price on this supplier's uploaded list. Enter a confirmed supplier quote in USD before using the suggested selling price.")
            manual_quote = st.number_input(f"Confirmed {size} closure quote (USD)", min_value=0.0, value=0.0, step=5.0)
            unquoted_closure = manual_quote <= 0
            closure_usd = manual_quote
        else:
            closure_usd = float(supplier_quote)
        closure_label = f'{closure_length}" {size}'
        if origin == "Indian":
            if st.checkbox("HD lace upgrade (+$10 per supplier quote)"):
                closure_usd += 10

    st.markdown('<div class="pricing-section-title">03 &nbsp; Additional Costs</div>', unsafe_allow_html=True)
    a, b = st.columns(2)
    with a:
        exchange_rate = st.number_input("USD → ZAR exchange rate (enter current rate)", min_value=0.01, value=18.00, step=0.10)
        shipping_usd = st.number_input("Supplier shipping per shipment (USD)", min_value=0.0, value=65.0, step=1.0)
        wigs_per_shipment = st.number_input("Wigs sharing this shipment", min_value=1, value=1, step=1)
        customs_total = st.number_input("Customs / clearance for shipment (R)", min_value=0.0, value=200.0, step=50.0)
    with b:
        making = st.number_input("Wig making per wig (R)", min_value=0.0, value=330.0, step=10.0)
        packaging = st.number_input("Packaging per wig (R)", min_value=0.0, value=0.0, step=10.0)
        other = st.number_input("Other costs per wig (R)", min_value=0.0, value=0.0, step=10.0)

    # Profit target sits in its own centered section, not inside either cost column.
    st.markdown('<div class="profit-target-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="profit-target-heading">PROFIT TARGET</div>', unsafe_allow_html=True)
    st.markdown('<div class="profit-target-subheading">Target gross margin</div>', unsafe_allow_html=True)
    if "pricing_margin_value" not in st.session_state:
        st.session_state["pricing_margin_value"] = 35

    left_space, minus_col, value_col, plus_col, right_space = st.columns([2, 1, 1.5, 1, 2], gap="small")
    with minus_col:
        if st.button("−", key="pricing_margin_decrease", disabled=st.session_state["pricing_margin_value"] <= 5, use_container_width=True):
            st.session_state["pricing_margin_value"] -= 5
            st.rerun()
    with value_col:
        st.markdown(f'<div class="profit-target-value">{st.session_state["pricing_margin_value"]}%</div>', unsafe_allow_html=True)
    with plus_col:
        if st.button("+", key="pricing_margin_increase", disabled=st.session_state["pricing_margin_value"] >= 75, use_container_width=True):
            st.session_state["pricing_margin_value"] += 5
            st.rerun()
    margin = st.session_state["pricing_margin_value"]
    st.markdown('<div class="profit-target-footnote">Adjust in 5% steps · Range 5%–75%</div>', unsafe_allow_html=True)

    material_usd = bundle_usd + closure_usd
    material_zar = material_usd * exchange_rate
    shipping_allocated = shipping_usd * exchange_rate / wigs_per_shipment
    customs_allocated = customs_total / wigs_per_shipment
    total_cost = material_zar + shipping_allocated + customs_allocated + making + packaging + other
    selling_price = total_cost / (1 - margin / 100)
    deposit = selling_price * 0.60
    balance = selling_price - deposit
    profit = selling_price - total_cost

    st.markdown('<div class="pricing-results-title">Your Pricing Summary.</div>', unsafe_allow_html=True)
    st.markdown('<div class="pricing-result-caption">04 — COST BREAKDOWN &amp; CUSTOMER PAYMENT</div>', unsafe_allow_html=True)
    st.markdown('<div style="height:1.3rem"></div>', unsafe_allow_html=True)
    if unquoted_closure:
        st.error("A closure quote is missing. Totals below exclude that closure and are NOT valid selling prices or deposit amounts.")
    import html
    def cost_row(label, value):
        st.markdown(
            f'<div class="pricing-cost-row"><span>{html.escape(label)}</span><span>{html.escape(value)}</span></div>',
            unsafe_allow_html=True,
        )
    with st.container():
        cost_row("Selected bundles", ", ".join(f"{qty} × {length}in" for length, qty, _ in lines))
        cost_row("Closure", closure_label)
        cost_row("Supplier materials (USD)", f"${material_usd:,.2f}")
        cost_row("Materials in rand", zar(material_zar))
        cost_row("Allocated international shipping", zar(shipping_allocated))
        cost_row("Allocated customs", zar(customs_allocated))
        cost_row("Wig construction", zar(making))
        cost_row("Packaging and other", zar(packaging + other))
    if unquoted_closure:
        return
    st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
    def metric_card(label, value):
        st.markdown(
            f'<div class="pricing-metric"><div class="label">{html.escape(label)}</div>'
            f'<div class="value">{html.escape(zar(value))}</div></div>',
            unsafe_allow_html=True,
        )
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1: metric_card("ESTIMATED TOTAL COST", total_cost)
    with c2: metric_card("SUGGESTED SELLING PRICE", selling_price)
    with c3: metric_card("ESTIMATED GROSS PROFIT", profit)
    st.markdown('<div style="height:1rem"></div>', unsafe_allow_html=True)
    c4, c5 = st.columns(2, gap="medium")
    with c4: metric_card("60% CUSTOMER DEPOSIT", deposit)
    with c5: metric_card("40% BALANCE BEFORE DELIVERY", balance)
    st.markdown('<div style="height:1.2rem"></div>', unsafe_allow_html=True)
    # The customer deposit and balance are shown above.
    # Funding coverage and the explanatory footer are intentionally not displayed.
